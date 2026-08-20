# Bright dual-pulse betatron X-ray generation from a laser wakefield accelerator

## 基本信息

- 作者：Bo Guo；Yang Wan；Shuang Liu；Xiaonan Ning；Jianfei Hua；Wei Lu
- 期刊/平台：*arXiv preprint*（`physics.plasm-ph`）
- DOI：[10.48550/arXiv.2608.17555](https://doi.org/10.48550/arXiv.2608.17555)
- 发表时间：2026-08-18
- 来源链接：[arXiv 摘要页](https://arxiv.org/abs/2608.17555)
- 本地 PDF：`daily/2026-08-21/pdfs/Guo et al. - 2026 - Bright dual-pulse betatron X-rays.pdf`

## 研究问题与方法

作者在 `40 TW` 级 Ti:sapphire LWFA 中使用氢氮混合、带激波前沿的密度定制气体靶。先由氮电离注入形成一束电子，再在密度下坡由激波前沿注入第二束电子；两束电子的 betatron 振荡产生不同角分布的 X 射线。实验以磁谱仪、X 射线成像板和 Ross 滤片阵列重建电子束与 X 射线谱，并以 PIC 模拟区分两电子群的辐射贡献和脉冲延迟。

## 主要结论

- 驱动脉冲为 `1.1 J`、`37 fs`、`800 nm`，焦斑 `10 μm`，靶上强度约 `1.2×10^19 W/cm²`（`a0=2.4`）。激波靶的 `>30 MeV` 总电子电荷为 `908±176 pC`，其中电离注入与激波注入分量分别为 `94±19 pC` 和 `817±173 pC`。
- 在 `1–15 keV` 范围，实测光子数为 `(9.1±2.2)×10^9` photons/shot；按拟合全谱外推为 `(3.1±0.9)×10^10` photons/shot，约为优化均匀等离子体源的 `8.5` 倍。`0.5–7 keV` 的谱通量超过 `10^6 photons/(0.1% BW·shot)`。
- 双分量 X 射线角分布的水平 RMS 发散分别约 `25 mrad` 与 `3 mrad`，与两束电子的高/低发散分量一致。改变激波位置和密度可将临界能从约 `1.6` 调至 `2.9 keV`。
- 双脉冲时间间隔未直接测量，而是由 PIC 推断：在 `9×10^18 cm^-3`，激波位置每后移 `100 μm`，延迟约增加 `2.7 fs`；模拟给出较窄分量约 `5 fs` FWHM。该“可调双脉冲”时间指标因此仍是模型推断，而非时域实测。

## 与本仓库方向的关系

- 主题关键词：LWFA；betatron X-ray；dual pulse；ionization injection；shock-front injection；Ross filter；PIC；ultrafast X-ray spectroscopy。
- 该工作把气体靶密度结构、双电子束注入、X 射线光子产额/角分布与 PIC 机制解释闭合，是面向超快 X 射线泵浦—探测的直接实验源。
- 相关性评分：5/5。

## 局限与注意事项

论文为预印本。X 射线光子数中“全拟合谱”值包含角分布和谱模型外推；双脉冲的时间间隔由 PIC 推断，未做直接时间诊断。该源是 keV 级 betatron X 射线，不是电子束打高 Z 转换靶的 MeV 韧致辐射，也未报告光核、中子、同位素产额、剂量或辐射防护性能。
