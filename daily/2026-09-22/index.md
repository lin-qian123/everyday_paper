# 每日论文索引 - 2026-09-22

## 今日概览

- 运行日期：2026-09-22
- 新增论文数：3（1 篇 2026-09-21 正式期刊论文，2 篇 2026-09-18 提交并于 2026-09-21 列出的 arXiv 预印本）
- 最新性：官方 arXiv 目标分类已更新到 2026-09-21 批次。正式来源检索覆盖 Crossref 2026-09-20 至 2026-09-22 元数据，并核对 APS、IOP、PST、DOI 与 arXiv 页面。本轮没有把 9 月 18 日提交的两篇预印本写成 9 月 22 日新投稿。
- 主题分布：Hall 推进器 EDI 异常电子输运的 3D PIC；KSTAR 约束的托卡马克 EC 微波气体击穿 Monte Carlo；高能电子打高 Z 靶后的慢正电子慢化器设计。
- 检索范围：官方 arXiv `physics.plasm-ph`、`physics.acc-ph`、`physics.comp-ph`、`nucl-ex`、`physics.ins-det`、`physics.optics`、`physics.atom-ph`、`nucl-th` 与 `hep-ph` 新论文列表；Crossref、出版商和 DOI 元数据；通用 Web 检索与本地多源搜索器。本地搜索器返回 0 条，最终选择不依赖聚合器排序，也不宣称穷尽全部数据库。
- 去重：按 DOI/arXiv identifier、规范化标题、366 条完成台账、18 条结构化重试队列和历史 `daily/` 核对。正式 PRE 与其 `arXiv:2603.14849` 作者稿按同一作品处理，只建立一个正式 DOI 记录。
- PDF / 正文：3 份全文均通过 `%PDF-`、`file`、`pdfinfo`、SHA-256 和非空 `pdftotext -layout`；3 份均完成 MinerU 转换，共保留并逐张查看 11 张关键图。详见 [pdf_validation.json](pdf_validation.json)。
- 来源边界：PRE 是正式 APS 论文但完全由作者模拟；Gwak 包含 KSTAR 实验边界验证，ITER 数值仍是外推；Crisp 是 workshop 预印本和 Geant4/扩散模型，驱动器是 linac 而不是激光等离子体电子束。

## 论文清单

### 1. Near-wall pathways of anomalous electron transport in Hall thrusters revealed by three-dimensional particle-in-cell simulations

- 标识符：[DOI: 10.1103/p8v6-66mq](https://doi.org/10.1103/p8v6-66mq)
- 发表日期：2026-09-21
- 期刊 / 平台：*Physical Review E* **114**, 035211（正式期刊论文）
- 本地 PDF：`daily/2026-09-22/pdfs/Liu et al. - 2026 - Near-wall electron transport in Hall thrusters.pdf`
- 中文笔记：[Liu et al. - 2026 - Near-wall electron transport in Hall thrusters.md](notes/Liu%20et%20al.%20-%202026%20-%20Near-wall%20electron%20transport%20in%20Hall%20thrusters.md)
- 来源影响力分：9/10
- 专业相似度分：8/10
- 推荐理由：正式论文把真实磁场、介质壁充电、二次电子发射、MCC 电离、连续中性气体和开放羽流边界放入长时间 3D PIC，并显式报告时间步、网格、粒子数和羽流域敏感性，适合作为“PIC 机制结论如何限定数值可信度”的案例。
- 一句话总结：三种边界闭合都留下下游双近壁 EDI 输运通道，相关项解释作者模拟中约 `80–90%` 的带平均电流；但绝对迁移率、高波数谱和 `40 μs` 晚期结构尚无匹配每格粒子数的全域网格收敛，也没有实验一一对照。

### 2. Mechanism of Ionization Avalanche in Tokamak Microwave Gas Breakdown

- 标识符：[arXiv:2609.21429](https://arxiv.org/abs/2609.21429)；归档 DOI `10.48550/arXiv.2609.21429`
- 提交日期：2026-09-18（2026-09-21 官方新论文列表）
- 期刊 / 平台：arXiv 预印本
- 本地 PDF：`daily/2026-09-22/pdfs/Gwak et al. - 2026 - Tokamak microwave gas breakdown.pdf`
- 中文笔记：[Gwak et al. - 2026 - Tokamak microwave gas breakdown.md](notes/Gwak%20et%20al.%20-%202026%20-%20Tokamak%20microwave%20gas%20breakdown.md)
- 来源影响力分：8/10
- 专业相似度分：9/10
- 推荐理由：把 KSTAR 零环电压 EC 击穿实验与三维 Monte Carlo 的非线性波—粒子作用、碰撞、电离和开场线输运连成可检验阈值，并明确把初始击穿与后续 burn-through 分开。
- 一句话总结：KSTAR 两种连接长度下的模拟—实验压力边界相符到约两倍；模型据此预测 ITER 相关 `D₂≈2 mPa`、残余极向场约 `30 G` 时 `1 MW` EC 功率可触发初始气体击穿，但这不是完整启动或等离子体电流建立的验证。

### 3. Moderator Modeling for High Intensity Slow Positron Sources

- 标识符：[arXiv:2609.22036](https://arxiv.org/abs/2609.22036)；归档 DOI `10.48550/arXiv.2609.22036`
- 提交日期：2026-09-18（2026-09-21 官方新论文列表）
- 期刊 / 平台：arXiv / LEEPP2026 workshop 预印本
- 本地 PDF：`daily/2026-09-22/pdfs/Crisp et al. - 2026 - Moderator modeling for slow positron sources.pdf`
- 中文笔记：[Crisp et al. - 2026 - Slow positron moderator modeling.md](notes/Crisp%20et%20al.%20-%202026%20-%20Slow%20positron%20moderator%20modeling.md)
- 来源影响力分：7/10
- 专业相似度分：8/10
- 推荐理由：直接覆盖“高能电子—高 Z 转换靶—正电子—材料/基础物理应用”的后端效率瓶颈，并把单能慢化效率与 `65 MeV e⁻` 打 `6 mm W` 后的快正电子谱放在同一张图中。
- 一句话总结：Geant4-Penelope 与经验扩散模型显示 `<300 keV` 时固态 Ne 可比 W 高约一个数量级，MeV 区多层 W 更优，靶回返可使低能效率增加约 `2–4` 倍；这些是 linac 条件的单粒子模型结果，不是激光正电子源的实测通量或完整 start-to-end 效率。

## 未入库候选与取舍

- `arXiv:2609.21951` 给出圆柱等离子体源的方位模分解 PIC，方法清晰且宣称相对二维 PIC 有约一个数量级计算时间节省；但验证集中于低温 Penning 放电，今天优先正式 3D PIC 的边界/收敛证据链以及含 KSTAR 实验约束的工作。
- `arXiv:2609.21634` 是约 `20–100 keV` 薄箔电子散射的半解析 Bethe 输运解；对转换靶前端有方法相关性，但能区和物理链与当前高能电子—次级辐射目标较远，未挤入前三篇。
- `10.1088/1741-4326/aea431` 是 EAST 复机阶段的杂质—压力启动指标，Crossref 在 9 月 21 日更新但其他正式来源显示 9 月 8 日已有记录；它与今天 Gwak 的托卡马克启动主题重叠，且后者提供更直接的实验—动理学机制闭环。
- 本轮 9 月 21 日新批次没有发现同等质量、全文可验证且未入库的激光加速、HEDP 或强场 QED 论文，因此没有用低相关候选填充这些主题。

## 当日综合总结

- Liu 说明三维 PIC 的真正增益不仅是解析 EDI 波，还能从强振荡场中提取净输运的空间拓扑；同时也展示了“质性拓扑较稳健”和“定量幅值未收敛”必须并列书写。
- Gwak 说明托卡马克微波击穿的源项与损失项都依赖非 Maxwell 电子历史；KSTAR 阈值检验提高了 ITER 外推可信度，但实验只闭合初始击穿边界。
- Crisp 说明正电子源的后端效率必须用入射能谱加权：材料扩散长度、靶回返、慢化器几何和热隔离相互耦合，不能只比较单一峰值效率。
- 推荐阅读顺序：先看 Gwak 图 4/5 区分实验验证与 ITER 外推；再看 Liu 图 8/11 理解平均输运拓扑和谱敏感性；最后看 Crisp 图 3/4 把几何、材料和实际快正电子能谱联系起来。
