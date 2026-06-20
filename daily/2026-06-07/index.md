# 每日论文雷达 - 2026-06-07

## 今日新增论文索引

- 今日未发现满足“新增且可完成 PDF 下载校验”的论文入库条目。

## 今日高相关候选（已去重，待重试）

### 1) Neural network-based deconvolution for GeV-Scale Gamma-Ray Spectroscopy
- 作者：Zhuofan Zhang, Mingxuan Wei, Kyle Fleck, Jun Liu, Xinjian Tan, Gianluca Sarri, Wenchao Yan
- 期刊/平台：High Power Laser Science and Engineering（Accepted manuscript，官方已接收）
- DOI：https://doi.org/10.1017/hpl.2026.10142
- 真实发表日期：2026-04-21（Published online by Cambridge University Press）
- 来源链接：https://www.cambridge.org/core/journals/high-power-laser-science-and-engineering/article/neural-networkbased-deconvolution-for-gevscale-gammaray-spectroscopy/2AB08C32D8EE51A389FBFC9696C6ED1A
- 与方向关系：机器学习反卷积直接服务于 GeV 伽马谱重建，面向强场 QED、高能量密度科学和激光驱动高能光子诊断，相关性高。

### 2) Generation of X-ray Spatiotemporal Vortices via Nonlinear Thomson Scattering
- 作者：Honggeng Wang, Fan Li, Kai-Hong Zhuang, Hao Peng, Baifei Shen, Yue-Yue Chen
- 期刊/平台：High Power Laser Science and Engineering（Accepted manuscript，官方已接收）
- DOI：https://doi.org/10.1017/hpl.2026.10117
- 真实发表日期：2026-02-16（Published online by Cambridge University Press）
- 来源链接：https://www.cambridge.org/core/journals/high-power-laser-science-and-engineering/article/generation-of-xray-spatiotemporal-vortices-via-nonlinear-thomson-scattering/0A87504E96FB1DFC71D3F9C2C5DDE77F
- 与方向关系：围绕非线性 Thomson 散射产生结构化 X 射线，直接连接激光等离子体辐射源、超快诊断与高场光源设计。

### 3) Plasma rotation driven by lasers with zero angular momentum
- 作者：Camilla Willim, Thales Silva, Luis O. Silva, Jorge Vieira
- 期刊/平台：Journal of Plasma Physics（正式期刊，Open Access）
- DOI：https://doi.org/10.1017/S0022377825101062
- 真实发表日期：2026-03-02
- 来源链接：https://www.cambridge.org/core/journals/journal-of-plasma-physics/article/plasma-rotation-driven-by-lasers-with-zero-angular-momentum/2520AF3C7BB408A786E25666F28AE043
- 与方向关系：研究零角动量激光驱动下的等离子体角动量转移，并结合多维 PIC/OSIRIS 模拟，和激光尾场/泡区动力学紧密相关。

## 检索与去重执行记录

- 检索日期：2026-06-07。
- 重点检索方向：激光等离子体、强场 QED、高能量密度物理、PIC，以及 AI/机器学习在上述方向中的应用。
- 优先来源：Cambridge Core 官方论文页、High Power Laser Science and Engineering accepted manuscript 页面、Journal of Plasma Physics 官方论文页。
- 去重基线：`state/processed_articles.json` 与 `state/daily_retry_candidates.json`（运行前唯一 DOI/标题键合计 181 条）。
- 本次新增候选：3 条，均未命中现有 processed/retry 台账；追加后唯一 DOI/标题键合计 187 条。
- 说明：今天继续剔除了已在历史台账中的旧论文，例如 `10.1038/s41586-026-10400-2`、`10.1140/epjp/s13360-026-07595-8` 与 `10.1038/s42005-026-02505-x`。

## 下载与校验状态

- 当日执行了 3 条候选论文 PDF 下载尝试，详见 `daily/2026-06-07/run_results.json`。
- 结果：三条候选均因本地运行环境网络受限失败，错误模式一致：
  - 走环境代理时返回 `Operation not permitted`
  - 直连时返回 DNS 解析失败 `nodename nor servname provided, or not known`
- `daily/2026-06-07/pdfs/` 无新增可校验 PDF。

## 笔记产出

- 今日无新增中文结构化笔记（无校验通过的 PDF）。

## 状态更新

- `state/processed_articles.json`：无新增（继续避免写入未校验论文）。
- `state/daily_retry_candidates.json`：已追加今日 3 条新增候选，待网络恢复后重试；当前累计 15 条。

## 当日总结

- 今天补入了 2 条 Cambridge 官方 accepted manuscript 和 1 条 Cambridge 正式期刊论文，覆盖了 AI 伽马谱反演、非线性 Thomson 散射 X 射线涡旋源，以及激光驱动等离子体角动量转移。
- 当前主阻塞仍是本地运行时外网出站；网络恢复后应优先连同现有 ScienceDirect/IOP/Nature 积压项一起完成 PDF 校验与中文笔记。

## 后续回填进展（2026-06-08）

- 上述 3 条候选已在 2026-06-08 通过重试队列自动补回 PDF，并从 retry 队列转入 `state/processed_articles.json`。
- 详见 `daily/2026-06-08/retry-recovery.md`。
