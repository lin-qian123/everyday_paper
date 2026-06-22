# 每日论文索引 - 2026-06-22

## 今日新增论文索引

- 今日新增并完成 PDF 校验入库 2 条，均来自正式发表来源。
- 2 条论文均已下载通过 PDF 校验，并已生成中文结构化笔记。
- 今天继续优先复查 Cambridge `Journal of Plasma Physics` 当前 issue；在 2026-06-21 已处理过更偏 wakefield / target engineering 增量后，本轮补入两条此前尚未入库、但与强场辐射反作用和“可微模拟器 + PIC + 机器学习”主线更直接相关的正式论文。

## 今日高相关候选（已去重，已完成 PDF 与笔记）

### 1) RR-induced breaking of ponderomotive invariants in EM modes
- 作者：Felipe Russman, Samuel Marini, Felipe Barbedo Rizzato, Iberê Luiz Caldas
- 期刊/平台：Journal of Plasma Physics（正式期刊）
- DOI：https://doi.org/10.1017/S0022377826101809
- 真实发表日期：2026-06-10（online）
- 来源链接：https://www.cambridge.org/core/journals/journal-of-plasma-physics/article/rrinduced-breaking-of-ponderomotive-invariants-in-em-modes/E30748825098B8A7C25777FE40575BA6
- 与方向关系：直接补强强场 QED / radiation reaction 理论主线。文章讨论 Landau-Lifshitz 辐射反作用如何破坏经典 ponderomotive invariant，并重写超强电磁脉冲中的粒子加速阈值与最终喷射速度。

### 2) Learning collision operators from plasma phase space data using differentiable simulators
- 作者：Diogo D. Carvalho, Pablo J. Bilbao, Warren B. Mori, Luis O. Silva, E. Paulo Alves
- 期刊/平台：Journal of Plasma Physics（正式期刊）
- DOI：https://doi.org/10.1017/S0022377826101755
- 真实发表日期：2026-06-10（online）
- 来源链接：https://www.cambridge.org/core/journals/journal-of-plasma-physics/article/learning-collision-operators-from-plasma-phase-space-data-using-differentiable-simulators/AF996FF9346FDF028DE03EFCD3F408ED
- 与方向关系：直接覆盖“机器学习在等离子体/PIC 中的应用”扩展主题。文章用 differentiable Fokker-Planck solver 和二维 PIC 数据反演 collision operator，连接了可微模拟、operator learning 和 kinetic plasma modelling。

## 检索与去重执行记录

- 检索日期：2026-06-22。
- 重点检索方向：强场辐射反作用、激光/电磁脉冲粒子加速、PIC 数值方法、可微模拟器与机器学习在等离子体中的应用。
- 优先来源：Cambridge `Journal of Plasma Physics` 当前 issue。
- 去重基线：`state/processed_articles.json` 与 `state/daily_retry_candidates.json`。
- 本次新增候选：2 条，均未命中现有 processed/retry 台账。

## 下载与校验状态

- 当日执行了 2 条候选论文 PDF 下载尝试，详见 `daily/2026-06-22/run_results.json`。
- 结果：2 条候选均通过环境代理路径下载，并通过 PDF 文件头校验。
- 今日没有重新运行 `scripts/retry_download_queue.py --source-family all`，因为旧重试队列仍是已明确的来源侧限制，继续全量跑只会在无效来源上耗时。
- 当前旧重试队列维持 12 条，仍全部属于来源侧限制：
  - 10 条 Elsevier / ScienceDirect `publisher_http_403`
  - 1 条 Nature `publisher_cookie_wall`
  - 1 条 IOP `publisher_bot_wall`

## 笔记产出

- 已生成 2 份中文结构化笔记：
  - `daily/2026-06-22/notes/Felipe Russman et al. - 2026 - RR-induced breaking of ponderomotive invariants in EM modes.md`
  - `daily/2026-06-22/notes/Diogo D. Carvalho et al. - 2026 - Learning collision operators from plasma phase space data using differentiable simulators.md`

## 状态更新

- `state/processed_articles.json`：从 128 条增至 130 条。
- `state/daily_retry_candidates.json`：保持 12 条，无新增来源失败重试记录。
- 当前“已补回 PDF 但尚无中文结构化笔记”的历史条目仍为 65 条。

## 当日总结

- 今天的增量继续偏“方法与物理机制补强”，不是常规凑数量：一篇从单粒子解析层补强强场辐射反作用下的加速阈值与守恒量破缺，一篇从可微模拟与 PIC 数据出发补强机器学习/闭式算子学习主线。
- 今天最值得优先读的是 `10.1017/S0022377826101755`，因为它同时触达 PIC、kinetic closure 和 ML 三条线，后续很容易被复用到更贴近 HEDP / beam-plasma 的 reduced-model 工作里。
