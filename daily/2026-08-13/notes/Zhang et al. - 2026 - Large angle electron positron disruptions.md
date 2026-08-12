# High-energy electron-positron beam collisions with large-angle disruptions

## 基本信息

- 作者：W. Zhang；T. Grismayer；L. O. Silva
- 期刊/平台：*arXiv preprint*（`physics.plasm-ph`、`physics.acc-ph`）
- DOI：https://doi.org/10.48550/arXiv.2608.10988
- 发表时间：2026-08-11
- 来源链接：https://arxiv.org/abs/2608.10988
- 本地 PDF：`daily/2026-08-13/pdfs/High energy electron positron beam collisions.pdf`

## 研究问题与方法

高亮度电子—正电子对撞中，常用束束程序把粒子近似为沿束轴以光速自由流动，因而忽略自洽纵向电场。本文引入无量纲大角度扰动参数 `ε`（同时为横向偏转角），推导横向偏转、纵向减速和感生纵向场的标度，并以三维全电磁 OSIRIS PIC 对照传统 GUINEA-PIG 束束模拟。扫描覆盖 `0.01 ≤ ε ≤ 1.7`；极端演示算例采用 10 GeV、`ε=3.5` 的对撞束。

## 主要结论

- 当 `ε ≳ 1`，纵向减速随 `ε²` 增长、感生纵向场幅度随 `ε` 增长；部分粒子可失去并反转纵向动量，因此自由流假设失效。
- 三维 PIC 验证了分析模型的动量损失标度；在高 `ε` 时，自洽纵向场与能量损失会加强聚焦并形成多环束密度结构。
- 对文中的 `ε=3.5` 算例，PIC 给出的光度约 `2.2×10^36 cm^-2 s^-1`，接近传统 GUINEA-PIG 预测的一个数量级以上；后者还出现 `|v_r|≈4c` 的非物理横向速度。
- 本文区分了 `ε` 控制的集体束动力学与束致辐射/对产生等 SF-QED 过程：二者都可耗散能量动量，但极端对照中关闭了后者，不能把该光度差直接归为 QED 产额预测。

## 与本仓库方向的关系

- 主题关键词：strong-field QED；electron-positron beam；beamstrahlung；pair production；large-angle disruption；OSIRIS；PIC。
- 该工作把强场 QED 可观测量的束束背景与全电磁 PIC 自洽性联系起来，提示极端束流参数区必须同时审计纵向场、能量谱和光度谱。
- 相关性评分：4/5。

## 局限与注意事项

这是未来对撞机参数的理论/PIC 研究，不是激光驱动电子束、转换靶或已实施的强场 QED 实验。高 `ε` 对照专门关闭了束致辐射和对产生，且分析模型的高长径比假设在部分高 `ε` 几何下需要与密度 pinch 的数值补偿共同解释；因此不能据此直接给出真实 SF-QED 产额、实验可达性或具体激光平台的性能结论。
