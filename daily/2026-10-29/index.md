# 每日论文索引：2026-10-29

新增 **3 篇独立作品**，台账 **506 → 509**：2篇正式VOR、1篇高相关预印本。3份PDF共 **45页、22,416,291字节**，布局文本 **239,194字节**；MinerU pipeline均成功，实际查看 **22个身份／关键页、9幅原图／表摘录**。全文、布局和解析文本依约留本地并Git忽略，笔记、原图和核验记录纳入仓库。

## 阅读顺序与证据

| 作品 | 核心内容与限制 | 中文笔记 |
|---|---|---|
| [Spatiospectral conditioning of laser-plasma-accelerated electron beams using electromagnetic solenoids](https://doi.org/10.1103/2dby-29s7) | PRAB 10-28正式VOR，恢复旧重试；OMEGA EP真实电子束／照相及Boris解释。18 mm实测斑点、局部峰值6倍、有限厚度内最高约3倍分辨改善；非二次产额或全束能散验收。 | [Ambat等](notes/Ambat%20et%20al.%20-%202026%20-%20Solenoid%20spatiospectral%20electron%20beam%20conditioning.md) |
| [Correlation Between Radiation Damage Evolution and Mechanical Properties of Fe-Irradiated Tungsten](https://doi.org/10.3390/ma19214540) | Materials 10-28正式VOR；84 MeV Fe照射／SEM／XRD／压痕，加作者SRIM。约5.6 μm处峰值dpa不能直接配给0.25 μm压入体积，均值下降与散布同阶。 | [Rakhadilov等](notes/Rakhadilov%20et%20al.%20-%202026%20-%20Fe%20irradiation%20tungsten%20damage%20mechanics.md) |
| [Recovering Non-Maxwellian Velocity Distribution Functions from Collective Thomson Scattering Spectra Using Generalized Basis Representations](https://arxiv.org/abs/2610.37516) | 10-27提交、10-28公告的arXiv v1；PIC合成谱／可微反演，近上游VDF残差38.7→20.3／20.5%，非全时域准确率。初值MC固定噪声，不是后验。 | [Baker等](notes/Baker%20et%20al.%20-%202026%20-%20Non%20Maxwellian%20Thomson%20VDF%20reconstruction.md) |

## 检索、版本与去重

- 正式来源优先：Crossref对 **10-27至29** 运行10组主题查询，各最多75条，最终 **750行／592个唯一DOI**。强场QED查询首轮HTTP429，降为单次补查后恢复；原错误保留。词面无关的医学plasma、普通激光加工和中子星条目剔除。本检索为有界筛选，未声称穷尽覆盖。
- arXiv两组五分类API分别HTTP429／503，未获可用Atom记录；改读十个官方分类recent页的**首个日期块（10-28公告）**，返回157行、去重137条。URL请求show=100不等于实际读取100条，未把首块计成整页或完整历史；CTS单篇页确认提交时间10-27 16:37:30 UTC。APS最近目录及精确标题查询补充核查。
- 依据DOI、arXiv别名、规范化标题、来源URL、作者和物理场景核对506条台账、45条重试及相关历史笔记。Baker与Sakai非Maxwell贝叶斯、Nakano双组分CTS、Foo2023先导论文具有方法联系，但作者、PIC真值、基函数与不确定性任务不同，作为独立作品。**旧506条完成记录全部不变**。
- 螺线管旧重试的09-28是接受日期，本轮正式PDF确认10-28出版。恢复该条并移出队列；Materials由官方mdpi-res CDN取得VOR。CTS精确标题Crossref前3项均为不同旧研究，作者仍标投稿Physics of Plasmas，未升级为正式发表。
- **重试45→45：恢复1条、新增1条。** 新项 `10.1103/bqll-w87s`（Automated optimization of microbunching for seeded free-electron laser schemes）仅有Crossref10-28日期；官方harvest代理／直连404，出版商PDF代理403／直连404，定向标题／作者搜索未找到经验证合法作者稿。保留精确失败，不生成摘要笔记或已读VOR声明。其余44条旧重试对象未改；JCP114707的processed PDF=null历史交集维持。
- HiPER第一壁热模型、极化非热D–³He等仅为未选元数据线索，没有全文阅读／入库声明。

## 科学边界与接续

1. 螺线管6倍为两炮局部峰值之比，激光输入和指向不同；实测能谱比理想模型宽。图3谱人为重标度，图6有聚焦谱是模拟。线圈轴尺寸、磁场半宽、Boris印刷式及照相几何疑点在笔记保留，未经源码确认不判断实际程序错误。
2. 钨是Fe离子材料实验，不是中子／激光／寿命试验；SRIM位移dpa不是存活缺陷量，压痕点数不是独立样品重复，硬度／模量下降不能当显著软化。
3. CTS是准1D、约化质量比／光速PIC合成诊断；残差掩膜、投影方向、固定电子解与固定噪声初值散布均有限制，需真实谱和仪器响应、噪声传播及跨视角验证。
4. 本轮没有重跑作者轨迹程序、SRIM、PSC、反演／训练、显著性检验或实验；未新增激光转换靶—光核中子／核素端到端实测、临床或防护验收。

## 核验与可追溯记录

[PDF校验](pdf_validation.json) · [下载及失败](download_report.json) · [来源元数据](research/sources.jsonl) · [检索范围](research/research-run.json) · [正式版核查](research/version-checks.json) · [MinerU](research/mineru-attempts.json) · [原图来源](research/figure-manifest.json) · [运行结果](run_results.json)
