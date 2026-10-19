# 每日论文索引：2026-10-20

本轮新增 **4 篇**：1 篇 10-19 正式 VOR、3 篇 10-15/16 官方 arXiv v1；台账 **473 → 477**。重点是激光电子束转换靶正电子实测、质子照相的密度/场联合诊断、动理学机器学习闭合和辐射源 MC 计量口径。

## 运行与检索范围

- 4 份真实 PDF 共 **78 页、12,821,360 字节**；通过 `%PDF-`、文件类型、SHA-256、pdfinfo/pypdf 页数一致和逐页正文检查。342,479 字节布局文本及 MinerU 正文留本地，四篇 pipeline 均完成；关键原图/表在笔记对应段落解释。
- Crossref 在 2026-10-19 至 20 的 10 组主题查询各最多 75 条，合计 **742 行、548 个唯一 DOI**；其中一组初次 429，降为顺序复查后成功，失败响应未计入行数。官方 arXiv 五类最近 300 条最新可见投稿为 **2026-10-16**。这是有界定向检索，不是穷尽检索或所有分类的实时镜像。
- 三篇预印本各做精确标题 Crossref 前三条核查，未核实同篇正式版。相近标题的高平均通量中子源和 PNAS 2025 十矩闭合具有不同作者/场景，未错误合并；新 arXiv 2610.23431 与已收录正式论文同题，未重复入库。
- 正式剂量学论文的期刊 PDF 入口返回 403，公开官方 CDN 提供了经验证的正式全文，故无需新增缺全文重试。既有 **42 条重试记录保持不变**；已知订阅/未来开放条目没有新的可用性信号，本轮未重复请求。

## 论文清单

### 1. On the Monte Carlo Calculation of the Air-Kerma Strength for Brachytherapy Sources

- Guerrero、Almansa、Lallena，*Radiation* 6(4), 41，2026-10-19，正式 VOR。[DOI](https://doi.org/10.3390/radiation6040041)
- [中文笔记](notes/Guerrero%20et%20al.%20-%202026%20-%20Monte%20Carlo%20air%20kerma%20strength.md)
- 来源影响力 6/10、专业相似度 7/10；为主观阅读优先级，不是期刊影响因子。
- 推荐理由：明确 MC 辐射计量中电子贡献、能量转移/吸收系数、谱分箱和低能截断的误差来源。
- 一句话结论：数个亚百分比的计算选择会影响空气比释动能强度，需同时保留定义、谱处理和统计口径；不能把它当成激光源效率或临床实测验证。

### 2. High average flux positron sources driven by a mJ-class laser

- Foster 等，2026-10-16，官方 arXiv v1。[来源](https://arxiv.org/abs/2610.23243v1)
- [中文笔记](notes/Foster%20et%20al.%20-%202026%20-%20mJ%20laser%20positron%20source.md)
- 来源影响力 8/10、专业相似度 10/10。
- 推荐理由：直接打通 mJ 激光—LWFA 电子—铅转换靶—磁接受度—探测响应，包含实测与 FLUKA 对照。
- 一句话结论：10 Hz、100 发累积测得 (1.0±0.2)×10³ 个 0.8–1.7 MeV 正电子；电子已表征到 kHz，正电子高重频仍受靶烧蚀和碎屑限制。

### 3. Measuring electron density and electromagnetic fields in low-density laser-driven plasmas using proton radiography

- Chu、Gregori、Bott、Tzeferacos，2026-10-15，官方 arXiv v1。[来源](https://arxiv.org/abs/2610.22605v1)
- [中文笔记](notes/Chu%20et%20al.%20-%202026%20-%20Proton%20radiography%20electron%20density.md)
- 来源影响力 8/10、专业相似度 9/10。
- 推荐理由：将焦散碰撞展宽从“成像模糊”转成沿同一视线的密度约束，并与独立诊断比较。
- 一句话结论：OMEGA 既有湍流发电机实验数据支持约 10²⁰ cm⁻³ 的模型辅助密度诊断；源尺寸、组分、路径及场结构仍决定适用范围，不能当作无模型三维密度测量。

### 4. Properties and challenges of machine learning closures for ten-moment fluid models in the case of Landau damping

- Jeß 等，2026-10-16，官方 arXiv v1。[来源](https://arxiv.org/abs/2610.23080v1)
- [中文笔记](notes/Jess%20et%20al.%20-%202026%20-%20Machine%20learning%20ten%20moment%20closures.md)
- 来源影响力 7/10、专业相似度 9/10。
- 推荐理由：将离线拟合分数与闭环流体部署的稳定性分开检验，适合审查代理模型评测是否覆盖真正使用方式。
- 一句话结论：域内 ML 闭合能再现部分非线性 Landau 阻尼行为，但离线高精度不能保证在线稳定，熵演化只能作为案例支持的诊断线索。

## 综合判断与接续

优先读正电子转换靶笔记。已测产额只对应接受能段、输运配置和 100 发累积；2 mm 是扫描内最清晰的探测信号条件，既非全球最优厚度，也非全源转换效率。约 50 fs 本征束长与约 90 ps 飞行时间差为估计；没有完成 kHz 正电子源、PALS 样品测量或屏蔽验收。

质子照相是实验图像上的模型反演与交叉诊断，机器学习工作是数值训练/闭环部署，空气比释动能工作是 MC 计量分析。笔记保留原文疑点和局限；本轮没有运行作者的 LWFA、FLUKA、输运、流体或训练程序。

本轮没有选出新的强场 QED、光核/中子/同位素端到端实验全文。ModeCast 等相关模拟代理留作较低优先级线索，没有为了补齐主题添加条目。

## 可追溯记录

- [逐篇 PDF 与目视核验](pdf_validation.json)
- [检索覆盖与去重](research/research-run.json)
- [版本、正式发表和相关作品核查](research/version-checks.json)
- [来源元数据](research/sources.jsonl)与[入库清单](research/import-manifest.json)
- [MinerU 解析记录](research/mineru-attempts.json)
- [原图/表裁框与哈希](research/figure-manifest.json)
- [本地验证与发布准备结果](run_results.json)

PDF、布局文本及 MinerU 正文按现有规则留本地并由 Git 忽略；中文笔记、原图摘录、下载报告、元数据和索引随 Git 发布。最终提交及远端一致性写入自动化运行记忆和完成消息。
