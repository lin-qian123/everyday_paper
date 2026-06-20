# Equation of state measurements of boron nitride under laser-driven compression at the Prague Asterix Laser System facility 笔记

## 0. 论文信息
- 标题: Equation of state measurements of boron nitride under laser-driven compression at the Prague Asterix Laser System facility
- 作者: Hanna Marchenko, Agnieszka Zaras-Szydlowska, Dimitri Batani, Donaldi Mancelli, Diluka Singappuli, Yair Ferber, Eran Greenberg, Artem S. Martynenko, Noaz Nissim, Roman Dudzak, Shubham Agarwal, Pooja Devi, David Ettel, Pavel Gajdoš, Simon Jelinek, Michal Krupka, Miroslav Krus, Libor Juha, Sushil Singh, Katarzyna Liliana Batani
- 期刊: High Power Laser Science and Engineering
- DOI: 10.1017/hpl.2026.10115
- 发表日期: 2026-02-06
- 主题关键词: 高能量密度物理、状态方程、激光驱动压缩、硼氮化物、ICF 材料

## 1. 核心结论
- 论文在 Prague Asterix Laser System 上对六方氮化硼（h-BN）进行了激光驱动冲击压缩状态方程测量，把 BN 在极端条件下的实验数据集进一步往高压区扩展到了约 `9 Mbar`。
- 这项结果的价值不在“发现新奇机制”，而在于把 BN 这种与高能量密度材料、p-B fusion 和潜在 ICF 靶材料都相关的材料，补上了更可靠的实验 EoS 约束点。

## 2. 方法与技术路线
- 实验使用 `438 nm`、约 `350 ps`、最高约 `200 J` 的激光脉冲，并通过 phase plate 形成约 `400 μm` 的平顶光斑，做标准的激光驱动冲击压缩。
- 冲击波速度通过 streaked optical pyrometer 的时空分辨自发光测量，同时在 BN 和参考材料中测量，再用阻抗匹配思路反推出 BN 的 EoS。

## 3. 与当前研究方向的关系
- 相关性评分: 8/10；影响力评分: 7/10。
- 这篇工作直接落在 HEDP / ICF 材料物性这一层，对做辐射流体、冲击压缩、靶设计或需要可靠材料表征的建模工作都很有参考价值。它也和仓库中近期关注的 WDM / ICF 方向形成了很自然的互补。

## 4. 可复现实验/仿真要点
- 如果后续想在仿真里使用这篇结果，关键不是只抄一条 Hugoniot 数据，而是明确参考材料、测速诊断和误差条是怎样传到 EoS 反演里的。
- 对建模者更有价值的复现点是：把这组新 BN 数据和已有 tabular EoS / average-atom / DFT-MD 模型逐一比对，看在 `Mbar` 级压缩区是否会影响冲击时序、压缩率或靶层阻抗匹配。

## 5. 后续行动项
- 如果后面你要继续跟进 ICF 靶材料或 p-B 相关路线，值得把 BN、Be、CH 这类常见材料的 EoS 数据和适用区间整理成一个对照表。
- 这篇论文也适合作为近期“正式来源优先”筛选中保留的样板，因为它不是泛激光工程，而是和 HEDP/ICF 核心物理直接相关的实验材料数据。
