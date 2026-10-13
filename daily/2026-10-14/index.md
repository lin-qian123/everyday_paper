# 每日论文索引 - 2026-10-14

## 今日概览

- 运行日期：2026-10-14
- 新增论文数：5（均为 2026-10-13 正式出版全文）。
- 最新性：官方 arXiv 目标分类最近 100 条的最新提交仍为 2026-10-09，本轮没有新的可入库 arXiv 条目；Crossref 对 2026-10-09 至 14 做 10 组主题查询，得到 740 个唯一元数据作品，并用出版商页面与精确标题补核。
- 主题：双振荡器双颜色红外 FEL、LHD 氚燃耗/高能粒子约束、EJ-315 γ 谱展开、CZT 机器学习波形甄别，以及 He 等离子体—材料表面可靠性。
- 去重：按 DOI、规范化标题、442 条完成台账、30 条重试队列、来源 URL、摘要和物理场景检查；5 篇均是未入库正式作品。
- PDF / 正文：5 份正式 PDF 均通过 `%PDF-`、`file`、`pdfinfo`、`pypdf`、SHA-256 与非空 `pdftotext -layout`；共 77 页、16,656,651 字节，人工核查 10 个关键页并解码 5 幅保留图。本轮未运行 MinerU，明确使用已验证本地 PDF、335,952 字节布局文本和页面渲染。
- 重试：5 篇高相关正式论文因 Optica/IOP/Nature/Taylor & Francis 的验证页、cookie wall 或 `HTTP 403` 无法取得文章全文；未从摘要生成笔记，队列 `30 → 35`。
- 覆盖边界：这是定向增量筛选，不宣称穷尽所有期刊、预印本或数据库。

## 论文清单

### 1. Two-color dual-oscillator infrared free-electron laser

- 标识符：[DOI: 10.1103/b27b-9gg1](https://doi.org/10.1103/b27b-9gg1)
- 发表：2026-10-13，*Physical Review Accelerators and Beams* 正式 CC BY VOR
- 中文笔记：[Schollkopf et al. - 2026 - Two-color dual-oscillator infrared FEL.md](notes/Schollkopf%20et%20al.%20-%202026%20-%20Two-color%20dual-oscillator%20infrared%20FEL.md)
- 来源影响力分：9/10；专业相似度分：8/10
- 推荐理由：真实束流设施把同一电子束团列交替送入 MIR/FIR 两个振荡器，为双颜色泵浦—探测和束流同步提供定量平台。
- 一句话总结：`500 MHz` kicker 将 `1 GHz` 束团列分成两路，`36.6 MeV` 时双路覆盖 `4.5–12 μm` 与 `9–37 μm`；交叉相关仅间接约束亚皮秒相对抖动。

### 2. Triton Burnup Detector in Large Helical Device

- 标识符：[DOI: 10.1007/s10894-026-00603-w](https://doi.org/10.1007/s10894-026-00603-w)
- 发表：2026-10-13，*Journal of Fusion Energy* 正式 CC BY VOR
- 中文笔记：[Ogawa et al. - 2026 - Triton burnup detector in LHD.md](notes/Ogawa%20et%20al.%20-%202026%20-%20Triton%20burnup%20detector%20in%20LHD.md)
- 来源影响力分：8/10；专业相似度分：9/10
- 推荐理由：以次级 D–T 中子在 LHD 中定量约束 MeV 高能粒子输运，兼具中子诊断与聚变物理相关性。
- 一句话总结：氚燃耗比随磁轴内移由约 `0.1%` 增至最高约 `0.45%`，FBURN 以 `0.25 m²/s` 径向扩散最接近时间趋势，但仍只是 α 约束的模型辅助代理。

### 3. Calibration of organic liquid scintillator EJ-315 and unfolding of gamma spectra

- 标识符：[DOI: 10.1007/s10751-026-02815-0](https://doi.org/10.1007/s10751-026-02815-0)
- 发表：2026-10-13，*Interactions* 正式会议论文 VOR
- 中文笔记：[Saikia et al. - 2026 - EJ-315 gamma spectrum unfolding.md](notes/Saikia%20et%20al.%20-%202026%20-%20EJ-315%20gamma%20spectrum%20unfolding.md)
- 来源影响力分：7/10；专业相似度分：9/10
- 推荐理由：把标准源、GEANT4 响应矩阵、GOLD/GRAVEL 展开和不确定度分解连成可审计 γ 谱诊断链。
- 一句话总结：校准源主要结构的总质心不确定度为 `5.4–12.7 keV`；环境 `2614 keV` 结构对算法明显敏感，不能当成精确高能谱线。

### 4. Pulse-Shape Discrimination with Machine Learning for CZT Detectors at DAΦNE Beam Test Facility

- 标识符：[DOI: 10.3390/condmat11040038](https://doi.org/10.3390/condmat11040038)
- 发表：2026-10-13，*Condensed Matter* 正式 CC BY VOR
- 中文笔记：[Manti et al. - 2026 - ML pulse-shape discrimination for CZT.md](notes/Manti%20et%20al.%20-%202026%20-%20ML%20pulse-shape%20discrimination%20for%20CZT.md)
- 来源影响力分：7/10；专业相似度分：10/10
- 推荐理由：直接覆盖电子束—铅转换靶、CZT γ 探测和机器学习波形清洗。
- 一句话总结：XGBoost 在约 `10,000` 条人工形态标签上达 `AUC=0.996`，应用到 `790,700` 个事件后保留 `48.2%`；这不是独立真值下的粒子识别效率。

### 5. Analysis of material reliability features of plasma material interactions

- 标识符：[DOI: 10.1186/s11671-026-04982-z](https://doi.org/10.1186/s11671-026-04982-z)
- 发表：2026-10-13，*Discover Nano* 正式 VOR
- 中文笔记：[Pahsa - 2026 - Plasma-material reliability from AFM and SEM.md](notes/Pahsa%20-%202026%20-%20Plasma-material%20reliability%20from%20AFM%20and%20SEM.md)
- 来源影响力分：6/10；专业相似度分：7/10
- 推荐理由：提供 AFM/SEM—Weibull 表面退化链，也暴露小样本和图表内部不一致，适合作为材料诊断质量审计案例。
- 一句话总结：Pearson `r≈0.988–0.994` 只基于 `n=3` 共同时间点，且 Fig. 3 阴极蓝线与 Table 6/正文的可靠性下降相反，不能据此外推聚变部件寿命。

## 当日综合总结

- 本轮 5 篇均为正式排版全文，其中 FEL、LHD 中子诊断和 CZT 束靶测试含直接实验；EJ-315 的展开结果依赖 GEANT4 与迭代算法；材料可靠性论文是既有实验数据的二次统计分析。
- 对 Pahsa 的 Fig. 3—Table 6 冲突保留显式警告，没有把视觉曲线升级为寿命证据。
- 5 个阻塞候选均保留结构化来源失败；Nature 页面暴露的 peer-review-history PDF 已经内容核验并拒绝，不冒充文章 VOR。
- 本轮没有运行 FEL/束流光学、FBURN、GEANT4、GOLD/GRAVEL、XGBoost、Weibull 或材料图像重分析。
