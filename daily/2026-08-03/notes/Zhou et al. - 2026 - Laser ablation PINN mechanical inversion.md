# Measurement of multiple mechanical properties from multi-dimensional signals in nanosecond laser ablation via PINN

## 基本信息

- 作者：Ying Zhou；Jian Wu；Ziyuan Song；Jinghui Li；Xinyu Guo；Hao Sun；Yuhua Hang；Cuixiang Pei；Xingwen Li
- 期刊/平台：arXiv preprint（physics.plasm-ph；physics.app-ph；physics.data-an；physics.optics）
- DOI：https://doi.org/10.48550/arXiv.2607.26965
- 发表时间：2026-07-29
- 来源链接：https://arxiv.org/abs/2607.26965
- 本地 PDF：`daily/2026-08-03/pdfs/Zhou et al. - 2026 - Laser ablation PINN mechanical inversion.pdf`

## 研究问题

服役或老化钢材的弹性模量、屈服强度、抗拉强度和显微维氏硬度通常需要破坏性或单参数测量。纳秒激光烧蚀产生的等离子体发射、冲击波和表面波能否在同一套非接触诊断中，受能量守恒约束地同时反演这四类力学量？

## 方法与模型

- 在激光-靶相互作用微元上建立热--力耦合能量方程；以耦合系数 `β=-∂σ/∂T` 表征热扩散、力学功和相变/等离子体屏蔽间的动态能量分配。
- 将难直接测量的状态量替换为可观测特征：光谱反演电子温度 `Te`、Stark 展宽反演电子密度 `ne`、谱线强度 `Ispec`、冲击波压强 `P` 与表面波能量 `Es`。
- 用 1064 nm、10 ns、约 20 mJ Nd:YAG 激光烧蚀不同热处理状态的 #45 钢；光谱、冲击波和表面波同步采集，共使用 210 组实验数据。
- 构建两层、每层 8 个神经元的浅层 PINN，输出 `(E, σs, UTS, Hv)`，损失由数据项和能量守恒物理项共同构成；以常规拉伸/显微硬度测试为基准。

## 主要结论

- 文中 PINN 对 `E`、`σs`、`UTS` 与 `Hv` 的测试拟合报告 `R²=0.9927`、`0.9912`、`0.9916`、`0.9959`；作为对照，超声速度回归 `E` 的 `R²=0.0012`。
- 热处理 0--3 h 阶段中，屈服强度、抗拉强度和硬度下降，并伴随表面波能量、冲击波和谱线信号改变；3--9 h 的晶粒粗化与等离子体屏蔽波动使这些特征呈非单调耦合，说明单一观测量不足以稳定反演。
- 该工作把激光烧蚀等离子体的 `Te/ne/谱强` 与力学波信号放入统一能量账本，提供了面向材料状态的可解释多模态反演路径。

## 与本仓库方向的关系

- 属于激光-物质相互作用、实验诊断与机器学习交叉：诊断对象是纳秒激光烧蚀等离子体及其冲击/表面波响应。
- 对高能量密度实验和激光束流应用的工程诊断有方法学参考价值，尤其是将等离子体发射、冲击波和结构响应联合定量化的思路。
- 主题关键词：laser ablation；laser-produced plasma；PINN；LIBS；shockwave；surface wave；materials diagnostics；physics-informed machine learning。
- 相关性评分：4/5。

## 局限与注意事项

结果基于单一 #45 钢热处理序列、210 组数据和实验室纳秒激光参数；高 `R²` 主要是同一材料/工况内的反演表现，尚未证明能跨材料、表面状态、激光能量、环境压强或更高能量密度条件泛化。文中把局部热力学平衡、理想气体压强及可观测代理量纳入模型，这些假设在强非平衡或高不透明等离子体中需另行验证。
