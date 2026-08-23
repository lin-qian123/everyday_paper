# Neural network predictions of plasma confinement loss in Wendelstein 7-X pellet-fueled discharges

## 基本信息

- 作者：K. C. Hammond；J.-P. Bähner；J. Baldzuhn；等；W7-X team
- 期刊/平台：*arXiv preprint*（`physics.plasm-ph`）
- DOI：[10.48550/arXiv.2608.18325](https://doi.org/10.48550/arXiv.2608.18325)
- 发表时间：2026-08-18
- 来源链接：[arXiv 摘要页](https://arxiv.org/abs/2608.18325)
- 本地 PDF：`daily/2026-08-24/pdfs/W7-X neural confinement prediction.pdf`

## 研究问题与方法

作者以 Wendelstein 7-X 的 ECRH 加热、弹丸燃料实验为对象，训练数据驱动神经网络，由实时可得的温度和密度剖面预测高约束态还可维持多久（remaining time）。该预测可作为下一颗弹丸的注入截止时间，从而为实时燃料注入反馈提供输入。

## 主要结论

- 对历史放电的测试中，至少 `90%` 的预测误差不超过 `51 ms`，小于典型 W7-X 能量约束时间，也小于连续弹丸间的最小时间间隔。
- 文中观测到单颗弹丸后密度和约束增强会在约 `1–2 s` 内衰减；较大的弹丸通常对应更长的增强阶段，但状态还受 ECRH 功率和放电条件影响。
- 模型推理速度足以作为控制系统候选输入，用于按预测的 remaining time 调整弹丸注入率。

## 与本仓库方向的关系

- 主题关键词：机器学习；磁约束聚变；W7-X；弹丸注入；能量约束；实时控制。
- 这是一项将诊断数据驱动模型接入等离子体燃料与约束控制的实验数据研究，补充本仓库的 AI/ML 等离子体方向。
- 相关性评分：4/5。

## 局限与注意事项

模型基于既有 W7-X、纯 ECRH 加热的弹丸放电数据，并非已上线闭环控制实验；`51 ms` 是该数据集上的预测统计，不等同于任意磁约束装置、混合加热方案或反应堆条件下的可靠性。文章也不涉及激光等离子体、PIC 或激光束流应用。
