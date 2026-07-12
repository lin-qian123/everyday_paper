# Characterizing an inverse Compton X-ray source and determining its electron beam parameters using a genetic algorithm

## 基本信息

- 作者：Johannes Melcher; Jen-Fu Tu; Balsa Terzic; Martin Dierolf; Erik Johnson; Franz Pfeiffer; Geoffrey Krafft; Benedikt Gunther
- 期刊/平台：arXiv preprint
- DOI：https://doi.org/10.48550/arXiv.2607.06226
- 发表时间：2026-07-07
- 来源链接：https://arxiv.org/abs/2607.06226
- 本地 PDF：`daily/2026-07-13/pdfs/Johannes Melcher et al. - 2026 - Characterizing an inverse Compton X-ray source.pdf`

## 研究问题

紧凑 inverse Compton X-ray source 通过相对论电子束与激光光子碰撞产生准单色 X 射线，但装置紧凑性限制了完整束流诊断。论文关注能否利用可测的激光、X 射线谱信息，反推出电子束发射度等关键参数，从而实现非侵入式、单谱诊断。

## 方法与模型

- 先给出激光参数和 X 射线参数的测量/确定方法。
- 建立计算成本很低的解析 inverse Compton scattering 谱模型，用于快速预测谱形。
- 将解析谱模型与遗传算法结合，从 X 射线谱形反演电子束参数，并在 Munich Compact Light Source 上验证框架。

## 主要结论

- 单个 X 射线谱携带了碰撞激光束与电子束参数的信息，可用于约束电子束发射度等参数。
- 解析模型计算开销低，适合和遗传算法耦合做快速参数反演。
- 该框架有潜力用于 inverse Compton X-ray source 的实时监测，也可作为储存环或加速器电子束的非侵入式诊断工具。

## 与本仓库方向的关系

- 论文提出用解析逆康普顿散射谱模型结合遗传算法，从单次 X 射线谱反演紧凑 inverse Compton X-ray source 的电子束参数，直接关联激光-电子束碰撞辐射源、束流品质诊断、机器学习/优化方法和紧凑光源应用。
- 主题关键词：inverse Compton source；X-ray source；electron beam diagnostics；genetic algorithm；beam quality；radiation source。
- 相关性评分：5/5。

## 阅读价值

适合关注激光 Compton/Thomson 辐射源、紧凑 X 射线/伽马源、电子束品质诊断和优化算法的读者。它为“只从辐射谱反推束流参数”的实用诊断路线提供了清晰模型框架，也可迁移到激光加速电子束辐射源的在线诊断问题。

## 局限与注意事项

当前验证对象是储存环型 Munich Compact Light Source，而不是 LWFA 电子束；若迁移到激光等离子体加速器，需要重新评估束流 shot-to-shot 波动、能散、发散角、碰撞几何和谱探测器响应对反演稳定性的影响。
