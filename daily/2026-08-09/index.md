# 每日论文索引 - 2026-08-09

## 今日新增论文索引

- 新增 3 条高相关 arXiv 预印本，均由官方 PDF 下载并通过 `%PDF-` 文件头、PDF 元数据和可提取文本复核。
- 对 `processed_articles.json`、`daily_retry_candidates.json` 与历史 daily 做 DOI、规范化标题和全文硬去重；使用 arXiv 官方近期列表与单篇页检查 `physics.plasm-ph`、`physics.acc-ph`、`physics.comp-ph`、`nucl-ex` 与 `physics.ins-det`。

### 1) Polarization-Conditioned Fourier-enhanced DeepONet for Electric Field Reconstruction from EFISH Measurements

- DOI：https://doi.org/10.48550/arXiv.2608.05937
- 来源：https://arxiv.org/abs/2608.05937
- 价值：为 EFISH 激光等离子体电场反演引入偏振条件 Fourier DeepONet、物理一致损失与 OOD 不确定度；含噪、截断输入测试中 `MSE<=4×10^-3` 的成功率仍为 95.1% 与 94.3%。

### 2) Net electron spin rotation in a plane-wave pulse: Holonomy set by the anomalous magnetic moment

- DOI：https://doi.org/10.48550/arXiv.2608.05698
- 来源：https://arxiv.org/abs/2608.05698
- 价值：给出有限脉冲后电子净自旋旋转的异常磁矩 holonomy 面积律，并量化聚焦背景会轻易淹没该极小信号的束腰条件。

### 3) Building a Start-to-End Model of the CESR Injector Linac

- DOI：https://doi.org/10.48550/arXiv.2608.05094
- 来源：https://arxiv.org/abs/2608.05094
- 价值：以 WarpX--Geant4--Impact-T/openPMD 跟踪电子束到钨转换靶、正电子产生与捕获，定量暴露转换靶后二次束发散/能散导致的传输损失。

## 下载、笔记与状态

- 3 份官方 arXiv PDF 已分别完成 `%PDF-` 文件头、22/24/8 页 PDF 元数据、SHA-256 与可提取文本复核；PDF 按仓库规则保持本地忽略。
- 已生成 3 份中文结构化笔记；12 条历史来源限制重试项未重复空跑。
- 台账由 255 条增至 258 条，随后重建总索引、分类索引、论文页和每日汇总。
