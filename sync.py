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


def project_plan(value):
    if not isinstance(value, dict):
        return None
    domains = []
    for d in value.get('domains', [])[:12]:
        modules = []
        for u in d.get('modules', [])[:20]:
            topics = []
            for t in u.get('topics', [])[:30]:
                topics.append({'title': clean(t.get('title'), 180), 'status': clean(t.get('status'), 40), 'focus': t.get('focus') is True, 'difficult': t.get('difficult') is True, 'knowledge_points': [clean(k, 180) for k in t.get('knowledgePoints', [])[:20]]})
            modules.append({'code': clean(u.get('code'), 30), 'title': clean(u.get('title'), 180), 'prerequisites': clean(u.get('prerequisites'), 400), 'acceptance': clean(u.get('acceptance'), 700), 'topics': topics})
        domains.append({'id': clean(d.get('id'), 40), 'name': clean(d.get('name'), 100), 'priority': clean(d.get('priority'), 160), 'modules': modules})
    hardware = value.get('hardware')
    if isinstance(hardware, dict):
        hardware = {'device': clean(hardware.get('device'), 400), 'device_status': clean(hardware.get('deviceStatus'), 160), 'environment_status': clean(hardware.get('environmentStatus'), 100), 'preparation_status': clean(hardware.get('preparationStatus'), 180), 'preparation_window': clean(hardware.get('preparationWindow'), 250), 'first_connection_steps': [clean(t, 500) for t in hardware.get('firstConnectionSteps', [])[:10]], 'competition_target': clean(hardware.get('competitionTarget'), 240), 'submission_deadline': date_only(hardware.get('submissionDeadline'))}
    else:
        hardware = None
    projects = []
    for p in value.get('projects', [])[:2]:
        stages = [{'code': clean(st.get('code'), 30), 'name': clean(st.get('name'), 180), 'status': clean(st.get('status'), 40), 'deliverable': clean(st.get('deliverable'), 800), 'acceptance': clean(st.get('acceptance'), 1000), 'transfer': clean(st.get('transfer'), 300)} for st in p.get('stages', [])[:10]]
        guide = p.get('planning', {})
        planning = {'preparation': clean(guide.get('preparation'), 800), 'start_window': clean(guide.get('startWindow'), 1000), 'duration': clean(guide.get('duration'), 600), 'flow_note': clean(guide.get('flowNote'), 1000), 'definition_of_done': [clean(c, 700) for c in guide.get('definitionOfDone', [])[:15]], 'prerequisites': [{'label': clean(r.get('label'), 240), 'before': clean(r.get('before'), 300), 'status': clean(r.get('status'), 80), 'basis': clean(r.get('basis'), 800), 'note': clean(r.get('note'), 800)} for r in guide.get('prerequisites', [])[:15]]}
        for st, original in zip(stages, p.get('stages', [])[:10]):
            st.update({'entry': clean(original.get('entry'), 1000), 'steps': [{'name': clean(step.get('name'), 240), 'action': clean(step.get('action'), 1600), 'artifact': clean(step.get('artifact'), 800)} for step in original.get('steps', [])[:10]], 'checklist': [clean(c, 800) for c in original.get('checklist', [])[:15]], 'troubleshooting': clean(original.get('troubleshooting'), 1200)})
        count = p.get('executionRecordCount', 0)
        projects.append({'code': clean(p.get('code'), 20), 'name': clean(p.get('name'), 180), 'priority': clean(p.get('priority'), 80), 'status': clean(p.get('status'), 40), 'goal': clean(p.get('goal'), 800), 'mvp': clean(p.get('mvp'), 800), 'optional': clean(p.get('optional'), 600), 'next_step': clean(p.get('nextStep'), 800), 'repository_state': clean(p.get('repositoryState'), 100), 'updated_at': timestamp(p.get('updatedAt')), 'execution_record_count': count if type(count) is int and count >= 0 else 0, 'first_execution_date': date_only(p.get('firstExecutionDate')), 'planning': planning, 'stages': stages})
    phases = [{'name': clean(p.get('name'), 240), 'time': clean(p.get('time'), 180), 'lane': clean(p.get('lane'), 80), 'learning': clean(p.get('learning'), 1000), 'deliverable': clean(p.get('deliverable'), 1000), 'gate': clean(p.get('gate'), 1000), 'budget': clean(p.get('budget'), 600)} for p in value.get('phases', [])[:20]]
    return {'version': clean(value.get('version'), 60), 'goal': clean(value.get('goal'), 400), 'policy': clean(value.get('policy'), 1000), 'hardware': hardware, 'projects': projects, 'phases': phases, 'domains': domains}

def learning_focus(value):
    if not isinstance(value, dict):
        return None
    return {
        'priority': clean(value.get('priority'), 50),
        'difficulty': clean(value.get('difficulty'), 600),
        'method': clean(value.get('method'), 600),
        'application': clean(value.get('application'), 700),
        'planned_practice': clean(value.get('plannedPractice'), 700),
        'review_tasks': [clean(t, 500) for t in value.get('reviewTasks', [])[:10]],
        'verification_boundary': clean(value.get('verificationBoundary'), 600),
    }

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
    courses = [{'number': l['number'], 'title': clean(l.get('title'), 160), 'status': clean(l.get('status'), 40), 'verification': clean(l.get('verification'), 800), 'review': clean(l.get('review'), 1000), 'learning_focus': learning_focus(l.get('learningFocus')), 'experiments': [{'id': clean(e.get('id'), 30), 'title': clean(e.get('title'), 180), 'status': clean(e.get('status'), 40), 'evidence': clean(e.get('evidence'), 800), 'expected_only': clean(e.get('expectedOnly'), 500)} for e in l.get('experiments', [])[:15]]} for l in sorted(lessons, key=lambda x: x['number'])]
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
    return {'schema_version': 1, 'data_version': revision, 'updated_at': timestamp(source.get('lastUpdatedAt')), 'updated_at_note': '旧记录可能没有精确保存时间；空值不是同步失败。', 'synced_at': timestamp(synced_at), 'last_learning_date': date_only(source.get('lastLearningDate')), 'current_cpp_lesson': current, 'cpp_lessons': courses, 'recent_learning': recent, 'verified_summary': clean(continuity.get('verified'), 2400), 'open_questions': clean(continuity.get('openQuestions'), 2400), 'next_step': clean(continuity.get('nextStep'), 2000), 'linux_and_cann_plan': clean(continuity.get('longTermPlan'), 2000), 'learning_path': project_plan(source.get('learningPlan'))}

def markdown(data):
    c = data['current_cpp_lesson']
    lines = ['# 学习进度只读镜像', '', f"数据版本：{data['data_version']}", f"网站最后保存：{data['updated_at'] or '未知（旧记录未记录精确保存时间）'}", f"本次同步：{data['synced_at']}", f"最近学习：{data['last_learning_date'] or '暂无'}", '', '每次使用请检查同步时间和 GitHub Actions 最近一次运行结果；文件可读取不代表同步服务始终正常。', '', '## 当前 C++ 起点', f"第 {c['number']}/48 节｜{c['title']}｜{c['status']}" if c else '48 节已全部记录为完成，请复盘。', '', '## 已验证与记录边界', data['verified_summary'], '', '## 疑问与薄弱点', data['open_questions'], '', '## 下一步', data['next_step'], '', '## Linux / CANN 主线', data['linux_and_cann_plan'], '', '## 最近学习摘要']
    for r in data['recent_learning']:
        lines += ['', f"### {r['date']}｜{r['track']}｜{r['title']}", r['summary'], '实验结论：' + r['experiments_and_verification'], '掌握情况：' + r['mastery'], '疑问：' + r['open_questions'], '下一步：' + r['next_step']]
    lines += ['', '## 48 节课程状态']
    for l in data['cpp_lessons']:
        lines.append(f"- 第 {l['number']} 节｜{l['title']}｜{l['status']}" + ('｜复习：' + l['review'] if l['review'] else ''))
        for e in l.get('experiments', []):
            lines += ['  - ' + e['title'] + '｜' + e['status'] + '｜' + e['evidence'] + ('｜仅预期、尚未实测：' + e['expected_only'] if e['expected_only'] else '')]

        focus = l.get('learning_focus')
        if focus:
            lines += ['  - 难点：' + focus['difficulty'], '    判断方法：' + focus['method'], '    实际用途：' + focus['application'], '    后续练习（未验收）：' + focus['planned_practice'], '    复习：' + '；'.join(focus['review_tasks']), '    验证边界：' + focus['verification_boundary']]

    plan = data.get('learning_path')
    if plan:
        lines += ['', '## AI Infra全体系学习路线', plan['goal'], plan['policy'], '规划版本：' + plan['version']]
        hardware = plan.get('hardware')
        if hardware:
            lines += ['', '## 设备与竞赛锚点', hardware['device'], '环境状态：' + hardware['environment_status'], '目标赛事：' + hardware['competition_target'], '正式提交截止T：' + (hardware['submission_deadline'] or '待核实；报名截止不作为T')]
            lines += ['首次连接：' + hardware.get('preparation_status', ''), '准备窗口：' + hardware.get('preparation_window', '')]
            lines += ['- ' + t for t in hardware.get('first_connection_steps', [])]
        for p in plan.get('projects', []):
            lines += ['', '### ' + p['code'] + ' ' + p['name'] + '｜' + p['status'], p['goal'], 'MVP：' + p['mvp'], '可选增强：' + p['optional'], '下一步：' + p['next_step'], '仓库：' + p['repository_state'], '实际执行记录数：' + str(p['execution_record_count'])]
            guide = p.get('planning', {})
            if guide:
                lines += ['准备窗口：' + guide.get('preparation', ''), '计划启动：' + guide.get('start_window', ''), '预计体量：' + guide.get('duration', ''), '实际首次执行日期：' + (p.get('first_execution_date') or '尚未开始')]
                for r in guide.get('prerequisites', []):
                    lines += ['- 前置：' + r['label'] + '｜' + r['status'] + '｜' + r['before'], '  依据：' + r['basis'], '  说明：' + r['note']]
                lines += ['流程规则：' + guide.get('flow_note', '')]
            for st in p['stages']:
                lines += ['- ' + st['code'] + ' ' + st['name'] + '｜' + st['status'], '  交付：' + st['deliverable'], '  验收：' + st['acceptance']]
                for i, step in enumerate(st.get('steps', []), 1):
                    lines += ['  ' + str(i) + '. ' + step['name'] + '：' + step['action'], '     交付：' + step['artifact']]
                if st.get('checklist'):
                    lines += ['  检查：' + '；'.join(st['checklist'])]
                if st.get('troubleshooting'):
                    lines += ['  排错：' + st['troubleshooting']]
        if plan.get('phases'):
            lines += ['', '## 学习与实践时间轴']
        for p in plan.get('phases', []):
            lines += ['- ' + p['time'] + '｜' + p['name'], '  学习：' + p['learning'], '  实践：' + p['deliverable'], '  门槛：' + p['gate'], '  建议投入：' + p['budget']]
        for d in plan['domains']:
            lines += ['', '### ' + d['name'] + '｜' + d['priority']]
            for u in d['modules']:
                lines += ['', '#### ' + u['code'] + ' ' + u['title'], '前置：' + u['prerequisites'], '验收：' + u['acceptance']]
                for t in u['topics']:
                    lines.append('- ' + t['title'] + '｜' + t['status'] + ('｜★重点' if t['focus'] else '') + ('｜▲难点' if t['difficult'] else ''))
                    lines.append('  学习范围：' + '；'.join(t['knowledge_points']))
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
