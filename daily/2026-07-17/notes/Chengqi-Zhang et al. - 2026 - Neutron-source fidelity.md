# Neutron-source fidelity for laser-driven D--D lithium-blanket tritium-breeding tests

## 基本信息

- 作者：Chengqi Zhang; Yang He; Mamat Ali Bake; Baisong Xie
- 期刊/平台：arXiv preprint
- DOI：https://doi.org/10.48550/arXiv.2607.13585
- 发表时间：2026-07-15
- 来源链接：https://arxiv.org/abs/2607.13585
- 本地 PDF：`daily/2026-07-17/pdfs/Chengqi-Zhang et al. - 2026 - Neutron-source fidelity.pdf`

## 研究问题

激光驱动 D-D 中子源可为锂包层产氚实验提供紧凑、可控的辐照场，但真实源的能谱和角分布与常用的 2.45 MeV 各向同性理想源不同。论文关注的问题是：在锂包层产氚测试中，忽略真实源谱和方向分布会造成多大偏差。

## 方法与模型

- 使用 PIC 模拟 target-normal-sheath-accelerated 氘离子。
- 将氘离子分布耦合到厚靶 `D(d,n)^3He` 中子源模型。
- 进一步接入 Monte Carlo 中子输运，比较二维源、匹配三维源和理想 2.45 MeV 各向同性源。
- 分离研究真实能谱和真实发射方向对天然锂、富集锂以及聚乙烯慢化条件下产氚量的影响。

## 主要结论

- 对天然锂，二维真实源相对理想源可使每源中子产氚量改变 `-2.5%` 到 `+54.1%`。
- 匹配三维计算中，真实源使天然锂产氚量增加约 43.5%，并改变关键产额比。
- 偏差主要来自中子能谱而非方向分布；真实方向在三维案例中只额外贡献约 1% 量级修正。
- 90% `^6Li` 富集条件下，总变化保持在约 `±1.5%`，说明源谱效应受包层同位素组成强烈调制。
- 聚乙烯慢化可使产氚量提高约一个数量级，但会削弱甚至反转真实源相对理想源的增益。

## 与本仓库方向的关系

- 论文直接覆盖激光离子加速、D-D 中子源、锂包层产氚、核反应应用、PIC 到 Monte Carlo 多物理耦合和源项保真度评估。
- 它与仓库扩展方向中的“激光离子加速在核反应和材料研究中的应用”“转换效率和实验诊断”高度相关。
- 主题关键词：laser-driven neutron source；D-D fusion neutron；TNSA deuteron；lithium blanket；tritium breeding；Monte Carlo transport。
- 相关性评分：5/5。

## 阅读价值

适合关注激光驱动中子源、产氚包层测试、核反应应用和多物理模拟链路的读者。该文的价值在于提醒 compact laser-driven source 不能简单替换为理想 2.45 MeV 各向同性源，源项保真度会实质影响产额解释。

## 局限与注意事项

当前为预印本，结果依赖 PIC 源项、厚靶反应模型和 Monte Carlo 几何设定。实际实验还需考虑靶热负载、重复频率、中子诊断、绝对归一化、散射背景和辐射防护边界。
