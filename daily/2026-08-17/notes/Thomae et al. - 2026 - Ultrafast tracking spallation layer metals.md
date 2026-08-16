# Ultrafast Tracking of the Spallation Layer in Bulk Gold, Aluminum, and Steel

## 基本信息

- 作者：Nicolas Thomae；Julian Vollmann；Julian Freundel；Maximilian Spellauge；David Redka；Heinz P. Huber
- 期刊/平台：*arXiv preprint*（`physics.plasm-ph`）
- DOI：[10.48550/arXiv.2608.13198](https://doi.org/10.48550/arXiv.2608.13198)
- 发表时间：2026-08-13
- 来源链接：[arXiv 摘要页](https://arxiv.org/abs/2608.13198)
- 本地 PDF：`daily/2026-08-17/pdfs/Thomae et al. - 2026 - Ultrafast tracking spallation layer metals.pdf`

## 研究问题与方法

超短脉冲激光烧蚀金属时，近阈值的应力约束加热会形成并抛出液态飞溅层；传统泵浦—探测反射率中的 Newton 环在层变得不透明、或上方蒸汽/颗粒层强吸收散射时消失，因而无法区分“未形成飞溅层”和“诊断失去对比度”。本文将空间分辨泵浦—探测反射率（PPR）与相位敏感干涉泵浦—探测（PPI）联合使用，并以传输矩阵模型（TMM）同时拟合反射率变化和相位变化，追踪 AISI 304 钢、铝、金的飞溅层位移、厚度及上方蒸汽层吸收。

## 主要结论

- 实验采用 `1030 nm`、`1 ps` 泵浦脉冲和 `515 nm`、`300 fs` 探测脉冲，在约两倍烧蚀阈值下观察至 `3.5 ns`；当反射探测在金、铝中于约 `100 ps` 后降至 `ΔR/R0 < -0.95` 且 Newton 环消失时，PPI 相位仍可追踪运动前界面。
- 由相位振荡得到的飞溅层速度为：钢约 `1125 m/s`、铝约 `907 m/s`、金约 `330 m/s`。联合拟合给出的初始层厚度分别约 `13 nm`、`20 nm`、金至少 `28 nm`；金的数值是下限，因为光学不透明后数据对更大厚度不再敏感。
- 模型拟合的蒸汽层吸收从钢的 `21%` 升至铝的 `66%`、金的 `68%`，解释了反射率干涉信号消失而相位信号仍存在的原因。铝层约 `500 ps` 解体，钢在 `1–2 ns` 内变薄/解体，金在 `3.5 ns` 观测窗后仍保持不透明。
- 飞溅层寿命给出 GHz burst 模式后续脉冲可能遇到完整液层或已解体烧蚀物的时间边界，因而可为超快激光加工中的能量耦合、脉冲间隔选择和原位诊断提供实验约束。

## 与本仓库方向的关系

- 主题关键词：ultrashort-pulse laser；laser ablation；spallation；pump-probe；interferometry；transfer-matrix model；metal target；experimental diagnostic。
- 与“激光等离子体/高能量密度条件下的靶材响应和实验诊断”相关：它给出了激光—金属靶耦合后纳秒早期物质状态的直接实验约束，也能为高重复频率激光靶和次级源靶的时序设计提供参照。
- 相关性评分：4/5。

## 局限与注意事项

本文研究的是空气中工业相关块材的 `1 ps` 超快烧蚀，不是相对论强度激光、激光尾波场、TNSA 离子加速或转换靶产生伽马/中子的实验。TMM 对金的厚度只能给出下限，且作者以灵敏度/可辨识性而非完整统计误差条表示拟合约束；横向尺度受限的既有 MD 也尚不能再现实验所见的层解体。因此这些结果不能直接外推为高能量密度靶、辐射源产额、束流品质或辐射防护性能，只能作为超快激光靶表面演化与诊断方法的实验基线。
