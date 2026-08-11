# Terahertz-based longitudinal phase space diagnostics of laser wakefield accelerated electron beams

## 基本信息

- 作者：Zhihao Chen；Yu Fang；Ran Li；Xiancong Yang；Tianliang Zhang；Jianfei Hua；Fei Li；Wei Lu
- 期刊/平台：*arXiv preprint*（`physics.acc-ph`、`physics.plasm-ph`）
- DOI：https://doi.org/10.48550/arXiv.2608.08586
- 发表时间：2026-08-09
- 来源链接：https://arxiv.org/abs/2608.08586
- 本地 PDF：`daily/2026-08-12/pdfs/THz LWFA longitudinal diagnostics.pdf`

## 研究问题与方法

LWFA 注入造成的能散会使双弯消色差（DBA）压缩对一阶 `R56` 与二阶 `T566` 纵向输运同时敏感。作者在紧凑 LWFA-UED 束线上，把太赫兹横向偏转腔（THz-TDC）与色散偶极磁铁组合，二维重建压缩束团的纵向相空间（LPS）。通过调节色散区狭缝位置和开口，分别选择不同中心能量和能量窗宽度，并以 200 连续发的统计比较束长。

## 主要结论

- 对平均能量约 `4.55 MeV` 的电子束，系统达到 `1.8 fs` 时间分辨能力和 `6.0 keV`（相对 `0.13%`）能量分辨率，直接分辨出二阶纵向输运造成的 C 形非线性 LPS。
- 在相近约 `2.9%` FWHM 能散下，能量窗中心由 `4.574 MeV` 移至 `4.532 MeV`，RMS 束长由 `26±3 fs` 增至 `42±5 fs`；这是因为后者避开了 LPS 的低局域时间--能量斜率区。
- 中心能量保持约 `4.55 MeV` 时，FWHM 能散由 `2.0±0.2%` 放宽至 `4.4±0.6%`，RMS 束长由 `27±3 fs` 增至 `44±6 fs`。因此，狭缝位置和开口可基于实测 LPS 联合优化，而不是仅靠一阶压缩条件。

## 与本仓库方向的关系

- 主题关键词：LWFA；electron beam；THz-TDC；longitudinal phase space；diagnostic；DBA compression；ultrafast electron diffraction。
- 这是激光加速电子束品质诊断到可操作压缩优化的实验案例，可为需要时域分辨的辐射源、UED 和二次源前端提供束线诊断思路。
- 相关性评分：5/5。

## 局限与注意事项

实验是约 `4.55 MeV`、fC 级 LWFA-UED 束线，并且 THz-TDC 位于设计全补偿点下游，测得的是具有显著二阶输运的欠压缩状态；结论不能直接给出 GeV 级或高电荷束团的分辨率和最优狭缝设置。相邻能散窗的束长误差条有部分重叠，且文中将空间电荷效应视为当前 fC 电荷下的次要项；高电荷运行仍需独立建模和实测。未来 `T566` 校正/六极铁线性化是建议方向，不是已验证结果。
