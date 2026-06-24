# TODO

## 当前待办

- [ ] 将每日自动化主流程固定为：新增论文与笔记 -> 更新 `state/processed_articles.json` -> 运行 `python scripts/build_indexes.py` -> 提交并推送 `origin/master`。
- [ ] 处理剩余 12 条未补回 PDF 的候选；其中 10 条为 Elsevier/ScienceDirect `HTTP 403`，1 条为 Nature `cookies_not_supported`，1 条为 IOP/Radware 验证页。
- [ ] 为当前 65 条已补回 PDF 但尚无笔记的条目补中文结构化笔记。
- [ ] 把每日自动化主流程接到 `scripts/retry_download_queue.py`，启动时先消化可恢复积压，避免配置恢复后仍只读旧 blocked-day 记录。
- [ ] 为来源可达性预检补一层轻量检查，避免在明显 `403` / bot-wall 来源上重复空跑，并对 arXiv / DOI 这类开放来源单独标记“仅运行时阻塞”。
- [ ] 修补 `scripts/safe_pdf_download.py` 在个别 Cambridge 官方 PDF 直链上的卡住问题；当前同 URL 用 `curl` 可正常完成下载，说明更像 Python 传输路径或读取策略问题。

## 开发记录

- 2026-06-24：完成当天目录初始化、去重基线检查和正式来源复查。先查看 Cambridge `Journal of Plasma Physics` / `High Power Laser Science and Engineering` 当前页面与近期条目，确认本轮高相关正式来源候选要么已在 `state/processed_articles.json` 中、要么属于此前旧日阻塞记录，继续补录会重复处理；随后转向近几天 arXiv 新稿与近期修订稿，补入 3 条高相关预印本：`10.48550/arXiv.2606.22427`、`10.48550/arXiv.2606.21221`、`10.48550/arXiv.2605.07929`。3 条 PDF 均通过环境代理路径下载与文件头校验，并同步生成中文结构化笔记；`processed_articles.json` 从 132 增至 135，重试队列保持 12 条不变。
- 2026-06-23：完成当天目录初始化、去重基线检查和正式来源复查。先查看 Cambridge `Journal of Plasma Physics` / `High Power Laser Science and Engineering` 当前页面，确认本轮没有比 2026-06-21 到 2026-06-22 已入库条目更强且明确非重复的正式来源增量；随后从 arXiv `physics.plasm-ph` / `physics.acc-ph` 近一周列表补入 2 条高相关预印本：`10.48550/arXiv.2606.15965`、`10.48550/arXiv.2606.16126`。2 条 PDF 均通过环境代理路径下载与文件头校验，并同步生成中文结构化笔记；`processed_articles.json` 从 130 增至 132，重试队列保持 12 条不变。
- 2026-06-22：完成当天目录初始化、去重基线检查和正式来源复查。继续优先检查 Cambridge `Journal of Plasma Physics` 当前 issue，在确认 2026-06-21 已处理过更偏 wakefield / target engineering 的增量后，本轮补入 2 条此前尚未入库、但更能补强强场辐射反作用与“可微模拟器 + PIC + 机器学习”主线的正式来源论文：`10.1017/S0022377826101809` 与 `10.1017/S0022377826101755`。2 条 PDF 均通过环境代理路径下载与文件头校验，并同步生成中文结构化笔记；`processed_articles.json` 从 128 增至 130，重试队列保持 12 条不变。
- 2026-06-21：完成当天目录初始化、去重基线检查和正式来源复查。优先检查 Cambridge HPL latest volume 与 JPP June 2026 current issue；确认 `physics.plasm-ph` 最近页里的最高相关新稿已在前一天入库后，本轮不再补边缘 arXiv，而是新增 2 条正式来源：`10.1017/S0022377826101858` 与 `10.1017/hpl.2026.10132`。2 条 PDF 均通过环境代理路径下载与文件头校验，并同步生成中文结构化笔记；`processed_articles.json` 从 126 增至 128，重试队列保持 12 条不变。
- 2026-06-20：仿照 `everyday_github` 的组织方式，为 `everyday_paper` 增加 GitHub 浏览结构：新增 `.gitignore` 排除 `.venv`、缓存和 PDF 大文件；新增 `scripts/build_indexes.py`，从 `state/processed_articles.json` 自动生成 `INDEX.md`、`categories/`、`papers/` 和 `daily/README.md`；更新 `README.md`/`AGENTS.md`，明确分类索引、总索引、每日更新和自动提交推送约定。
- 2026-06-20：按用户要求扩展每日论文索引的主题过滤范围：在原有激光等离子体、强场 QED、高能量密度物理、PIC 与 机器学习应用基础上，新增“激光加速电子束与离子束应用”关注点；下一轮检索应覆盖电子束打转换靶产生韧致辐射 / 伽马源、光核反应、中子 / 同位素产生、激光离子加速辐照/诊疗/材料/核反应用途，以及束流品质、靶设计、转换效率、实验诊断和辐射防护等工程问题。已同步更新项目 `README.md` 与 everyday-paper 自动化 prompt。
- 2026-06-20：完成当天目录初始化、去重基线检查和外部检索。先复查 Cambridge HPL latest volume / accepted manuscripts 与 JPP recent 页面，确认正式来源本轮没有筛到比当前基线更强且明确非重复的增量；随后转向 arXiv `physics.plasm-ph` / `physics.acc-ph` 近两日新稿，补入 3 条高相关预印本：`10.48550/arXiv.2606.20298`、`10.48550/arXiv.2606.19523`、`10.48550/arXiv.2606.20125`。3 条 PDF 均通过环境代理路径下载与文件头校验，并同步生成中文结构化笔记；`processed_articles.json` 从 123 增至 126，重试队列保持 12 条不变。
- 2026-06-19：完成当天目录初始化、去重基线检查和外部检索。先复查 Cambridge HPL / JPP 近期页面，确认正式来源本轮没有筛到比当前基线更强且明确非重复的增量；随后转向 arXiv `physics.plasm-ph` / `physics.acc-ph` 近一周列表与相关检索，补入 4 条高相关预印本：`10.48550/arXiv.2606.18845`、`10.48550/arXiv.2606.12127`、`10.48550/arXiv.2606.12567`、`10.48550/arXiv.2606.12322`。4 条 PDF 均通过环境代理路径下载与文件头校验，并同步生成中文结构化笔记；`processed_articles.json` 从 119 增至 123，重试队列保持 12 条不变。顺手按当前台账纠正了“已补回 PDF 但尚无笔记”的真实历史数量为 65 条。
- 2026-06-18：完成当天目录初始化、去重基线检查和外部检索。先复查 Cambridge HPL accepted manuscripts / latest volume，确认页面可访问，但没有筛到比当前基线更强且明确非重复的正式来源增量；随后转向 arXiv `physics.plasm-ph` / `physics.acc-ph` 新稿与近几日相关检索，补入 3 条高相关预印本：`10.48550/arXiv.2606.17733`、`10.48550/arXiv.2606.15035`、`10.48550/arXiv.2606.13183`。3 条 PDF 均通过环境代理路径下载与文件头校验，并同步生成中文结构化笔记；`processed_articles.json` 从 116 增至 119，重试队列保持 12 条不变。
- 2026-06-17：完成当天目录初始化、去重基线检查和外部检索。先复查 Cambridge HPL accepted manuscripts / latest volume，确认正式来源页面仍可访问，但 2026-06-16 附近的新条目以激光工程/器件为主，没有筛到比当前基线更强的非重复增量；随后转向 arXiv 新稿与相关检索，补入 3 条高相关预印本：`10.48550/arXiv.2606.15687`、`10.48550/arXiv.2606.16066`、`10.48550/arXiv.2606.15512`。3 条 PDF 均通过环境代理路径下载与文件头校验，并同步生成中文结构化笔记；`processed_articles.json` 从 113 增至 116，重试队列保持 12 条不变。
- 2026-06-16：完成当天目录初始化、去重基线检查和外部检索。先检查 Cambridge HPL 最新卷，确认到 1 条高相关且未重复的正式来源 `10.1017/hpl.2026.10115`；随后从 arXiv `physics.plasm-ph` 当前新稿与月度列表补入 3 条高相关预印本：`10.48550/arXiv.2606.14300`、`10.48550/arXiv.2606.02890`、`10.48550/arXiv.2606.04332`。4 条 PDF 均通过环境代理路径下载与文件头校验，并同步生成中文结构化笔记；`processed_articles.json` 从 109 增至 113，重试队列保持 12 条不变。今日还尝试先跑 `retry_download_queue.py --source-family all`，但在来源受限条目上耗时过长，已中断且未改动队列状态。
- 2026-06-15：完成当天目录初始化、去重基线检查和外部检索。先检查 Cambridge HPL accepted manuscripts 等正式来源，未筛出比现有基线更强且明确非重复的新条目；随后从 arXiv `physics.plasm-ph` 与 `physics.acc-ph` 当前列表补入 4 条新的高相关预印本：`10.48550/arXiv.2606.08827`、`10.48550/arXiv.2606.09168`、`10.48550/arXiv.2606.05948`、`10.48550/arXiv.2606.01860`。4 条 PDF 均通过环境代理路径下载与文件头校验，并同步生成中文结构化笔记；`processed_articles.json` 从 105 增至 109，重试队列保持 12 条不变。
- 2026-06-14：完成当天目录初始化、去重基线检查和外部检索。优先检查 Cambridge HPL 正式来源与 accepted manuscripts，确认到 1 条新的高相关正式来源 `10.1017/hpl.2026.10148`；随后从 arXiv 近期 plasma / accelerator 列表补入 3 条高相关预印本：`10.48550/arXiv.2606.02454`、`10.48550/arXiv.2606.04887`、`10.48550/arXiv.2606.06210`。4 条 PDF 均通过校验，其中 3 条通过现有 `safe_pdf_download.py` 闭环完成；Cambridge 那条通过抽取官方 PDF 直链并用 `curl` 下载成功，暴露出脚本在该直链上的 Python 读取路径会卡住。已同步生成 4 份中文结构化笔记，`processed_articles.json` 从 101 增至 105，重试队列保持 12 条不变。
- 2026-06-13：完成当天目录初始化、去重基线检查和外部检索。先检查 Cambridge HPL 最新卷与 Nature 检索页；其中 Cambridge 确认到 1 条新的高相关正式论文 `10.1017/hpl.2026.10136`，Nature 检索页仍落到 `cookies_not_supported`，未形成稳定的正式增量筛选结果。随后补入 2 条新的高相关 arXiv 预印本：`10.48550/arXiv.2606.07147`、`10.48550/arXiv.2605.12132`。3 条 PDF 均通过环境代理路径下载成功，Cambridge 那篇还验证了“文章页/DOI 自动解析官方 PDF”的回退链路；已同步生成 3 份中文结构化笔记，`processed_articles.json` 从 98 增至 101，重试队列保持 12 条不变。
- 2026-06-12：完成当天目录初始化、去重基线检查和外部检索。先检查 Cambridge HPL 最新期与 Nature 检索页，本轮未确认到清晰且未重复的新增正式论文，于是补入 3 条新的高相关 arXiv 预印本：`10.48550/arXiv.2604.20124`、`10.48550/arXiv.2603.05282`、`10.48550/arXiv.2603.04606`。三条 PDF 均通过环境代理路径直接下载成功，并同步生成中文结构化笔记；`processed_articles.json` 从 95 增至 98，重试队列保持 12 条不变。
- 2026-06-11：完成配置恢复后的队列重试验证。当前 Codex shell 由 `codex doctor` 确认为 `danger-full-access` 且 network enabled；单篇 arXiv smoke test 可经 `127.0.0.1:1087` 成功下载。随后执行 `python scripts/retry_download_queue.py --source-family other` 恢复 6 条 arXiv PDF，执行 `python scripts/retry_download_queue.py --source-family cambridge` 恢复 3 条 Cambridge/JPP PDF；`processed_articles.json` 从 86 增至 95，重试队列从 21 收敛到 12，剩余均为来源侧限制。
- 2026-06-11：完成当天目录初始化、去重基线检查和外部检索。优先尝试正式来源增量后，未找到清晰且未重复的官方新条目，转而补入 3 条新的高相关 arXiv 预印本：`10.48550/arXiv.2606.06232`、`10.48550/arXiv.2605.18542`、`10.48550/arXiv.2604.00462`。三条候选的本地 PDF 下载继续全部失败，错误模式与昨日一致：`curl` 经环境代理无法连接 `127.0.0.1:1087`，直连则 DNS 无法解析 `arxiv.org` / `doi.org`。已更新 `daily/2026-06-11/`、`state/daily_retry_candidates.json` 与项目文档。
- 2026-06-10：完成当天目录初始化、去重基线检查和外部检索。先排除了历史 `daily/2026-04-01/` 已处理过的旧 arXiv 题目，再补入 3 条新的高相关 2026 arXiv 预印本：`10.48550/arXiv.2602.19110`、`10.48550/arXiv.2603.28473`、`10.48550/arXiv.2604.09032`。三条候选的本地 PDF 下载继续全部失败，错误模式与昨日一致：`curl` 经环境代理无法连接 `127.0.0.1:1087`，直连则 DNS 无法解析 `arxiv.org` / `doi.org`。已更新 `daily/2026-06-10/`、`state/daily_retry_candidates.json` 与项目文档。
- 2026-06-09：通过 Cambridge Core / JPP 官方页面确认 3 条新的高相关候选并完成去重：`10.1017/S0022377825101050`、`10.1017/hpl.2026.10152`、`10.1017/hpl.2026.10147`。3 条候选的本地 PDF 下载继续全部失败，但这次失败已明确表现为 `curl` 经环境代理无法连接 `127.0.0.1:1087`、直连 DNS 无法解析主机。已更新 `daily/2026-06-09/`、`state/daily_retry_candidates.json` 与项目文档。
- 2026-06-09：修补 `scripts/safe_pdf_download.py` 的失败分类回归，新增 `curl` 回退路径下对代理不可连与 DNS 失败的识别，并补充单元测试，避免当前这类运行环境阻塞再被误记为 `unknown`。
- 2026-06-08：新增 `scripts/retry_download_queue.py`，并增强 `scripts/safe_pdf_download.py` 支持失败分类、`curl` 传输回退和结构化报告输出。随后在当前可联网环境下自动回填了 `2026-06-07` 与 `2026-06-08` 的 6 条 Cambridge / JPP 积压 PDF，使 `processed_articles.json` 从 80 条提升到 86 条，重试队列从 18 条收敛到 12 条；剩余条目已明确分类为 Elsevier `HTTP 403`、Nature cookie wall 与 IOP bot wall。
- 2026-06-08：通过 Cambridge Core 官方 `Accepted Manuscripts` 页面确认 3 条新的高相关候选并完成去重，分别覆盖冲击点火下的 SRS/SBS 增长、双锥点火中的 colliding-plasma shock breakout，以及高重复频 LWFA 光导与电子加速。3 条候选的本地 PDF 下载继续全部因 `Operation not permitted` / DNS 失败受阻，已更新 `daily/2026-06-08/`、`state/daily_retry_candidates.json` 与项目文档。
- 2026-06-07：通过 Cambridge Core 官方论文页与 accepted manuscript 页面确认 3 条新的高相关候选并完成去重，其中 2 条为 HPLSE 官方 accepted manuscript，1 条为 Journal of Plasma Physics 正式论文。3 条候选的本地 PDF 下载继续全部因 `Operation not permitted` / DNS 失败受阻，已更新 `daily/2026-06-07/`、`state/daily_retry_candidates.json` 与项目文档。
- 2026-06-06：集中回填历史缺失 PDF，成功补回唯一论文 29 篇；从重试队列移除 35 条成功记录并额外清理 1 条重复失败记录，当前重试队列收敛到 12 条。详情见 `daily/2026-06-06/pdf-backfill.md`。
- 2026-06-06：修复 `scripts/safe_pdf_download.py` 对 Cambridge Core 文章页 / DOI 落地页的误判问题。脚本现在会从 HTML 页面中的 `citation_pdf_url` 与官方 PDF 链接继续跟进下载，并新增单元测试覆盖“HTML 落地页 -> PDF”链路。
- 2026-06-06：通过 Nature Portfolio 与 Cambridge Core 官方页面确认 3 条新的高相关候选并完成去重，其中 1 条为正式论文、2 条为官方 accepted manuscript。3 条候选的本地 PDF 下载均因 `Operation not permitted` / DNS 失败受阻，已更新 `daily/2026-06-06/`、`state/daily_retry_candidates.json` 与项目文档。
- 2026-06-05：通过 ScienceDirect、Nature Portfolio 与 Cambridge Core 官方页面确认 3 条新的高相关候选并完成去重，其中 2 条为正式论文、1 条为官方 accepted manuscript。3 条候选的本地 PDF 下载均因 `Operation not permitted` / DNS 失败受阻，已更新 `daily/2026-06-05/`、`state/daily_retry_candidates.json` 与项目文档。
- 2026-06-04：通过正式来源检索确认 3 条新的正式论文候选并完成去重；剔除了已在 `processed_articles.json` / `daily_retry_candidates.json` 中的旧论文。3 条候选的本地 PDF 下载均因 `Operation not permitted` / DNS 失败受阻，已更新 `daily/2026-06-04/`、`state/daily_retry_candidates.json` 与项目文档。
- 2026-06-03：通过官方网页检索确认 3 条新的正式论文候选并完成去重；检索过程中剔除了已在 `processed_articles.json` / `daily_retry_candidates.json` 中的旧论文。3 条候选的本地 PDF 下载仍因 `Operation not permitted` / DNS 失败受阻，已更新 `daily/2026-06-03/`、`state/daily_retry_candidates.json` 与项目文档。
- 2026-06-02：通过官方网页检索确认 2 条新的正式论文候选并完成去重；剔除了 1 条已在 `processed_articles.json` 中的旧论文。本地 PDF 下载仍因 `Operation not permitted` / DNS 失败受阻，已更新 `daily/2026-06-02/`、`state/daily_retry_candidates.json` 与项目文档。
- 2026-06-01：完成当日目录初始化、去重基线装载与来源连通性诊断；外网出站受限（Operation not permitted），在线检索阻塞，未产生候选与可校验 PDF。
- 2026-05-31：完成当日目录初始化、去重基线装载与来源连通性诊断；外网出站受限（Operation not permitted），在线检索阻塞，未产生候选与可校验 PDF。
- 2026-05-30：完成当日目录初始化、去重基线装载与来源连通性诊断；外网出站受限（Operation not permitted），在线检索阻塞，未产生候选与可校验 PDF。
- 2026-05-29：完成当日目录初始化、去重基线装载与来源连通性诊断；外网出站受限（Operation not permitted），在线检索阻塞，未产生候选与可校验 PDF。
- 2026-05-27：完成当日目录初始化、去重基线装载与来源连通性诊断；外网出站受限（Operation not permitted），在线检索阻塞，未产生候选与可校验 PDF。
- 2026-05-26：完成当日目录初始化、去重基线装载与来源连通性诊断；外网出站受限（Operation not permitted），在线检索阻塞，未产生候选与可校验 PDF。

- 2026-05-25：完成当日目录初始化、去重基线装载与来源连通性诊断；外网出站受限（Operation not permitted），在线检索阻塞，未产生候选与可校验 PDF。
- 2026-05-24：完成当日目录初始化、去重基线装载与来源连通性诊断；外网出站受限（Operation not permitted），在线检索阻塞，未产生候选与可校验 PDF。
- 2026-05-23：完成当日目录初始化、去重基线装载与来源连通性诊断；外网出站受限（Operation not permitted），在线检索阻塞，未产生候选与可校验 PDF。
- 2026-05-22：完成当日目录初始化、去重基线装载与来源连通性诊断；外网出站受限（Operation not permitted），在线检索阻塞，未产生候选与可校验 PDF。
- 2026-05-21：完成当日目录初始化、去重基线装载与来源连通性诊断；外网出站受限（Operation not permitted），在线检索阻塞，未产生候选与可校验 PDF。
- 2026-05-20：完成当日目录初始化、增量候选检索与 2 条预印本下载尝试；外网受限（Operation not permitted / DNS 失败），未产生可校验 PDF。
- 2026-05-19：完成当日目录初始化、去重基线装载与来源连通性检查；外网受限（Operation not permitted / DNS 失败），未产生可校验 PDF。
- 2026-05-18：完成当日目录初始化、去重装载、1 条新候选检索与下载尝试；外网受限（Operation not permitted / DNS 失败），未产生可校验 PDF。
- 2026-05-17：完成当日目录初始化、去重基线装载与来源连通性检查；外网受限（Operation not permitted），未产生可校验 PDF。
- 2026-05-16：完成当日目录初始化、去重基线装载与来源连通性检查；外网受限（Operation not permitted），未产生可校验 PDF。
- 2026-05-15：完成当日目录初始化、去重基线装载与来源连通性检查；外网受限（Operation not permitted），未产生可校验 PDF。
- 2026-05-13：完成当日目录初始化与连通性诊断；外网来源不可达，未产生可校验 PDF。

## 阻塞点

- 队列里的 12 条旧阻塞已明确是来源侧访问限制：Elsevier `HTTP 403`、Nature cookie wall、IOP bot wall。
- `2026-06-09` Cambridge/JPP 3 条、`2026-06-10` arXiv 3 条和 `2026-06-11` arXiv 3 条已在配置恢复后全部补回 PDF，不再是 runtime-blocked 积压。

## 下一步

- 在每日自动化开始阶段优先按来源分组或限额运行 `scripts/retry_download_queue.py` 消化可恢复条目；只有在队列成分重新变化时才考虑更大的全量重试。
- 如果后续 automation UI 仍显示旧失败，需要确认是否只是读取旧 `run_results.json`，而不是重新执行下载命令。
- 对剩余的 Elsevier / Nature / IOP 条目，优先寻找合法 OA 镜像或作者稿来源，而不是在相同来源上重复空跑。
