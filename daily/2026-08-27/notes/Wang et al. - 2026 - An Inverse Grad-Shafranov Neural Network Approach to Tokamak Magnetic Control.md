# An Inverse Grad-Shafranov Neural Network Approach to Tokamak Magnetic Control 笔记

## 基本信息

- 作者：Allen M. Wang；Adriano Mele；Cosmas Heiß；Cristian Galperti；Zander Keith；Alessandro Pau；Antoine Merle；Olivier Sauter；Daniel Gonzalez Castiñeiras；Francesco Carpanese；Federico Felici；Mark Dan Boyer；Cristina Rea；TCV Team；EUROfusion Tokamak Exploitation Team
- 期刊/平台：*arXiv preprint*（`physics.plasm-ph`）
- DOI：[10.48550/arXiv.2608.23976](https://doi.org/10.48550/arXiv.2608.23976)
- 发表时间：2026-08-25
- 来源链接：[arXiv 摘要页](https://arxiv.org/abs/2608.23976)
- 本地 PDF：`daily/2026-08-27/pdfs/Inverse Grad-Shafranov neural network.pdf`

## 研究问题与控制架构

文章研究如何把目标等离子体边界快速转换为极向场线圈电流，从而提高 tokamak 磁形状控制的实时适应能力。核心观点是：在一组线圈、容器和等离子体响应近似下，实时 inverse Grad–Shafranov（IGS）求解器可看作近似的最优控制策略。

- 神经网络 surrogate 接收目标形状描述和内部等离子体参数，输出 PF 线圈电流；低层 RZIP 控制器负责线圈电流执行、约束和硬件隔离。
- 在 TCV 上用 LIUQE 等平衡重建/控制数据生成训练与测试集合；用于初始实验演示的数据集约含 `3.6×10^5` 个平衡态。
- 文章同时评估 LSN、DN、USN 等形状，比较网络预测误差、线圈电流误差、控制点误差，并测试 strike-point 扫描和触发早停等事件适应。

## 主要结果

- TCV 实验中，IGSnn 与传统放电准备流程相比实现了更灵活的 LSN 和 DN 等离子体成形。一个 TCV 测试集的线圈电流预测误差约 `18 A/coil`，而对照的较大误差约为 `56` 和 `105 A/coil`；作者将几十安培量级视为 TCV 可接受的测量/预测误差范围。
- TCV LSN 脉冲 `#86708/#86713` 的形状控制在偏滤器阶段控制点误差约数毫米，整体 RMSE 约 `7 mm`；过渡阶段约 `2.5 cm` 的 RMSE 被归因于 limiter-to-diverted transition，而不是稳定偏滤器阶段的典型误差。
- 对称 DN 的 strike-point 平衡和扫描在 TCV `#87970` 中进行了演示；基于 `β_p` 调整扫描幅度以及低 Ohmic flux 触发早停的完整适应能力主要在 FGE 仿真中展示，在实验中只做到了部分验证。
- 单一网络可覆盖多种目标形状，说明输入目标形状本身可以作为网络条件；但这属于在 TCV 数据和控制架构内的泛化，不等价于跨装置、跨诊断或聚变堆部署。

## 与本仓库方向的关系

- 主题关键词：机器学习；神经网络 surrogate；Grad–Shafranov；tokamak；实时控制；实验验证；等离子体形状。
- 对本仓库的价值主要在“物理求解器—代理模型—低层控制器—实验脉冲”的分层接口：它展示了如何把 ML 限定在可审计的 inverse-equilibrium 映射中，而把安全约束交给经典控制器。
- 相关性评分：3/5；来源层级评分：3/5（arXiv 预印本，但包含 TCV 实验与仿真两类证据）。

## 局限与注意事项

- 初始 TCV 实验并没有显式实时形状反馈；实时适应在仿真中较完整、在实验中部分实现。因此不能写成已经完成闭环 tokamak 控制或电站级控制验证。
- 文章的模型假设忽略或弱化部分 vessel/plasma 动力学，且控制性能与 TCV 线圈、诊断和 RZIP 低层控制器密切相关；跨装置迁移仍需重新训练和实验校验。
- 这不是激光加速或 PIC 论文；与激光等离子体方向的联系限于“物理约束 surrogate 和实时实验控制”的方法论借鉴。

## 复习用速记

把 inverse Grad–Shafranov 映射作为快速 surrogate，再用经典 RZIP 控制器承接线圈执行，是一种可审计的物理—ML 分层架构。TCV 的成形实验是真实证据，但实时适应和普适性仍只到部分实验/数值演示层级。
