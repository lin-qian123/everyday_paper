# Laser-Plasma Accelerator Beams in Light Sources: Femtosecond High-Brightness Radiation through Chirped Pulse Injection

## 基本信息

- 作者：Sergey A. Antipov；Philipp Burghart；Ilya Agapov；Alberto Martinez de la Ossa；Wim Leemans
- 期刊/平台：arXiv preprint（physics.acc-ph）
- DOI：https://doi.org/10.48550/arXiv.2608.04699
- 发表时间：2026-08-05
- 来源链接：https://arxiv.org/abs/2608.04699
- 本地 PDF：`daily/2026-08-07/pdfs/Antipov et al. - 2026 - LPA beams chirped pulse light sources.pdf`

## 研究问题与方法

LPA 束本身短而峰值流强高，却具有较大能散和运输困难。作者提出先在 LPA 注入器中解压束团并施加受控负能量啁啾，再利用储存环弧段的正 `R56` 在指定用户线站重新压缩；以 PETRA IV 6 GeV 等低发射度硬 X 射线储存环为例，从 LPA 源、注入线到一圈弧段进行 FBPIC/Optimas 与 Ocelot 起止端跟踪，并包含孔径和 CSR。

- 最优压缩条件是 `h=-1/R56`；射频电压用于把注入的能量-纵向位置相关调到目标线站。
- 基准 LPA 出口为 87 pC、3.7 kA、0.46% rms 能散；追踪后在用户线站选择高流强核心而非整束团性能。

## 主要结论

- 对 PETRA IV U61 示例，75 pC 可传至线站，其中 33 pC 核心重压缩至 2.3 µm rms、2.2 kA，模拟归一化发射度约 0.30/0.32 nm、相对能散 `3.6×10^-3`。
- 多个相邻线站在同一设定下仍可达到超过 1 kA；一次通过后快速踢出束团，理论可按 LPA 驱动激光的 10--30 Hz 复现。
- 该高流强核心可产生 THz 至近 UV 的相干同步辐射；13.6 nm EUV 单程 FEL 的估算接近可行边界，但需要更长的 20--25 m undulator 或进一步降低发射度/切片能散。

## 与本仓库方向的关系

- 给出把激光等离子体电子束接入现有同步辐射基础设施、转化为飞秒高亮度光源的系统级束流操纵路线。
- 对二次 X/γ 源应用而言，定量呈现了束团电荷、CSR、环接受度、能散与峰值流强的共同约束，而不是只报告 LPA 出口指标。
- 相关性评分：5/5。

## 局限与注意事项

这是 PETRA IV 参数下的设计与起止端模拟，尚非储存环注入或用户线实验。模型将 wakefield、非相干同步辐射和环 RF 的影响判为小而略去；能量抖动、注入元件孔径和 CSR 会限制传输，FEL 增益尤其依赖尚待改善的 LPA 发射度与切片能散。
