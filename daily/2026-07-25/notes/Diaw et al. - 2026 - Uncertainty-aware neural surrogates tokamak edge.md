# Cycle-Consistent and Uncertainty-Aware Neural Surrogates for Tokamak Edge Plasmas

## 基本信息

- 作者：Abdourahmane Diaw; Sebastian De Pascuale; Jae-Sun Park; Ivan Paradela Perez; J. D. Lore; S. Dasbach
- 期刊/平台：arXiv preprint
- DOI：https://doi.org/10.48550/arXiv.2607.21407
- 发表时间：2026-07-23
- 来源链接：https://arxiv.org/abs/2607.21407
- 本地 PDF：`daily/2026-07-25/pdfs/Diaw et al. - 2026 - Uncertainty-aware neural surrogates tokamak edge.pdf`

## 研究问题

Tokamak 边界与偏滤器等离子体的高保真 SOLPS-ITER 模拟昂贵且在宽参数扫描中容易不收敛，难以直接服务于实时控制、反演和不确定度评估。本文目标是在不牺牲物理状态场预测精度的前提下，给出可自检的快速代理模型。

## 方法与模型

- 基于 DIII-D lower-single-null 的 SOLPS-ITER 数据，使用条件 U-Net 将 5 个控制量映射为二维 `Te`、`Ti`、`ne` 与流速场。
- 冻结前向网络后以优化反演控制量，并以正反循环一致性作为无需真值标签的可靠性检查。
- 另建 committee MLP 预测外中平面和偏滤器靶板的一维 `Te/ne` 剖面；成员间分歧用于不确定度与主动学习指示。

## 主要结论

- 各二维状态场的归一化 RMSE 小于 2.6%，Pearson 相关系数大于 0.95；循环一致性使平均循环 `R²` 从 0.59 提升到 0.99。
- 五个控制参数的反演相关系数均不低于 0.97，能够恢复仅前向训练难以辨识的核心粒子源。
- 约 4 百万参数的模型可在毫秒级给出二维预测，比原始 SOLPS-ITER 快约 5--6 个数量级；k-d tree warm-start 的收敛完成率超过 95%。

## 与本仓库方向的关系

- 直接连接机器学习、边界等离子体输运与磁约束聚变控制，是高保真模拟向实时数字孪生过渡的可复现路线。
- 主题关键词：SOLPS-ITER；tokamak edge；neural surrogate；cycle consistency；uncertainty quantification；digital twin。
- 相关性评分：4/5。

## 局限与注意事项

结果基于特定 DIII-D 工况及五维控制空间；循环一致性衡量的是模型内部自洽，不替代对装置诊断数据、脱靶阈值和分布外参数的独立验证。
