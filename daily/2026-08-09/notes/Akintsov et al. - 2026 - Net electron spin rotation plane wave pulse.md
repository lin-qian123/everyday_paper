# Net electron spin rotation in a plane-wave pulse: Holonomy set by the anomalous magnetic moment

## 基本信息

- 作者：N. S. Akintsov；A. P. Nevecheria；S. N. Andreev；Qing-Hua Qin
- 期刊/平台：arXiv preprint（hep-ph；交叉列入 physics.acc-ph、physics.plasm-ph）
- DOI：https://doi.org/10.48550/arXiv.2608.05698
- 发表时间：2026-08-06
- 来源链接：https://arxiv.org/abs/2608.05698
- 本地 PDF：`daily/2026-08-09/pdfs/Akintsov et al. - 2026 - Net electron spin rotation plane wave pulse.pdf`

## 研究问题与方法

研究相对论电子穿过有限时长平面波激光脉冲后仍保留多少净自旋旋转。作者在精确 `g=2` 演化的相互作用绘景下重写 Thomas--Bargmann--Michel--Telegdi 方程：脉冲只通过横向矢势在偏振平面围成的闭合曲线进入问题。再对任意脉冲形状推导二阶异常磁矩展开，并以 180 组脉冲验证 `g=2` 抵消、89 组验证面积律；最后估算聚焦、辐射和量子效应背景。

## 主要结论

- 净旋转是平行移动 holonomy：`Theta_net=-a_e^2 A/2`，其中 `a_e=(g-2)/2`，`A` 为矢势闭曲线的两倍有符号面积，也就是脉冲单位面积自旋角动量/螺旋度的量。
- 对带电电子，通常的 `g/2` 耦合在 Volkov 轨道上严格抵消，仅留异常磁矩通道；因此相对把电子当中性磁偶极子的估计抑制约 `1.3×10^-6`。线偏振时该面积为零，任何阶均无净旋转。
- 有限聚焦会在 `1/(k w0)^2` 阶恢复非异常背景；文中给出要令其低于异常信号，`gamma=10` 需 `w0≳16 lambda`，`gamma=1` 需 `w0≳270 lambda`，显示测量窗口非常苛刻。

## 与本仓库方向的关系

- 主题关键词：strong-field QED；laser；electron beam；spin polarization；radiation reaction；nonlinear Compton。
- 为强场激光--电子束相互作用中的自旋输运提供解析可检验基线，可与辐射自旋翻转、非线性 Compton/QED-PIC 的偏振诊断区分。
- 对偏振电子源和激光等离子体电子束方案，指出“脉冲内大进动”不等于“脉冲后可见净偏转”，需要把聚焦背景和异常磁矩小量一起纳入设计。
- 相关性评分：4/5。

## 局限与注意事项

核心结果严格限于有限时长平面波、真空 `a_e`、经典 BMT 自旋、无辐射反作用/自旋翻转/EDM/Stern--Gerlach 力。虽然文中估算聚焦和量子背景，但未作真实激光聚焦场、能散电子束、时空抖动或探测统计的端到端模拟；它是理论可观测性界，而非强场实验的直接可实现指标。
