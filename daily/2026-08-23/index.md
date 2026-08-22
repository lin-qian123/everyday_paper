# 每日论文索引 - 2026-08-23

## 今日新增论文索引

- 新增 3 条高相关 arXiv 预印本，官方 PDF 均通过 `%PDF-` 文件头、PDF 元数据、SHA-256 与可提取文本复核。
- 对 `processed_articles.json`、`daily_retry_candidates.json` 与历史 daily 进行了 DOI、规范化标题和主题内容去重；复核 arXiv 官方 Atom API 的近期目标分类及激光/PIC/强场关键词结果。官方增量停在 `2026-08-20`，故从该未入库窗口筛选；12 条已知来源限制重试项未重复空跑。

### 1) Wavefront shaping of terahertz radiation using two-color flying-focus pulses with time-dependent focal velocities

- DOI：[10.48550/arXiv.2608.20142](https://doi.org/10.48550/arXiv.2608.20142)
- 来源：[arXiv 摘要页](https://arxiv.org/abs/2608.20142)
- 价值：以解析线源模型和 UPPE 模拟显示，减速双颜色飞行焦点的电离前沿可将 THz 辐射由锥形波前塑造成抛物面波前，为激光等离子体 THz 耦合提供可控几何。

### 2) Exact hierarchical algorithms for accelerating particle--mesh coupling in sparse-grid particle-in-cell methods

- DOI：[10.48550/arXiv.2608.19702](https://doi.org/10.48550/arXiv.2608.19702)
- 来源：[arXiv 摘要页](https://arxiv.org/abs/2608.19702)
- 价值：在二维 SGCT-/HSG-PIC 中，精确层级粒子—网格算法将沉积和插值热点分别加速至最高 `66.9×` 和 `62.6×`，为大粒子数动理学模拟提供可评估的数值路径。

### 3) Revisiting the Growth Rate of the Relativistic Tearing Instability: The Role of the Non-ideal MHD Structure

- DOI：[10.48550/arXiv.2608.19645](https://doi.org/10.48550/arXiv.2608.19645)
- 来源：[arXiv 摘要页](https://arxiv.org/abs/2608.19645)
- 价值：以 extrapolated-A 取代 constant-A 近似，并用二维 PIC 证实对低漂移速度下最不稳定撕裂波数的改进预测，为磁主导相对论重联建立线性基准。

## 下载、笔记与状态

- 三份官方 arXiv PDF 均已通过 `%PDF-` 文件头、11/20/12 页元数据、SHA-256 和非空文本提取；PDF 按仓库规则保持本地忽略。
- 已生成中文结构化笔记并标注证据边界：THz 工作是解析/UPPE 波前设计，PIC 工作是二维数值基准，相对论撕裂工作是理想化电流片的理论—PIC 比较；均不是已完成的束流、核应用或强场实验性能验证。
- 台账由 282 条增至 285 条，随后重建总索引、分类索引、论文页和每日汇总。
