# 每日论文索引：2026-10-27

新增 **5 篇独立作品**，台账 **495 → 500**：1 篇正式 VOR、1 篇正式发表记录对应较早作者稿、3 篇近期 arXiv 全文。5 份 PDF **59 页、8,444,702 字节**通过独立核验，全部 MinerU pipeline 成功；目视检查 22 个身份/关键页及 9 幅原图摘录。PDF、布局文本和 MinerU 全文保留本地并由 Git 忽略。

## 阅读顺序与证据

| 作品 | 结果与限制 | 笔记 |
|---|---|---|
| [Maximization of nuclear fusion reactivity via optimal energy distributions](https://doi.org/10.1103/xhzy-hxdw) | 正式 PRE VOR，10-23；固定平均能量和 MB 混合族内凹包络优化，DT 例子约 2.04、DD 约 1.7；非实验净增益。 | [中文全文笔记](notes/Onofrio%20et%20al.%20-%202026%20-%20Optimal%20energy%20distributions%20fusion%20reactivity.md) |
| [Self-Synchronized Soft X-Ray and Infrared Free-Electron Lasers from a Single Prebunched Electron Beam](https://doi.org/10.1103/3kmz-18bp) | 正式 PRL 10-26；实际读 8-15 对应作者稿，197 μJ/400发、595 μJ 低频输出等数值属于作者稿；VOR 401，细节待对照。 | [中文全文笔记](notes/Kang%20et%20al.%20-%202026%20-%20Self%20synchronized%20soft%20X%20ray%20infrared%20FEL.md) |
| [Plasma transport by carrier electrons: delocalization length for heat-flux](https://doi.org/10.48550/arXiv.2610.32085) | 10-23 arXiv，PDF 印 10-26；线性 VFP/拟合热输运，局部限流值、图例 f 与正文定义及非线性外推仍需核实。 | [中文全文笔记](notes/Walsh%20-%202026%20-%20Carrier%20electron%20heat%20flux%20nonlocality.md) |
| [Two-component Bayesian modeling in the data analysis of collective Thomson scattering](https://doi.org/10.48550/arXiv.2610.32033) | 10-23 arXiv，PFR 10-16 接受但未核实正式 DOI；既有 2.9 ns 实测谱的 Maxwellian 双谱六维后验，非新实验。 | [中文全文笔记](notes/Nakano%20et%20al.%20-%202026%20-%20Two%20component%20Bayesian%20Thomson%20scattering.md) |
| [Coherent axion electrodynamics in OSIRIS: a counter-propagating axion-photon parametric instability](https://doi.org/10.48550/arXiv.2610.32091) | 10-23 arXiv，PDF 印 10-26；OSIRIS 一维周期真空/大代码耦合的理论—场基准，非轴子观测、非粒子路径验证。 | [中文全文笔记](notes/Radford%20et%20al.%20-%202026%20-%20Coherent%20axion%20electrodynamics%20OSIRIS.md) |

## 检索、版本与去重

- Crossref 对 **10-25 至 27** 作 10 组有界主题查询，各最多 75 行，返回 **750 行、552 个唯一 DOI**，请求无错误。含词面无关、非期刊与不同日期口径结果，不是穷尽检索。APS 最新正式目录补入 10-23 的反应率论文。
- 官方 arXiv 两组五分类各 300 条、并集 **516 条**，最新可见提交为 **10-23T17:40:04Z**；核医学/仪器与医学物理/高能理论均有覆盖。预印本精确标题的 Crossref 前三项没有验证匹配正式版本；CTS 官方页面注明 PFR 接受状态，明确区别于出版。
- 按 DOI、arXiv 别名、规范化标题、URL、作者组与物理场景去重。FEL 的新正式标题与旧 arXiv 标题不同，通过作者/装置识别为同一作品，保留一个正式 DOI 与作者稿别名；未将 401 正式端点误记为无全文入库。
- **既有 Karmakar 漂移声波 DOI 10.1103/mmzz-gq7q 不重复计数**。APS 目录确认 10-26 正式发表，旧台账 10-07 为接受日期；已在原笔记与台账原位纠正日期和卷页，现有作者稿仍非 VOR。本轮未重新验收其科学内容。
- 既有 **45 条重试保持不变，新增 1 条，队列 45→46**：10-26 新闻引出的 PRL 日冕加热 10.1103/tmll-l58c 实际正式发表在 10-20；官方全文代理/直连均 HTTP 401，精确标题 arXiv 零结果，未验证合法作者稿，故不写摘要笔记。其中 JCP 10.1016/j.jcp.2026.114707 与完成台账有历史交集，但完成记录 PDF 为空，故保留全文恢复任务，不把它删除成“已恢复”。其余旧出版商/embargo 条目未有新开放信号，不重复空跑。
- Tokamak-SI、Gkeyll 负三角度、DoseRAD2026、DeepONet 中子数据压缩作为较低优先级元数据线索，未计为全文阅读或入库。

## 本轮应重点保留的限制

1. 聚变凹包络是指定 MB 混合、平均能量与支持区间内的理论上界，未计算维持非热分布的代价或真实冷热碰撞交叉项；峰归一化增量与当前温度增益倍数不同。
2. OSIRIS 采用大代码耦合、理想驻波、无粒子真空基准；线性粒子插值/open边界与非 PML 限制不能省略。没有本地代码运行或轴子探测证据。
3. 热输运是线性模拟合与 VFP 保留点测试；局部梯度没有全局模信息，不能宣称通用非局域闭合已解决。Fig. 8 的 f 标定与正文 f=δ 需核对定义；最大残差和未测试混合磁角均在笔记记录。
4. CTS 是已有实验谱反演，Maxwellian 失配峰、有效同方差似然、先验和双谱权重均影响后验；较窄后验不保证更接近真值。
5. FEL 详细数值来自旧作者稿，正式版改用 SXR/MIR 术语；“jitter-free”缺逐发相对到达时间分布，不视为零抖动验收。拍频扫描 μJ 为能量而非强度。
6. 本轮未重新运行作者求解器、模型、输运或实验；未新增激光转换靶—光核中子/核素端到端实测、剂量或防护验收。

## 核验与可追溯记录

[PDF/哈希](pdf_validation.json) · [下载与作者稿回退](download_report.json) · [来源元数据](research/sources.jsonl) · [有界检索与筛选](research/research-run.json) · [版本核查](research/version-checks.json) · [日冕加热全文重试](research/corona-fallback.json) · [MinerU](research/mineru-attempts.json) · [原图来源](research/figure-manifest.json) · [运行结果](run_results.json)
