# 2026-11-27 每日论文

新增 **3篇经验证全文／中文笔记**：1篇11-26上线的出版社Article in Press、2篇11-25首投／11-26公告的作者预印本。去重台账 **602→605**；RF鞘层正式论文PDF返回订阅HTML，新增1项重试，队列 **80→81**。旧602个完成对象与80个重试对象保持。

## 今日论文

| 论文与实际版本 | 阅读重点和证据限制 | 本地资产 |
| --- | --- | --- |
| De Dominicis等，EJNMMI Physics，[10.1186/s40658-026-00968-z](https://doi.org/10.1186/s40658-026-00968-z)，11-11接收、11-26在线，**14页Article in Press** | 富集⁵⁰Ti质子／⁴⁹Ti氘核制备⁴⁷Sc：厚靶活度、冷却纯度和污染剂量的选择不同。旧截面＋SRIM积分＋鼠到男性人体外推，非新生产／临床实验；无完整不确定度传播。 | [中文笔记](./notes/dedominicis-2026-sc47.md) · [PDF](./pdfs/dedominicis-2026-sc47.pdf) · [S1–S3原始DOCX](./supplements/dedominicis-2026-sc47-tables.docx) |
| Masson-Laborde等，[2611.33971v1](https://arxiv.org/abs/2611.33971)，**6页作者v1** | 相同功率谱／相干时间的RPP+BB与ISI，2%带宽指定二维PIC对照中SRS相对少约34%；非实验效率增益，两个光学实现的半极差非置信区间，PDF与时间持续性未独立消融。 | [中文笔记](./notes/massonlaborde-2026-speckle.md) · [PDF](./pdfs/massonlaborde-2026-speckle.pdf) |
| Walsh，[2611.34766v1](https://arxiv.org/abs/2611.34766)，**15页作者v1，含A/B/C** | 动理学f₂应力使Nernst与热流的抑制分离；磁场纹理长度引入独立Kn_B。约50%是固定外加磁场热前沿算例的瞬时场变化率，不是磁通保持实测或整靶增益。 | [中文笔记](./notes/walsh-2026-nernst.md) · [PDF](./pdfs/walsh-2026-nernst.pdf) |

优先关注⁴⁷Sc中同一能窗／同一EOB后时刻的RIP与RelD口径，以及两篇HEDP论文的受控对照实际排除了什么。三篇均未提供新的激光光核全链、临床或屏蔽验收。

## 版本、去重与补充材料

⁴⁷Sc官网元数据的普通PDF路径404；实际下载锚点_reference.pdf成功，首页标Article in Press且印有11-26在线日期。没有把它升级成最终编辑版。补充链接确实给出S1–S3科学DOCX，3表均读，ZIP／Word XML结构与SHA已核；本地转换5页仅作目视核验，原始DOCX保留、临时转换PDF不留。

两篇新作者稿经官方arXiv身份／历史核验，与Crossref原题前3结果未发现可验证同作正式记录。Raman源码包只有主TeX、参考与图PDF，没有引用[50]指向的独立Supplement；缺口已保留，笔记里的统计推导从正文定义展开。Walsh旧系列2610.30303、2610.32085是不同论文，后者已在库，不作本篇别名或重复入库。

去重核查DOI、规范化标题、同作arXiv标识、作者和物理场景。原602对象不改，related_work不充当身份别名。旧JCP 10.1016/j.jcp.2026.114707完成／重试交集保留为继承状态，本轮未新增重叠。

## 正式全文重试

PSST **35,115021**，[10.1088/1361-6595/aec324](https://doi.org/10.1088/1361-6595/aec324)，Scaling of RF sheath rectification in magnetized plasmas: electron phase-induced enhancement and collapse：官方PDF入口 **200／text/html／196656字节**，无PDF签名；文章页 **200／196619字节**，明确当前计算机无机构订阅。HAL精确标题前5返回0；OSTI引号精确标题200返回JSON空数组（2字节），有界网页检索未找到可核实同作作者PDF。

只记入重试，不写摘要笔记。重试命令仅构造检查，未执行整队，原80项未重复探测。未进行订阅、付费或凭据修改。

## 检索范围与未读线索

Crossref十主题，在线日期 **11-26至11-27**、journal-article、每主题相关性前40，共 **400行／343不同DOI**；HEDP与converter主题最初429，各顺序重试恢复200。两预印本的期刊身份查询初次JSON解析失败，没有将异常当成无结果；最终各顺序200结果保留。

官方arXiv十类11-26最新公告块，共 **396行／382不同ID**；从标题所在dl取块，逐类核对标题数量，含cs.LG完整271条。范围有界非穷尽，排除血液plasma、普通ML和无关激光制造；不据未选中宣称没有相关新论文。

crossing-beam speckle统计、physical-mass-ratio shock PIC、有限Larmor半径响应、复合闪烁体中子／γ转换、会聚束流Geant4诊疗等只作元数据线索，未读入库、未探测者不加入重试。前轮B-11、冷中子、轴子、ML锁模及旧ICF／光核／活化线索未补读。

## 阅读、核验与接续

3PDF共 **35页／3,804,278字节**，经签名、MIME、SHA-256、pdfinfo／pypdf／PyMuPDF三路页数和逐页非空文本校验。35源页由阅读者实际总览，另有补充DOCX转换5页总览；21幅有效原图全部由主代理重开并核源裁框像素。原始PDF和布局文本本地保留、沿用Git忽略；笔记、原图、科学补充DOCX和来源记录提交。

MinerU零请求，历史401认证失败未复测；明确采用本地提取／渲染回退。本轮没有复跑作者PIC、VFP、截面拟合、剂量程序或实验。

接续：恢复RF鞘层全文及⁴⁷Sc最终编辑版；补Raman独立Supplement、增加光学集合并拆分PDF／持续性因果贡献；Nernst固定代码／载流权重与滤波边界，加入自洽J、B反馈及多维验证。⁴⁷Sc需截面协方差、真实能散、靶热工、化学收率／回收和真实药代；图4图注keV/nd与轴MeV/nd不符，按S1和柱高解释但保留疑点。

README／TODO与索引同步；原有AGENTS.md修改保留并排除本次提交。提交／远端一致性在自动化记忆记录。

## 运行记录

- [检索范围](./research/discovery_sources.json) · [Crossref快照](./research/crossref_discovery.json) · [arXiv快照](./research/arxiv_discovery.json) · [未读线索](./research/deferred_candidates.json)
- [正式元数据](./research/selected_formal_crossref.json) · [新增台账对象](./research/selected_metadata.json) · [去重](./research/dedup_checks.json) · [arXiv Raman身份](./research/2611.33971-identity.json) · [arXiv Nernst身份](./research/2611.34766-identity.json)
- [原始访问](./research/formal_access.json) · [恢复PDF／HAL](./research/followup_access.json) · [RF订阅／PDF入口](./research/rf_pdf_link_inspection.json) · [OSTI精确查询](./research/rf_osti_exact.json) · [重试命令](./research/retry_command_check.json)
- [补充／同作期刊检查](./research/supplement_and_publication_checks.json) · [两篇主代理图源](./research/primary_figure_provenance.json) · [Walsh阅读／图源](./research/walsh_reading.json)
- [下载报告](./download_report.json) · [PDF核验](./pdf_validation.json) · [补充三表核验](./research/supplement_validation.json) · [运行结果](./run_results.json) · [索引保留](./research/index_rebuild_preservation.json) · [最终核验](./research/verification.json)
