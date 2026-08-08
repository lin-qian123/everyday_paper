# Polarization-Conditioned Fourier-enhanced DeepONet for Electric Field Reconstruction from EFISH Measurements

## 基本信息

- 作者：Zhijian Yang；Edwin Setiadi Sugeng；Yaqi Zhang；Anbang Sun；Tat Loon Chng
- 期刊/平台：arXiv preprint（physics.plasm-ph）
- DOI：https://doi.org/10.48550/arXiv.2608.05937
- 发表时间：2026-08-06
- 来源链接：https://arxiv.org/abs/2608.05937
- 本地 PDF：`daily/2026-08-09/pdfs/Yang et al. - 2026 - Fourier DeepONet EFISH electric field reconstruction.pdf`

## 研究问题与方法

EFISH 将沿探测光路积分的二次谐波信号反演为电场，受 Gouy 相移、波矢失配和未知全局场形限制，本质上是病态逆问题。作者提出 PC-FDON：Fourier 分支为这些光学核提供频谱归纳偏置；FiLM 与门控分支输入偏振标签，统一处理水平/竖直分量；将预测电场重新代入 EFISH 前向积分形成物理一致损失。以 95.6 万组归一化场--信号对训练，并用 MC dropout 给出逐点认知不确定度和 OOD 判据。

## 主要结论

- 在无噪、截断输入和含噪输入测试中，以 `MSE <= 4×10^-3` 为阈值的成功率分别为 99.6%、94.3% 与 95.1%；对训练的相位失配范围 `u∈[-1,-0.01]` 保持有效。
- 对未见的 Quartic/Raised-Cosine 场形、`SNR=20 dB` 测试，表现与仅支持竖直偏振的 DDON 相近；代价是 PC-FDON 在更强噪声下退化较快。
- 对盘状/齿状 SDBD 的三峰类分布，100 次 dropout 的超阈不确定度正确标为 OOD；对盘--盘、球--球电极的实测 EFISH，重建与模拟基准相符且判为 in-distribution。

## 与本仓库方向的关系

- 主题关键词：laser diagnostic；plasma；machine learning；DeepONet；physics-informed；electric field reconstruction。
- 直接关联激光诊断、等离子体电场反演和物理约束机器学习；EFISH 的纳秒/皮秒时间分辨可服务于脉冲放电与激光等离子体的可重复诊断。
- “前向物理一致性 + 置信度/OOD”链路比只报回归误差更适合迁移到 PIC 合成诊断、靶前鞘层或束流场反演。
- 相关性评分：4/5。

## 局限与注意事项

模型假设超极化率、密度和失配在轴向均匀，并依赖扫描平移的准稳态/可重复放电，不能做单发随机场重建。仅支持两种离散线偏振且每次只能反演一个分量；训练形状主要是平滑单峰/双峰或反对称场，尖锐多峰 SDBD 已显示为 OOD，不能将该精度外推到强非均匀激光等离子体。
