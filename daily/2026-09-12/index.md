# 每日论文索引 - 2026-09-12

## 今日概览

- 运行日期：2026-09-12
- 新增论文数：3
- 正式来源优先：核对 APS PRL accepted/recent 与 2026-09-11 issue；新发现的高相关 PRL 正式论文均受订阅/`HTTP 403` 限制且没有合法开放作者稿，因此没有从摘要扩写笔记，转入结构化重试。
- 预印本增量：从官方 arXiv Atom API 的 2026-09-10 最新批次补入 LPA 漂移诊断、TREX 磁声波密度反演和带 AMR 的 `kobra` Vlasov–Poisson 代码。
- 主题分布：机器学习/状态空间方法与激光等离子体加速器运行、磁重联实验诊断、Vlasov 动理学与 plasma-wall 数值方法。
- 检索范围：检查 APS PRL accepted/recent 和 issue 137(11)，并扫描官方 arXiv `physics.plasm-ph`、`physics.acc-ph`、`physics.ins-det`、`physics.med-ph`、`nucl-ex` 的 120 条近期记录；另按 laser-plasma、PIC、strong-field QED、HEDP、beam application 和 exact title 定向核对。多源搜索聚合器本轮未返回可用记录，因此不宣称覆盖全部数据库。
- 去重：按 DOI/arXiv identifier、规范化标题、历史 `daily/`、341 条完成台账、14 条重试队列、摘要和物理场景逐项核对，三篇均为新记录。
- PDF / 正文：3 份官方 arXiv PDF 通过 `%PDF-`、`file`、`pdfinfo`、SHA-256 和非空 `pdftotext -layout`；三篇均用 `MINERU_API_KEY` 完成正文/图件转换，保留并逐张查看 14 张关键图。完整校验见 [pdf_validation.json](pdf_validation.json)。

## 论文清单

### 1. Physics-Informed Drift Diagnosis for Laser-Plasma Accelerator Operations

- DOI：[10.48550/arXiv.2609.11874](https://doi.org/10.48550/arXiv.2609.11874)
- arXiv v1：2026-09-10
- 来源：[arXiv 摘要页](https://arxiv.org/abs/2609.11874)
- 期刊 / 平台：arXiv 预印本
- 本地 PDF：`daily/2026-09-12/pdfs/Labun et al. - 2026 - Physics-informed drift diagnosis for laser-plasma accelerator operations.pdf`
- 中文笔记：[Labun et al. - 2026 - Physics-informed drift diagnosis for laser-plasma accelerator operations.md](notes/Labun%20et%20al.%20-%202026%20-%20Physics-informed%20drift%20diagnosis%20for%20laser-plasma%20accelerator%20operations.md)
- 来源影响力分：7/10
- 专业相似度分：10/10
- 推荐理由：把 $a_0$、密度和啁啾构成的 physical latent state、简化 blowout emission map、EKF innovation 与硬件候选模型竞赛接成可审计的 LPA 漂移诊断链。
- 一句话总结：作者同族 toy-model 合成会话中，$6\,{}^\circ\mathrm C/30$ 炮的主动 thermal dither 可产生 $+27.5$ nats 的候选优势和 33.4 MeV 预测漂移，而安静会话仍不可归因；没有输入真实 LPA 炮次，family 平局和 model mismatch 尚未解决。

### 2. Experimental Plasma Density Profiles Determined Through Measurements of the Magnetosonic Wave Speed

- DOI：[10.48550/arXiv.2609.11743](https://doi.org/10.48550/arXiv.2609.11743)
- arXiv v1：2026-09-10
- 来源：[arXiv 摘要页](https://arxiv.org/abs/2609.11743)
- 期刊 / 平台：arXiv 预印本；作者注明已投稿 *Physics of Plasmas*
- 本地 PDF：`daily/2026-09-12/pdfs/Kuchta et al. - 2026 - Magnetosonic-wave plasma density profiles.pdf`
- 中文笔记：[Kuchta et al. - 2026 - Magnetosonic-wave plasma density profiles.md](notes/Kuchta%20et%20al.%20-%202026%20-%20Magnetosonic-wave%20plasma%20density%20profiles.md)
- 来源影响力分：7/10
- 专业相似度分：9/10
- 推荐理由：把 TREX 重联驱动前的快磁声波从“启动瞬态”转化为 B-dot 阵列逐炮密度剖面诊断，并用 Langmuir probe 与线性 MHD 交叉核对。
- 一句话总结：BRB 实验中，作者由早期波前的径向到达时间反演低 $\beta$ 初始密度，中心高密度区与 Langmuir profile 大体一致；方法只验证于足够高密度、近轴对称、重联前的未扰动波前，不是重联层内动态密度诊断。

### 3. kobra: a new Vlasov code intended for plasma-wall modeling

- DOI：[10.48550/arXiv.2609.11563](https://doi.org/10.48550/arXiv.2609.11563)
- arXiv v1：2026-09-10
- 来源：[arXiv 摘要页](https://arxiv.org/abs/2609.11563)
- 期刊 / 平台：arXiv 预印本；作者元数据注明已被 *Contributions to Plasma Physics* 接收，尚无正式 DOI
- 本地 PDF：`daily/2026-09-12/pdfs/Konewko et al. - 2026 - kobra Vlasov code for plasma-wall modeling.pdf`
- 中文笔记：[Konewko et al. - 2026 - kobra Vlasov code for plasma-wall modeling.md](notes/Konewko%20et%20al.%20-%202026%20-%20kobra%20Vlasov%20code%20for%20plasma-wall%20modeling.md)
- 来源影响力分：7/10
- 专业相似度分：9/10
- 推荐理由：展示 phase-space AMR 如何在 finite-volume Vlasov–Poisson 中集中解析 Landau/two-stream/DGH 与 sheath 的局域速度结构，并量化作者算例的成本—精度权衡。
- 一句话总结：低维 benchmark 中 AMR 报告约 1.7–8 倍 speedup，DGH 内存由 11.4 GB 降至 2.7 GB；当前仍是 1d1v/1d2v、无碰撞静电原型，没有源码运行、实验墙面验证或 3d3v 生产性能证据。

## 未入库但需保留的候选

- [High-Energy-Density Plasma Nanorod by Collisionless Absorption of Ultrafast Laser Pulse Inside Dielectrics](https://doi.org/10.1103/k23j-c9y7) 是 2026-09-10 正式发表的 PRL 蓝宝石 Bessel 光束实验 + first-principles/PIC 论文。APS/DOI 路径本轮均返回 `HTTP 403`，OpenAlex 标记 closed 且未发现 repository full text；已加入重试队列。摘要中的 `<400 nm`、`MJ/cm³` 和厘米尺度不能替代全文误差与方法审查。
- [Generalized Lawson–Cordey–Mills Accessibility of Fusion Ignition](https://doi.org/10.1103/mmc9-nzfx) 是同日正式发表的 PRL 0D 点火可达性理论；APS 页面明确 accepted manuscript 要到 2027-09-10 才公开，本轮下载仍为 `HTTP 403`，已加入重试队列。不能从摘要把高 $\beta$ 要求或 damping 稳定反馈写成反应堆验证。
- [First experimental evidence of helicon current drive](https://journals.aps.org/prl/accepted/10.1103/mbn4-fd4v) 是 2026-09-08 接收的 DIII-D 实验；本轮 exact-title 搜索只找到会议摘要/幻灯片，没有对应论文作者稿，accepted/DOI 下载为 `HTTP 403`，已加入重试队列。
- `10.1103/p7k8-mjn7` 与 `10.1103/nc7w-yr34` 本轮按上次接续线索各重试一次，accepted/DOI 路径仍为 `HTTP 403` 且未发现开放作者稿；保留在队列，未重复扩写。
- `10.1103/sgyf-lrw1`、`10.1103/2rqf-hq77` 与 `10.1103/d45l-hsgg` 是既有 APS blocked 候选，本轮没有再次触发下载，旧失败记录不冒充今天的新复查。

## 当日综合总结

- Labun 的框架把 LPA 维护问题转成可辨识性设计：只有让不同硬件路径在观测空间产生足够独立的 signature，更多炮数才有意义。它目前是 synthetic consistency study，最需要的是 archival machine data、受控 step 和 model-mismatch 验证。
- Kuchta 提供一条可复用的诊断思想：利用装置固有波前携带局部密度信息，从 B-dot 到达时间恢复单炮剖面。其精度依赖低 $\beta$、已知背景场、组分/温度和清晰早期波前。
- Konewko 说明 Vlasov 的无采样噪声优势可与相空间 AMR 结合，但 speedup 与精度容差耦合；当前结果不应升级为真实 plasma-facing component 或高维 SOL 性能。
- 推荐阅读顺序：先读 Kuchta 看真实实验 observable 与模型假设怎样闭合，再读 Labun 看如何把运行漂移映射到隐状态；最后读 Konewko 比较 PIC sampling noise 与 Vlasov numerical diffusion 的不同误差预算。
