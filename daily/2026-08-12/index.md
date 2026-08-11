# 每日论文索引 - 2026-08-12

## 今日新增论文索引

- 新增 2 条高相关 arXiv 预印本，均由官方 PDF 下载并通过 `%PDF-` 文件头、PDF 元数据、SHA-256 和可提取文本复核。
- 对 `processed_articles.json`、`daily_retry_candidates.json` 与历史 daily 做 DOI、规范化标题和全文硬去重；使用 arXiv 官方 Atom API 检索近期 `physics.plasm-ph`、`physics.acc-ph`、`physics.comp-ph`、`nucl-ex` 与 `physics.ins-det` 条目。12 条历史来源限制重试项未重复空跑。

### 1) Energy-optimized scaling laws for self-guided laser wakefield accelerators

- DOI：https://doi.org/10.48550/arXiv.2608.08903
- 来源：https://arxiv.org/abs/2608.08903
- 价值：用 BO 与 PIC 给出自引导 LWFA 的能量最优化标度；在规定扫描域内，`1 J`、`1 μm` 驱动对应约 `833 MeV` 和 `5.1 mm`，可为紧凑电子束平台的初始设计提供量级约束。

### 2) Terahertz-based longitudinal phase space diagnostics of laser wakefield accelerated electron beams

- DOI：https://doi.org/10.48550/arXiv.2608.08586
- 来源：https://arxiv.org/abs/2608.08586
- 价值：THz-TDC 与色散磁铁重建 DBA 压缩 LWFA 束团的非线性 LPS，在约 `4.55 MeV` 达到 `1.8 fs` 时间和 `6.0 keV` 能量分辨率，并将能量窗选择转化为可测量的束长优化问题。

## 下载、笔记与状态

- 2 份官方 arXiv PDF 已分别完成 `%PDF-` 文件头、14/9 页 PDF 元数据、SHA-256 与可提取文本复核；PDF 按仓库规则保持本地忽略。
- 已生成 2 份中文结构化笔记；标度仅适用于本文自引导 PIC 优化域，诊断仅在约 `4.55 MeV`、fC 级束线验证，均未外推为普适束流品质预测。
- 台账由 263 条增至 265 条，随后重建总索引、分类索引、论文页和每日汇总。
