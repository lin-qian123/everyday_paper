# everyday_paper

一个持续更新的高功率激光、等离子体物理与相关应用论文索引仓库。按天搜集、去重、下载并分析本仓库研究方向相关论文，并将已入库论文整理为分类索引。

## 目录

- [项目定位](#项目定位)
- [关注主题](#关注主题)
- [索引文件](#索引文件)
- [仓库结构](#仓库结构)
- [分类索引](#分类索引)
- [当前状态](#当前状态2026-07-23)
- [去重规则](#去重规则)
- [PDF 下载稳健性](#pdf-下载稳健性)
- [维护约定](#维护约定)

## 项目定位

仓库内容包括：

- 每日跟踪激光等离子体、强场 QED、高能量密度物理、PIC、机器学习等方向的新论文。
- 优先从正式发表来源检索，必要时补充高质量 arXiv 预印本。
- 为新增论文下载并校验 PDF，生成中文结构化笔记。
- 维护分类索引、论文页、每日索引和 GitHub 同步记录。

## 关注主题

- 激光等离子体（laser plasma）
- 强场 QED（strong-field QED）
- 高能量密度物理（high energy density physics）
- PIC 及相关计算方法
- 机器学习 / 数据驱动方法 / 先进算法在上述方向中的应用与结合
- 激光加速电子束、离子束及其应用：包括电子束打转换靶产生韧致辐射 / 伽马源、光核反应、中子 / 同位素产生、核诊断、辐照、诊疗、材料研究，以及相关束流品质、靶设计、转换效率和辐射防护问题

## 索引文件

- 总索引：[`INDEX.md`](./INDEX.md)
- 分类索引：[`categories/`](./categories/)
- 单篇论文索引：[`papers/<paper>/README.md`](./papers/)
- 每日索引：[`daily/README.md`](./daily/README.md)
- 中文笔记：`daily/YYYY-MM-DD/notes/`

## 仓库结构

- `daily/`：按日期归档的每日论文索引、下载报告、中文笔记和运行结果。
- `papers/`：按单篇论文生成的索引页，由 `scripts/build_indexes.py` 自动维护。
- `categories/`：按主题生成的分类索引，由 `scripts/build_indexes.py` 自动维护。
- `state/processed_articles.json`：已处理论文去重台账和索引数据源。
- `state/daily_retry_candidates.json`：下载失败或待重试候选台账。
- `scripts/`：下载、重试和索引构建脚本。
- `templates/`：每日索引模板。
- `yearly/`：历史年度回填索引。
- `AGENTS.md`：自动化执行规则。
- `TODO.md`：待办、阶段记录、阻塞点和接续线索。

## 分类索引

完整索引见 [`INDEX.md`](./INDEX.md) 与 [`categories/README.md`](./categories/README.md)。当前分类包括：

- [激光等离子体与束流加速](./categories/laser-plasma-acceleration.md)
- [激光加速电子/离子束应用](./categories/laser-accelerated-beam-applications.md)
- [强场 QED 与辐射反作用](./categories/strong-field-qed-radiation.md)
- [高能量密度物理、ICF 与实验室天体](./categories/hedp-icf-laboratory-astrophysics.md)
- [PIC、动理学与数值模拟](./categories/pic-and-plasma-simulation.md)
- [机器学习与等离子体物理](./categories/ai-ml-plasma-physics.md)
- [磁约束聚变与 alpha 粒子](./categories/magnetic-fusion-and-alpha-particles.md)
- [实验平台、靶设计与诊断](./categories/experimental-platforms-diagnostics.md)
- [综合等离子体与交叉方法](./categories/general-plasma-and-methods.md)

## 目录约定

- `daily/YYYY-MM-DD/`: 每日运行输出目录
- `daily/YYYY-MM-DD/pdfs/`: 当天新发现论文 PDF
- `daily/YYYY-MM-DD/notes/`: 逐篇中文笔记
- `daily/YYYY-MM-DD/index.md`: 当天论文索引与汇总
- `papers/<paper>/README.md`: 单篇论文索引页
- `categories/*.md`: 主题分类索引
- `INDEX.md`: 总索引
- `state/processed_articles.json`: 已处理论文去重台账
- `templates/daily-index-template.md`: 每日索引模板

## 当前状态（2026-07-23）

- 已连续维护到 `daily/2026-07-23/`。
- 关注主题已扩展到激光加速电子束与离子束应用方向，后续每日检索纳入转换靶韧致辐射、伽马源、光核反应、中子/同位素产生、激光离子加速应用和相关靶/诊断/防护问题。
- `2026-07-23` 补跑 3 条已完成官方 PDF 校验的 arXiv 预印本 `10.48550/arXiv.2607.19930`、`10.48550/arXiv.2607.19976`、`10.48550/arXiv.2607.20278`，分别覆盖磁控放电降阶 Monte Carlo、非冗余孔径电子束尺寸干涉测量，以及低温碰撞等离子体 QBMM 框架。
- `2026-07-22` 补跑 3 条已完成官方 PDF 校验的 arXiv 预印本 `10.48550/arXiv.2607.19180`、`10.48550/arXiv.2607.19495`、`10.48550/arXiv.2607.19610`，分别覆盖复杂等离子体尘埃二聚体有序、正电子素三光子探测，以及加速器 RF 连续相移器。
- `2026-07-21` 先加载 `processed_articles.json`、`daily_retry_candidates.json` 和历史 daily 索引做硬去重；随后复查 Cambridge HPL/JPP 可见正式来源，并使用 arXiv 官方 Atom API 检索近期 `physics.plasm-ph`、`physics.acc-ph`、`physics.comp-ph`、`nucl-ex` 与 `physics.ins-det` 条目。本轮补入 1 条 HPL 正式 accepted manuscript `10.1017/hpl.2026.10182` 和 2 条 arXiv 预印本 `10.48550/arXiv.2607.15805`、`10.48550/arXiv.2607.15857`，分别覆盖双皮秒 PW 脉冲增强激光-箔耦合与次级源、Flying-Focus 增强 LWFA Thomson X 射线源，以及电阻率条件 Koopman neural operator 等离子体湍流代理模型。
- `2026-07-20` 先加载 `processed_articles.json`、`daily_retry_candidates.json` 和历史 daily 索引做硬去重；arXiv API 查询一度超时，因此改用 arXiv 官方近期列表页与单篇页面核对元数据。本轮补入 3 条 arXiv 预印本 `10.48550/arXiv.2607.14495`、`10.48550/arXiv.2607.14142`、`10.48550/arXiv.2607.14286`，分别覆盖近表面微波谐振等离子体击穿、磁约束等离子体 outlier-robust Bayesian 剖面拟合，以及可压缩电阻 Hall-MHD 结构保持数值方法。
- `2026-07-18` 复查正式来源可见检索结果，并使用 arXiv 官方 API 检索近期 `physics.plasm-ph`、`physics.acc-ph`、`physics.comp-ph`、`nucl-ex` 与 `physics.ins-det` 条目；按台账、重试队列和历史 daily 去重。本轮补入 3 条 arXiv 预印本 `10.48550/arXiv.2607.15019`、`10.48550/arXiv.2607.14496`、`10.48550/arXiv.2607.14308`，分别覆盖 AP 五矩两物种等离子体到 MHD 的多尺度耦合、旋转 p-11B 多流体平衡中的聚变功率/韧致辐射损失参数扫描，以及弱非线性动理学等离子体端到端量子算法。
- `2026-07-17` 复查 Cambridge `High Power Laser Science and Engineering` / `Journal of Plasma Physics` 可见页面，并使用 arXiv 官方 API 检索近期 `physics.plasm-ph`、`physics.acc-ph`、`physics.comp-ph`、`nucl-ex` 与 `physics.ins-det` 条目；按台账、重试队列和历史 daily 去重。本轮补入 1 条 JPP 正式开放论文 `10.1017/S0022377826101986` 和 3 条 arXiv 预印本 `10.48550/arXiv.2607.13672`、`10.48550/arXiv.2607.13585`、`10.48550/arXiv.2607.13507`，分别覆盖大振幅弱碰撞电子等离子体波 VPFP 动理学、双脉冲微喷嘴 sub-GeV 质子加速、激光驱动 D-D 中子源锂包层产氚源项保真度，以及 callback-centric PIC 框架。
- `2026-07-16` 复查 Cambridge `High Power Laser Science and Engineering` / `Journal of Plasma Physics` 可见页面，并使用 arXiv 官方 API 检索近期 `physics.plasm-ph`、`physics.acc-ph`、`physics.comp-ph`、`nucl-ex` 与 `physics.ins-det` 条目；按台账、重试队列和历史 daily 去重。本轮补入 3 条 arXiv 预印本 `10.48550/arXiv.2607.12984`、`10.48550/arXiv.2607.12451`、`10.48550/arXiv.2607.12439`，分别覆盖 LWFA 驱动单发高能缪子/粒子照相、PW 级激光残余角啁啾对质子加速的影响，以及高强度激光-电子碰撞中辐射反作用能量损失的单发测量方案。
- `2026-07-15` 复查 Cambridge `High Power Laser Science and Engineering` / `Journal of Plasma Physics` 可见页面，并使用 arXiv 官方 API 检索近期 `physics.plasm-ph`、`physics.acc-ph`、`physics.comp-ph`、`nucl-ex` 与 `physics.ins-det` 条目；按台账、重试队列和历史 daily 去重。本轮补入 3 条 arXiv 预印本 `10.48550/arXiv.2607.11045`、`10.48550/arXiv.2607.10497`、`10.48550/arXiv.2607.11309`，分别覆盖低相干激光增强热电子/硬 X 射线源、高效率等离子体加速器横向不稳定性与 3D PIC 设计窗口，以及 PHITS 粒子输运的 AI agent 辅助工作流。
- `2026-07-14` 复查 Cambridge `High Power Laser Science and Engineering` / `Journal of Plasma Physics` 可见页面，并使用 arXiv 官方 API 检索近期 `physics.plasm-ph`、`physics.acc-ph`、`physics.comp-ph`、`nucl-ex` 与 `physics.ins-det` 条目；按台账、重试队列和历史 daily 去重。本轮补入 3 条 arXiv 预印本 `10.48550/arXiv.2607.09229`、`10.48550/arXiv.2607.09453`、`10.48550/arXiv.2607.09088`，分别覆盖 PW 级激光纳结构靶质子加速、实验室产生天体相关间歇磁湍流，以及端到端可微 tokamak 全场景优化模拟器。
- `2026-07-13` 复查 Cambridge `High Power Laser Science and Engineering` / `Journal of Plasma Physics` 可见页面，并使用 arXiv 官方 API 检索近期 `physics.plasm-ph`、`physics.acc-ph`、`physics.comp-ph`、`nucl-ex` 与 `physics.ins-det` 条目；按台账、重试队列和历史 daily 去重。本轮补入 3 条 arXiv 预印本 `10.48550/arXiv.2607.05778`、`10.48550/arXiv.2607.06226`、`10.48550/arXiv.2607.05766`，分别覆盖弱磁化电子-离子激波中的 PIC 粒子加速效率、逆康普顿 X 射线源电子束参数遗传算法反演，以及 NIF 时间分辨高分辨 X 射线谱仪绝对标定。
- `2026-07-12` 复查 Cambridge `High Power Laser Science and Engineering` / `Journal of Plasma Physics` 可见页面，并使用 arXiv 官方 API 检索近期 `physics.plasm-ph`、`physics.acc-ph`、`physics.comp-ph`、`nucl-ex` 与 `physics.ins-det` 条目；按台账、重试队列和历史 daily 去重。本轮补入 2 条 HPL 正式开放 accepted manuscripts `10.1017/hpl.2026.10183`、`10.1017/hpl.2026.10180` 和 1 条 arXiv 预印本 `10.48550/arXiv.2607.08464`，分别覆盖结构化等离子体抑制后向 Raman 放大丝化、双皮秒激光大交角优化快电子产生，以及强磁化等离子体 photon acceleration 解释快速射电暴的机制。
- `2026-07-11` 先复查 Cambridge `High Power Laser Science and Engineering` / `Journal of Plasma Physics` 可见页面，未筛到比已入库条目更强且明确非重复的正式来源增量；随后使用 arXiv 官方 API 检索近期 `physics.plasm-ph`、`physics.acc-ph`、`physics.comp-ph`、`nucl-ex` 与 `physics.ins-det` 条目，并按台账、重试队列和历史 daily 去重。本轮补入 3 条 arXiv 预印本 `10.48550/arXiv.2607.08680`、`10.48550/arXiv.2607.08069`、`10.48550/arXiv.2607.07979`，分别覆盖 HEDP 平面靶中 RT 不稳定性产生磁场的质子照相精密映射、等离子体尾场加速器中的 multi-GeV electron comb，以及 regenerative cascading PWFA 产生 TeV 电子束的概念与 PIC 模拟。
- `2026-07-10` 复查近期 arXiv `physics.plasm-ph`、`physics.acc-ph`、`physics.comp-ph`、`nucl-ex` 与诊断相关分类；Cambridge HPL/JPP 页面可访问但未直接暴露清晰新 DOI，旧重试队列仍为来源侧限制，未重复空跑全量重试。本轮补入 3 条 arXiv 预印本 `10.48550/arXiv.2607.07356`、`10.48550/arXiv.2607.06946`、`10.48550/arXiv.2607.07005`，分别覆盖激光驱动 RT 不稳定性中的自生磁场自相似演化、激光驱动 coil current 外加磁场源的质子照相测量，以及 LWIR 激光等离子体相互作用产生高能 THz 辐射源。
- `2026-07-09` 复查近期 arXiv `physics.plasm-ph`、`physics.acc-ph`、`physics.comp-ph`、`nucl-ex` 与诊断相关分类；正式来源旧队列仍为来源侧限制，未重复空跑全量重试。本轮补入 3 条 arXiv 预印本 `10.48550/arXiv.2607.06458`、`10.48550/arXiv.2607.05746`、`10.48550/arXiv.2607.05738`，分别覆盖质子驱动等离子体尾场加速的 AWAKE benchmark、OMEGA 环形激光束产生兆高斯磁化等离子体射流，以及 NIF 热斑演化高分辨 X 射线谱诊断。
- `2026-07-08` 先复查 Cambridge HPL/JPP 正式来源和近期 arXiv `physics.plasm-ph` 最新列表；正式来源未筛到比已入库条目更强且明确非重复的增量，因此转向 2026-07-05 到 2026-07-06 的未入库高相关 arXiv 条目，补入 3 条 arXiv 预印本 `10.48550/arXiv.2607.04994`、`10.48550/arXiv.2607.04865`、`10.48550/arXiv.2607.04465`，分别覆盖磁化过密等离子体中的激光驱动准单能电子束、ADITYA-U 深度学习 MHD 平衡重建，以及 PIC/动理学模拟 hyper Boris 粒子推进器。
- `2026-07-07` 先复查 Cambridge `High Power Laser Science and Engineering` / `Journal of Plasma Physics` 正式来源与近期 arXiv `physics.plasm-ph` / `physics.acc-ph` / `physics.comp-ph` / `nucl-ex` 候选；多个 HPL 高相关条目已在历史 daily 或台账中入库，因此转向近期未入库预印本，补入 3 条 arXiv 条目 `10.48550/arXiv.2607.00875`、`10.48550/arXiv.2606.26484`、`10.48550/arXiv.2607.02323`，分别覆盖 XFEL 加热致密等离子体碰撞电离截面重分析、长束团 2.5 维辛空间电荷求解器，以及动态阻抗匹配的谐振微波等离子体源。
- `2026-07-06` 先复查 Cambridge `High Power Laser Science and Engineering` Volume 14 与近期 arXiv `physics.plasm-ph` / `physics.acc-ph` / `physics.comp-ph` / `nucl-ex` 候选；HPL 多个高相关条目已按 DOI 或标题在 2026-04 与 2026-06 历史 daily 中入库，因此跳过重复项，补入 1 条未入库 HPL 正式开放论文 `10.1017/hpl.2025.10099` 和 2 条高相关 arXiv 预印本 `10.48550/arXiv.2606.25213`、`10.48550/arXiv.2606.21418`，分别覆盖时空部分相干多模光源驱动的 ICF 激光驱动器方案、XGC 中面向 reduced MHD 型模式的环向谱场求解器，以及 GEMPICX 准中性电磁模型的结构保持几何离散。
- `2026-07-05` 先复查 Cambridge `Journal of Plasma Physics` 与 `High Power Laser Science and Engineering` 页面；HPL 中两个看似新 DOI 的高相关条目已按标题在 `2026-06-08` 入库，因此跳过，转向真正未入库的 JPP 正式条目，补入 3 条 JPP 正式论文 `10.1017/S0022377826101883`、`10.1017/S0022377826101779`、`10.1017/S0022377826101652`，分别覆盖碰撞无关 ITG 湍流 zonal-flow 饱和、tokamak X-point 几何下 gyrokinetic 场线跟随坐标构造，以及谱精度反向模式可微 bounce-averaging 算法与 stellarator 优化应用。
- `2026-07-04` 先复查 Cambridge `Journal of Plasma Physics` listing 与近期正式来源可见增量；JPP 当前高相关正式条目多已在前两日入库，因此转向 arXiv `physics.plasm-ph`、`physics.acc-ph` 与 `physics.comp-ph` 的近期高相关条目，补入 3 条未入库高相关预印本 `10.48550/arXiv.2607.02373`、`10.48550/arXiv.2607.01488`、`10.48550/arXiv.2606.30622`，分别覆盖尾场光子加速种子的多 GeV Compton 偏振伽马源、Aditya-U tokamak 受限 runaway electron 薄靶硬 X 射线韧致辐射诊断，以及 symplectic neural network 辅助的 δf PIC 非线性控制变量方法。
- `2026-07-03` 先复查 Cambridge `Journal of Plasma Physics` 最新 listing 与 `High Power Laser Science and Engineering` accepted/latest 页面；HPL 当前增量多偏激光器件，JPP 当前期仍有与开放磁约束、中性束和磁喷管等离子体流相关的未入库条目，因此补入 3 条 JPP 正式开放论文 `10.1017/S0022377826101895`、`10.1017/S0022377826101834`、`10.1017/S0022377826101718`，分别覆盖 GOL-NB 多镜磁阱中性束/快离子实验进展、travelling rotating magnetic field 多镜端塞方案，以及磁喷管中的等离子体流与平衡。
- `2026-07-02` 先复查 Cambridge `Journal of Plasma Physics` 当前期与 `High Power Laser Science and Engineering` accepted manuscripts，按 DOI 去重跳过此前已入库的 JPP 高相关条目；随后补入 2 条未入库 JPP 正式论文 `10.1017/S0022377826101901`、`10.1017/S0022377826101780` 和 1 条高相关 arXiv 预印本 `10.48550/arXiv.2606.30978`，分别覆盖 MIDAS-1D2V 聚变反应/中性束俘获扩展、Weibel 磁场种子到 dynamo 放大的无碰撞模拟，以及冷物质到 HEDP 等离子体的离子 stopping power 开源框架。
- `2026-07-01` 先复查 Cambridge `High Power Laser Science and Engineering` accepted manuscripts 与 `Journal of Plasma Physics` 当前页面，确认高相关正式来源增量有限；随后从近期未入库 arXiv `physics.plasm-ph`、`physics.acc-ph`、`physics.comp-ph` 与 `stat.ML` 交叉条目中补入 3 条高相关预印本 `10.48550/arXiv.2606.29214`、`10.48550/arXiv.2606.28534`、`10.48550/arXiv.2606.29620`，分别覆盖激光产生 surface QED plasma 中辐射反作用量子随机效应、multi-GPU PIC-Monte Carlo 大规模弹性模拟，以及面向 MHD 正/反问题的双向自回归 latent diffusion。
- `2026-06-30` 先复查 Cambridge `High Power Laser Science and Engineering` accepted manuscripts 与 `Journal of Plasma Physics` 当前页面，确认高相关正式来源增量要么已入库、要么偏激光器件；随后从近期未入库 arXiv 中补入 3 条高相关预印本 `10.48550/arXiv.2606.26198`、`10.48550/arXiv.2606.27064`、`10.48550/arXiv.2606.23966`，分别覆盖 ICF 等离子体单发 X 射线强度关联衍射成像、天然锡 photon activation 半衰期测量，以及 40 MeV 电子打钽转换靶产生韧致辐射后的天然镍光核反应截面测量。
- `2026-06-29` 先复查 Cambridge `Journal of Plasma Physics` / `High Power Laser Science and Engineering` 当前页面，补入 1 条未入库 HPL 正式/accepted manuscript `10.1017/hpl.2026.10172`，随后从近期未入库 arXiv 中补入 2 条高相关预印本 `10.48550/arXiv.2606.23602`、`10.1103/yw76-d6kh`，分别覆盖 shock ignition 外加磁场调控热电子输运、Omega/NIF 激光动态压缩 PXRD 强度分析方法，以及激光驱动 capacitor-coil 磁泡中的等离子体流与粒子加速。
- `2026-06-28` 先复查了 Cambridge `Journal of Plasma Physics` / `High Power Laser Science and Engineering` 当前页面，确认 HPL 当前高相关增量大多已在库，随后补入 1 条 JPP 正式来源论文 `10.1017/S0022377826101342`，并从近期未入库 arXiv 中补入 2 条与激光驱动中子/光核应用直接相关的高价值预印本 `10.48550/arXiv.2605.18968`、`10.48550/arXiv.2605.18969`，分别覆盖强场波在磁化等离子体中的传播边界、LWFA 光核源与激光 DD 中子源的快中子俘获系统级比较，以及超短脉冲 PW 激光驱动离子束与次级中子源实验基线。
- `2026-06-27` 先快速复查了 Cambridge `Journal of Plasma Physics` / `High Power Laser Science and Engineering` 当前页面，没有筛到比近几日更强且明确非重复的正式来源增量；随后转向 arXiv `physics.plasm-ph` / `physics.acc-ph` 最新列表，补入 3 条未入库高相关预印本：`10.48550/arXiv.2606.23953`、`10.48550/arXiv.2606.23974`、`10.48550/arXiv.2606.26514`，分别覆盖聚变系统中子外逸诱发大气 `14C` 的环境约束、LM26 磁化靶聚变压缩加热实验，以及复杂介质加载 wakefield 结构的可靠 wake function 提取方法。
- `2026-06-26` 先复查了 Cambridge `Journal of Plasma Physics` / `High Power Laser Science and Engineering` 当前页面，没有发现比近几日更强且明确非重复的正式来源增量；随后转向 arXiv `physics.plasm-ph` / `physics.acc-ph` 最新提交列表，补入 3 条未入库高相关预印本：`10.48550/arXiv.2606.26054`、`10.48550/arXiv.2606.25528`、`10.48550/arXiv.2606.25327`，分别覆盖宽带激光下两等离子体衰变驱动热电子增强、PIC 数值热化时间尺度审计，以及超临界介质中致密等离子体电子密度干涉诊断。
- `2026-06-25` 先复查了 Cambridge `Journal of Plasma Physics` / `High Power Laser Science and Engineering` 当前页面，没有筛到比近几日已入库条目更强且明确非重复的正式来源增量；随后转向 arXiv `physics.plasm-ph` / `physics.acc-ph` 近两日列表，补入 3 条未入库高相关预印本：`10.48550/arXiv.2606.23224`、`10.48550/arXiv.2606.24067`、`10.48550/arXiv.2606.23109`，分别覆盖双层靶 TNSA 质子束多目标贝叶斯优化、hollow-channel 正电子友好 quadrupole wakefield 稳定性，以及激光加速碳离子驱动的强耦合 stopping power 实验 benchmark。
- `2026-06-24` 先复查了 Cambridge `Journal of Plasma Physics` / `High Power Laser Science and Engineering` 当前页面与近期条目，确认本轮高相关正式来源候选要么已在 `processed_articles.json` 中、要么属于此前旧日阻塞记录，继续补录会重复处理；随后转向近几天 arXiv 新稿与近期修订稿，补入 3 条未入库高相关预印本：`10.48550/arXiv.2606.22427`、`10.48550/arXiv.2606.21221`、`10.48550/arXiv.2605.07929`，分别覆盖强场 QED 非线性康普顿谱解析、相对论束流-等离子体丝化不稳定性时空演化，以及 proton-driven PWFA 注入器应用。
- 已处理论文总数增至 220 条；`state/daily_retry_candidates.json` 维持 12 条。
- 当前重试队列只剩已明确的来源侧限制：10 条 ScienceDirect / Elsevier `HTTP 403`、1 条 Nature `cookies_not_supported`、1 条 IOP / New Journal of Physics Radware/Perfdrive 验证页。
- 2026-06-11 配置级诊断显示当前 Codex shell 已是 `danger-full-access` 且 network enabled；`127.0.0.1:1087` 代理路径可下载 arXiv PDF。此前 06-09 到 06-11 的 9 条 runtime-blocked 候选已通过 `retry_download_queue.py` 全部恢复。
- 当前有 65 条已补到 PDF 但尚未补中文结构化笔记的历史条目。
- 已新增自动索引脚本 `scripts/build_indexes.py`，可从 `state/processed_articles.json` 重建 `INDEX.md`、`papers/`、`categories/` 与 `daily/README.md`。
- `scripts/safe_pdf_download.py` 已支持 HTML 落地页自动提取官方 PDF、失败分类输出和 `curl` 传输回退；其中 `curl` 回退下的代理不可连 / DNS 失败也已单独归类。`scripts/retry_download_queue.py` 可批量重试并自动更新 processed/retry 台账。今天再次验证：arXiv PDF 可经环境代理路径下载；但对来源侧长期受限的 12 条旧队列，全量重试仍会在无效来源上耗时过长，后续更适合按来源分组或限额运行。

## 去重规则

默认以 DOI 为第一去重键；没有 DOI 时，使用规范化标题；仍无法稳定识别时，结合源链接与 PDF 文件名判断。已经记录在 `state/processed_articles.json` 或已出现在历史 `daily/` 目录中的论文，不应重复下载和重复分析。

## 评分规则

- 影响因子分：`1-10`
- 专业相似度分：`1-10`

影响因子分优先依据期刊影响力、领域声誉和发表平台层级；若是预印本，则明确标注为预印本并给出保守评分。专业相似度分衡量该论文与本仓库关注方向的直接相关程度。

## PDF 下载稳健性

为避免自动化因本地代理失效（常见于 `http_proxy/https_proxy/all_proxy` 指向 `127.0.0.1` 但代理未启动）导致下载失败，统一使用：

```bash
python scripts/safe_pdf_download.py --url <候选URL> --doi <DOI> --output <目标pdf路径>
```

该脚本会自动两阶段重试：
- 先按当前环境代理下载
- 若失败，自动绕过环境代理直连重试
- 若 DOI 存在且出版社链接不可得，会自动查询 Unpaywall 的合法开放获取链接再重试
- 若候选链接先返回 HTML 文章页（例如 Cambridge Core），会自动解析页面中的官方 PDF 链接并继续尝试
- 若 `urllib` 传输层失败，会自动回退到 `curl`

并会校验下载结果是否为真实 PDF（`Content-Type` 或 `%PDF-` 文件头）。

需要批量消化历史重试队列时，可使用：

```bash
python scripts/retry_download_queue.py --source-family cambridge
python scripts/retry_download_queue.py --source-family nature
python scripts/retry_download_queue.py --source-family elsevier
python scripts/retry_download_queue.py --source-family iop
```

重试脚本会自动在队列条目上写入 `retry_count`、`last_retry_at`、`source_family` 与 `last_failure_class`，并在成功时把 PDF 转入 `state/processed_articles.json`。

说明：仅使用合法来源（出版社站点、DOI 跳转、Unpaywall 收录的 OA 地址）；不使用侵权镜像站。

## 年度回填目录（历史）

- `yearly/YYYY/pdfs/`: 对应年份回填论文 PDF
- `yearly/YYYY/notes/`: 对应年份回填中文笔记
- `yearly/YYYY/index.md`: 对应年份索引
- `yearly/index.md`: 年度回填总索引

## 维护约定

- 默认直接在当前分支更新，不新建分支。
- 每日新增论文后，同步更新 `state/processed_articles.json`、当天 `daily/YYYY-MM-DD/index.md` 和中文笔记。
- 每次更新台账后运行：

```bash
python scripts/build_indexes.py
```

- 索引脚本会重建 `papers/`、`categories/`、`daily/README.md` 与 `INDEX.md`；这些文件构成 GitHub 论文索引。
- GitHub 仓库默认不跟踪 PDF 文件，避免仓库过大；PDF 本地路径仍保留在元数据与论文页中。
- 自动化成功完成后，默认提交并推送到 `origin/master`。
