# Flow-based surrogate models for particle tracking

## 基本信息

- 作者：Matthias Remta；Yann Dutheil；Francesco Velotti
- 期刊/平台：*arXiv preprint*（`physics.acc-ph`）
- DOI：[10.48550/arXiv.2608.21080](https://doi.org/10.48550/arXiv.2608.21080)
- 发表时间：2026-08-21
- 来源链接：[arXiv 摘要页](https://arxiv.org/abs/2608.21080)
- 本地 PDF：`daily/2026-08-25/pdfs/Flow surrogate particle tracking.pdf`

## 研究问题与方法

作者以 CERN Proton Synchrotron 的 Xsuite 常规粒子追踪为真值，在十维装置参数空间训练 conditional flow matching（CFM），直接生成末态六维相空间分布；针对分布相关空间电荷，分别引入对初态粒子集做交叉注意力的 CA-CFM，以及以少量常规追踪粒子校正预测的 Hybrid-CFM。

## 主要结论

- 在十维单粒子 PS 任务中，CFM 的末态分布中位 `MMD²=3×10⁻⁴`，单次推理约 `0.04 s`，相对常规追踪快约三个数量级。
- vanilla CFM 在含 halo 的空间电荷基准中退化；CA-CFM 通过初态粒子集的交叉注意力维持整个 mixture-weight 扫描中的稳定误差。
- Hybrid-CFM 在每个查询仅追踪 `100` 个辅助粒子、训练集 `200` 个分布时，可匹配 vanilla CFM 用 `1500` 个分布训练的第 90 百分位 `MMD²`，并在等规模训练下将最差尾部误差最多降低约 `4` 倍。

## 与本仓库方向的关系

- 主题关键词：机器学习；粒子追踪；相空间；束流品质；空间电荷；加速器代理模型。
- 它为激光加速器后续束线、转换靶注入或诊断优化提供方法学参考，重点是分布级代理而不是激光—等离子体相互作用本身。
- 相关性评分：4/5。

## 局限与注意事项

训练与验证均基于 CERN PS 的规定十维任务和 Xsuite 基准；分布误差用 `MMD²` 概括，不能自动保证尾部损失、辐射、靶端剂量或机器保护等任务指标。模型仍需常规追踪训练，Hybrid-CFM 也需每次辅助追踪；不能把三个数量级加速外推为所有 PIC、LWFA 或强场 QED 全流程计算的性能承诺。
