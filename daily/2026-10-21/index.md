# 每日论文索引：2026-10-21

本轮新增 **5 篇**：2 篇 10-20 PRAB 正式 VOR、3 篇 10-17 至 19 官方 arXiv v1；台账 **477 → 482**。覆盖束流失准容差、XFEL 脉冲整形与损失监测、LWFA 晶体 γ 源、NIF 动理学—辐射模型和高重频液体靶。

## 检索、去重与全文

- 先检索正式来源：Crossref 在 2026-10-20 至 21 窗口对 10 组主题各取最多 75 条，合计 **729 行、551 个唯一 DOI**；本轮无请求错误。宽泛关键词包含大量离题结果，经过相关性筛选；这是有界检索，不能代表全部新论文。
- 安装的 search-layer 单次定向查询无结果，使用 Crossref、官方 arXiv 和 web 原始来源补查。arXiv 五类最近 300 条的最新可见提交为 **2026-10-19T17:40:03Z**；没有把当前不可见批次当成不存在。
- 按 DOI/arXiv 别名、规范化题名、作者和物理场景去重。Zymak 的 Si(110) 平面沟道源与已收 Sytov 的 W⟨111⟩ 光核级联设计不同；同题 arXiv 2610.23431 对应既有正式 DOI，未重复收录。三篇新预印本各经 Crossref 精确题名前三条核查，尚未核实同篇正式版。
- **5 份 PDF 共 97 页、23,706,118 字节**，通过文件头、类型、SHA-256、pdfinfo/pypdf 页数一致和逐页正文检查；保留 362,893 字节布局文本，五篇 MinerU pipeline 均成功。29 个首页/关键页及 10 幅原图/表摘录完成目视核查；临时页面渲染与解析缓存清理，仅保留有效全文、正文、原图和可追溯记录。
- 两篇 APS 正式 PDF 从官方 harvest 取得，未以网页接受稿标签代替正式首页身份。**42 条既有重试记录不变**；已知订阅/未来开放条目没有新可用信号，本轮没有重复探测或新增缺全文笔记。

## 论文清单

以下来源影响力/专业相似度均为主观阅读排序，满分 10，不是期刊影响因子或正式质量认证。

### 1. Tolerances to driver-witness misalignment in a quasilinear plasma wakefield accelerator

- Wilson、Farmer、Lotov、Pukhov，PRAB **29**, 103602，2026-10-20，正式 VOR。[DOI](https://doi.org/10.1103/47mg-t29q)
- [中文笔记与两幅原图](notes/Wilson%20et%20al.%20-%202026%20-%20Quasilinear%20PWFA%20misalignment%20tolerances.md)
- 来源影响力 8/10、专业相似度 9/10。推荐理由：用相混合后有效密度关联成泡时间、切片发射度和电荷保留，适合建立真实束流误差预算。
- 一句话结论：高电荷见证束可缓解初始横向失准导致的束质损失，但结果是固定驱动束下的 PIC 扫描；正式 PDF 的角波数单位与 1.7 mrad 换算存在量纲冲突，已在笔记标出。

### 2. Experimental demonstration of an L-shaped corrugated wakefield structure for beam shaping at a high-repetition-rate free-electron laser

- Qin 等，PRAB **29**, 103405，2026-10-20，正式 VOR、Editors’ Suggestion。[DOI](https://doi.org/10.1103/r4nx-blvw)
- [中文笔记、谱重建与中子剂量原图](notes/Qin%20et%20al.%20-%202026%20-%20L%20shaped%20corrugated%20XFEL%20shaping.md)
- 来源影响力 8/10、专业相似度 8/10。推荐理由：将尾场整形、低 beta、准直器与实测损失监测放在同一高重频装置中。
- 一句话结论：7 keV 的重建 rms 脉宽 27.2→6.3 fs，伴随能量 2.3→0.2 mJ；列内 MHz 与连续 MHz、谱重建与直接时域、波荡器损伤评估与人员防护均分别标注。

### 3. Construction of crystal-based light sources with LWFA electron beams

- Zymak 等，2026-10-18，官方 arXiv v1。[来源](https://arxiv.org/abs/2610.25336v1)
- [中文笔记与电子/正电子谱图](notes/Zymak%20et%20al.%20-%202026%20-%20LWFA%20crystal%20gamma%20source.md)
- 来源影响力 7/10、专业相似度 10/10。推荐理由：直接比较硅晶体辐射的入射散角、沟道接受率、厚度与接受锥，适合激光电子束转换靶研究。
- 一句话结论：窄束可显著提升小角接受内谱峰，但通量以带宽、平均电流和接受角为条件；未来 4 GeV 正电子支路未计实际产生/输运损失，不是已建成 γ 或中子源。

### 4. Beyond Radiation Hydrodynamics: A Coupled Kinetic Plasma and Radiation Modeling of NIF Polar Direct Drive Capsule

- Hammer 等，2026-10-19，官方 arXiv v1；PDF 内署日期 10-20。[来源](https://arxiv.org/abs/2610.26537v1)
- [中文笔记、原始对照表和弹道离子图](notes/Hammer%20et%20al.%20-%202026%20-%20Kinetic%20radiation%20NIF%20capsule.md)
- 来源影响力 8/10、专业相似度 9/10。推荐理由：把离子漏失、弹道预热与辐射损失放进同一动理学求解器，并给出与既有实验的残差。
- 一句话结论：含辐射 iFP 的中子产额仍约为实测 2.10 倍，燃烧宽度只有实测约 56.5%；早期激光驱动与边界来自经校准 xRAGE，不能称完整端到端预测。

### 5. Micrometer-thin liquid sheets from single-jet impact on a sharp edge for multi-kHz laser-plasma experiments

- Kumar、Harsha、Singh，2026-10-17，官方 arXiv v1；PDF 内署日期 10-20。[来源](https://arxiv.org/abs/2610.24504v1)
- [中文笔记、反射率和帧级稳定性原图](notes/Kumar%20et%20al.%20-%202026%20-%20Multi%20kHz%20thin%20liquid%20sheets.md)
- 来源影响力 7/10、专业相似度 10/10。推荐理由：针对高重频靶更新与光学污染给出直接实验条件和工程限制。
- 一句话结论：60:40 乙二醇/水微米薄片支持最高 10 kHz 镜面运行；77% 反射率在另一组 25 fs、1 kHz 工况，约 18 μrad 稳定性来自 40 s/598 帧，尚非逐脉冲测量。

## 优先阅读与接续

优先读晶体 γ 源和液体薄靶：前者突出角接受与光子率的定义，后者直接涉及高重频更新、蒸汽与碎屑。两者还没有被同一实验连成“高重频激光—优质电子束—晶体 γ—光核/中子”链。XFEL 的实际中子剂量曲线可作为束损位置和准直策略的参考，不能直接移植防护结论。

NIF 论文是既有 DT 聚变实验的模型比较；Wilson 是 PIC/解析工作。五篇均未在本地复跑作者物理求解器、训练或原始数据分析。PRIORA 质子照相、聚变强化学习、Thomson 参数归因和离子束第二核查系统保留为低优先级检索线索，未写成已读笔记。本轮未选出新的强场 QED、光核中子/同位素或临床端到端实测全文。

## 可追溯记录

- [PDF 身份、逐页正文与目视核验](pdf_validation.json)
- [检索覆盖、候选状态和去重](research/research-run.json)
- [正式版检索与版本核查](research/version-checks.json)
- [来源元数据](research/sources.jsonl)与[新增台账清单](research/import-manifest.json)
- [MinerU 解析记录](research/mineru-attempts.json)
- [原图出处、PDF 裁框与哈希](research/figure-manifest.json)
- [本地验收与发布准备结果](run_results.json)

PDF、布局文本与 MinerU 正文按仓库规则保存在本地并由 Git 忽略；中文笔记、原图、元数据、报告与索引随 Git 发布。最终提交和远端一致性写入自动化运行记忆与完成消息。
