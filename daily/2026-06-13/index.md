# 每日论文索引 - 2026-06-13

## 今日新增论文索引

- 今日新增并完成 PDF 校验入库 3 条，其中 1 条来自 Cambridge 正式期刊，2 条为在正式来源增量不足时补入的高相关 arXiv 预印本。
- 3 条论文均已下载通过 PDF 校验，并已生成中文结构化笔记。

## 今日高相关候选（已去重，已完成 PDF 与笔记）

### 1) Spectral and spatial ion beam parameter optimization at petawatt laser facilities
- 作者：Evgeny Filippov, Michael Ehret, Iuliana Mariana Vladisavlevici, Jose Luis Henares, Jose Antonio Perez-Hernandez, Carlos Salgado-Lopez, J. I. Apinaniz, Enrique Garcia-Garcia, R. Hernandez-Martin, Diego De Luis, Pilar Puyuelo-Valdes, Luca Volpe, Giancarlo Gatti
- 期刊/平台：High Power Laser Science and Engineering（正式期刊）
- DOI：https://doi.org/10.1017/hpl.2026.10136
- 真实发表日期：2026-06-08
- 来源链接：https://www.cambridge.org/core/journals/high-power-laser-science-and-engineering/article/spectral-and-spatial-ion-beam-parameter-optimization-at-petawatt-laser-facilities/0D7DD5608E6A14B3F752AD7DFD6A6E45
- 与方向关系：直接面向 PW 激光装置上的离子束通量、发散角和截止能量优化，属于激光等离子体与高能量密度实验束流工程的正式来源增量。

### 2) Multi-kilohertz laser plasma acceleration driven by an industrial-grade Yb:YAG laser
- 作者：Bonaventura Farace, Nikita Khodakovskiy, Rob Shalloo, Tae Gyu Pak, Esmerando Escoto, Supriya Rajhans, Arthur Schonberg, Ingmar Hartl, Jens Osterhoff, Christoph Heyl, Andreas Maier, Kristjan Poder, Wim Leemans
- 期刊/平台：arXiv 预印本（高相关补充）
- DOI：https://doi.org/10.48550/arXiv.2606.07147
- 真实发表日期：2026-06-05（arXiv submitted）
- 来源链接：https://arxiv.org/abs/2606.07147
- 与方向关系：聚焦高平均功率、多 kHz 重复频率的激光等离子体加速器实现，和紧凑辐射源、稳定高重复频运行直接相关。

### 3) High-order exponential solver method for particle-in-cell simulations in cylindrical geometry
- 作者：Szilard Majorosi, Nasr A. M. Hafz, Zsolt Lecz
- 期刊/平台：arXiv 预印本（高相关补充）
- DOI：https://doi.org/10.48550/arXiv.2605.12132
- 真实发表日期：2026-05-12（arXiv submitted）
- 来源链接：https://arxiv.org/abs/2605.12132
- 与方向关系：针对圆柱几何 LWFA/PIC 模拟提出高阶指数求解器，直接落在本仓库持续关注的 PIC 算法与激光等离子体数值建模上。

## 检索与去重执行记录

- 检索日期：2026-06-13。
- 重点检索方向：激光等离子体、强场 QED、高能量密度物理、PIC，以及 机器学习在上述方向中的应用。
- 优先来源：先检查 Cambridge HPL 最新卷与 Nature 检索页。Cambridge 确认到 1 条新的高相关正式论文；Nature 检索页本轮仍落到 `cookies_not_supported`，未形成稳定的正式增量筛选结果，因此再以 arXiv 补入 2 条高相关预印本。
- 去重基线：`state/processed_articles.json` 与 `state/daily_retry_candidates.json`（运行前唯一 DOI/标题键合计 211 条）。
- 本次新增候选：3 条，均未命中现有 processed/retry 台账；追加后唯一 DOI/标题键合计 214 条。

## 下载与校验状态

- 当日执行了 3 条候选论文 PDF 下载尝试，详见 `daily/2026-06-13/run_results.json`。
- 结果：1 条 Cambridge 正式论文与 2 条 arXiv 预印本均通过环境代理路径下载成功，并通过 PDF 文件识别校验。
- Cambridge 那篇起始 PDF 直链返回 `404`，但 `safe_pdf_download.py` 通过文章页 / DOI 落地页自动解析到了官方 PDF，说明当前 Cambridge HTML 落地页回退链路工作正常。
- 当前旧重试队列维持 12 条，仍全部属于来源侧限制：
  - 10 条 Elsevier / ScienceDirect `publisher_http_403`
  - 1 条 Nature `publisher_cookie_wall`
  - 1 条 IOP `publisher_bot_wall`

## 笔记产出

- 已生成 3 份中文结构化笔记：
  - `daily/2026-06-13/notes/Evgeny Filippov et al. - 2026 - Spectral and spatial ion beam parameter optimization at petawatt laser facilities.md`
  - `daily/2026-06-13/notes/Bonaventura Farace et al. - 2026 - Multi-kilohertz laser plasma acceleration driven by an industrial-grade YbYAG laser.md`
  - `daily/2026-06-13/notes/Szilard Majorosi et al. - 2026 - High-order exponential solver method for particle-in-cell simulations in cylindrical geometry.md`

## 状态更新

- `state/processed_articles.json`：从 98 条增至 101 条。
- `state/daily_retry_candidates.json`：保持 12 条，无新增来源失败重试记录。
- 当前“已补回 PDF 但尚无中文结构化笔记”的历史条目仍为 43 条。

## 当日总结

- 今天补入了 1 条正式来源增量和 2 条高相关预印本，分别覆盖 PW 激光离子束优化、高重复频 LPA 实验，以及圆柱几何 PIC 数值方法。
- 当前运行环境的 Cambridge / arXiv 下载链路都工作正常，因此今天完成了从检索、去重、PDF 校验到中文笔记生成的完整闭环。
