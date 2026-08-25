# AI Surrogate Modeling for Real-Time Tokamak Equilibrium Prediction: Benchmarking Neural Architectures and Validation on EXL-50U

## 基本信息

- 作者：Guoyang Shi；Zitong Zhang；Siqi Ding；Jianguo Chen；等
- 期刊/平台：*arXiv preprint*（`physics.plasm-ph`；`cs.AI`）
- DOI：[10.48550/arXiv.2608.23217](https://doi.org/10.48550/arXiv.2608.23217)
- 发表时间：2026-08-24
- 来源链接：[arXiv 摘要页](https://arxiv.org/abs/2608.23217)
- 本地 PDF：`daily/2026-08-26/pdfs/AI tokamak equilibrium surrogate.pdf`

## 研究问题与方法

作者以 Grad--Shafranov (GS) 数值解构造 `100,000` 个 IID 与 `10,000` 个 OOD 平衡样本，在统一训练与测试协议下比较 MLP、CNN、FNO、Transformer 和 KAN 对极向磁通的代理预测。装置关联部分选取 EXL-50U 放电平衡构型，并与 GS 数值解及 Shape Editor (SE) 参考解对照；同时测量 TensorRT 推理延迟和几何/压强、电流剖面超出训练域时的误差。

## 主要结论

- IID 测试中 Transformer 最精确，`L1/L2=0.201%/0.242%`；CNN 在精度、速度和鲁棒性之间更均衡，报告 TensorRT 延迟约 `0.7 ms`。
- OOD 几何与参数外推中，CNN 与 FNO 的 `L2` 误差分别约 `4.3%` 与 `4.0%`；Transformer、MLP 分别约 `5.8%`、`7.8%`，KAN 退化至约 `67.2%`。
- 装置关联验证中的代理—GS 相对误差为 `10^-3–10^-2`，GS—SE 差异为 `10^-3` 量级；增加训练数据或模型容量可提升插值，却不必然改善 OOD 泛化。

## 与本仓库方向的关系

- 主题关键词：机器学习；Grad--Shafranov 平衡；磁约束聚变；代理模型；OOD 泛化；实时控制。
- 工作提供等离子体物理代理模型的架构比较和装置参考解校验范式，可借鉴于 PIC/束流诊断中的“插值精度不等于外推可靠性”评估。
- 相关性评分：4/5。

## 局限与注意事项

所谓 EXL-50U “validation”是模拟 GS、代理与 SE 参考平衡的对照，而非将该网络部署到真实回路并报告控制效果。OOD 样本仍由规定 GS 参数/几何构造，且指标是磁通误差；它不能证明对未见装置、扰动、诊断噪声或完整实时控制的安全泛化。
