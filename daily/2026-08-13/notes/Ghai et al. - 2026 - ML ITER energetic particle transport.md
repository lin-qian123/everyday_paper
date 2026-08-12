# Machine-learning surrogate models for nonlinear energetic-particle transport predictions in ITER

## 基本信息

- 作者：Yashika Ghai；Donald A. Spong；Jacobo Varela；Luis Garcia
- 期刊/平台：*arXiv preprint*（`physics.plasm-ph`）
- DOI：https://doi.org/10.48550/arXiv.2608.11058
- 发表时间：2026-08-11
- 来源链接：https://arxiv.org/abs/2608.11058
- 本地 PDF：`daily/2026-08-13/pdfs/ML ITER energetic particle transport.pdf`

## 研究问题与方法

ITER 燃烧等离子体中，Alfvén 本征模驱动的快粒子输运必须多次评估，却依赖昂贵的非线性三维计算。本文以含中性束离子和聚变 α 粒子的 FAR3d 回转流体 ITER 稳态模拟为训练源，用 `ρ、q、磁剪切、两类快粒子密度及其梯度` 的七维状态预测径向通量；比较多任务高斯过程（GP）与分内外半径区域的层级神经网络（NN），并分别以后验方差和 MC dropout 给出不确定度。

## 主要结论

- 一个完整非线性 FAR3d 工况（保留 11 份输运剖面）约需 158 墙钟小时 / 2528 GPU 小时；训练后 GP 与 NN 连同不确定度分别在约 `2.97 s` 与 `0.19 s` 生成同类输出，量级加速约 5–6 个数量级。
- 在约 9180 个局域状态构成的数据集中，局域/全局通量变异比在大部分区域低于 0.3；高变异主要聚集在 `ρ≈0.35` 的强输运、较大梯度区，说明该低维状态表示并非处处等效。
- 两种模型的全局预测精度相近；GP 在强输运峰值附近通常有更低剖面重构误差和更均一的不确定度，NN 的 MC-dropout 不确定度更能区分早、晚非线性饱和阶段。

## 与本仓库方向的关系

- 主题关键词：machine learning；surrogate model；ITER；energetic particle；alpha particle；Alfvén eigenmode；FAR3d；uncertainty quantification。
- 它是将高保真等离子体输运计算转换为可重复调用代理模型的案例，特别适合借鉴到 PIC/高能量密度计算中的参数扫描与不确定性报告设计。
- 相关性评分：4/5。

## 局限与注意事项

模型仅学习已进入非线性饱和的、两个指定 ITER 稳态剪切工况中的瞬时输运响应，而非 Alfvén 模增长的完整时间演化；训练/测试剖面也均来自同一 FAR3d 计算族。强输运与大梯度区域的特征空间密度较低、误差较大，因此不能把秒级推理直接外推到未见装置、瞬态失稳、激光等离子体或跨代码精度保证。
