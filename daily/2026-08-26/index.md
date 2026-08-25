# 每日论文索引 - 2026-08-26

## 今日新增论文索引

- 新增 3 条高相关 arXiv 预印本，官方 PDF 均通过 `%PDF-` 文件头、PDF 元数据、SHA-256 与可提取文本复核。
- 先对 `processed_articles.json`、`daily_retry_candidates.json` 和历史 daily 进行 DOI、规范化标题及主题内容去重；本轮以官方 arXiv `physics.plasm-ph` 近期提交为主，未发现更高优先级且可获得的正式发表增量。12 条已知来源限制重试项未重复空跑。

### 1) Wavefront-Guided Electron Injection for Direct Laser Acceleration in Relativistic Laser-Driven Plasma Channel

- DOI：[10.48550/arXiv.2608.22211](https://doi.org/10.48550/arXiv.2608.22211)
- 来源：[arXiv 摘要页](https://arxiv.org/abs/2608.22211)
- 价值：以二维 EPOCH PIC 将近临界 DLA 的前沿密度堆积、局域横向相空间筛选、磁岛与持续电子注入关联起来。

### 2) Helical jets driven by a ring of laser irradiation

- DOI：[10.48550/arXiv.2608.23466](https://doi.org/10.48550/arXiv.2608.23466)
- 来源：[arXiv 摘要页](https://arxiv.org/abs/2608.23466)
- 价值：提出 OMEGA 约束下的顺序环形激光靶设计，利用 FLASH 3D MHD 预测高螺度 HED 射流及 X 射线/Thomson 合成诊断指纹。

### 3) AI Surrogate Modeling for Real-Time Tokamak Equilibrium Prediction: Benchmarking Neural Architectures and Validation on EXL-50U

- DOI：[10.48550/arXiv.2608.23217](https://doi.org/10.48550/arXiv.2608.23217)
- 来源：[arXiv 摘要页](https://arxiv.org/abs/2608.23217)
- 价值：在统一 GS 数据集上量化五种神经网络的插值、OOD 和延迟权衡，并用 EXL-50U/Shape Editor 参考平衡做装置关联对照。

## 下载、笔记与状态

- 三份官方 arXiv PDF 均已通过 `%PDF-` 文件头、18/9/40 页元数据、SHA-256 和非空文本提取；PDF 按仓库规则保持本地忽略。
- 已生成中文结构化笔记并标注证据边界：DLA 是二维无辐射反作用 PIC；螺旋射流是 FLASH/合成诊断提案；AI 平衡代理只与数值/SE 参考解对照，未构成真机闭环控制。
- 台账由 291 条增至 294 条，随后重建总索引、分类索引、论文页和每日汇总。
