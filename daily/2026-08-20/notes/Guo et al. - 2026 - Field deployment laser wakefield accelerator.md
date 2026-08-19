# Field deployment of a laser wakefield accelerator for on-site application

## 基本信息

- 作者：Bo Guo；Xiaonan Ning；Dexiang Liu；Yue Ma；Weiwang Zeng；等
- 期刊/平台：*arXiv preprint*（`physics.acc-ph`、`physics.plasm-ph`）
- DOI：[10.48550/arXiv.2608.17554](https://doi.org/10.48550/arXiv.2608.17554)
- 发表时间：2026-08-18
- 来源链接：[arXiv 摘要页](https://arxiv.org/abs/2608.17554)
- 本地 PDF：`daily/2026-08-20/pdfs/Guo et al. - 2026 - Field deployment laser wakefield accelerator.pdf`

## 研究问题与方法

作者把 `40 TW` Ti:sapphire LWFA 系统装入 `7450×2450×2800 mm³` 集装箱，在工业无损检测车间完成七个月现场试运行。`25 fs`、`800 nm` 脉冲驱动 He:N2 (`99:1`) 气体靶的电离注入 LWFA；电子束由磁谱仪诊断，约 `100 MeV` 电子束打钨转换靶得到韧致辐射 X 射线。论文用电子谱、剂量/角分布/滤片谱仪、半影成像，以及多视角 CT 重建评估系统稳定性与工业检测能力。

## 主要结论

- 在连续 `72 h`、`0.1 Hz` 电子谱采集中，平均电子能量为 `86.2±1.1 MeV`，单发 RMS 稳定度 `1.3%`；`>70 MeV` 电荷为 `164±16 pC`（RMS `9.8%`）。以 60 发为一个 `10 min` 积分窗口后，能量和电荷稳定度分别为 `0.4%`、`1.9%`。
- 系统在七个月内平均每天全功率运行超过 `10 h`，总体可用日比例超过 `70%`；最长连续运行达 `12 d`。这属于现场连续运转证据，而不只是实验室单日稳定性演示。
- 钨靶后实测韧致辐射谱峰约 `1.9 MeV`、平均光子能量 `13.1±0.9 MeV`，高能尾超过 `100 MeV`；在 `1 m`、`3.3 Hz` 下单发剂量 `157±21 μGy`，约 `3.1 cGy/min`。以半影法得到 `38 μm` FWHM 源尺寸。
- 以超过 `60,000` 次曝光完成镍基合金涡轮叶片 CT，在 MTF `10%` 处得到 `43 μm` 空间分辨率；又以超过 `170,000` 次曝光和拼接/偏轴转台把有效视场扩至 `>650 mm`，分辨出 `100 μm` 尺度复合材料内部缺陷。

## 与本仓库方向的关系

- 主题关键词：LWFA；field deployment；electron beam stability；tungsten converter；bremsstrahlung；micro-CT；industrial NDT；beam diagnostics。
- 这是激光加速电子束—转换靶—高能 X 射线—材料无损检测链条的直接现场实证，并同时给出束流稳定度、剂量、源尺寸、空间分辨率和长时运行约束。
- 相关性评分：5/5。

## 局限与注意事项

论文为预印本，仍需同行评议。束流为约 `70–100 MeV`、百 pC 级的应用优化电子束，文中并未报告光核反应、同位素/中子产额或医学剂量学。CT 指标来自特定靶、探测器、扫描几何和多发累计曝光，不能把单发源参数直接等同于任意材料、任意厚度或实时检测性能。
