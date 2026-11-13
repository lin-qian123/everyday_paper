# 2026-11-14 每日论文

本轮新增 **5篇已核验全文与中文笔记**：2篇11-12出版社正式版、3篇11-13公告的作者预印本；台账 **559→564**。另将7月已入库的ADITYA-U论文原位补入正式DOI和11-13在线发表信息，不重复计数。旧558对象保持，1对象只补出版/版本信息；65条重试对象保持。

## 新增论文

| 论文与实际版本 | 核心内容与阅读边界 | 全文与笔记 |
| --- | --- | --- |
| Gutberlet等，HiCANS欧洲项目；[Quantum Beam Science正式版](https://doi.org/10.3390/qubs10040026)，11-12 | ARGITU、ICONE、HBS-I的RF质子束、靶/慢化/仪器方案；IPHI原型靶100 h试验与整设施设计/MC性能分开。表文反应标签、产额、平台脉冲/慢化材料存在待澄清口径。 | [21页PDF](./pdfs/gutberlet-2026-hicans.pdf) · [中文笔记](./notes/gutberlet-2026-hicans.md) |
| Hu等，弱形式中子扩散PINN；[Frontiers正式版](https://doi.org/10.3389/fenrg.2026.2005399)，11-12 | 两群TWIGL/IAEA-3D数值基准，神经网络预测FEM节点通量；瞬态由FEM/C–N推进。TWIGL训练110.96 s，对FEM0.665 s；不能称已实现加速。 | [14页PDF](./pdfs/hu-2026-neutron-diffusion-pinn.pdf) · [中文笔记](./notes/hu-2026-neutron-diffusion-pinn.md) |
| Beverido等，CP驻波QED级联饱和；[arXiv:2611.15519v1](https://arxiv.org/abs/2611.15519v1)，11-11首投、11-13公告 | 有种子的1D3V PIC-QED；局部产生/迁移、过密反射和包络共同决定耗尽。约70%是总吸收，图读约61%辐射能不是能阈/准直后的可用γ效率。 | [16页PDF](./pdfs/beverido-2026-qed-cascade.pdf) · [中文笔记](./notes/beverido-2026-qed-cascade.md) |
| Kolobov与Arslanbekov，PAMAR；[arXiv:2611.14820v1](https://arxiv.org/abs/2611.14820v1)，11-10首投、11-13公告 | 独立物种网格、时钟和局域模型。CCP离子混合未得到可靠加速；球面电子自洽全程序仅省11% CPU。静电弱电离演示，不是相对论激光PIC替代验证。 | [39页PDF](./pdfs/kolobov-2026-pamar.pdf) · [中文笔记](./notes/kolobov-2026-pamar.md) |
| Fujioka等，非连续光子能群；[arXiv:2611.15095v1](https://arxiv.org/abs/2611.15095v1)，11-11首投、11-13公告 | 一维稳态等温Sn FLD，以1500群为数值参照；100群总通量误差中位2.1%、p90为8%，全谱L2中位14.9%。约58倍单例计时不含离线训练/建表，窄带误差不全面优于连续分组。 | [10页含补充PDF](./pdfs/fujioka-2026-radiation-groups.pdf) · [中文笔记](./notes/fujioka-2026-radiation-groups.md) |

## 既有论文原位升级

[Maurya等ADITYA-U笔记](../2026-07-08/notes/Udaya%20Maurya%20et%20al.%20-%202026%20-%20Deep%20Learning%20Models%20for%20ADITYA-U%20MHD%20Equilibrium.md)补入[Nuclear Fusion正式DOI](https://doi.org/10.1088/1741-4326/aebc9d)。标题、四作者、100760例/766炮数据库对应；官方arXiv仍只有2607.04865v1。本地18页作者稿首页和哈希核对，保留7月入库日期。IOP PDF实际返回HTTP200、14371字节HTML/Radware；本轮未取得VOR、未重新精读旧全文，不把正式摘要新增内容写回旧作者稿结论。该项不新增完成论文或全文重试。

## 检索与去重范围

- 正式来源优先：Crossref十组主题，出版日期11-12至11-14，每组分别取最新出版与相关性前40，合计 **789行/587个DOI**。一次HTTP500后定向重试成功200，初始失败和恢复均保留。
- 官方arXiv十类recent列表取11-13公告块：**582行/547个ID**；本次cs.LG完整读取该块340条。类别交叉重复已合并；这是有界检索，非全球穷尽。
- 新条目按DOI、规范化标题、arXiv别名和物理场景去重；三篇预印本额外用精确标题Crossref前3项核查，未核实同作品期刊版，不据此断言其绝对不存在。
- QED与旧Wei外加电子束代际诊断、Dou的CH空穴钻进火球作者和场景不同。ADITYA正式记录对应旧条目，已原位升级。
- 碳中子反应2611.16075仅取得元数据/PDF，核实正式版发表于9月，未阅读全文或入库；纳米粒子剥离2611.16505、Vlasov-Maxwell2611.15248等仍是未读候选。旧TPF-2等65条重试未做全队列探测、未改对象。

## 全文、图像与核验

5 PDF共 **100页、17770498字节**；文件头、MIME、SHA-256、pdfinfo/pypdf/PyMuPDF页数和逐页非空文本检查通过。全文布局文本456160字节；共25个关键原页完成阅读者目视，15个保留原图/表摘录均由主代理再次打开，裁框与源PDF像素匹配记录见[图源清单](./research/figure_provenance.json)。PDF和文本本地保留并沿用Git忽略规则；图、笔记、元数据与索引随仓库发布。

MinerU此前认证已失效，本轮未再次验证凭据、未提交请求，明确采用本地全文与原页渲染回退。未复跑作者PIC、FLD、PAMAR、训练、MC或设施实验；新内容主要为方法/设计/模拟与已引用原型证据，未新增激光转换靶光核核素完整实验链、临床或防护验收。

- [检索来源与范围](./research/discovery_sources.json) · [候选元数据](./research/discovery_candidates.jsonl)
- [正式/作者版本证据](./research/selected_metadata.json) · [标题版本核查](./research/journal_version_checks.json) · [去重核查](./research/dedup_checks.json)
- [下载报告](./download_report.json) · [PDF核验](./pdf_validation.json) · [运行结果](./run_results.json) · [最终验证](./research/verification.json)
