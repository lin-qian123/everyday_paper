# Bayesian Optimization of Molybdenum-99 Production by Laser Wakefield Acceleration Using Coupled PIC and Monte Carlo Simulations

## 基本信息

- 作者：Bruno Silveira Nunes；Nilson Dias Vieira Junior；Mirko Salomón Alva Sánchez；Alexandre Bonatto；Ricardo Elgul Samad
- 期刊/平台：*arXiv preprint*（`physics.acc-ph`、`physics.comp-ph`、`physics.plasm-ph`）
- DOI：[10.48550/arXiv.2608.17119](https://doi.org/10.48550/arXiv.2608.17119)
- 发表时间：2026-08-17
- 来源链接：[arXiv 摘要页](https://arxiv.org/abs/2608.17119)
- 本地 PDF：`daily/2026-08-20/pdfs/Nunes et al. - 2026 - Mo-99 production laser wakefield.pdf`

## 研究问题与方法

本文将准圆柱 FBPIC 的自调制 LWFA 扫描与 openTOPAS 蒙特卡洛耦合，以自然 Mo 靶中的 `100Mo(γ,n)99Mo` 产额为贝叶斯优化目标，而不是仅优化电子束。每轮以 PIC 给出完整电子相空间，电子经 `Ta` 转换靶产生韧致辐射并打 `5 cm` Mo 靶；在 Santos Dumont 上以 8 张 V100 GPU 跑 PIC、CPU 跑 MC。扫描气体密度、上下坡长度、平台长度和聚焦位置，驱动脉冲设为 `10 TW`、`35 fs`、`372 mJ`。

## 主要结论

- 最优模拟为 `nH=2.84×10^19 cm^-3`、`1 mm` 上坡、`286.5 μm` 平台和 `5 μm` 下坡；PIC 束流 `>8 MeV` 部分的电荷 `2.48 nC`、平均能量 `58.6 MeV`、最高 `249 MeV`、激光到束流能量转换效率 `39.1%`。
- 该相空间送入 MC 后，自然 Mo 靶的预测 `99Mo` 产额为每发 `9.42×10^6` 原子，比作者先前“仅 PIC 优化、事后 MC 评估”的工作提高超过一个数量级。
- 在假设 `1 kHz` 重复频率下，模型估计自然 Mo 约 `10 h` 可到 `370 MBq` 的 `99mTc` 活度；完全富集 `100Mo` 将单发 `99Mo` 产额按 `10.4` 倍提高，估算时间低于 `3 h`。
- 目标函数直接包含转换和光核步骤，因此发现仅有束流电荷不足以决定同位素产额；平均电子能量超过约 `45 MeV` 和较高激光—束流转换同样关键。

## 与本仓库方向的关系

- 主题关键词：LWFA；PIC；Monte Carlo；Bayesian optimization；Ta converter；bremsstrahlung；photonuclear；Mo-99；Tc-99m。
- 提供激光电子束—转换靶—光核同位素产额的端到端计算优化例子，并明确将 PIC 相空间而非理想高斯束作为核反应输运输入。
- 相关性评分：5/5。

## 局限与注意事项

这是 PIC+MC 预测，非 `99Mo` 实测。`1 kHz`、数百 mJ 脉冲是作者明确标注为当前尚不可获得的乐观假设；最优 `5 μm` 下坡也可能难以实验实现。优化未纳入不期望的光核反应、中子和二次粒子，因而不能把预测产额写成已完成的临床生产、剂量、辐射防护或设施安全验证。
