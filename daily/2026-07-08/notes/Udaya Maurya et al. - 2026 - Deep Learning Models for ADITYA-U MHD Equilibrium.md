# Deep Learning Models for ADITYA-U MHD Equilibrium

## 基本信息

- 作者：Udaya Maurya; Suman Aich; Indranil Bandyopadhyay; Daniel Raju
- 期刊/平台：arXiv preprint
- DOI：https://doi.org/10.48550/arXiv.2607.04865
- 发表时间：2026-07-06
- 本地 PDF：`daily/2026-07-08/pdfs/Udaya Maurya et al. - 2026 - Deep Learning Models for ADITYA-U MHD Equilibrium.pdf`

## 研究问题

托卡马克平衡重建通常依赖 Grad-Shafranov 求解器和诊断约束，计算成本与实时控制需求之间存在张力。论文面向 ADITYA-U 装置，研究深度学习是否可以在实验相关工作域内快速预测 MHD 平衡参数、一维安全因子剖面和二维极向磁通剖面。

## 方法与模型

- 使用 pyIPREQ Grad-Shafranov 求解器生成 `100,760` 个自由边界合成平衡样本。
- 输入约束来自 `766` 次 ADITYA-U 放电，并聚焦 flat-top 附近的圆形 limiter 等离子体。
- 比较 dense neural network、PCA 降阶模型、一维/二维卷积网络和带 Grad-Shafranov 残差约束的 physics-informed neural network。
- 额外建立反问题模型，用目标平衡条件估计极向场线圈电流。

## 主要结论

- 在训练数据覆盖的操作域内，模型能够高效预测关键平衡标量、q 剖面和极向磁通分布。
- 深度学习模型可作为传统平衡求解器的快速替代或前端近似，用于实时控制、快速分析和实验规划。
- 反问题模型提供了从目标平衡到线圈电流设置的快速估计路径。

## 与本仓库方向的关系

- 属于机器学习与等离子体物理交叉方向，也涉及 MHD 平衡和实验装置控制。
- 虽然不是激光等离子体论文，但其“物理求解器生成数据 + 神经网络快速替代 + physics-informed 约束”的流程，对 HEDP/PIC 代理模型和实验控制优化有方法参考价值。
- 可为后续用机器学习做等离子体状态重建、诊断反演和参数扫描降阶提供模板。

## 阅读价值

- 适合关注 plasma control、MHD equilibrium reconstruction、PINN、surrogate model 和实验规划的读者。
- 对需要把复杂等离子体求解器嵌入实时决策或大规模扫描的项目尤其有参考意义。

## 局限与注意事项

- 模型有效性受合成数据覆盖范围限制，超出 ADITYA-U limiter flat-top 操作域时需要重新训练或外推验证。
- 论文侧重磁约束聚变平衡，和激光加速/强场 QED 主线的物理对象不同，主要贡献在方法论和机器学习 workflow。
