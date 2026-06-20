# 每日论文索引 - 2026-06-11

## 今日新增论文索引

- 初始运行时未发现满足“新增且可完成 PDF 下载校验”的论文入库条目；2026-06-11 后续重试已恢复本日 3 条 PDF，并写入 `state/processed_articles.json`，中文结构化笔记仍待补。

## 今日高相关候选（已去重，PDF 已于后续重试恢复）

### 1) Plasma wakefield dynamics of self-generated electron bunch trains
- 作者：Salome Benracassa, Sheroy Tata, Yinren Shou, Aaron Liberman, Victor Malka
- 期刊/平台：arXiv 预印本（高相关补充）
- DOI：https://doi.org/10.48550/arXiv.2606.06232
- 真实发表日期：2026-06-04（arXiv submitted）
- 来源链接：https://arxiv.org/abs/2606.06232
- 与方向关系：聚焦激光尾场加速中的自发电子 bunch train 形成、能谱压缩和周期结构演化，并用 PIC 支撑实验解释，直接对应激光等离子体加速主线。

### 2) An explicit, energy-conserving particle-in-cell scheme for relativistic plasmas
- 作者：Lee Ricketson, Jingwei Hu
- 期刊/平台：arXiv 预印本（高相关补充）
- DOI：https://doi.org/10.48550/arXiv.2605.18542
- 真实发表日期：2026-05-18（arXiv submitted）
- 来源链接：https://arxiv.org/abs/2605.18542
- 与方向关系：工作核心是相对论 Vlasov-Maxwell 显式守恒 PIC 格式，兼容 Yee/FDTD 与 PSATD，对高能激光等离子体与强场数值模拟都具有直接方法学价值。

### 3) A machine learning framework for developing quasilinear saturation rules of turbulent transport from linear gyrokinetic data
- 作者：Preeti Sar, Sebastian De Pascuale, Harry Dudding, Gary Staebler
- 期刊/平台：arXiv 预印本（高相关补充）
- DOI：https://doi.org/10.48550/arXiv.2604.00462
- 真实发表日期：2026-04-01（arXiv submitted）
- 来源链接：https://arxiv.org/abs/2604.00462
- 与方向关系：用神经网络从线性 gyrokinetic 数据回归非线性饱和输运规则，属于 机器学习 加速等离子体湍流建模的高相关补充。

## 检索与去重执行记录

- 检索日期：2026-06-11。
- 重点检索方向：激光等离子体、强场 QED、高能量密度物理、PIC，以及 机器学习在上述方向中的应用。
- 优先来源：先尝试正式发表来源增量；今天没有找到清晰且未重复的官方新条目后，补充转向高相关 arXiv 预印本。
- 去重基线：`state/processed_articles.json` 与 `state/daily_retry_candidates.json`（运行前唯一 DOI/标题键合计 202 条）。
- 本次新增候选：3 条，均未命中现有 processed/retry 台账；追加后唯一 DOI/标题键合计 208 条。

## 下载与校验状态

- 当日初始执行了 3 条候选论文 PDF 下载尝试，详见 `daily/2026-06-11/run_results.json`。
- 初始结果：三条候选均因当时运行环境外网阻塞失败，错误模式一致：
  - 走环境代理时 `curl` 无法连接 `127.0.0.1:1087`
  - 直连时 DNS 无法解析 `arxiv.org` 与 `doi.org`
- 后续恢复：2026-06-11 12:32 +0800 重试后，本日 3 条 arXiv PDF 均下载成功并通过 PDF 文件识别。
- 结论：初始阻塞是运行环境侧问题，不是候选本身的来源侧限制。

## 笔记产出

- 今日无新增中文结构化笔记（无校验通过的 PDF）。

## 状态更新

- 初始运行：`state/processed_articles.json` 无新增，保持 86 条；`state/daily_retry_candidates.json` 已追加今日 3 条新增候选，累计 21 条。
- 后续重试恢复（2026-06-11 12:32 +0800）：本日 3 条 arXiv 候选 PDF 均已下载校验并转入 `state/processed_articles.json`。

## 当日总结

- 今天补入了 3 条新的高相关 2026 预印本，分别覆盖激光尾场加速实验与 PIC 动力学、相对论守恒 PIC 数值格式，以及 机器学习 驱动的 gyrokinetic 湍流输运建模。
- 由于当前自动化运行时仍然无法连通外部网络，今天继续维持 blocked-day 模式：保留真实下载失败证据、更新去重台账与重试队列，但不向 processed 台账写入未校验论文。
