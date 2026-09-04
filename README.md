# everyday_paper

一个持续更新的高功率激光、等离子体物理与相关应用论文索引仓库。按天搜集、去重、下载并分析本仓库研究方向相关论文，并将已入库论文整理为分类索引。

## 目录

- [项目定位](#项目定位)
- [关注主题](#关注主题)
- [索引文件](#索引文件)
- [仓库结构](#仓库结构)
- [分类索引](#分类索引)
- [当前状态](#当前状态2026-09-05)
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

## 当前状态（2026-08-26）

- 已连续维护到 `daily/2026-08-26/`。本轮新增 3 条完成官方 PDF 校验的 arXiv 预印本：`10.48550/arXiv.2608.22211` 用二维 PIC 解析相对论 DLA 通道的波前引导电子注入，`10.48550/arXiv.2608.23466` 用 OMEGA 参数 FLASH 3D MHD 设计螺旋 HED 射流，`10.48550/arXiv.2608.23217` 比较 GS 平衡代理的 IID/OOD 误差并做 EXL-50U/Shape Editor 参考对照。三者分别限于二维无辐射反作用数值、尚未实施的合成诊断设计和数值/参考解验证；不能写成实测高品质 DLA 束流、已观测螺旋射流或真机闭环控制。

## 当前状态（2026-08-27）

- 已连续维护到 `daily/2026-08-27/`。本轮新增 4 条完成官方 PDF 校验的论文：Cambridge HPL accepted manuscript `10.1017/hpl.2026.10185` 研究短脉冲 LWFA 的两步反啁啾、束流品质与能量转换效率；arXiv `10.48550/arXiv.2608.23894` 量化不同宏粒子权重造成的 PIC 非物理温度平衡；arXiv `10.48550/arXiv.2608.22486` 推导 plasma bubble 中电子涡旋 LG/HG 定态；arXiv `10.48550/arXiv.2608.23976` 给出 inverse Grad–Shafranov neural surrogate 并在 TCV 上部分实验验证。
- 本轮将“激光加速电子/离子束—转换靶—光核/中子/同位素应用”继续作为检索重点，但没有把关联较间接的 γ 探测器或同位素方案硬凑入当日索引。LWFA 和涡旋电子结果主要是理论/PIC，IGSnn 的完整实时适应主要是仿真；这些均不能升级为端到端束线、核产额或电站级闭环实验事实。

## 当前状态（2026-08-28）

- 已连续维护到 `daily/2026-08-28/`。本轮新增 3 条官方 arXiv 预印本：`10.48550/arXiv.2608.25020` 实验实现高电荷固体靶 MeV 电子束的磁选与脉冲磁场准直，`10.48550/arXiv.2608.24387` 验证反向飞秒脉冲的空间—时间同步协议，`10.48550/arXiv.2608.25137` 以解析模型和 CAIN 模拟优化含 Breit–Wheeler 成对产生的 10 TeV γγ 对撞机光子亮度。
- 3 份 PDF 均完成官方来源、PDF 文件头/类型、页数/元数据和文本提取校验；台账增至 301 条，12 条来源限制重试项保持不变。第一篇是电子束选择/准直实验，第二篇是衰减光束的光学同步验证，第三篇是未来对撞机设计模拟；均不能跨越证据边界写成转换靶 γ/核产额、强场 QED 过程观测或已运行对撞机性能。

## 当前状态（2026-08-31）

- 已连续维护到 `daily/2026-08-31/`。本轮新增 4 条官方 arXiv 记录：`10.48550/arXiv.2602.12765` v2 实测 kHz LWFA 低发射度电子束并完成硅纳米膜电子衍射，`10.48550/arXiv.2608.26216` 完成 MAST-U 实时神经网络虚拟电路的 PCS 集成与 piggyback commissioning，`10.48550/arXiv.2608.26369` 给出 CERN HEARTS@LEIR 高能重离子电子辐照设施概念设计，`10.48550/arXiv.2608.26826` 用 U-Net/autoencoder 完成 XFEL 束流图像 ROI 分割与原型在线部署。
- 4 份官方 PDF 均通过 `%PDF-`、`file` 类型、`pdfinfo` 页数/元数据、SHA-256 下载记录和文本提取校验；台账增至 305 条，12 条来源限制重试项保持不变。本轮环境未配置 MinerU token，中文笔记使用 `pdftotext -layout` fallback 并已明确记录。
- 证据边界：Monzac 是低能 LWFA/UED 实验，但发射度仅测一个横向方向且衍射炮次约 500 keV、25 fC；Marshall 以软件集成、仿真和真实炮次 piggyback 为主；CERN 文档尚未经最终审查且仍是规划/成本估算；Chandratreya 的高 IoU 主要来自合成数据。它们均不能被写成转换靶 γ、光核/中子产额、屏蔽认证或已完成的激光束线端到端性能。

## 当前状态（2026-09-01）

- 已连续维护到 `daily/2026-09-01/`。本轮新增 3 条官方 arXiv 记录：`10.48550/arXiv.2608.26313` 用 flying-focus 延长高能光子在高场区的相互作用，并以 Ptarmigan/LCFA 比较 nonlinear Breit–Wheeler 对产额；`10.48550/arXiv.2608.28468` 把实时 neural virtual circuits 从 PCS/piggyback 验证推进到 MAST-U 主动控制炮次；`10.48550/arXiv.2608.27845` 在改写的二维 MHW 系统中用 SAC/TD3 优化湍流—zonal-flow 双向转换。
- 3 份官方 PDF 均通过 `%PDF-`、`file`、`pdfinfo`、SHA-256 和非空文本提取，并成功完成 MinerU Markdown 转换；台账从 305 增至 308 条，12 条来源限制重试项保持不变。笔记中的关键图来自本次 MinerU 输出并保存在当日资源目录。
- 证据边界：Rahman 是理想单能光子束上的解析标度和 Monte Carlo 模拟，不是对产生观测；Amorisco 是真实 MAST-U 主动控制实验，但未做传统 VC 优越性对照且部分炮次暴露 nose interaction/伪逆病态；Sun 只在二维周期 MHW 和规定 actuator 中验证，策略接近开环，不能写成实机湍流控制。

## 当前状态（2026-09-02）

- 已连续维护到 `daily/2026-09-02/`。本轮新增 3 条官方 arXiv 记录：`10.48550/arXiv.2608.29653` 用 STOV 双箔构型和 3D spin-resolved QED-PIC 设计偏振孤立阿秒 γ 束；`10.48550/arXiv.2608.30455` 用轴向强磁场重排 electron-driven blowout 回流电子以扩展正电子聚焦/加速区；`10.48550/arXiv.2608.28769` 实验研究 Sn LBO 预等离子体对 `13.5 nm` EUV 发射和自吸收的影响。
- 3 份官方 PDF 均通过 `%PDF-`、`file`、`pdfinfo`、SHA-256 和非空 `pdftotext -layout`；台账从 308 增至 311 条，12 条来源限制重试项保持不变。本轮未配置 MinerU CLI/token，中文笔记使用本地文本提取 fallback。
- 证据边界：Xie 的 `500 as`、`64.4%` 偏振和 `1.1×10^9` 光子均来自 QED-PIC，不是 γ/光核实测；Liu 的 `92%` 捕获和 `100–150 MeV/6 cm` 来自理想 driver/witness 模拟，且能增益对分辨率敏感、发射度仍远离对撞机指标；Polek 是实验，但 `35%` 是未绝对标定、每点两次测量的相对 in-band 信号增强，不是绝对 CE 或工业光源认证。

## 当前状态（2026-09-03）

- 已连续维护到 `daily/2026-09-03/`。本轮新增 2 条正式期刊记录与 1 条官方 arXiv 预印本：`10.1038/s41566-026-01958-4` 用涂层等离子体镜自发聚焦增强全光学 ICS；`10.1038/s41598-026-56639-7` 实验实现稳定、可调谐的双激光 LWFA–ITS MeV γ 源；`10.48550/arXiv.2609.01494` 用自旋/偏振分辨 Monte Carlo 预测强激光—电子束相互作用的可计数量子信号。
- 3 份全文均通过 `%PDF-`、`file`、`pdfinfo`、SHA-256、非空 `pdftotext -layout` 和 MinerU Markdown 转换；台账从 311 增至 314 条，12 条来源限制重试项保持不变。Nature Photonics 期刊 PDF 受 cookie/订阅路径限制，本地全文明确保存为对应的 Research Square v1 作者预印本。
- 证据边界：Hu、Tsai 的 γ 源结果是实验，但前者的自发聚焦机制和两者的部分能谱/场强依赖 PIC、Geant4 或响应反演；Moritaka 的 ELI-NP 计数、偏振和自旋差异完全是模拟预测。三篇都没有给出 NRF、光裂变、中子/活化、剂量或屏蔽实测。

## 当前状态（2026-09-04）

- 已连续维护到 `daily/2026-09-04/`。本轮新增 Nature Photonics 正式开放论文 `10.1038/s41566-026-01977-1` 和官方 arXiv `10.48550/arXiv.2609.02326`、`10.48550/arXiv.2609.01705`，分别覆盖超宽带 laser–plasma Raman 放大实验、非均匀等离子体 cFRA 理论/PIC 与物理方差锚定的 diffusion transport surrogate。
- 3 份全文均通过 `%PDF-`、`file`、`pdfinfo`、SHA-256 和非空 `pdftotext -layout`，并完成 MinerU Markdown 转换；台账从 314 增至 317 条，12 条来源限制重试项保持不变。当日笔记存入 9 张关键图，便于复核实验布局、增长窗和生成模型验证。
- 证据边界：Shaw 直接测得 `64 fs`、约 `0.31 TW` 和最高 `8.7%` 时间重叠修正效率，但超过 `1.8 TW` 是无 SPIDER 炮次的条件估算；Lei 的近单周期、约 `10⁷` 增益和约 `4 PW` 来自理论/PIC；Reichherzer 用 MHD/test-particle 模拟与历史 proton-radiography 数据验证 surrogate，未运行新的等离子体实验。三篇都不能写成强场 QED、光核/中子产额或剂量实测。

## 当前状态（2026-09-05）

- 已连续维护到 `daily/2026-09-05/`。本轮新增官方 arXiv `10.48550/arXiv.2609.03550`、`10.48550/arXiv.2609.03354`、`10.48550/arXiv.2609.03314`，以及 2026-09-04 被 Physical Review E 接收的 `10.1103/hdkp-2mpm`；分别覆盖 EPOCH quasi-cylindrical QDS、GTC hybrid spectral PIF、standing-wave cavity QED proposal 和 density-gradient SRS/SBS 守恒律。
- 4 份全文均通过 `%PDF-`、`file`、`pdfinfo`、SHA-256、非空 `pdftotext -layout` 和 MinerU Markdown 转换；台账从 317 增至 321 条，12 条来源限制重试项保持不变。PRE 论文的本地全文明确保存为对应 arXiv v2 author preprint，不是 APS 排版版。
- 证据边界：An 和 Bao 的精度/性能均为作者 benchmark，本轮未做源码审计、编译或复现；Mehdi 的一天量级 QED sensitivity 是依赖最小 mode volume 与 shot-noise-limited readout 的理论估算；Patel 是 Noether 推导和代码校验框架，不是新实验。另一篇 cone-guided proton PRE accepted paper 因 PDF 403 且无开放预印本未入库。

## 当前状态（2026-08-25）

- 已连续维护到 `daily/2026-08-25/`。本轮新增 3 条完成官方 PDF 校验的 arXiv 预印本：`10.48550/arXiv.2608.17839` 在激光 HEDP 实验中用第三束相对论脉冲按时序切换重联，`10.48550/arXiv.2608.20645` 实验验证臭氧全气体 UV 束流终端/能量计，`10.48550/arXiv.2608.21080` 用条件流与辅助追踪粒子代理 PS 粒子分布。它们分别限于指定靶与时序、UV ns/mJ 标定和 PS/Xsuite 基准；不能写成聚变堆控制、PW 级通用防护或 PIC/LWFA 端到端性能。

## 当前状态（2026-08-24）

- 已连续维护到 `daily/2026-08-24/`。本轮新增 3 条完成官方 PDF 校验的 arXiv 预印本：`10.48550/arXiv.2608.20027` 用 PIC 扫描三角双光栅 DLA 的齿角、反射设计和同步窗口，`10.48550/arXiv.2608.18325` 用神经网络预测 W7-X 弹丸高约束态的 remaining time，`10.48550/arXiv.2608.18373` 以两导线磁零点连接粒子迁移与低温等离子体 PIC 输运。三者分别是微结构数值设计、历史放电预测和无导引场理论—PIC 基准；不能写成可部署的加速器梯度、已完成的闭环燃料控制或真实磁重联/聚变装置性能。

## 当前状态（2026-08-22）

- 已连续维护到 `daily/2026-08-22/`。本轮新增 3 条完成官方 PDF 校验的 arXiv 预印本：`10.48550/arXiv.2608.20299` 在 OMEGA capacitor-coil 重联实验中解析低混杂漂移不稳定性，`10.48550/arXiv.2608.19591` 量化激光烧蚀等离子体的 Biermann-battery 重联速率与能量分配，`10.48550/arXiv.2608.19382` 用暖稠密 Cu 的 K-edge 吸收谱约束 CR/DFT 原子模型。前两者是特定构型的实验诊断，后者是带模型相关性的光谱约束；不能写成粒子束/核应用验证、聚变点火结果或已解决的 WDM 理论。

## 当前状态（2026-08-21）

- 已连续维护到 `daily/2026-08-21/`。本轮新增 3 条完成官方 PDF 校验的 arXiv 预印本：`10.48550/arXiv.2608.17555` 实测密度定制 LWFA 的双脉冲 betatron X 射线，`10.48550/arXiv.2608.15272` 完成 ELIMAIA--ELIMED 激光质子束线的剂量学 commissioning，`10.48550/arXiv.2608.18718` 解析比较韧致辐射 γ 驱动 BW 与相对论离子 BH 对产生。三者分别是 X 射线源实验、低通量束线标定和理论比较；不能写成已实测双脉冲时延、临床疗效或强场对产生观测。

## 当前状态（2026-08-20）

- 已连续维护到 `daily/2026-08-20/`。本轮新增 3 条完成官方 PDF 校验的 arXiv 预印本：`10.48550/arXiv.2608.17554` 给出集装箱化 LWFA—钨转换靶 X 射线的七个月工业 μCT 现场运行；`10.48550/arXiv.2608.17119` 以 PIC+MC+贝叶斯优化预测 `99Mo` 光核生产；`10.48550/arXiv.2608.17772` 实测黑腔预热泡沫 DLA 的高电荷电子束。三者分别是 NDT 实证、数值预测和上游束流实验，不能互相替代为已测光核/临床产额或普适束流品质。

## 当前状态（2026-08-19）

- 已连续维护到 `daily/2026-08-19/`。本轮新增 1 条完成官方 PDF 校验的 arXiv 预印本 `10.48550/arXiv.2608.16459`：LMJ-PETAL 的实验以 SMLWFA/DLA 混合机制产生 `1.1 ± 0.13 μC`、最高约 `500 MeV` 的宽谱电子束，并经 In/Fe/Zr 转换靶得到约 `3.3 J` 的多 MeV 硬 X 射线。实证范围是电子束和韧致辐射源；光核、同位素、中子、剂量和屏蔽是后续方向，尚非本文产额或应用性能验证。

## 当前状态（2026-08-18）

- 已连续维护到 `daily/2026-08-18/`。本轮新增 1 条完成官方 PDF 校验的 arXiv 预印本 `10.48550/arXiv.2608.14521`：以波导模型和 WarpX 准柱对称 PIC 扫描两级多 PW 激光—近临界密度氢靶，发现 snowplow 后加速只在窄初始相空间高效；`500 J`、`4 nc` 受控测试粒子最优条件下可得到近 `2.2 GeV` 增益至约 `2.5 GeV`。这是预加速级未建模、零初始横向动量的解析/PIC 概念扫描，不是实测束流、端到端两级加速器或医疗/核应用性能验证。

## 当前状态（2026-08-17）

- 已连续维护到 `daily/2026-08-17/`。本轮新增 1 条完成官方 PDF 校验的 arXiv 预印本 `10.48550/arXiv.2608.13198`：以反射率泵浦—探测、相位敏感干涉和传输矩阵模型联合追踪块材钢、铝、金的超快激光烧蚀飞溅层；报告约 `1125/907/330 m/s` 的层速度，并显示铝约 `500 ps`、钢约 `1–2 ns` 解体，而金在 `3.5 ns` 后仍保持不透明。结果是 `1 ps`、空气中金属烧蚀的实验诊断，不是相对论激光、LWFA/TNSA 或转换靶性能验证。

## 当前状态（2026-08-16）

- 已连续维护到 `daily/2026-08-16/`。本轮新增 1 条完成官方 PDF 校验的 arXiv 预印本 `10.48550/arXiv.2608.11628`：以 PINN 同时反演电子束能谱与滤片透射核误差，直接使用 14 点稀疏衰减曲线重建 `10–500 keV` 亚纳秒放电二极管电子谱，并报告约 `130 keV` 特征峰。其算法可借鉴到激光等离子体束流和次级辐射诊断，但未在 LWFA、转换靶或激光靶端实验验证，不能外推为通用绝对能谱诊断。

## 当前状态（2026-08-15）

- 已连续维护到 `daily/2026-08-15/`。本轮新增 1 条完成官方 PDF 校验的 arXiv 预印本 `10.48550/arXiv.2608.12551`：提出反向激光扫描电离前沿，使其持续遇到未发生 hose 的高流强 REB；3D PIC 给出约 `250 MV/m`、亚米级约 `150 MeV/250 nC` 准单能束或约 `75 MeV/>5 μC` 高电荷束的权衡。本文是解析/PIC 概念验证，未覆盖端到端激光电离、电子束生成、束流输运或医疗/聚变靶性能，不能视为应用实证。

- 已连续维护到 `daily/2026-08-14/`。本轮新增 1 条完成官方 PDF 校验的 arXiv 预印本 `10.48550/arXiv.2608.11664`：在 OMEGA EP 的 He 气填充替代黑腔平台，用阴影法、干涉和 TNSA 质子照相测得 Cu 等离子体膨胀与 `10–100 μm` 丝状结构；Gorgon/HYDRA 可再现大尺度形貌但在 `1–3 ns` 系统高估膨胀，显示自生磁场、磁化/非局域热输运与动理学物理仍需审计。本文是单泡替代实验，质子照相的定量场反演仍在进行，不能直接外推为完整黑腔驱动或内爆性能。

- 已连续维护到 `daily/2026-08-13/`。本轮新增 2 条完成官方 PDF 校验的 arXiv 预印本 `10.48550/arXiv.2608.10988` 与 `10.48550/arXiv.2608.11058`：前者以三维全电磁 PIC 审计未来电子—正电子对撞中 `ε≳1` 的纵向减速/束束光度边界，后者用 GP 与层级 NN 加速 ITER 稳态快粒子输运评估并量化不确定度。前者不是激光平台或完整 SF-QED 产额计算，后者仅覆盖 FAR3d 的饱和训练域，均不应跨场景外推。

- 已连续维护到 `daily/2026-08-12/`。本轮新增 2 条完成官方 PDF 校验的 arXiv 预印本 `10.48550/arXiv.2608.08903` 与 `10.48550/arXiv.2608.08586`：前者以 BO/PIC 给出自引导 LWFA 的能量最优化标度及对应最短加速长度，后者以 THz-TDC 和色散磁铁实测 DBA 压缩 LWFA 电子束的非线性纵向相空间。前者局限于自引导扫描域和最大能量单目标，后者局限于约 4.55 MeV、fC 级束线，均不应直接外推为所有束流品质或应用束线的预测。

- 已连续维护到 `daily/2026-08-11/`。本轮新增 2 条可访问官方开放接受稿 `10.1088/1741-4326/ae96c0` 与 `10.1088/1741-4326/ae96c1`：前者以 C-2W 实验对照验证含中性束、供料和偏压源项的 WarpX hybrid-PIC 宏观模态/停源衰变；后者用二维燃烧模拟指出多冲击 DT 快点火靶必须在点火区周围保留连续高密度燃料，不能仅以总面密度或局域高密度核心衡量燃耗。二者分别受限于代表性炮次的定性验证和规定加热/二维模型，均不可外推为任意工况的端到端预测。

- 已连续维护到 `daily/2026-08-10/`。本轮新增 3 条完成官方 PDF 校验的 arXiv 预印本 `10.48550/arXiv.2608.05669`、`10.48550/arXiv.2608.05667` 与 `10.48550/arXiv.2608.05555`，分别覆盖以宏观状态量在线重建偏滤器热流的机器学习框架、兼容三维磁构型的宽频 RF 射线追踪、以及双零位自由边界 GS 平衡的 FNO 代理；三者分别受限于单数据集、几何光学近似和单几何/拓扑训练域，尚不应作跨装置或端到端控制结论。

- 已连续维护到 `daily/2026-08-09/`。本轮新增 3 条完成官方 PDF 校验的 arXiv 预印本 `10.48550/arXiv.2608.05937`、`10.48550/arXiv.2608.05698` 与 `10.48550/arXiv.2608.05094`，分别覆盖 EFISH 等离子体电场反演的偏振条件物理约束 DeepONet、有限激光脉冲中相对论电子净自旋旋转的异常磁矩 holonomy、以及 WarpX--Geant4 正电子转换靶端到端建模；前两篇分别属于受限的机器学习诊断验证和理想平面波理论，第三篇仍受不完整加速腔场图限制。

- 已连续维护到 `daily/2026-08-07/`。本轮新增 3 条完成官方 PDF 校验的 arXiv 预印本 `10.48550/arXiv.2608.04932`、`10.48550/arXiv.2608.04699` 与 `10.48550/arXiv.2608.04363`，分别覆盖激发卤化氢等离子体光阴极的高偏振电子束、LPA 束啁啾注入储存环获得飞秒高亮度辐射、以及锥靶产生偏振阿秒 MeV γ 源；三者均为模拟/设计研究，尚未构成端到端实验验证。

- 已连续维护到 `daily/2026-08-06/`。本轮新增 3 条完成官方 PDF 校验的 arXiv 预印本 `10.48550/arXiv.2608.03969`、`10.48550/arXiv.2608.03331` 与 `10.48550/arXiv.2608.03240`，分别覆盖 PW 激光离子束汤姆孙抛物线谱仪实证、强场 QED 级联末态诊断，以及涡旋激光自生磁箍缩的高密度相对论电子束实验；后两项中，QED 的参数反演仍为模型提案，SMP 高功率/nC 外推仍待实验验证。

- 已连续维护到 `daily/2026-08-06/`。本轮新增 3 条完成官方 PDF 校验的 arXiv 预印本 `10.48550/arXiv.2608.03969`、`10.48550/arXiv.2608.03331` 与 `10.48550/arXiv.2608.03240`，分别覆盖 PW 激光离子束汤姆孙抛物线谱仪实证、强场 QED 级联末态诊断，以及涡旋激光自生磁箍缩的高密度相对论电子束实验；后两项中，QED 的参数反演仍为模型提案，SMP 高功率/nC 外推仍待实验验证。

- 已连续维护到 `daily/2026-08-05/`。本轮新增 1 条完成官方 PDF 校验的 arXiv 预印本 `10.48550/arXiv.2608.01323`，覆盖任意电子横向波包在强场非线性 Compton 散射中对涡旋 γ 光子轨道角动量谱的直接调控；结果限于理想化单电子、圆偏振平面波和长脉冲模型，尚未给出真实束流容差或绝对产额。

- 已连续维护到 `daily/2026-08-04/`。本轮新增 1 条完成官方 PDF 校验的 arXiv 预印本 `10.48550/arXiv.2607.29364`，覆盖在可微流体求解器中在线训练的带记忆 Fourier Neural Operator 闭合，用于线性到非线性 Landau 阻尼的动理学近似与稳定部署。

- 已连续维护到 `daily/2026-08-03/`。本轮新增 1 条完成官方 PDF 校验的 arXiv 预印本 `10.48550/arXiv.2607.26965`，覆盖纳秒激光烧蚀等离子体的光谱--冲击波--表面波多模态诊断，以及物理约束机器学习的材料性能反演。

- 已连续维护到 `daily/2026-08-02/`。本轮新增 2 条完成官方 PDF 校验的 arXiv 预印本 `10.48550/arXiv.2607.26252`、`10.48550/arXiv.2607.26408`，分别覆盖双激光横向准静态场辅助相对论电子加速，以及相对相位控制的多光子真空电子--正电子对产生。

- 已连续维护到 `daily/2026-08-01/`。本轮新增 3 条完成官方 PDF 校验的 arXiv 预印本 `10.48550/arXiv.2607.28305`、`10.48550/arXiv.2607.28208`、`10.48550/arXiv.2607.27234`，分别覆盖保结构的全动理离子--回旋动理电子混合模型、弱电离等离子体离心机的同位素/质量分离标度，以及低温等离子体化学的开源 0D 全局模型框架。

- 已连续维护到 `daily/2026-07-31/`。本轮新增 2 条完成官方 PDF 校验的 arXiv 预印本 `10.48550/arXiv.2607.25856`、`10.48550/arXiv.2607.26045`，分别覆盖 LWFA 宽谱 X 射线闪烁体诊断标定，以及面向转换靶/光中子链条的 OpenMC 光核输运验证；后者明确限于非官方开发分支和单次碰撞数值基准。

- 已连续维护到 `daily/2026-07-30/`。本轮新增 3 条完成官方 PDF 校验的 arXiv 预印本 `10.48550/arXiv.2607.25843`、`10.48550/arXiv.2607.25481`、`10.48550/arXiv.2607.25313`，分别覆盖带严格能量分账的 PIC--MCC 等离子体激光接收器、HEDP XRTS 的 Bethe `f`-sum 规则一致性，以及自旋极化 D--T 燃料的 α channeling 与氦灰输运。

- 已连续维护到 `daily/2026-07-29/`。本轮新增 3 条完成官方 PDF 校验的 arXiv 预印本 `10.48550/arXiv.2607.24602`、`10.48550/arXiv.2607.24234`、`10.48550/arXiv.2607.24505`，分别覆盖 JOREK 三维 MHD--full-f PIC 的逃逸电子雪崩、相对论束流不稳定性的准静态 PIC 验证，以及 HEDP/ICF 非局域离子输运的离子--电子碰撞修正。

- 已连续维护到 `daily/2026-07-28/`。本轮新增 1 条正式开放论文 `10.15407/jnpae2026.02.148` 与 1 条完成官方 PDF 校验的 arXiv 预印本 `10.48550/arXiv.2607.22344`，分别覆盖 SiPM 闪烁体伽马谱/紧凑辐射监测的性能基线，以及 EAST 鱼骨模驱动细尺度反向带状流的实验与 GTC 解释。

- 已连续维护到 `daily/2026-07-27/`。本轮新增 3 条完成官方 PDF 校验的 arXiv 预印本 `10.48550/arXiv.2607.22473`、`10.48550/arXiv.2607.21830`、`10.48550/arXiv.2607.21723`，分别覆盖非轴对称 blowout 尾场、LPA 驱动 GeV μ 子主动成像和燃烧聚变等离子体反应--Boltzmann 动理学。
- `2026-07-26` 新增 `10.48550/arXiv.2607.21362`、`10.48550/arXiv.2607.21238`，覆盖 ST40 偏滤器热流诊断和 HEDP L 壳层不透明度增强。
- `2026-07-25` 新增 3 条完成官方 PDF 校验的 arXiv 预印本 `10.48550/arXiv.2607.21407`、`10.48550/arXiv.2607.20966`、`10.48550/arXiv.2607.20861`，分别覆盖 tokamak 边界等离子体循环一致性不确定性代理、HEDP 激光散斑统计和 GPU 可微新经典输运求解。
- `2026-07-24` 新增 3 条已完成官方 PDF 校验的 arXiv 预印本 `10.48550/arXiv.2607.20281`、`10.48550/arXiv.2607.19121`、`10.48550/arXiv.2607.17059`，分别覆盖宽带下混合波参量衰变、真实非对称啁啾激光的 PIC/LWFA 建模工具，以及相对论电子束 DRZ 荧光屏绝对电荷标定。
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
- 已处理论文总数增至 233 条；`state/daily_retry_candidates.json` 维持 12 条。
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
