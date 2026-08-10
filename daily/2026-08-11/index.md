# 每日论文索引 - 2026-08-11

## 今日新增论文索引

- 新增 2 条高相关的 *Nuclear Fusion* 开放接受稿；均从 IOP 官方 PDF 下载，并通过 `%PDF-` 文件头、PDF 元数据、可提取文本和 SHA-256 复核。
- 对 `processed_articles.json`、`daily_retry_candidates.json` 与历史 daily 做 DOI、规范化标题和全文硬去重。arXiv 官方 API 本轮返回限流页，故不把它作为候选证据；改由 OpenAlex 当日正式发表记录发现并以 IOP 官方落地页/PDF核验以下两篇。

### 1) Validation of hybrid-PIC Simulations for Advanced Beam-Driven FRC Modeling

- DOI：https://doi.org/10.1088/1741-4326/ae96c0
- 来源：https://iopscience.iop.org/article/10.1088/1741-4326/ae96c0
- 价值：扩展 WarpX hybrid-PIC，纳入 C-2W 的中性束、供料与端板偏压；对三类快离子驱动模及偏压/束流停源后的破裂或衰变给出实验对照。

### 2) Effect of nonuniform density structure on burn-up ratio of multi-shock-compressed DT fuel in fast ignition

- DOI：https://doi.org/10.1088/1741-4326/ae96c1
- 来源：https://iopscience.iop.org/article/10.1088/1741-4326/ae96c1
- 价值：二维燃烧模拟表明，多冲击实心 DT 靶的局域高密度核心不足以保证高燃耗；点火区周围的连续高密度路径是自持燃烧波的必要设计约束。

## 下载、笔记与状态

- 两份 IOP 官方接受稿 PDF 已完成 `%PDF-` 文件头、25/11 页 PDF 元数据、SHA-256 与可提取文本复核；PDF 按仓库规则保持本地忽略。
- 已生成 2 份中文结构化笔记；12 条历史来源限制重试项未重复空跑。
- 台账由 261 条增至 263 条，随后重建总索引、分类索引、论文页和每日汇总。
