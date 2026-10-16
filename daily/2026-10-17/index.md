# 每日论文索引 - 2026-10-17

## 今日概览

- 新增 **6 篇作品**，台账 **459 → 465**：2 篇 10 月 16 日正式 VOR，2 篇同日正式出版元数据对应的较早作者稿，以及 2 篇近期高相关 arXiv 预印本。正式记录与作者稿只入库一次。
- 覆盖强场 QED 火球、温稠密物质输运、结构靶 SAXS 诊断、GPU 等离子体可视化、中子共振多次散射和 PIC 重联注入。没有为覆盖所有主题而补入弱相关机器学习论文。
- 搜索层 3 个定向查询返回 0；Crossref 10 组主题查询取得 750 行、615 个唯一 DOI，时间窗 2026-10-15 至 17，按发表日降序、每主题上限 75 行。官方 arXiv 五类最近 300 条最新投稿为 10 月 15 日。另查具体出版商、arXiv 作者/标题关系与精确标题；有界查询不代表全球穷尽检索。
- 去重同时检查 DOI、arXiv ID/版本、规范化/近似标题、作者和物理场景，并对照既有 459 条完成台账、39 条重试项与历史日更。空 DOI 按缺失处理，不作为重复标识。
- 全文 **6 份、69 页、50,354,929 字节**；文件头、类型、SHA-256、pdfinfo、全页 pypdf 和 400,936 字节布局文本通过。MinerU 显式 pipeline 对六篇全部成功；检查 12 个首页/关键页，保留 7 幅原图/原表摘录。
- APS 的相位锁定 LWFA 密度论文因 harvest 404、期刊 PDF 403/404 进入重试，队列 **39 → 40**；未取得全文则不写笔记。两篇已找到匹配作者稿的 APS 作品分别标注正式 PDF 仍缺失，未把作者稿冒充 VOR。

## 论文清单

### 1. Beamstop-free small-angle X-ray scattering for multiscale structure measurement of high-energy-density plasma

- 标识符：[10.1038/s42005-026-02872-5](https://doi.org/10.1038/s42005-026-02872-5)
- 日期与来源：2026-10-16，*Communications Physics*；2026-10-16 正式 VOR。
- 中文笔记：[Ota et al. - 2026 - Beamstop free HED plasma SAXS](notes/Ota%20et%20al.%20-%202026%20-%20Beamstop%20free%20HED%20plasma%20SAXS.md)
- 来源影响力分：9/10；专业相似度分：10/10（主观阅读优先级，不是期刊影响因子）。
- 推荐理由：用直接实验约束结构靶预等离子体和纳米—皮秒稀疏化。
- 一句话总结：单曝光覆盖多个空间尺度；时间扫描来自多炮，吸收效率转折来自二维 PIC。

### 2. Generation of a polarized pair-photon fireball via a laser-driven nonlinear-linear QED cascade

- 标识符：[10.1103/xvmh-mcg7](https://doi.org/10.1103/xvmh-mcg7)
- 日期与来源：2026-10-16，*Physical Review E*；正式出版登记；实际阅读 2026-07-03 arXiv v2 作者稿。
- 中文笔记：[Dou et al. - 2026 - Polarized pair photon fireball](notes/Dou%20et%20al.%20-%202026%20-%20Polarized%20pair%20photon%20fireball.md)
- 来源影响力分：9/10；专业相似度分：10/10（主观阅读优先级，不是期刊影响因子）。
- 推荐理由：含线性/非线性 QED 过程开关、轨道加热和光子能量预算。
- 一句话总结：约 30% 激光到光子能量是模拟；过密指光子浴，对等离子体的集体性仍有限。

### 3. Plasma conductivity from warm dense matter to the Spitzer limit using mean-force kinetic theory

- 标识符：[10.1103/177n-4yfm](https://doi.org/10.1103/177n-4yfm)
- 日期与来源：2026-10-16，*Physical Review Letters*；正式出版登记；实际阅读 2026-06-01 arXiv v1 作者稿。
- 中文笔记：[Babati et al. - 2026 - Mean force plasma conductivity](notes/Babati%20et%20al.%20-%202026%20-%20Mean%20force%20plasma%20conductivity.md)
- 来源影响力分：9/10；专业相似度分：9/10（主观阅读优先级，不是期刊影响因子）。
- 推荐理由：提供 HED/ICF 输运闭合，强调简并与 Spitzer 渐近极限。
- 一句话总结：电子—电子碰撞改变弱简并输运；每状态点数分钟，适合制表而非流体逐步内联。

### 4. Fast Monte Carlo calculation of multiple scattering in resonant neutron capture

- 标识符：[10.48550/arXiv.2610.20435](https://doi.org/10.48550/arXiv.2610.20435)
- 日期与来源：2026-10-14，*arXiv preprint*；2026-10-14 官方 arXiv v1。
- 中文笔记：[Djilkibaev - 2026 - Fast neutron multiple scattering Monte Carlo](notes/Djilkibaev%20-%202026%20-%20Fast%20neutron%20multiple%20scattering%20Monte%20Carlo.md)
- 来源影响力分：7/10；专业相似度分：9/10（主观阅读优先级，不是期刊影响因子）。
- 推荐理由：为中子样品多次散射校正、噪声与共振反演提供可核验模型基准。
- 一句话总结：约 9.4 倍耗时差包括并行收益；金靶 eV 模型尚非激光 MeV 中子实测。

### 5. Are $E>B$ regions essential for particle injection in relativistic magnetic reconnection?

- 标识符：[10.48550/arXiv.2610.22118](https://doi.org/10.48550/arXiv.2610.22118)
- 日期与来源：2026-10-15，*arXiv preprint*；2026-10-15 官方 arXiv v1。
- 中文笔记：[French et al. - 2026 - Reconnection particle injection channels](notes/French%20et%20al.%20-%202026%20-%20Reconnection%20particle%20injection%20channels.md)
- 来源影响力分：8/10；专业相似度分：9/10（主观阅读优先级，不是期刊影响因子）。
- 推荐理由：用清晰的注入总体和净功预算辨别相关性与机制，适合 PIC 分析。
- 一句话总结：表 2 的磁主导通道人数占比为 93%→63%；不是总能量占比，结论限二维无辐射对等离子体。

### 6. Visual tools for 3D plasma simulation: GPU-based isosurface extraction and particle-based rendering

- 标识符：[10.1371/journal.pone.0359294](https://doi.org/10.1371/journal.pone.0359294)
- 日期与来源：2026-10-16，*PLOS One*；2026-10-16 正式 VOR。
- 中文笔记：[Kim et al. - 2026 - GPU plasma visualization](notes/Kim%20et%20al.%20-%202026%20-%20GPU%20plasma%20visualization.md)
- 来源影响力分：7/10；专业相似度分：8/10（主观阅读优先级，不是期刊影响因子）。
- 推荐理由：GPU 缓冲管理和可视化性能口径可用于三维场/轨迹浏览。
- 一句话总结：512³、42.81M 顶点提取 44.7 ms；显示帧率不等于 PIC 求解速度。

## 当日综合总结

优先读 SAXS 诊断、中子校正和 QED 机制：三者分别约束初始靶状态、诊断反演与辐射能量通道。输运模型和重联分析则提供极限检验与统计总体设计，可直接用于审查数值结果。

- **直接实验：** SAXS 原始散射与多炮次结构演化有实测支持；温度/电离态含模型推断，吸收效率扫描为二维 PIC。
- **模拟与基准：** QED 火球、输运理论、中子模型反演和重联注入均不能写成新实验。中子算法性能包括并行收益；注入人数份额不等于能量总占比。
- **计算与显示：** GPU 等值面提取、生成后的渲染、引擎 staging 和物理求解是不同成本；当前 VR 仅演示技术可行性。
- **版本边界：** 两篇 APS 元数据与作者稿按标题和全部作者匹配；arXiv 尚未登记最终 DOI，未验证与正式 PDF 的内容一致性。两篇新预印本本轮未核实正式期刊版本；具体精确标题补查与限流状态见检索记录。
- **本地边界：** 只验证来源、PDF、解析、图表与文档；没有运行 QED-PIC、AA-TCP、EPIC3D、FLYCHK、MC-fast、SAMMY、VPIC、GPU 可视化或机器学习训练。

## 维护与证据记录

- [PDF 与逐篇核验](pdf_validation.json)
- [运行与验收记录](run_results.json)
- [检索、正式版与去重记录](research/research-run.json)
- [入库元数据](research/import-manifest.json)
- [原始来源与受阻候选](research/sources.jsonl)
- [MinerU 任务状态](research/mineru-attempts.json)
- [原图出处与裁框](research/figure-manifest.json)

PDF、布局正文与 MinerU 正文仅本地保留于 pdfs/ 并被 Git 忽略；GitHub 同步中文笔记、原图摘录、台账、索引和核验元数据。
