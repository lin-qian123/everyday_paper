# SafeDivertor: Faithful Divertor Heat Flux Reconstruction from Macroscopic Plasma State Signals via Time-Frequency Prior Exploitation

## 基本信息

- 作者：Hao Si；Zehua Chen；Qingquan Yang；Xiao Wang；Dengdi Sun；Wanli Lyu；Gaoting Chen；Guosheng Xu；Hang Su；Jin Tang；Jun Zhu
- 期刊/平台：arXiv preprint（physics.plasm-ph；cs.AI；cs.CV）
- DOI：https://doi.org/10.48550/arXiv.2608.05669
- 发表时间：2026-08-06
- 来源链接：https://arxiv.org/abs/2608.05669
- 本地 PDF：`daily/2026-08-10/pdfs/Si et al. - 2026 - SafeDivertor heat flux reconstruction.pdf`

## 研究问题与方法

偏滤器热流通常依赖放电后的红外图像和导热反演，难以直接进入在线控制。作者把任务改写为：仅由放电期间可得的宏观状态信号，直接重建靶板上随时间变化的径向热流剖面。DivMPS2HF 数据集含 77 炮，按炮次而非滑窗切分为 64/3/10 炮训练、验证与测试；输入为 67 路状态、诊断、平衡/位形和控制信号，目标为 116 路热流通道，统一到 1 kHz、以 0.5 s 窗口训练。SafeDivertor 组合热流径向分布先验初始化、输入高斯扰动、多尺度 STFT 频谱损失和渐进训练，以同时保留瞬态高频结构与时空剖面。

## 主要结论

- 在该炮次隔离测试集上，完整模型的 MSE/MAE/SSIM/LSD/LSD-HF 为 0.200/0.291/0.870/2.475/2.729；相对最佳基线，MSE 从 0.262 降至 0.200、LSD-HF 从 3.829 降至 2.729。
- 消融表明，物理先验主要改善点值和结构误差，而多尺度频谱监督最明显改善频谱一致性（单独使用时 LSD 为 2.306、LSD-HF 为 2.511）；二者与输入扰动、渐进训练共同取得更均衡表现。
- 文中测量的是模型前向推理而非完整控制链路；每 0.5 s 输入窗口的在线重建可避免把红外反演作为实时输入依赖。

## 与本仓库方向的关系

- 主题关键词：magnetic confinement fusion；divertor；plasma-wall interaction；diagnostics；machine learning；time-frequency reconstruction。
- 直接面向聚变装置的热负荷诊断与壁面防护；其“多源状态量到不可直测靶面量”的建模范式可迁移到激光等离子体的合成诊断、靶后粒子/辐射场反演。
- 炮次级隔离与频谱指标尤其值得作为 PIC 或实验束流诊断机器学习的验证基线，避免同一炮滑窗泄漏造成虚高精度。
- 相关性评分：4/5。

## 局限与注意事项

标签仍来自放电后红外--导热分析，模型并没有取代该物理反演的标定链路；数据只有 77 炮，且文章未展示跨装置、跨工况或真正闭环控制部署的泛化。数据集仅承诺经合理请求提供，代码尚未随预印本公开；因此结果应视作单数据集基准，不能直接推断为任意偏滤器上的在线可用精度。
