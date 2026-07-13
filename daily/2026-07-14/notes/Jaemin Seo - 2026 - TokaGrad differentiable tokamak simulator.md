# TokaGrad: End-to-end differentiable tokamak simulator for L-to-H full scenario optimization

## 基本信息

- 作者：Jaemin Seo
- 期刊/平台：arXiv preprint
- DOI：https://doi.org/10.48550/arXiv.2607.09088
- 发表时间：2026-07-10
- 来源链接：https://arxiv.org/abs/2607.09088
- 本地 PDF：`daily/2026-07-14/pdfs/Jaemin Seo - 2026 - TokaGrad differentiable tokamak simulator.pdf`

## 研究问题

反应堆级 tokamak 场景设计涉及多执行器、非线性等离子体响应和多重物理/工程约束，传统手工调参或黑箱扫描成本高。论文关注能否把全放电场景模拟做成端到端可微计算图，使梯度能从目标函数反传到执行器波形、机器参数和等离子体响应，从而直接做场景优化。

## 方法与模型

- 提出 TokaGrad：端到端可微 tokamak 输运模拟器。
- 将等离子体平衡、输运、加热、L-H transition 和 pedestal formation 等模块自洽耦合。
- 覆盖 ramp-up、L-mode operation 和 H-mode access 等动态全场景。
- 与梯度优化器结合，演示反应堆设计优化、执行器控制和全场景波形优化。

## 主要结论

- 可微模拟框架能把机器参数、执行器波形和等离子体响应连接为统一计算图，并传播全流程 Jacobian。
- TokaGrad 可在同一框架内处理平衡、pedestal、约束模式转换和输运响应，避免完全黑箱化的参数扫描。
- 该路线为 burning-plasma scenario 和反应堆概念的自动化、梯度驱动优化提供了方法学入口。

## 与本仓库方向的关系

- 论文属于机器学习/先进算法与等离子体物理结合方向，虽然主场景是磁约束聚变而非激光等离子体，但对“可微模拟 + 梯度优化 + 等离子体控制”的方法框架有直接参考价值。
- 对 PIC、MHD 或 HEDP surrogate/differentiable modeling 工作也有启发：关键不只是训练替代模型，而是把物理模块、执行器、诊断目标和约束放入可优化链路。
- 主题关键词：differentiable simulation；tokamak；scenario optimization；plasma control；machine learning；gradient-based optimization。
- 相关性评分：4/5。

## 阅读价值

适合关注机器学习等离子体、可微物理模拟、聚变控制和全场景优化的读者。它提供了一个从黑箱优化转向白箱梯度优化的范例，有助于思考高维实验参数空间中的自动化设计问题。

## 局限与注意事项

当前为预印本，并且模拟器的物理保真度、边界条件、模型闭合和跨装置泛化仍需进一步验证。可微框架会提高优化效率，但也可能把模型偏差直接传递到梯度方向；用于实验决策前需要与高保真集成建模和真实放电数据交叉校验。
