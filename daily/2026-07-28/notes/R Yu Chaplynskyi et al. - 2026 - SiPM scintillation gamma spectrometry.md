# Gamma spectrometry with CsI(Tl), NaI(Tl) and CdWO4 scintillation crystals using a silicon photomultiplier

## 基本信息

- 作者：R. Yu. Chaplynskyi; F. A. Danevich; D. V. Kasperovych; V. R. Klavdiienko; V. V. Kobychev; E. E. Petrosian; A. R. Podviianiuk; R. B. Podviianiuk; O. G. Polischuk
- 期刊/平台：Nuclear Physics and Atomic Energy 27(2), 148--152（开放获取；arXiv 收录本）
- DOI：https://doi.org/10.15407/jnpae2026.02.148
- 发表时间：2026-06-25
- 来源链接：https://arxiv.org/abs/2607.21996
- 本地 PDF：`daily/2026-07-28/pdfs/R Yu Chaplynskyi et al. - 2026 - SiPM scintillation gamma spectrometry.pdf`

## 研究问题

面向轻量、低压、抗磁场的野外伽马谱与辐射监测，现代 SiPM 配合不同闪烁晶体能否以可接受的能量分辨率替代传统 PMT，及其主要性能限制是什么。

## 方法与模型

- 以 3$\times$3 mm$^2$ Onsemi MICROFC-30035-SMT-TR SiPM（28 V 偏压）分别耦合 CdWO4、CsI(Tl) 与 NaI(Tl) 晶体；用 100 MS/s 数字示波器采集波形并在基线扣除后积分电荷。
- 用 $^{207}$Bi 的 570 和 1064 keV 全能峰计算 FWHM，并在相同条件下与 Hamamatsu R6233 PMT 对比。

## 主要结论

- CsI(Tl)+SiPM 表现最好：570 keV 与 1064 keV 的 FWHM 分别为 11.6(4)% 和 9.1(5)%；相应 PMT 为 8.2(2)% 与 6.2(3)%。
- NaI(Tl)+SiPM 的 FWHM 为约 20.0(5)% 和 15.0(9)%；作者归因于 25 mm 晶体输出窗与 3$\times$3 mm$^2$ SiPM 的几何失配、集光不足。
- CdWO4 的长衰减（约 15 $\mu$s）与暗计数叠加，未形成可分辨全能峰；在本文条件下 SiPM 方案的分辨率整体约比 PMT 低 40%。

## 图表与证据角色

- 图 3 比较三种晶体的单次波形及时间尺度：CdWO4 可见离散光电子和长尾，解释其对暗计数积分敏感；CsI(Tl) 的信号形状最利于模拟电荷读出。
- 图 4 在相同 $^{207}$Bi 条件下叠加 CsI(Tl)+SiPM 与 CsI(Tl)+PMT 能谱，是两类读出分辨率差异的直接证据。
- 表 2 汇总三种晶体、两种读出在两个能量峰的 FWHM，区分了“晶体/耦合限制”与“SiPM 本体可行性”；样品尺寸和电子学固定，不能直接外推至更大探测器或冷却方案。

## 与本仓库方向的关系

- 可为激光加速电子束二次伽马源、光核/中子实验以及现场辐射防护的紧凑伽马诊断提供器件选型基线；并非激光驱动源性能论文。
- 主题关键词：gamma spectrometry；SiPM；scintillator；radiation monitoring；nuclear diagnostic；CsI(Tl)。
- 相关性评分：3/5。

## 局限与注意事项

结论对应小尺寸晶体、单一 SiPM、室温和简化示波器读出；作者已指出可通过光学耦合优化、降温抑制暗计数与更先进信号处理改进，故不应将当前 FWHM 视为 SiPM 谱学的性能上限。
