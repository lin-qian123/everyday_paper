# Terahertz Generation through Photon Deceleration of Long-Wavelength Infrared Laser Pulses in Plasma

## 基本信息

- 作者：Srimanta Maity
- 期刊/平台：arXiv preprint
- DOI：https://doi.org/10.48550/arXiv.2607.07005
- 发表时间：2026-07-08
- 本地 PDF：`daily/2026-07-10/pdfs/Srimanta Maity - 2026 - Terahertz Generation through Photon Deceleration.pdf`

## 研究问题

高场强、高能量 THz 源对超快诊断、强场物理和等离子体控制有重要价值。论文研究单色长波红外激光脉冲与气体靶相互作用时，是否可以通过等离子体中的 photon deceleration 机制高效产生强 THz 辐射，并给出可用于参数设计的转换效率标度。

## 方法与模型

- 使用 Particle-In-Cell 模拟研究 LWIR 激光脉冲在气体靶中的传播。
- 分析 self-modulated wakefield regime 中脉冲前沿电子密度堆积导致的 photon deceleration。
- 扫描靶密度、激光强度和传播长度等参数对 THz 产生效率的影响。
- 用理论分析验证 PIC 模拟得到的能量转换效率标度。

## 主要结论

- 模拟显示可通过 LWIR 激光在等离子体中的 photon deceleration 产生高能 THz 脉冲。
- 论文给出的代表性参数下，激光到 THz 的能量转换效率约为 `4%`。
- 输出 THz 场强可达约 `100 GV/m`，脉冲能量约 `50 mJ`。
- 关键效率受靶密度、激光强度和传播长度共同控制。

## 与本仓库方向的关系

- 直接关联激光等离子体、PIC 模拟、wakefield regime 和强场辐射源设计。
- 虽然目标是 THz 源而非电子/离子加速本身，但机制依赖激光-等离子体非线性调制，与先进光源、诊断和强场等离子体控制相关。
- 可补充本仓库对“激光等离子体产生二次辐射源”的跟踪范围。

## 阅读价值

- 适合关注高能 THz 源、LWIR laser-plasma interaction、PIC 参数扫描和 radiation source scaling 的读者。
- 对设计下一代强 THz 驱动源或把 THz 辐射作为等离子体诊断/控制工具的工作有参考意义。

## 局限与注意事项

- 主要结果来自 PIC 模拟，实验可实现性取决于 LWIR 激光参数、气体靶长度、等离子体均匀性和能量沉积控制。
- 需要关注模拟维度、边界条件、离化模型和噪声对 THz 输出效率估计的影响。
