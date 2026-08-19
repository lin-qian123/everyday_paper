# 每日论文索引 - 2026-08-20

## 今日新增论文索引

- 新增 3 条高相关 arXiv 预印本，官方 PDF 均已通过 `%PDF-` 文件头、PDF 元数据、SHA-256 与可提取文本复核。
- 对 `processed_articles.json`、`daily_retry_candidates.json` 与历史 daily 进行了 DOI、规范化标题和全文硬去重；复核 arXiv 官方 Atom API 的近期 `physics.plasm-ph`、`physics.acc-ph` 与 `nucl-ex` 分类。12 条已知来源限制重试项未重复空跑。

### 1) Field deployment of a laser wakefield accelerator for on-site application

- DOI：[10.48550/arXiv.2608.17554](https://doi.org/10.48550/arXiv.2608.17554)
- 来源：[arXiv 摘要页](https://arxiv.org/abs/2608.17554)
- 价值：给出 `72 h` 连续束流稳定度、七个月现场试运行、钨转换靶高能 X 射线和工业 μCT 的完整实证链条；涡轮叶片 CT 达 `43 μm` 分辨率，适合作为激光电子束应用走向现场部署的基线。

### 2) Bayesian Optimization of Molybdenum-99 Production by Laser Wakefield Acceleration Using Coupled PIC and Monte Carlo Simulations

- DOI：[10.48550/arXiv.2608.17119](https://doi.org/10.48550/arXiv.2608.17119)
- 来源：[arXiv 摘要页](https://arxiv.org/abs/2608.17119)
- 价值：以 PIC 束流相空间—Ta 转换靶—openTOPAS 光核输运的闭环为目标函数，预测每发 `9.42×10^6` 个 `99Mo` 原子；是同位素应用的端到端计算优化，尚非实测产额。

### 3) Tunable high-charge relativistic electron beams via direct laser acceleration in hohlraum-preheated foam targets

- DOI：[10.48550/arXiv.2608.17772](https://doi.org/10.48550/arXiv.2608.17772)
- 来源：[arXiv 摘要页](https://arxiv.org/abs/2608.17772)
- 价值：黑腔软 X 预热泡沫与时序调控使 DLA 电子束达到约 `13 MeV` 有效温度、`80 MeV` 截止能和最高约 `471 nC/sr`（`>7.5 MeV`），为高通量转换靶和 HED 背光的上游束流设计提供实验/3D PIC 基线。

## 下载、笔记与状态

- 三份官方 arXiv PDF 均已通过 `%PDF-` 文件头、页数/元数据、SHA-256 和非空文本提取；PDF 按仓库规则保持本地忽略。
- 已生成中文结构化笔记并记录实证边界：现场 NDT 论文不涉及光核或医疗剂量；`99Mo` 论文是 PIC+MC 预测且依赖乐观的 kHz 激光假设；高电荷 DLA 论文未测转换后 γ、中子、活化或同位素产额。
- 台账由 273 条增至 276 条，随后重建总索引、分类索引、论文页和每日汇总。
