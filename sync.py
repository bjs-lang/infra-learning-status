#!/usr/bin/env python3
"""Only publish the approved learning summary. No credentials or third-party deps."""
import argparse
import datetime as dt
import json
import pathlib
import re
import sys
import tempfile
import time
import urllib.request

SOURCE = 'https://infra-path-jjs.beauty2002w.chatgpt.site/api/learning-status'

def clean(value, limit=1800):
    text = value if isinstance(value, str) else ''
    text = re.sub(r'```[\s\S]*?```', '[代码正文未公开]', text)
    text = re.sub(r'https?://[^\s)）]+', '[链接已省略]', text, flags=re.I)
    text = re.sub(r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}', '[邮箱已省略]', text, flags=re.I)
    text = re.sub(r'\bBearer\s+[A-Za-z0-9._~+/=-]+', '[凭据已省略]', text, flags=re.I)
    text = re.sub(r'\b(?:sk-|ghp_|github_pat_)[A-Za-z0-9_-]+', '[凭据已省略]', text)
    text = re.sub(r'(?:api[_ -]?key|token|password|secret|密码|密钥)\s*[:=：]\s*[\"\x27]?[^\s,，;；\"\x27]+', '[敏感字段已省略]', text, flags=re.I)
    text = re.sub(r'(?:~/|/(?:Users|home|workspace|root)/)[^\s，；。\n`）)]+', '[本地路径已省略]', text)
    text = re.sub(r'\b[A-Z]:\\[^\s，；。\n`]+', '[本地路径已省略]', text)
    return text[:limit]

def date_only(value):
    if value is None:
        return None
    if not isinstance(value, str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}', value):
        raise ValueError('invalid learning date')
    dt.date.fromisoformat(value)
    return value

def timestamp(value):
    if value is None:
        return None
    if not isinstance(value, str):
        raise ValueError('invalid timestamp')
    parsed = dt.datetime.fromisoformat(value.replace('Z', '+00:00'))
    if parsed.tzinfo is None:
        raise ValueError('timestamp requires timezone')
    return parsed.astimezone(dt.timezone.utc).isoformat().replace('+00:00', 'Z')

def project(source, synced_at):
    if source.get('schemaVersion') != 1:
        raise ValueError('unsupported source schema')
    revision = source.get('revision')
    if type(revision) is not int or revision < 1:
        raise ValueError('invalid source data version')
    lessons = source.get('cppLessons', [])
    if len(lessons) != 48 or {l.get('number') for l in lessons} != set(range(1, 49)):
        raise ValueError('incomplete 48-lesson data')
    completed = {'已实践', '已实验通过', '已验收'}
    courses = [{'number': l['number'], 'title': clean(l.get('title'), 160), 'status': clean(l.get('status'), 40), 'verification': clean(l.get('verification'), 800), 'review': clean(l.get('review'), 500)} for l in sorted(lessons, key=lambda x: x['number'])]
    current = next((l for l in courses if l['status'] not in completed), None)
    original_current = source.get('currentCppLesson')
    if (original_current.get('number') if original_current else None) != (current['number'] if current else None):
        raise ValueError('source current lesson disagrees with course states')
    if current:
        current = {**current, 'goal': clean(original_current.get('goal'), 700), 'acceptance': clean(original_current.get('acceptance'), 700)}
    recent = []
    for r in source.get('recentLearning', [])[:5]:
        recent.append({'date': date_only(r.get('date')), 'track': clean(r.get('track'), 40), 'title': clean(r.get('title'), 180), 'summary': clean(r.get('summary')), 'experiments_and_verification': clean(r.get('experimentsAndVerification')), 'mastery': clean(r.get('mastery'), 700), 'open_questions': clean(r.get('openQuestions')), 'next_step': clean(r.get('nextStep'))})
    continuity = source.get('continuity', {})
    # Explicit allowlist: never publish source wholesale, note bodies, identities or files.
    return {'schema_version': 1, 'data_version': revision, 'updated_at': timestamp(source.get('lastUpdatedAt')), 'updated_at_note': '旧记录可能没有精确保存时间；空值不是同步失败。', 'synced_at': timestamp(synced_at), 'last_learning_date': date_only(source.get('lastLearningDate')), 'current_cpp_lesson': current, 'cpp_lessons': courses, 'recent_learning': recent, 'verified_summary': clean(continuity.get('verified'), 2400), 'open_questions': clean(continuity.get('openQuestions'), 2400), 'next_step': clean(continuity.get('nextStep'), 2000), 'linux_and_cann_plan': clean(continuity.get('longTermPlan'), 2000)}

def markdown(data):
    c = data['current_cpp_lesson']
    lines = ['# 学习进度只读镜像', '', f"数据版本：{data['data_version']}", f"网站最后保存：{data['updated_at'] or '未知（旧记录未记录精确保存时间）'}", f"本次同步：{data['synced_at']}", f"最近学习：{data['last_learning_date'] or '暂无'}", '', '每次使用请检查同步时间和 GitHub Actions 最近一次运行结果；文件可读取不代表同步服务始终正常。', '', '## 当前 C++ 起点', f"第 {c['number']}/48 节｜{c['title']}｜{c['status']}" if c else '48 节已全部记录为完成，请复盘。', '', '## 已验证与记录边界', data['verified_summary'], '', '## 疑问与薄弱点', data['open_questions'], '', '## 下一步', data['next_step'], '', '## Linux / CANN 主线', data['linux_and_cann_plan'], '', '## 最近学习摘要']
    for r in data['recent_learning']:
        lines += ['', f"### {r['date']}｜{r['track']}｜{r['title']}", r['summary'], '实验结论：' + r['experiments_and_verification'], '掌握情况：' + r['mastery'], '疑问：' + r['open_questions'], '下一步：' + r['next_step']]
    lines += ['', '## 48 节课程状态']
    for l in data['cpp_lessons']:
        lines.append(f"- 第 {l['number']} 节｜{l['title']}｜{l['status']}" + ('｜复习：' + l['review'] if l['review'] else ''))
    lines += ['', '## 使用规则', '只以网站已保存的学习摘要为来源；不推测时长或补写实验。读取失败时应明确告知用户，不能把历史缓存视为最新进度。原始笔记、身份、凭据和私密文件不在本镜像中。', '']
    return '\n'.join(lines)

def fetch_source():
    for attempt in range(3):
        try:
            request = urllib.request.Request(SOURCE, headers={'Accept': 'application/json', 'Cache-Control': 'no-cache', 'User-Agent': 'infra-learning-status-mirror/1.0'})
            with urllib.request.urlopen(request, timeout=30) as response:
                if response.status != 200 or response.geturl() != SOURCE:
                    raise ValueError('source did not return the expected direct HTTP 200')
                raw = response.read(512001)
                if len(raw) > 512000:
                    raise ValueError('source exceeds summary size limit')
                return json.loads(raw.decode('utf-8'))
        except Exception:
            if attempt == 2:
                raise RuntimeError('Source fetch/validation failed; existing mirror files retained') from None
            time.sleep(2 ** attempt)

def save(data, destination):
    destination.mkdir(parents=True, exist_ok=True)
    previous = destination / 'learning-status.json'
    if previous.exists():
        old = json.loads(previous.read_text())
        if old.get('data_version', 0) > data['data_version']:
            raise ValueError('source version regressed; old mirror retained')
    with tempfile.TemporaryDirectory(dir=destination) as tmp:
        staging = pathlib.Path(tmp)
        (staging / 'learning-status.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
        (staging / 'learning-status.md').write_text(markdown(data))
        for name in ['learning-status.json', 'learning-status.md']:
            (staging / name).replace(destination / name)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=pathlib.Path, default=pathlib.Path('.'))
    args = parser.parse_args()
    data = project(fetch_source(), dt.datetime.now(dt.timezone.utc).isoformat())
    save(data, args.output)
    print(f"Synced data_version={data['data_version']}, current_cpp_lesson={data['current_cpp_lesson']['number'] if data['current_cpp_lesson'] else 'completed'}")

if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print(f'Sync failed: {type(error).__name__}; no stale data was republished', file=sys.stderr)
        sys.exit(1)
