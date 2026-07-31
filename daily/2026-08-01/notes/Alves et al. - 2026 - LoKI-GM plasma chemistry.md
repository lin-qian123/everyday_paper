# LoKI-GM: a global model framework for plasma chemistry studies

## 基本信息

- 作者：L. L. Alves；A. Tejero-Del-Caz；L. Marques；P. Pereira；N. Pinhão；C. D. Pintassilgo；T. Silva；P. Viegas；V. Guerra
- 期刊/平台：arXiv preprint（physics.plasm-ph，submitted to *Plasma Sources Science and Technology*）
- DOI：https://doi.org/10.48550/arXiv.2607.27234
- 发表时间：2026-07-23
- 来源链接：https://arxiv.org/abs/2607.27234
- 本地 PDF：`daily/2026-08-01/pdfs/Alves et al. - 2026 - LoKI-GM plasma chemistry.pdf`

## 研究问题

低温等离子体中电子、重粒子与表面反应耦合复杂；怎样以比空间分辨模型低得多的成本，可靠识别主导反应路径并快速扫参数？

## 方法与模型

- 介绍开源 MATLAB 框架 LoKI-GM：耦合电子 Boltzmann 求解器 LoKI-B 与重粒子零维速率方程求解器 LoKI-C。
- LoKI-B 采用空间均匀、二项近似电子 Boltzmann 方程；LoKI-C 处理带电/中性物种及表面反应的体平均动力学。
- 覆盖 DC/HF 和非振荡时变电场下的活性放电与余辉，给出输入输出、数值策略和代表性放电构型。

## 主要结论

- 0D 全局模型可显著压低计算成本，并用于辨识主要生成/损失通道；框架的特征是可切换输运模型和表面动力学。
- 在高压、局域场近似有效时，该方法最适合；也可借助批式--塞流类比局部化处理某些空间非均匀流动问题。
- 作者明确指出低压强、强非局域 EEDF、鞘层和强密度梯度会限制纯空间平均近似。

## 与本仓库方向的关系

- 为低温放电源、材料处理、等离子体化学与快速反应网络扫描提供可复现实用工具。
- 与高强度激光 PIC 并非同一尺度模型，但可补充从电子能量分布到气相/表面化学的轻量级计算链。
- 主题关键词：low-temperature plasma；global model；Boltzmann solver；plasma chemistry；surface kinetics；LoKI-GM。
- 相关性评分：3/5。

## 局限与注意事项

这是教程/框架论文，示例结果不能直接等同于某个装置的预测精度；对强空间非均匀、低压非局域或超快高能密度等离子体，应采用更高维或全动理学模型并做实验/基准交叉验证。
