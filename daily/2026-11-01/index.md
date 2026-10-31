# 每日论文索引：2026-11-01

新增 **4篇独立作品**：1篇10月30日正式VOR、1篇7月28日正式VOR补收、2篇近期预印本。台账 **517→521**，重试 **45→45**。四份主文共33页，另有3页作者补充材料；PDF及文本按项目约定留本地并Git忽略，中文笔记、8幅原图摘录、来源和核验记录进入仓库。

## 阅读顺序

| 论文与版本 | 主要收获及边界 | 中文笔记 |
|---|---|---|
| [同发CR-39绝对标定闪烁体](https://arxiv.org/abs/2610.38063v1)，10-27提交 | 2 mm周期取样，P43约0.8 MeV穿透峰；CsI:Tl图中仅约至2.1 MeV。拟合误差未含约21%／10%光学转换误差，同发仍假设相邻空间谱平滑。 | [Lin等：响应标定](notes/Lin%20et%20al.%20-%202026%20-%20In%20situ%20scintillator%20absolute%20calibration.md) |
| [CR-39蚀刻坑自动识别](https://doi.org/10.1063/5.0338529)，7-28 VOR | 10-28 arXiv新上传对应旧正式论文，只计一次。Hough／椭圆及REL模型；约10%人工边界差，>2 MeV排除拟合，轴／半轴及角度印刷定义待查。 | [Lin等：计数与几何](notes/Lin%20et%20al.%20-%202026%20-%20Automated%20CR39%20pit%20detection.md) |
| [中子成像材料校准无关散射修正](https://doi.org/10.1038/s41598-026-77789-8)，10-30 VOR | 双屏保留近端约75 μm分辨率，改善D₂O浓度反演；20 cm远端仍4—17%散射／透射比，20%管恢复27±5%。不是无需仪器校准或严格散射归零。 | [Sans-Planell等](notes/Sans-Planell%20et%20al.%20-%202026%20-%20Calibration%20independent%20neutron%20imaging.md) |
| [Helsinki LiF(p,n)与NCT-WES谱仪](https://arxiv.org/abs/2610.39763v1)，10-29提交 | 1.960／2.040／2.310 MeV厚靶宽谱实验，FRUIT依赖初猜；NCT-WES与LB 6411低两档相差约27—42%，绝对通量单位／归一化需闭合。不是激光源或BNCT临床验收。 | [Myllymäki等](notes/Myllymaki%20et%20al.%20-%202026%20-%20NCT%20WES%20neutron%20spectrometry.md) |

## 检索和去重

- Crossref：10个主题相关性查询，10-30至11-01窗口，每组60条；最终 **600返回行／511唯一DOI**。三组初次429，顺序补查全部成功，初始错误仍记录。11月只有年月的卷期日期不当成新在线发表证据。
- arXiv：十分类recent页面首个日期块共 **348行／311唯一ID**，均为10-30公告；cs.LG只覆盖当日372条中的前100条。没有声称全库穷尽，也未在本轮额外调用Atom API。泛网页检索返回精度低，只作补充线索。
- 对517已完成和45重试，检查DOI、规范化标题、arXiv别名、来源、作者和物理任务；旧对象保持不变。两篇Lin作品任务不同但共用团队／平台／方法链，不作独立复现实验计数。Crossref里的AIP科普摘要 *Framework automates pit detection...* 不作为另一篇原始研究收录。
- CR-39正式VOR日期以PDF确认7-28，而非Crossref卷期7-01或arXiv10-28；两篇预印本精确标题Crossref前三均未核实本作正式版，保留版本边界。
- 全部选中全文已取得，无新增摘要笔记／未解决全文项；45条既有受限重试本轮不重复全队列空跑，历史JCP已处理PDF=null的交集保留。
- IFE会议综述、UGKWP、磁化射流和CNT靶优化仍为未读候选；本轮不宣称完成这些论文的全文阅读。

## 核验与接续

5份PDF全部通过文件头、类型、SHA-256、pdfinfo／pypdf／PyMuPDF页数及全页非空文本校验。实际目视18个身份／关键页及8幅保留原图。MinerU成功解析三份主文和CR-39对应作者稿；AIP正式URL解析失败，正式版采用本地布局／渲染核验；作者稿解析不冒称VOR解析。作者补充材料只使用本地布局与渲染。

下一轮优先恢复新正式全文和既有受限来源；诊断方向优先独立CR-39计数真值／几何定义、闪烁体相关尺度误差及遮罩取样验证、中子双屏残余散射和长度坐标、NCT-WES绝对通量及核库／束能敏感性。本轮未重跑作者模拟、反演、代码或实验，未新增激光转换靶—光核核素端到端、临床或防护验收。

[PDF核验](pdf_validation.json) · [下载与恢复](download_report.json) · [来源](research/sources.jsonl) · [检索覆盖](research/research-run.json) · [候选元数据](research/discovery-candidates.json) · [版本与去重](research/version-checks.json) · [解析及回退](research/mineru-attempts.json) · [原图清单](research/figure-manifest.json) · [运行结果](run_results.json)
