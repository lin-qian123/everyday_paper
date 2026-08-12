# 每日论文索引 - 2026-08-13

## 今日新增论文索引

- 新增 2 条高相关 arXiv 预印本，均由官方 PDF 下载并通过 `%PDF-` 文件头、PDF 元数据、SHA-256 和可提取文本复核。
- 对 `processed_articles.json`、`daily_retry_candidates.json` 与历史 daily 做 DOI、规范化标题和全文硬去重；通过 arXiv 官方 Atom API 检索近期 `physics.plasm-ph`、`physics.acc-ph`、`physics.comp-ph`、`nucl-ex` 与 `physics.ins-det` 条目。12 条历史来源限制重试项未重复空跑。

### 1) High-energy electron-positron beam collisions with large-angle disruptions

- DOI：https://doi.org/10.48550/arXiv.2608.10988
- 来源：https://arxiv.org/abs/2608.10988
- 价值：引入大角度扰动参数 `ε`，以全电磁 PIC 说明 `ε≳1` 时纵向减速和感生场改变光度及能谱；为极端束束 SF-QED 设计中的 PIC 自洽性审计提供边界。

### 2) Machine-learning surrogate models for nonlinear energetic-particle transport predictions in ITER

- DOI：https://doi.org/10.48550/arXiv.2608.11058
- 来源：https://arxiv.org/abs/2608.11058
- 价值：用 GP/层级 NN 代理非线性 FAR3d 快粒子输运，将完整 ITER 工况的输运评估从 158 小时降至秒量级，并显式比较两类不确定度表征。

## 下载、笔记与状态

- 2 份官方 arXiv PDF 已分别完成 `%PDF-` 文件头、20/22 页 PDF 元数据、SHA-256 与可提取文本复核；PDF 按仓库规则保持本地忽略。
- 已生成 2 份中文结构化笔记；电子—正电子工作是未来对撞机理论/PIC 并在极端对照关闭 SF-QED 过程，ITER 代理限于 FAR3d 的饱和稳态训练域，均未外推为激光平台或跨装置预测。
- 台账由 265 条增至 267 条，随后重建总索引、分类索引、论文页和每日汇总。
