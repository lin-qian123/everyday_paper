# 每日论文雷达 - 2026-06-10

## 今日新增论文索引

- 初始运行时未发现满足“新增且可完成 PDF 下载校验”的论文入库条目；2026-06-11 后续重试已恢复本日 3 条 PDF，并写入 `state/processed_articles.json`，中文结构化笔记仍待补。

## 今日高相关候选（已去重，PDF 已于后续重试恢复）

### 1) Machine learning prediction of plasma behavior from discharge configurations on WEST
- 作者：Chenguang Wan, Feda Almuhisen, Philippe Moreau, Remy Nouailletas, Zhisong Qu, Youngwoo Cho, Robin Varennes, Kyungtak Lim, Kunpeng Li, Jia Huang, Weidong Chen, Jiangang Li, Xavier Garbet
- 期刊/平台：arXiv 预印本（高相关补充）
- DOI：https://doi.org/10.48550/arXiv.2602.19110
- 真实发表日期：2026-02-22（arXiv submitted）
- 来源链接：https://arxiv.org/abs/2602.19110
- 与方向关系：虽然场景是 WEST 托卡马克，但文章核心是用 transformer 直接从预设放电配置预测全局等离子体参数，属于 AI/ML 加速等离子体建模与控制的高相关补充。

### 2) Simulation Design for Velocity-Controlled Spatio-Temporal Drivers in Laser Wakefield Acceleration
- 作者：Chiara Badiali, Rafael Almeida, Thales Silva, Jorge Vieira
- 期刊/平台：arXiv 预印本（高相关补充）
- DOI：https://doi.org/10.48550/arXiv.2603.28473
- 真实发表日期：2026-03-30（arXiv submitted）
- 来源链接：https://arxiv.org/abs/2603.28473
- 与方向关系：围绕 OSIRIS 中时空驱动激光尾场加速的 PIC 仿真设计与缩放规律，直接对应激光等离子体加速和数值建模主线。

### 3) A Fully Electromagnetic Hybrid PIC-Fluid Model for Predictive Fusion Neutron Yield in Dense Plasma Focus
- 作者：Yinjian Zhao, Zhe Liu, Qiang Sun, Qianhong Zhou, Guangrui Sun
- 期刊/平台：arXiv 预印本（高相关补充）
- DOI：https://doi.org/10.48550/arXiv.2604.09032
- 真实发表日期：2026-04-10（arXiv submitted）
- 来源链接：https://arxiv.org/abs/2604.09032
- 与方向关系：用混合 PIC-fluid 框架预测 dense plasma focus 的中子产额，贴近 HEDP、脉冲功率驱动等离子体与混合动理学建模。

## 检索与去重执行记录

- 检索日期：2026-06-10。
- 重点检索方向：激光等离子体、强场 QED、高能量密度物理、PIC，以及 AI/机器学习在上述方向中的应用。
- 优先来源：先尝试正式出版社来源增量；今日未找到清晰且未重复的官方新条目后，补充转向高相关 arXiv 预印本。
- 去重基线：`state/processed_articles.json` 与 `state/daily_retry_candidates.json`（运行前唯一 DOI/标题键合计 196 条）。
- 历史去重补充：额外排除了已在 `daily/2026-04-01/` 中出现过的 `Single-laser scheme for reaching strong field QED regime via direct laser acceleration`，避免重复处理旧预印本。
- 本次新增候选：3 条，均未命中现有 processed/retry 台账；追加后唯一 DOI/标题键合计 202 条。

## 下载与校验状态

- 当日初始执行了 3 条候选论文 PDF 下载尝试，详见 `daily/2026-06-10/run_results.json`。
- 初始结果：三条候选均因当时运行环境外网阻塞失败，错误模式一致：
  - 走环境代理时 `curl` 无法连接 `127.0.0.1:1087`
  - 直连时 DNS 无法解析 `arxiv.org` 与 `doi.org`
- 后续恢复：2026-06-11 12:32 +0800 重试后，本日 3 条 arXiv PDF 均下载成功并通过 PDF 文件识别。
- 结论：初始阻塞是运行环境侧问题，不是 arXiv 页面本身返回的来源侧限制。

## 笔记产出

- 今日无新增中文结构化笔记（无校验通过的 PDF）。

## 状态更新

- 初始运行：`state/processed_articles.json` 无新增，保持 86 条；`state/daily_retry_candidates.json` 已追加今日 3 条新增候选，累计 18 条。
- 后续重试恢复（2026-06-11 12:32 +0800）：本日 3 条 arXiv 候选 PDF 均已下载校验并转入 `state/processed_articles.json`。

## 当日总结

- 今天补入了 3 条新的高相关 2026 预印本，分别覆盖 AI/ML 等离子体参数预测、LWFA 时空驱动的 PIC 仿真设计，以及 dense plasma focus 的混合 PIC-fluid 建模。
- 由于当前自动化运行时仍然无法连通外部网络，今天继续维持 blocked-day 模式：保留真实下载失败证据、更新去重台账与重试队列，但不向 processed 台账写入未校验论文。
