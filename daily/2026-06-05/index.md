# 每日论文雷达 - 2026-06-05

## 今日新增论文索引

- 今日未发现满足“新增且可完成 PDF 下载校验”的论文入库条目。

## 今日高相关候选（已去重，待重试）

### 1) Three-Dimensional Hybrid PIC-Fluid Simulation of Electron and Ion Dynamics in Laser-Produced Plasma Plumes
- 作者：Fundamental Plasma Physics 页面摘要可确认，作者名单待网络恢复后补全
- 期刊/平台：Fundamental Plasma Physics（正式期刊，Open Access，In Press）
- DOI：https://doi.org/10.1016/j.fpp.2026.100125
- 真实发表日期：2026-05-25（Available online）
- 来源链接：https://www.sciencedirect.com/science/article/pii/S277282852600018X
- 与方向关系：激光产生等离子体 + 三维 hybrid PIC-fluid 建模 + 非局域输运与离子加速

### 2) Influence of plasma, surface, and angle on interlinked X-ray emission dynamics in femtosecond burst pulse ablation
- 作者：Daniel Metzner, Philipp Rebentrost, Peter Lickschat et al.
- 期刊/平台：Scientific Reports（正式期刊，Open Access）
- DOI：https://doi.org/10.1038/s41598-025-34221-x
- 真实发表日期：2026-01-08
- 来源链接：https://www.nature.com/articles/s41598-025-34221-x
- 与方向关系：超快激光-等离子体 X 射线发射 + 激光烧蚀等离子体动力学 + 高场诊断

### 3) Compensation of Carrier Envelope Phase Slip using Machine Learning
- 作者：Sung In Hwang, Jeong Moon Yang, Dongyoon Yoo et al.
- 期刊/平台：High Power Laser Science and Engineering（Accepted manuscript，官方已接收）
- DOI：https://doi.org/10.1017/hpl.2026.10129
- 真实发表日期：2026-05（Cambridge 官方 accepted manuscript，在线可引）
- 来源链接：https://www.cambridge.org/core/services/aop-cambridge-core/content/view/B32858B8FE18A723B7BE4BB80A4F8D9B/S2095471926101297a.pdf/compensation-of-carrier-envelope-phase-slip-using-machine-learning.pdf
- 与方向关系：AI/机器学习用于高功率飞秒激光控制 + CEP 稳定 + 强场实验基础设施

## 检索与去重执行记录

- 检索日期：2026-06-05。
- 重点检索方向：激光等离子体、强场 QED、高能量密度物理、PIC，以及 AI/机器学习在上述方向中的应用。
- 优先来源：ScienceDirect、Nature Portfolio、Cambridge Core 官方论文页 / 官方 accepted manuscript 页面。
- 去重基线：`state/processed_articles.json` 与 `state/daily_retry_candidates.json`（运行前唯一 DOI/标题键合计 85 条）。
- 本次新增候选：3 条，均未命中现有 processed/retry 台账。
- 说明：今天继续剔除了近期已处理或已在失败重试台账中的旧论文，例如 `10.1038/s41467-026-72697-x`、`10.1038/s41467-026-73196-9`、`10.1017/hpl.2026.10121` 与 `10.1038/s41586-026-10400-2`。

## 下载与校验状态

- 当日执行了 3 条候选论文 PDF 下载尝试，详见 `daily/2026-06-05/run_results.json`。
- 结果：三条候选均因本地运行环境网络受限失败，错误模式一致：
  - 走环境代理时返回 `Operation not permitted`
  - 直连时返回 DNS 解析失败 `nodename nor servname provided, or not known`
- `daily/2026-06-05/pdfs/` 无新增可校验 PDF。

## 笔记产出

- 今日无新增中文结构化笔记（无校验通过的 PDF）。

## 状态更新

- `state/processed_articles.json`：无新增（继续避免写入未校验论文）。
- `state/daily_retry_candidates.json`：已追加今日 3 条新增候选，待网络恢复后重试。

## 当日总结

- 今天补入了 2 条正式论文和 1 条官方 accepted manuscript，继续覆盖激光等离子体建模、超快激光等离子体诊断以及 AI 控激光三个子方向。
- 当前主阻塞仍是本地运行时外网出站；网络恢复后应优先把 `2026-06-05` 这 3 条与 `2026-06-03`、`2026-06-04` 的积压候选一起完成 PDF 校验与中文笔记。
