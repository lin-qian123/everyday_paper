# 每日论文索引 - 2026-10-03

## 今日概览

- 运行日期：2026-10-03
- 新增论文数：5（1 篇标注已被 *Applied Radiation and Isotopes* 接收的作者稿，4 篇 2026-10-01 投稿、2026-10-02 官方公告的 arXiv 预印本）
- 最新性：核对官方 arXiv `/new` 页面 2026-10-02 公告批次，并用 Crossref 检查 2026-10-01 至 10-03 正式元数据；未发现具有可验证全文且优先级更高的正式增量。
- 主题分布：AWAKE 通道 schlieren 符号回归；有限 β 守恒漂移动理学 PIC；PIC 网格不稳定性；聚变 AI 毫秒推理；`⁶⁵Cu(α,n)⁶⁸Ga` 厚靶中子/同位素应用。
- 去重：按 DOI/arXiv identifier、规范化标题、402 条完成台账、21 条重试队列、历史 `daily/`、摘要和物理场景检查；5 篇均为独立作品。
- PDF / 正文：5 份官方 arXiv PDF 均通过 `%PDF-`、`file`、`pdfinfo`、SHA-256 与非空 `pdftotext -layout`；20 个选定页面完成渲染和人工查看。Meisel 条目是已接收作者稿，不是期刊 VOR。
- 重试：21 条既有来源受限记录未出现新的合法全文信号，未重复空跑，队列不变。
- 覆盖边界：多来源搜索层未返回可用结果，Crossref 主题检索用于正式元数据核对，官方 arXiv 新稿页用于最新批次；这是定向增量筛选，不宣称穷尽全部期刊或数据库。

## 论文清单

### 1. Quantitative schlieren imaging of a laser-ionized plasma channel in atomic vapor using symbolic regression

- 标识符：[arXiv:2610.01485](https://arxiv.org/abs/2610.01485)；归档 DOI `10.48550/arXiv.2610.01485`
- 提交日期：2026-10-01（2026-10-02 官方公告批次）
- 期刊 / 平台：arXiv 预印本
- 本地 PDF：`daily/2026-10-03/pdfs/Demeter - 2026 - AWAKE plasma channel schlieren symbolic regression.pdf`
- 中文笔记：[Demeter - 2026 - AWAKE plasma channel schlieren symbolic regression.md](notes/Demeter%20-%202026%20-%20AWAKE%20plasma%20channel%20schlieren%20symbolic%20regression.md)
- 来源影响力分：7/10
- 专业相似度分：9/10
- 推荐理由：把 AWAKE 近共振 schlieren 诊断、模拟标定和可解释机器学习连起来，适合比较“黑箱反演”和“可审计解析式”的代价与泛化边界。
- 一句话总结：约 `10^3` 个模拟样本即可把通道等效半径反演到 `0.02–0.03 mm` 平均绝对误差并恢复旧实验的能量幂律，但鞘宽和跨密度迁移仍依赖碰撞展宽与探针失谐。

### 2. Electromagnetic drift-kinetic particle-in-cell model with energy and charge conservation for studying finite-β plasmas

- 标识符：[arXiv:2610.01429](https://arxiv.org/abs/2610.01429)；归档 DOI `10.48550/arXiv.2610.01429`
- 提交日期：2026-10-01（2026-10-02 官方公告批次）
- 期刊 / 平台：arXiv 预印本（标注 submitted to *Journal of Computational Physics*）
- 本地 PDF：`daily/2026-10-03/pdfs/Morozov et al. - 2026 - Conservative drift kinetic PIC.pdf`
- 中文笔记：[Morozov et al. - 2026 - Conservative drift kinetic PIC.md](notes/Morozov%20et%20al.%20-%202026%20-%20Conservative%20drift%20kinetic%20PIC.md)
- 来源影响力分：7/10
- 专业相似度分：10/10
- 推荐理由：直接处理有限 β 磁化等离子体中电子回旋/Debye 尺度的 PIC 代价，并把放大时间步、磁化电流和离散守恒闭合起来。
- 一句话总结：在 `Δt=10Ω_e^-1`、`Δx=10c/ω_pe` 的测试中仍给出约 `10^-12` 能量误差和 `10^-14` 电荷误差，但目标混合物种模型与复杂几何性能尚未验证。

### 3. Analysis of grid instabilities in particle-in-cell codes based on a meshfree approach

- 标识符：[arXiv:2610.02052](https://arxiv.org/abs/2610.02052)；归档 DOI `10.48550/arXiv.2610.02052`
- 提交日期：2026-10-01（2026-10-02 官方公告批次）
- 期刊 / 平台：arXiv 预印本
- 本地 PDF：`daily/2026-10-03/pdfs/Finn and Evstatiev - 2026 - PIC grid instability analysis.pdf`
- 中文笔记：[Finn and Evstatiev - 2026 - PIC grid instability analysis.md](notes/Finn%20and%20Evstatiev%20-%202026%20-%20PIC%20grid%20instability%20analysis.md)
- 来源影响力分：7/10
- 专业相似度分：10/10
- 推荐理由：从无网格极限追踪 MCP/ECP 离散谱，给出网格、每格粒子数与形函数阶数如何共同控制 aliasing 增长的可检验标度。
- 一句话总结：冷静止一维体系中 ECP 线性稳定，MCP 的增长率随线性 spline 约按 `N_ppc^-1`、高阶 spline 约按 `N_ppc^-3` 降低；该结论不能直接外推到多维电磁 PIC。

### 4. Is Your AI Fast Enough to Run a Fusion Reactor?

- 标识符：[arXiv:2610.00845](https://arxiv.org/abs/2610.00845)；归档 DOI `10.48550/arXiv.2610.00845`
- 提交日期：2026-10-01（2026-10-02 官方公告批次）
- 期刊 / 平台：arXiv 预印本
- 本地 PDF：`daily/2026-10-03/pdfs/Chen et al. - 2026 - Fusion AI inference benchmark.pdf`
- 中文笔记：[Chen et al. - 2026 - Fusion AI inference benchmark.md](notes/Chen%20et%20al.%20-%202026%20-%20Fusion%20AI%20inference%20benchmark.md)
- 来源影响力分：7/10
- 专业相似度分：9/10
- 推荐理由：把 DIII-D/ITER 控制周期与十个模型的实际部署后端延迟对齐，能直接指导实时诊断和控制的模型—硬件协同选择。
- 一句话总结：大于约 `5M` 参数的模型通常需要 GPU，TokEye 的 GPU 延迟约 `1.01 ms`、比最佳 CPU 快约 `201×`，但硬件不对等且没有反应堆或 PCS 闭环验证。

### 5. Thick-target Yield of 65Cu(α,n)68Ga Near Threshold and Implications for Nuclear Medicine, Deep Underground Detector Backgrounds, and Nucleosynthesis

- 标识符：[arXiv:2610.01719](https://arxiv.org/abs/2610.01719)；归档 DOI `10.48550/arXiv.2610.01719`
- 提交日期：2026-10-01（2026-10-02 官方公告批次）
- 期刊 / 平台：已标注 accepted to *Applied Radiation and Isotopes*；本地为 arXiv 接收稿/预印本，非 VOR
- 本地 PDF：`daily/2026-10-03/pdfs/Meisel et al. - 2026 - Cu65 alpha n Ga68 thick target yield.pdf`
- 中文笔记：[Meisel et al. - 2026 - Cu65 alpha n Ga68 thick target yield.md](notes/Meisel%20et%20al.%20-%202026%20-%20Cu65%20alpha%20n%20Ga68%20thick%20target%20yield.md)
- 来源影响力分：8/10
- 专业相似度分：9/10
- 推荐理由：以直接中子计数约束近阈值核反应，再明确分开同位素产额、地下本底和核合成外推，适合作为激光/常规离子束核应用的基础数据参照。
- 一句话总结：`8 MeV` 天然铜的测量锚定活度为 `0.12±0.02 MBq/μAh`，而 `14 MeV` 富集铜的 `161^{+5}_{-24} MBq/μAh` 是 TALYS+SRIM 外推，不是高流强生产实测。

## 未入库候选与取舍

- `arXiv:2610.00243` 的 EAST 温度剖面 attention network 与实时控制相关，但提交日期早于本轮最新批次，且物理/部署增量不及 MILF-BENCH 的跨模型延迟基准。
- `arXiv:2610.00244` 的 EAST 知识图谱 ELM 识别同样偏早，且离线分类结果与本轮“实时推理预算”主线相比优先级较低。
- `arXiv:2610.00611` 的 NSLS-II FLUKA 屏蔽 proceedings 与防护相关，但装置和束流场景距激光/聚变主线较远。
- `arXiv:2610.01406` 的 activation-depth framework 有材料活化价值，但本轮优先选择了带直接厚靶中子测量的 `⁶⁵Cu(α,n)`。
- 21 条既有来源受限记录没有新的合法全文线索，继续保留重试状态，不从摘要生成笔记。

## 当日综合总结

- 两篇 PIC 工作互补：Morozov 关注跨越电子尺度时的离散守恒，Finn/Evstatiev 关注网格采样引出的离散谱不稳定；“能量守恒”和“冷静止线性稳定”都不能代替生产配置的完整回归测试。
- 两篇数据/AI 工作强调部署端闭合：AWAKE 符号回归需要随光谱与仪器重标定，聚变 AI 则必须把平均推理延迟扩展到尾时延、数据链路和闭环稳定性。
- `⁶⁵Cu(α,n)` 给出本轮最直接的核实验数据，但核医学活度、高流强靶和核合成速率包含不同程度的 TALYS/SRIM 与工程外推，不能与近阈值中子计数混为一层证据。
- 推荐阅读顺序：守恒漂移动理学 PIC → PIC 网格不稳定性 → AWAKE schlieren 符号回归 → 聚变 AI 延迟 → `⁶⁵Cu(α,n)`，依次覆盖算法守恒、数值稳定、诊断反演、实时部署与核应用数据。
