# Generation of dense relativistic electron beams via vortex laser-driven self-generated magnetic pinching

## 基本信息

- 作者：Mingxuan Wei；Fengyu Sun；Zhongpeng Li；Xichen Hu；Huiting Ma；Guangwei Lu；等
- 期刊/平台：arXiv preprint（physics.plasm-ph；physics.acc-ph）
- DOI：https://doi.org/10.48550/arXiv.2608.03240
- 发表时间：2026-08-04
- 来源链接：https://arxiv.org/abs/2608.03240
- 本地 PDF：`daily/2026-08-06/pdfs/Chowdhury et al. - 2026 - Vortex laser electron beam pinching.pdf`

## 研究问题与机制

高电荷 LPA 电子束通常伴随大横向发散，限制转换靶、伽马/中子源和罕见核过程所需的有效通量密度。本文实验演示 Laguerre--Gaussian（LG）涡旋激光在欠密度等离子体中触发的 self-generated magnetic pinching（SMP）：内鞘层电子的瞬态横向 kick 将已加速电子装载到磁箍缩相区，自生方位磁场再通过 `v×B` 持续降低横向动量。

- SULF 1 PW 系统靶上 0.5 PW；14 J、30 fs、800 nm 激光经拓扑荷 `ℓ=1` 螺旋相位板聚焦到 1.2 mm 纯氮气靶，等离子体密度约 `7×10^18 cm^-3`。
- 给出形成判据 `S≈0.717 ℓ a0 [ne/(10^18 cm^-3)]^-3/4≈1`；PIC 模拟再现了远场分布和时序演化。

## 主要结论

- 在 SMP 工作点，LG 驱动的 `>15 MeV` 电子束发散角从高斯驱动的 `156±8 mrad` 降至 `50±3 mrad`；电荷从 `678±45 pC` 降至 `497±27 pC`，即准直改善约 3 倍但总电荷减少约 27%。
- 由实测电荷、发散和模拟束长估计，有效电子密度从 `6.4×10^17` 提升到 `4.5×10^18 cm^-3`，约 7 倍；最高能量从约 90 提升至 100 MeV。模拟得到约 45 mrad、535 pC，与实验相符。
- 作者外推 `ℓ=3`、1 PW、`ne≈2.3×10^19 cm^-3` 可得约 3.7 nC（>10 MeV）和约 60 mrad，这属于预测，不是本轮实验结果。

## 与本仓库方向的关系

- 直接连接激光加速电子束品质与高通量次级源：更高有效密度可提高紧凑伽马源、高通量中子与光核/罕见过程的相互作用概率。
- 亮点是加速过程中用激光模式与集体场做内部束流整形，而非在加速后加外部透镜；但是否转换为更高的绝对伽马/中子产额，仍需将该束流接入具体转换靶和输运模型验证。
- 相关性评分：5/5。

## 局限与注意事项

形成判据只在一个 `(ne, ℓ)` 实验点直接验证；更高功率、较大 OAM、nC 级电荷和 `>10^19 cm^-3` 有效密度均依赖 PIC 外推。LG 与高斯比较在固定入射能量下进行，LG 的有效 `a0` 更低，因此并非严格的等 `a0` 对照；且更低发散以 27% 电荷损失为代价，对总电荷主导的应用未必更优。转换靶能量沉积、辐射防护和下游探测也未建模。
