# 每日论文索引 - 2026-07-05

## 今日新增论文索引

- 今日新增并完成 PDF 校验入库 3 条：均为 Cambridge `Journal of Plasma Physics` 正式论文。
- 3 条论文均已通过 DOI / Cambridge Core 页面解析到官方 PDF，并通过 PDF 文件头校验。
- 今天先复查 Cambridge `Journal of Plasma Physics` 与 `High Power Laser Science and Engineering` 页面；HPL 中两个看似新 DOI 的高相关条目已按标题在 `2026-06-08` 入库，因此跳过，转向真正未入库的 JPP 正式条目。

## 今日高相关候选（已去重，已完成 PDF 与笔记）

### 1) Saturation of collisionless ion temperature gradient turbulence via symmetric dynamics. I. The zonal flow

- 作者：A.A. Azelis; P.W. Terry
- 期刊/平台：Journal of Plasma Physics
- DOI：https://doi.org/10.1017/S0022377826101883
- 真实发表日期：2026-06
- 来源链接：https://doi.org/10.1017/S0022377826101883
- 与方向关系：论文解析碰撞无关 ITG 湍流中 zonal flow 的非线性饱和机制，直接服务于磁约束聚变、gyrokinetic/流体化湍流建模和输运抑制问题。

### 2) Constructing field-aligned coordinate systems for gyrokinetic simulations of tokamaks in X-point geometries

- 作者：Akash Shukla et al.
- 期刊/平台：Journal of Plasma Physics
- DOI：https://doi.org/10.1017/S0022377826101779
- 真实发表日期：2026-06
- 来源链接：https://doi.org/10.1017/S0022377826101779
- 与方向关系：论文给出 tokamak X-point 几何下场线跟随坐标的构造算法，面向 core/SOL 一体化 gyrokinetic 模拟，是 PIC/动理学和磁约束边界模拟的基础数值方法条目。

### 3) Spectrally accurate, reverse-mode differentiable bounce-averaging algorithm and its applications

- 作者：Kaya Unalmis et al.
- 期刊/平台：Journal of Plasma Physics
- DOI：https://doi.org/10.1017/S0022377826101652
- 真实发表日期：2026-06
- 来源链接：https://doi.org/10.1017/S0022377826101652
- 与方向关系：论文实现谱精度、反向模式可微的 bounce-averaging 算法，并嵌入 DESC stellarator 优化套件，连接 kinetic model 简化、stellarator 设计优化和可微物理计算。

## 检索与去重执行记录

- 检索日期：2026-07-05。
- 重点检索方向：Cambridge JPP/HPL 正式来源，近期 `physics.plasm-ph` / `physics.acc-ph` / `physics.comp-ph` arXiv 候选，以及 fusion、gyrokinetic、PIC/ML 和 HEDP 相关关键词。
- 优先来源：正式发表来源优先；本轮正式来源足以形成 3 条高相关未入库增量，因此未再补入边缘 arXiv 条目。
- 去重基线：`state/processed_articles.json` 与 `state/daily_retry_candidates.json`；同时全文检索历史 `daily/`，确认 HPL `10.1017/hpl.2026.10159` 与 `10.1017/hpl.2026.10164` 已按标题在 `2026-06-08` 入库，故跳过。
- 本次新增候选：3 条，均未命中现有 processed/retry 台账。

## 下载与校验状态

- 当日执行了 3 条候选论文 PDF 下载尝试，详见 `daily/2026-07-05/*.download_report.json`。
- 结果：3 条候选均通过环境代理路径解析 Cambridge 官方 PDF 并下载成功。
- 今日没有重新运行 `scripts/retry_download_queue.py`，因为旧重试队列仍是 12 条明确来源侧限制条目，继续全量重试收益很低。

## 笔记产出

- 已生成 3 份中文结构化笔记：
  - `daily/2026-07-05/notes/A.A. Azelis and P.W. Terry - 2026 - Saturation of collisionless ion temperature gradient turbulence.md`
  - `daily/2026-07-05/notes/Akash Shukla et al. - 2026 - Constructing field-aligned coordinate systems for gyrokinetic simulations.md`
  - `daily/2026-07-05/notes/Kaya Unalmis et al. - 2026 - Spectrally accurate reverse-mode differentiable bounce-averaging algorithm.md`

## 状态更新

- `state/processed_articles.json`：从 165 条增至 168 条。
- `state/daily_retry_candidates.json`：保持 12 条，无新增来源失败重试记录。
- 当前“已补回 PDF 但尚无中文结构化笔记”的历史条目仍为 65 条。

## 当日总结

- 今天补强了三个正式来源方向：ITG 湍流 zonal-flow 饱和、tokamak X-point gyrokinetic 网格/坐标构造，以及 stellarator 优化中的可微 bounce averaging。
- 如果只优先读一篇，建议先看 `10.1017/S0022377826101779`，因为它最直接影响后续 tokamak core/SOL 一体化动理学模拟的几何与数值基础。
