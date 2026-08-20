# Relative and absolute dosimetric commissioning of the ELIMAIA--ELIMED laser-driven proton beamline at 23.45 MeV

## 基本信息

- 作者：G. A. P. Cirrone；G. Petringa；A. Kurmanova；R. Catalano；A. Amato；等
- 期刊/平台：*arXiv preprint*（`physics.acc-ph`、`physics.app-ph`、`physics.med-ph`、`physics.plasm-ph`；投稿至 *High Power Laser Science and Engineering*）
- DOI：[10.48550/arXiv.2608.15272](https://doi.org/10.48550/arXiv.2608.15272)
- 发表时间：2026-08-15
- 来源链接：[arXiv 摘要页](https://arxiv.org/abs/2608.15272)
- 本地 PDF：`daily/2026-08-21/pdfs/Cirrone et al. - 2026 - ELIMAIA ELIMED dosimetry.pdf`

## 研究问题与方法

本文在 ELI Beamlines 的 ELIMAIA--ELIMED 用户束线，对能量选择后的激光驱动质子束进行相对与绝对剂量学 commissioning。约 `10 J`、`27 fs` 的 L3-HAPLS 脉冲打 `6 μm` 金属箔，靶上强度约 `3×10^21 W/cm²`，处于 TNSA 主导条件；ELIMED 磁输运、能量选择和整形后，在照射点用放射变色膜（RCF）、Faraday cup（FC）、双隙电离室（DGIC）、ICT 与 SEM 建立剂量/在线监测链，并用 G4ELIMED 审计 RCF 对 FC 测量的扰动。

## 主要结论

- 照射点的质子谱中心为 `23.45±0.5 MeV`、FWHM `2.60 MeV`；50% 等剂量场尺寸为约 `5.5±0.3 mm`，布拉格峰在水等效深度 `5.5–5.7 mm`。这表明输运后得到的是能量选择但非单能的质子场。
- FC 作为绝对水剂量参考，DGIC 经逐发复合修正后作为主在线剂量计；50 发独立 RCF--FC 对比给出 FC `30.45±3.5 cGy`、EBT3 膜 `36.46±1.8 cGy`。
- G4ELIMED 显示放在 FC 上游的 RCF 会改变 FC 接受度内的质子损失和有效束斑面积。采用 `C_MC=1.109` 修正后，RCF 与 FC 剂量残差降至约 `7%`。
- 结果建立了低通量 commissioning 条件下的可追溯剂量学、在线监测和逐发束流表征链，为后续放射生物学用户实验提供必要的平台基线。

## 与本仓库方向的关系

- 主题关键词：laser-driven proton；TNSA；ELIMAIA；ELIMED；beam transport；dosimetry；Faraday cup；ionization chamber；G4ELIMED；radiobiology。
- 该工作直接覆盖激光离子源后的输运、能量选择、剂量绝对标定和在线诊断，是从靶后宽谱质子束走向可控辐照应用的关键实证环节。
- 相关性评分：5/5。

## 局限与注意事项

该论文是低通量 commissioning，而非肿瘤治疗或临床剂量学结论；质子场能量约 `24 MeV`，不能代表深部治疗能区。单发激光束的高瞬时剂量率不等同于已验证的 UHDR 生物效应；文中也明确尚需更高重复率、稳定性和剂量控制的用户实验来验证应用终点。
