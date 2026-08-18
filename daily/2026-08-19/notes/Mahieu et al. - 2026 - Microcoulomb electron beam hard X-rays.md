# Microcoulomb-level electron beam and multi-Joule hard X-rays driven by a high-efficiency laser-plasma accelerator

## 基本信息

- 作者：B. Mahieu；L. Ribotte；W. Cayzac；G. Boutoux；R. Parreault；J. Gastineau；E. Lamoine；F. Audo；R. Babjak；D. Batani；等
- 期刊/平台：*arXiv preprint*（`physics.plasm-ph`）
- DOI：[10.48550/arXiv.2608.16459](https://doi.org/10.48550/arXiv.2608.16459)
- 发表时间：2026-08-17
- 来源链接：[arXiv 摘要页](https://arxiv.org/abs/2608.16459)
- 本地 PDF：`daily/2026-08-19/pdfs/LMJ PETAL microcoulomb electron beam hard X-rays.pdf`

## 研究问题与方法

本文在 Laser Mégajoule（LMJ）靶腔中，将 PETAL 的 `719 J`、`753 fs`、约 `0.95 PW` 脉冲聚焦到 `10 mm` 狭缝超声 He 气体靶；最高靶上强度约 `2.0×10^19 W cm^-2`，电子密度最高约 `2–3×10^19 cm^-3`。电子由 SESAME 磁谱仪、CRACC 成像板测量；位于成像板后的 `1 cm` 厚 In/Fe/Zr 板作为偏轴高 Z 韧致辐射转换靶，硬 X 射线由滤片—成像板 cannon stack 测谱。作者以 3D CALDER PIC 重现谱与角度分布，以准 3D OSIRIS 分解 wakefield 与激光场做功，并用 Geant4、FLUKA 分别评估探测器响应和转换后光子输运。

## 主要结论

- 最佳炮次（shot 5）的电子总电荷为 `1.1 ± 0.13 μC`（有效阈值 `>0.9 MeV`），峰值能量约 `500–550 MeV`；其中 `>10 MeV` 约 `467 nC`、`>100 MeV` 约 `17 nC`。全束二维重建的平均能量为约 `15 MeV`（而非小角接受角内的 `50 MeV`），对应电子束总能量约 `17 J`、相对全激光能量的 `2.3%`；若只以 `1/e^2` 主焦斑的 `194 J` 计，则有效电子转换效率约 `8.5%`。
- 电子谱为双温 Maxwell 型而非准单能。CRACC 面上的 HWHM 发散约 `209×152 mrad^2`，只有约 `31%` 电荷位于 FWHM 区域；这明确表明该平台以高总通量而不是低发散、窄能散束流品质为优势。
- PIC 表明 SMLWFA 主要负责高电荷俘获和中低能预加速，DLA 为高能尾提供显著附加增益；该归因有场做功分解支撑，避免仅由末态电子谱断言 DLA。
- 转换靶后的实测硬 X 射线高能分量温度约 `9.3±1.1 MeV`、平均光子能量约 `6.4±1.6 MeV`；FLUKA 与 `>1 MeV` 谱段相符。光子总能量约 `3.3 J`，相对有效主焦斑能量转换约 `1.7%`；`>10 MeV` 产额估计约 `2×10^12 photons/sr`、`>1 MeV` 通量超过 `10^13 photons/sr`。

## 与本仓库方向的关系

- 主题关键词：laser wakefield acceleration；SMLWFA；DLA；high-charge electron beam；bremsstrahlung converter；hard X-ray；high-energy-density diagnostic；Geant4；FLUKA；PIC。
- 直接覆盖激光加速电子束—高 Z 转换靶—硬 X/γ 次级源链路，并把电子束电荷、能谱、发散、转换效率和光子谱在大型 HED 设施环境中共同量化；尤其适合作为脉冲 X 射线背光和后续光核实验的输入基线。
- 相关性评分：5/5。

## 局限与注意事项

本文的电子总能量与全角谱、光子总能量和转换效率均部分依赖 PIC/FLUKA 角度或输运外推；成像板中心孔需用二维拟合补回，且高通量下须多次扫描，构成电荷不确定度来源。其电子束是宽角、Maxwell 型分布，不能写成高品质或准单能 LWFA 束。虽然转换板为未来诱发光核反应而设计，论文将 γ 谱测量与活化/光核产额的发表明确分开：没有给出中子、放射性同位素、剂量、辐射屏蔽或临床/材料终端指标。因此本文实证的是电子束与韧致辐射硬 X 源，光核、放射性同位素和 HED 泵浦—探测应用仅是有物理依据的后续方向，不能表述为已完成的应用性能。
