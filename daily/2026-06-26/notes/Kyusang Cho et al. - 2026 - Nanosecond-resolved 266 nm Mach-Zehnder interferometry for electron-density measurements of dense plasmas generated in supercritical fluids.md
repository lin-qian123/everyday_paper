# Nanosecond-resolved 266 nm Mach-Zehnder interferometry for electron-density measurements of dense plasmas generated in supercritical fluids 笔记

## 0. 论文信息
- 标题: Nanosecond-resolved 266 nm Mach-Zehnder interferometry for electron-density measurements of dense plasmas generated in supercritical fluids
- 作者: Kyusang Cho, Juho Lee, Gunsu Yun
- 平台: arXiv 预印本
- DOI: 10.48550/arXiv.2606.25327
- 发表日期: 2026-06-24
- 主题关键词: laser-produced plasma、Mach-Zehnder interferometry、electron density、dense plasma diagnostics、supercritical fluid

## 1. 核心结论
- 作者搭建了 266 nm、纳秒分辨的 Mach-Zehnder 干涉系统，用于测量 100 bar 超临界氦中激光产生致密等离子体的电子密度分布。
- 通过分别记录 plasma-arm-only 与 reference-arm-only 图像来校正条纹可见度，再用二维傅里叶法重建相位图，最后结合 Abel 反演得到局域电子密度。
- 文中给出的代表性峰值局域电子密度约为 2.5×10^18 cm^-3，同时讨论了自由-自由吸收、折射偏转和碰撞频率对诊断保真度的限制。

## 2. 方法与技术路线
- 技术路线很清楚：UV 探针减少截止密度与折射限制，图像归一化改善条纹质量，频域相位提取再接物理反演。
- 对仓库而言，它的价值在于把“高密度、短寿命等离子体怎么定量测”这个经常被略过的问题展开成了可执行诊断流程。
- 摘要摘录线索: We developed a nanosecond-resolved 266 nm Mach-Zehnder interferometer for electron-density measurements of dense laser-produced plasmas generated in 100-bar supercritical-fluid (SCF) helium. A 1064 nm pump pulse was focused into the SCF helium medium, and the plasma-induced phase shift of a 266 nm UV probe beam was recorded using an ICCD-based interferometric imaging system. Plasma-arm-only and reference-arm-only images were used to normalize raw interferograms and improve the effective fringe visibility. The corrected interferograms were analyzed using a two-dimensional Fourier-transform method to reconstruct phase-shift maps, which were converted into line-integrated electron-density distributions through the plasma dispersion relation. Assuming cylindrical symmetry, Abel inversion was applied to the plasma with the largest line-integrated electron density, yielding a maximum local electron density of approximately \(2.5\times10^{18}~\mathrm{cm^{-3}}\). The measurement fidelity was evaluated by considering free-free absorption of the probe beam, probe-beam refraction by plasma electron density gradients, and effect of finite-collision-frequency effects on the plasma dielectric response. These estimates indicate that the inferred electron density is not altered by more than an order of magnitude under the present experimental conditions. The present system demonstrates the applicability of 266 nm UV interferometry to nanosecond-resolved density diagnostics of dense plasmas in high-pressure supercritical fluids.

## 3. 与当前研究方向的关系
- 相关性评分: 8/10；影响力评分: 7/10。
- 这篇落在实验平台与诊断主线，虽然不是典型加速论文，但它提供了致密激光等离子体电子密度定量诊断方案，对 HEDP 实验和源区表征都很有参考价值。

## 4. 可复现实验/仿真要点
- 如果后续要借鉴到激光靶实验或次级辐射源前端等离子体诊断，应优先评估 UV 探针在更高密度和更强梯度下的透过与折射误差。
- 论文里对诊断误差来源的拆分很适合作为实验方案设计时的 checklist。
- PDF 前几页可见信息摘录: 266 nm UV Mach-Zehnder interferometry Nanosecond-resolved 266 nm Mach-Zehnder interferometry for electron-density measurements of dense plasmas generated in supercritical fluids Kyusang Cho, 1,a) Juho Lee, 1, 2,a) and Gunsu Yun 1, 3 1)Department of Physics, POSTECH, 77 Cheongam-ro, Nam-gu, Pohang 37673, Republic of Korea 2)Samsung Electronics, Memory Material Technology Team, Republic of Korea 3)Division of Advanced Nuclear Engineering, POSTECH, 77 Cheongam-ro, Nam-gu, Pohang 37673, Republic of Korea (*Electronic mail: gunsu@postech.ac.kr) (Dated: 25 June 2026) 1 arXiv:2606.25327v1 [physics.plasm-ph] 24 Jun 2026 266 nm UV Mach-Zehnder interferometry We developed a nanosecond-resolved 266 nm Mach-Zehnder interferometer for electron- density measurements of dense laser-produced plasmas generated in 100-bar supercritical- fluid (SCF) helium. A 1064 nm pump pulse was focused into the SCF helium medium, and the plasma-induced phase shift of a 266 nm UV probe beam was recorded us- ing an ICCD-based interferometric imaging system. Plasma-arm-only and reference- arm-only images were used to normalize raw interferograms and improve the effective fringe visibility. The corrected interferograms were analyzed using a two-dimensional Fourier-transform method to reconstruct phase-shift maps, which were converted into line- integrated electron-density distributions through the plasma dispersion relation. Assum- ing cylindrical symmetry, Abel inversion was applied to the plasma with the largest line- integrated electron density, yielding a maximum local electron density of approximately 2.5×10 18 cm−3. The measurement fidelity was evaluated by considering free-free ab- sorption of the probe beam, probe-beam refraction by plasma electron density gradients, and effect of finite-collision-frequency effects on the plasma dielectric response. These estimates indicate that the inferred electron density is not altered by more than an order of magnitude under the present experimental conditions. The present system demonstrates the applicability of 266 nm UV interferometry to nanosecond-resolved density diagnostics of dense plasmas in high-pressure supercritical fluids. Keywords: UV interferometry; Mach-Zehnder interferometer; laser-produced plasma; dense plasma diagnostics; Abel inversion; supercritical fluids a)These authors contributed equally. 2 266 nm UV Mach-Zehnder interferom

## 5. 后续行动项
- 可与仓库现有的实验平台、X 射线成像和靶诊断论文并读，形成“束流/源区/背景等离子体诊断”专题。
- 如果后续要跟踪转换靶、喷流或超临界介质中的源区形成过程，这篇的方法会比只看发光图像更定量。
