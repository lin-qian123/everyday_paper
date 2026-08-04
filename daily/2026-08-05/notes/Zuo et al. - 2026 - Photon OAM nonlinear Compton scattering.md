# Photon Orbital Angular Momentum Control by Electron Wavepackets in Nonlinear Compton Scattering

## 基本信息

- 作者：Zheng-Yang Zuo；Peng-Pei Xie；Xiang-Nan Shi；Yan-Fei Li
- 期刊/平台：arXiv preprint（physics.plasm-ph）
- DOI：https://doi.org/10.48550/arXiv.2608.01323
- 发表时间：2026-08-02
- 来源链接：https://arxiv.org/abs/2608.01323
- 本地 PDF：`daily/2026-08-05/pdfs/Zuo et al. - 2026 - Photon OAM nonlinear Compton scattering.pdf`

## 研究问题

强激光与相对论电子的非线性 Compton 散射（NCS）可产生涡旋 γ 光子；过去可用的 OAM 通道主要由入射涡旋电子/光子和多光子吸收的角动量守恒决定，一旦碰撞构型固定，调控自由度很少。本文问：即便电子没有确定的本征 OAM，能否利用其横向量子波包的形状，选择并调节输出 γ 光子的 OAM 谱？

## 方法与模型

- 将任意横向动量波包 `rho(p_perp)` 的相对论电子与圆偏振平面波激光正碰；将末态电子和光子投影到 Bessel 态，从而分辨纵向 OAM。
- 把入射电子波包展开为 Bessel/OAM 分量 `C_nu`。在长脉冲近似下，得到一般化选择定则：`ell_gamma = n - lambda + nu`；其中 `n` 为吸收的激光谐波数，`lambda` 为出射光子螺旋度，`nu` 来自电子横向波包的角向 Fourier 分量。
- 分别考察 Gaussian 波包、具有确定 OAM 的涡旋电子、三分量横向动量叠加态和连续相位整形态。数值例取归一化激光强度 `xi=1`、电子能量 `E=511 MeV`，并解析第一谐波附近 `2.5--5 MeV` γ 光子。

## 主要结论

- 电子横向 Fourier 谱会直接写入 γ 光子的 OAM 谱；Gaussian 与涡旋电子只是只有单一 `nu` 分量的特殊情形。因而波包结构本身是除外加场和本征角动量外的一项独立控制旋钮。
- 对三分量动量叠加态，`M` 决定允许 OAM 分量间隔，`mu_0` 决定主 OAM 通道，横向尺度参数 `z` 调节各通道权重。`M=3, z=0.5, mu_0=1` 时，正螺旋 `ell_gamma=1` 通道在所选能段占 `92.7%`；只改 `mu_0=2`，主通道切换到 `ell_gamma=-1`（`92.8%`），而无需改变能谱或激光场。
- 增大 `z` 会连续牺牲模纯度以增强副通道：示例中主通道占比由约 `92.8%`（`z=0.5`）降至 `63.4%`（`z=0.8`），`ell_gamma=-2` 副通道升至约 `28.4%`。连续相位整形也能产生多 OAM γ 谱，证明调控不依赖预制的确定 OAM 电子。

## 与本仓库方向的关系

- 直接属于强场 QED / 非线性 Compton 与结构化 γ 源；它提出的电子波包工程为激光加速电子束与高能 γ 辐射的角动量维度设计提供了可计算目标。
- 面向核共振、选择定则敏感的核诊断或材料研究时，OAM 可作为额外自由度；但本文只建立辐射产生的理论映射，未计算转换靶、光核产额、探测效率或辐射防护。
- 主题关键词：strong-field QED；nonlinear Compton scattering；vortex gamma ray；electron wavepacket；orbital angular momentum；structured radiation。
- 相关性评分：4/5。

## 局限与注意事项

结论基于圆偏振平面波、长脉冲和解析的单电子量子波包模型，示例参数为 `xi=1`、`511 MeV`；并未包含激光加速器真实电子束的能散、发射度、有限碰撞几何、集体等离子体效应、辐射反作用或探测端 OAM 分辨。文中展示的是 OAM 模态的相对概率而非绝对光子产额或实验容差，因此其“可控 γ 源”意义仍需结合可制备波包、强场全数值模拟和实验诊断验证。
