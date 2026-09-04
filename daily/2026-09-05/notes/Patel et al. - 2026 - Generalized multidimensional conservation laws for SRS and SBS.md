# 密度梯度中 SRS/SBS 的广义多维守恒律 笔记

## 0. 论文信息

- 英文标题：Generalized multi-dimensional conservation laws for stimulated Raman and Brillouin scattering in a density gradient
- 作者：Vijay Patel；Sarah Chase；Frank S. Tsung；John P. Palastro；Denise E. Hinkel；Warren B. Mori
- 期刊：Physical Review E，2026-09-04 accepted paper
- 正式 DOI：[10.1103/hdkp-2mpm](https://doi.org/10.1103/hdkp-2mpm)
- 来源：[APS accepted papers 页面](https://journals.aps.org/pre/accepted/10.1103/hdkp-2mpm)
- 本地全文版本：与正式标题/作者对应的 [arXiv:2604.00295v2](https://arxiv.org/abs/2604.00295v2) author preprint；不是 APS 排版版
- 本地 PDF：daily/2026-09-05/pdfs/Patel et al. - 2026 - Generalized multidimensional conservation laws for SRS and SBS.pdf
- 正文处理：对应 arXiv v2 PDF 通过文件头、类型、21 页元数据、SHA-256 和非空文本校验，并成功完成 MinerU Markdown 转换。

## 1. 摘要与文章定位

论文从含 density-gradient mismatch 的三波 paraxial envelope equations 出发，构造无耗散 Lagrangian density，再用 Noether theorem 系统导出局域 wave action、energy、momentum 和 orbital angular momentum（OAM）守恒律。对 damping，作者不声称存在纯 Lagrangian，而是把耗散函数加入 Euler–Lagrange equations，使守恒律右侧出现明确 sink terms。

工作是理论推导和数值算法校验框架；没有新的 PIC/实验结果。它能为 pF3D 类 envelope code 提供 residual/invariant checks，但本轮未运行 pF3D，也未对任何代码做守恒误差测试。

## 2. 起点：三波包络方程

三波分别是 pump $b_0$、backscattered light $b_1$ 和向前传播的 plasma wave $b_2$（SRS 为 EPW，SBS 为 IAW）。结构上可写成

$$
\omega_\alpha\left(
\partial_t+\nu_\alpha+v_{g\alpha}\partial_z
-\frac{i u_\alpha^2}{2\omega_\alpha}\nabla_\perp^2
-\frac{\partial_zv_{g\alpha}}{2}
\right)b_\alpha
=\text{three-wave coupling},
$$

耦合项带有密度梯度产生的 mismatch phase

$$
\phi(z)=\int dz\,[k_1(z)+k_2(z)-k_0(z)].
$$

频率匹配 $\omega_0=\omega_1+\omega_2$ 采用固定 carrier frequencies；波数只在 resonance point 满足 $k_{0,0}=k_{1,0}+k_{2,0}$，远离该点的失配由 $\phi(z)$ 显式记录。

## 3. Lagrangian 与耗散处理

无 damping 时，Lagrangian density 包含三部分：时间的一阶反对称导数、轴向 group-velocity transport、横向 paraxial gradient，以及

$$
b_0^*b_1b_2e^{-i\phi(z)}+\mathrm{c.c.}
$$

三波耦合。对 $b_\alpha^*$ 作 Euler–Lagrange variation 可恢复三条 envelope equations。

damping 不是由该作用量自身产生；作者用类似 Rayleigh dissipation 的函数 $F$ 增广 E–L equations。因而守恒式的通用形式从 $\partial_\mu J^\mu=0$ 变为

$$
\partial_\mu J^\mu=\text{damping sink}.
$$

在具体 action laws 中，每个波的耗散项按 $-2\nu_\alpha\omega_\alpha|b_\alpha|^2$ 出现。这是模型内的 phenomenological loss，不自动包含 kinetic damping、trapping 或 wave breaking 的完整微观物理。

## 4. 多维 Manley–Rowe / wave-action 守恒

对三波作保持耦合项不变的 phase rotations，可得到三组局域 action relations。例如 pump–plasma-wave 组合的密度是

$$
\omega_0|b_0|^2+\omega_2|b_2|^2,
$$

pump–scattered-light 组合为

$$
\omega_0|b_0|^2+\omega_1|b_1|^2,
$$

两式相减给出常见的第三条 Manley–Rowe 关系

$$
\omega_1|b_1|^2-\omega_2|b_2|^2.
$$

论文的新意在于每条关系都同时带 $z$ flux 和 $\nabla_\perp$ diffraction flux；令横向梯度为零才退化为熟悉的一维形式。对有限 speckle 或 side-scatter，检查空间积分前应正确处理横向边界通量，不能只比较体积分量。

## 5. 两类 energy / momentum 不应混淆

由 carrier phase transformation $b_\alpha\mapsto e^{i\omega_\alpha T}b_\alpha$ 和 $b_\alpha\mapsto e^{ik_{\alpha,0}Z}b_\alpha$ 得到 quasi-energy 与 quasi-$z$-momentum；它们本质上是 action law 乘以 carrier frequency 或 resonance-point wavenumber，并非独立的新守恒量。

另一类由真实 time/space translations 和 energy–momentum tensor 得到，包含 envelope frequency/wavenumber shift，是不同的物理量。密度梯度使 Lagrangian 显含 $z$，所以真实 $z$-momentum 方程会出现

$$
\phi'(z)\times\text{three-wave coupling}
$$

源项；这精确表达了 inhomogeneous medium 与波之间的动量交换，而不是假装全局轴向平移对称仍成立。

进一步将 energy 与 action equations 联立可见，频率匹配只有在各 $\omega_j$ 沿特征线保持常数时才直接跟随；对 wavenumber matching 也有同样限定。carrier matching 与完整 envelope energy/momentum conservation 因此不能互相替代。

## 6. OAM 守恒与“匹配”的限定

绕 $z$ 轴的 rotation symmetry 给出

$$
L_z=\frac{\omega_\alpha}{2ic_\alpha}
\left(b_\alpha^*\partial_\phi b_\alpha
-b_\alpha\partial_\phi b_\alpha^*\right),
$$

以及相应轴向/横向 flux。该形式与 $({\bf r}\times{\bf P})\cdot\hat{\bf z}$ 一致，并可扩展到 circular polarization 的 spin angular momentum。

作者强调 effective OAM index $\bar\ell$ 一般会随传播改变。由 OAM 与 action equations 联立得到的关系含

$$
(\bar\ell_0-\bar\ell_1-\bar\ell_2)
(\partial_t\bar a_0+\partial_zv_{g0}\bar a_0),
$$

所以简单的 $\bar\ell_0=\bar\ell_1+\bar\ell_2$ 只有在每个 $\bar\ell_j$ 固定时成立；严格成立的是总 OAM 局域守恒式，而非任意时刻的单一 mode-index matching。

## 7. 可用于数值代码的检查清单

- 无 damping、闭合边界：空间积分后的 action/energy/OAM residual 应只剩时间离散和边界误差。
- 有 damping：右端必须与 $2\nu_\alpha$ 加权的 sink 对齐，不能仍以零漂移为判据。
- density gradient：真实 $z$-momentum 必须包含 $\phi'(z)$ source；若把它遗漏，非零 residual 不一定是数值 bug。
- 多维有限口径：同步记录 transverse flux，避免把离开诊断窗口的 action 误判成非守恒。
- quasi-energy/quasi-momentum 与 Noether translation energy/momentum 分别实现，避免用线性相关的 carrier-weighted action 重复验算同一条关系。

## 8. 限制与开放问题

- 基础是 paraxial、envelope、three-wave model；强相对论、宽带到载频分离失效、波破裂及 kinetic trapping 不在核心推导内。
- damping 以增广 E–L 的方式加入，不是耗散系统的完整变分理论。
- 论文给出 higher-order paraxial 和 nonlinear frequency-shift 扩展，但未给出生产代码的离散守恒测试。
- 本地 PDF 是正式接收论文对应的 arXiv v2 author preprint，页码和排版可能与最终 APS version of record 不同。

## 9. 复习用速记

三波 paraxial Lagrangian 把 density-gradient mismatch 放进 $e^{\pm i\phi(z)}$；phase symmetry 给多维 Manley–Rowe，真实平移/旋转对称给 envelope energy、momentum 与 OAM。密度梯度会给 $z$-momentum 加源项，而 OAM mode-index matching 仅在各有效 index 不变时成立。
