# Investigation of transverse instability in efficient plasma-based accelerators

## 基本信息

- 作者：Arohi Jain; Navid Vafaei-Najafbadi
- 期刊/平台：arXiv preprint
- DOI：https://doi.org/10.48550/arXiv.2607.10497
- 发表时间：2026-07-11
- 来源链接：https://arxiv.org/abs/2607.10497
- 本地 PDF：`daily/2026-07-15/pdfs/Arohi Jain and Navid Vafaei-Najafbadi - 2026 - Investigation of transverse instability.pdf`

## 研究问题

高效率等离子体加速器需要强 beam loading，但强 beam loading 会改变等离子体腔边界并触发横向 beam breakup 不稳定性。论文关注的问题是：能否在保持高能量转移效率的同时，通过可解析模型和 PIC 验证找到稳定运行窗口。

## 方法与模型

- 从 plasma wake potential 推导横向 wake 模型，使模型能自洽描述强 beam loading 下变形的 cavity boundary。
- 扫描效率限制和稳定性阈值，构造可用于设计的运行窗口。
- 使用三维 particle-in-cell 模拟验证解析质心演化，并跟踪定制梯形电子束在 1 m 传播中的加速和横向品质保持。

## 主要结论

- 解析横向 wake 模型与 3D PIC 中的质心演化相符，可用于预估高效率运行下的横向稳定性边界。
- 定制 trapezoidal trailing bunch 可获得最高约 16.5 GeV 能量增益，同时几乎保持横向发射度。
- 模拟给出接近 `80%` 的 wake-to-trailing-bunch 功率转移效率和低于 `1.5%` 的最终相对能散，说明效率-不稳定性约束可通过精细 beam loading 设计缓解。

## 与本仓库方向的关系

- 论文直接服务 PWFA/等离子体尾场加速、束流品质、高效率紧凑加速器和 PIC 验证方向。
- 它与仓库近期收录的 multi-GeV electron comb、TeV regenerative cascading PWFA 和 AWAKE benchmark 条目形成连续脉络：从概念/输出到稳定性和可设计运行窗口。
- 主题关键词：plasma-based accelerator；beam breakup instability；transverse wake；beam loading；3D PIC；emittance preservation。
- 相关性评分：5/5。

## 阅读价值

适合关注紧凑高亮度对撞机、PWFA 设计和高效率束流加载的读者。它把横向不稳定性从定性风险推进到可扫描、可验证的设计约束。

## 局限与注意事项

当前为预印本；结果依赖特定束型、等离子体参数和 1 m 级仿真条件。后续仍需评估注入误差、等离子体非均匀性、实验可达束型和更长级联中的累积容差。
