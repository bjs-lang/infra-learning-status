# 同步说明

- 唯一课程数据来源：现有网站 `/api/learning-status`，不手改 JSON/Markdown。
- `schema_version` 为镜像格式版本；`data_version` 对应网站 revision。
- `updated_at` 是网站真实保存时间，旧记录未知则 null。`synced_at` 是本次成功抓取并生成文件的时间，并非 Pages 完成发布时间。
- 公开内容：当前课次、48节课程状态、近期学习摘要与实验结论、疑问、下一步、Linux/CANN主线。无原始笔记、完整代码、账号、身份、密钥或令牌。
- 常见敏感格式会再次过滤；不要把秘密填入本来就用于公开的学习摘要。
- Actions 约每5分钟检查，可能排队或延迟；公开仓库长期无活动时计划任务可能停用，需查看 Actions。
- 抓取、格式、版本回退校验失败则停止，不发布失败时的新时间戳。查看文件同步时间和最近工作流结果判断新鲜度。
- 使用 GitHub Actions 的临时 GITHUB_TOKEN；无长期 PAT、无第三方密钥。同步作业仅 contents:write；部署作业仅 pages:write、id-token:write。
- 首次发布需要仓库 Settings → Pages → Build and deployment → Source 选择 GitHub Actions。
- 再次运行：Actions → Sync learning status → Run workflow。
- 本地测试：`python3 -m unittest -v test_sync.py`；同步：`python3 sync.py`。

测试状态：本地字段筛选、脱敏、48节完整性、版本变化与拒绝版本回退已测试。真实 GitHub runner 可访问性、Pages 发布与实际延迟以 Actions 运行结果为准，不能用本地测试代替。
