# 每日论文索引 - 2026-08-10

## 今日新增论文索引

- 新增 3 条高相关 arXiv 预印本，均由官方 PDF 下载并通过 `%PDF-` 文件头、PDF 元数据和可提取文本复核。
- 对 `processed_articles.json`、`daily_retry_candidates.json` 与历史 daily 做 DOI、规范化标题和全文硬去重；使用 arXiv 官方 API 的 `physics.plasm-ph`、`physics.acc-ph`、`physics.comp-ph`、`nucl-ex` 与 `physics.ins-det` 近期条目筛选。该集合在周末没有 2026-08-06 之后的新投稿，故补入此前未处理的 8 月 6 日高相关稿。

### 1) SafeDivertor: Faithful Divertor Heat Flux Reconstruction from Macroscopic Plasma State Signals via Time-Frequency Prior Exploitation

- DOI：https://doi.org/10.48550/arXiv.2608.05669
- 来源：https://arxiv.org/abs/2608.05669
- 价值：以 67 路宏观状态信号在线重建 116 路偏滤器热流；炮次级隔离的测试集上，SafeDivertor 将 MSE 降至 0.200、SSIM 提至 0.870，并以多尺度频谱损失保留瞬态结构。

### 2) BORAY-3D: A ray tracing code for three-dimensional magnetized plasma configurations

- DOI：https://doi.org/10.48550/arXiv.2608.05667
- 来源：https://arxiv.org/abs/2608.05667
- 价值：把宽频 IC/helicon/LH/EC 射线追踪、任意二维/三维磁构型与相对论 EC 吸收/ECE 放入同一柱坐标框架，并与 GENRAY、Raytrax、TRAVIS 及公开结果对比。

### 3) Millisecond-Scale Neural Operator Surrogates for Double-Null Free-Boundary Grad--Shafranov Equilibria

- DOI：https://doi.org/10.48550/arXiv.2608.05555
- 来源：https://arxiv.org/abs/2608.05555
- 价值：对单几何双零位 FreeGS 家族，FNO 以 2.77 ms GPU 推理重建极向磁通，报告 0.052% 平均相对 L2 误差与约 640 倍配置内加速，同时检验 X/O 点和 GS 残差。

## 下载、笔记与状态

- 3 份官方 arXiv PDF 已分别完成 `%PDF-` 文件头、11/12/13 页 PDF 元数据、SHA-256 与可提取文本复核；PDF 按仓库规则保持本地忽略。
- 已生成 3 份中文结构化笔记；12 条历史来源限制重试项未重复空跑。
- 台账由 258 条增至 261 条，随后重建总索引、分类索引、论文页和每日汇总。
