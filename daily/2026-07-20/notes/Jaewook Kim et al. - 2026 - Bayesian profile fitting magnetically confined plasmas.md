# Automated Outlier-Robust Bayesian Profile Fitting for Magnetically Confined Plasmas with Modified Tanh Profiles and Good-and-Bad Gaussian Mixture Likelihoods

## 基本信息

- 作者：Jaewook Kim; Jekil Lee; Laurent Jung; Sang-hee Hahn; Sehyun Kwak
- 期刊/平台：arXiv preprint
- DOI：https://doi.org/10.48550/arXiv.2607.14142
- 发表时间：2026-07-13
- 来源链接：https://arxiv.org/abs/2607.14142
- 本地 PDF：`daily/2026-07-20/pdfs/Jaewook Kim et al. - 2026 - Bayesian profile fitting magnetically confined plasmas.pdf`

## 研究问题

磁约束等离子体的动力学剖面拟合容易受到异常诊断通道和多峰优化面的影响。论文关注的是：如何把 modified tanh 剖面拟合做成可批量运行、抗异常点、可输出质量指标的 Bayesian 工作流，用于后续 kinetic-EFIT、TRANSP、FASTRAN 和数据驱动分析。

## 方法与模型

- 使用 modified tanh 参数化拟合 `n_e`、`T_e`、`T_i` 和环向速度等剖面。
- 引入 Box-Tiao 型 good-and-bad Gaussian mixture likelihood，对异常测量通道自动降权。
- 在确定性 MAP 初值附近启动 affine-invariant ensemble MCMC，降低陷入次优局部极值的风险。
- 自动从 MDSplus 获取 KSTAR 诊断数据，并并行处理任意时间片，输出可回写和下游分析的数据格式。

## 主要结论

- 混合似然能够在保留合理 pedestal 结构的同时，降低污染通道对剖面拟合的偏置。
- 后验异常概率可作为通道级质量指标，为诊断健康状态和数据清理提供辅助信息。
- 批处理层使该方法适合大规模 kinetic profile 生产，而不是只用于单次手动拟合。
- 论文把不确定性量化、异常点识别和生产工作流结合起来，补强聚变诊断数据处理链。

## 与本仓库方向的关系

- 论文直接关联机器学习/统计推断、等离子体诊断、磁约束聚变和数据驱动工作流。
- 虽然不是激光等离子体论文，但对实验诊断数据自动化、异常通道鲁棒处理和剖面反演有可迁移方法价值。
- 主题关键词：Bayesian fitting；outlier robust；plasma diagnostics；MDSplus；KSTAR；data-driven analysis。
- 相关性评分：4/5。

## 阅读价值

适合关注实验诊断数据处理、自动化分析和不确定性量化的人阅读。对未来把激光等离子体诊断数据接入批处理拟合、异常点识别和代理模型训练，也有清晰工程参考。

## 局限与注意事项

方法基于磁约束装置的剖面形状先验和 MDSplus 数据结构，不能直接搬到激光靶瞬态诊断。迁移时需要重新定义剖面模型、时间同步、空间标定和异常通道先验。
