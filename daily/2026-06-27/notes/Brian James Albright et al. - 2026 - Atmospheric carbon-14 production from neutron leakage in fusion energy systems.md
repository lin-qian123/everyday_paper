# Atmospheric carbon-14 production from neutron leakage in fusion energy systems 笔记

## 0. 论文信息
- 标题: Atmospheric carbon-14 production from neutron leakage in fusion energy systems
- 作者: Brian James Albright, James Alastair Mercer-Smith
- 平台: arXiv 预印本
- DOI: 10.48550/arXiv.2606.23953
- 发表日期: 2026-06-22
- 主题关键词: neutron leakage、carbon-14、fusion systems、radiological assessment、beamlines and ducts

## 1. 核心结论
- 论文把“聚变装置末端中子外逸进入含氮气体后会产生多少大气 `14C`”明确写成了一个可缩放的源项问题，而不是只停留在定性提醒。
- 对 14.1 MeV DT 中子，在代表性近地几何下，泄漏中子转化为 `14C` 的条件概率约为 `0.25-0.50`；若泄漏谱更软，产额还可能更高。
- 按文中尺度估算，若 1 GWe 聚变电站有百分级中子泄漏进入空气，其大气 `14C` 源项就会逼近天然全球产额的同量级；若扩展到大规模装机，平均泄漏分数需压到 `10^-6` 量级才能把额外 `14C` 控制在天然源的 `10%` 左右。

## 2. 方法与技术路线
- 文章用 MCNP6.2 做中子输运与源项估算，核心不是为某一个具体装置做详尽屏蔽设计，而是抽出“终端泄漏到空气后的条件响应”这一更通用的量。
- 这种处理把 reactor-specific 的 shielding、duct、port、window 等差异留在前端，只把最终进入含氮气体的中子当作输入，因此更适合作为部署级 screening tool。
- PDF 前几页可见信息摘录: `For 14.1 MeV deuterium-tritium source neutrons, the conversion probability is 0.25-0.50 ... At a 2500 GWe fleet scale, limiting fusion-derived radiocarbon to 10% of the natural source implies a mean atmospheric leakage fraction of order 10^-6.`

## 3. 与当前研究方向的关系
- 相关性评分: 8/10；影响力评分: 6/10。
- 这篇和仓库扩展后的“激光加速电子/离子束应用、光核反应、中子源、辐射防护”支线高度相关。虽然对象是 fusion energy systems，不是激光装置本身，但它对任何会把快中子通过 port、beamline、duct 或转换结构放到外环境中的系统都提供了很实用的上限思维。

## 4. 可复现实验/仿真要点
- 如果后续要把它迁移到激光驱动次级中子源场景，关键不是直接照搬数字，而是复用它的“终端泄漏分数 -> 环境源项”框架，再换成对应的源谱和几何。
- 对光核/韧致辐射驱动中子方案，这篇尤其提醒要把 beam dump、target cave、诊断开口和束线流道一起纳入环境约束，而不只是看靶室中心区剂量。
- 可作为后续专题的上游参考：中子产额工程优化不能只追求源强，还要同时管理外逸谱形、开口几何和通风/空气耦合路径。

## 5. 后续行动项
- 可与仓库中后续收集到的光核中子源、激光离子加速核应用、辐射防护类论文并读，整理“源强提升”和“环境约束”之间的共同设计变量。
- 若后续关注实验站或束线系统设计，可把这篇作为“为什么 beamline / duct / streaming path 不能晚做”的提醒性文献。
