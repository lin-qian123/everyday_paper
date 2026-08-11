# Energy-optimized scaling laws for self-guided laser wakefield accelerators

## 基本信息

- 作者：Petr Valenta；Marcel Lamač；Kyle G. Miller；Brandon K. Russell；Gabriele M. Grittani；Alec G. R. Thomas；Sergei V. Bulanov
- 期刊/平台：*arXiv preprint*（`physics.plasm-ph`、`physics.acc-ph`、`physics.comp-ph`）
- DOI：https://doi.org/10.48550/arXiv.2608.08903
- 发表时间：2026-08-09
- 来源链接：https://arxiv.org/abs/2608.08903
- 本地 PDF：`daily/2026-08-12/pdfs/Self guided LWFA energy scaling.pdf`

## 研究问题与方法

本文针对自引导激光尾场加速（LWFA）中“给定驱动激光能量和波长时，可达到多高电子能量、需要多长等离子体”的设计问题，以贝叶斯优化（BO）高效搜索脉宽归一化量 `τ0ωp` 与相对临界功率 `P0/Pcr`。主体为 Lorentz-boosted-frame PIC 扫描，每个能量或波长切片使用 128 次试验建立代理模型；在识别的最优点另以准三维实验室系 PIC 复核。优化目标是第一泡后电子能谱前 1% 宏粒子的最大能量，长度为达到该值的最短传播距离。

## 主要结论

- 在文中扫描范围内，最大电子能量与最短加速长度分别给出 `E*/(m_ec^2)≈3.81(E0/EJ)^0.58`、`l*/λ0≈0.78(E0/EJ)^0.84`；故激光能量翻倍时，电子能量约提高 `1.5` 倍、所需长度约增 `1.8` 倍。
- 作为设计量级示例，`1 J`、`1 μm` 驱动对应约 `833 MeV` 最大电子能量和约 `5.1 mm` 加速长度。减半波长可得到类似的能量提升，同时所需长度略减。
- 高能区域不是单一尖锐点而是参数空间中的较宽脊线；作者还发现平均达到最终最大能量的 50% 和 75% 分别只需约 `0.26l*` 与 `0.53l*`，可用于按有限长度反推可得能量。

## 与本仓库方向的关系

- 主题关键词：LWFA；laser wakefield；self-guiding；particle-in-cell；Bayesian optimization；electron beam；scaling law。
- 该结果把 PIC 参数扫描压缩为仅依赖激光能量和波长的初始设计标度，对激光加速电子束的束流能量规划、平台选型和后续转换靶/辐射源应用的输入束参数评估直接有用。
- 相关性评分：5/5。

## 局限与注意事项

标度只针对自引导、本文规定的激光能量和波长范围及“最大能量最短长度”单目标，不包含电荷、能散、发射度、稳定性或特定注入机制的共同优化；因而不能直接当作应用束流品质或转换靶产额的预测器。低能端出现短脉冲泵浦耗尽与 CEP 效应相关偏离；准三维复核相对 boosted-frame 结果仍显示约 8%–16% 的能量差异和 3%–9% 的长度差异，外推到扫描域外须谨慎。
