# 2026-10-02 定向论文研究报告

## 检索覆盖

本轮先运行安装的多来源搜索层，4 个定向查询返回 0 条可用结果；随后使用官方 arXiv Atom/API 核对 `physics.plasm-ph`、`physics.acc-ph`、`physics.comp-ph`、`physics.ins-det`、`nucl-ex`、`nucl-th` 和 `hep-ph` 的 2026-10-01 公告批次，并用 Crossref 核对 2026-09-30 至 10-02 的正式元数据。Web 复核直接打开 3 个 arXiv 摘要页和 APS Accepted Paper 页面；IOP 页面受 robots/验证页限制。覆盖是定向的，不宣称穷尽全部期刊。

## 选择逻辑

- **激光束流—转换靶—核应用链：** `2609.40005` 直接把 FBPIC/Wake-T 的 LWFA 输入接到取向晶体 Geant4，并分别报告 γ、正电子和光核中子；其优势是应用链完整，限制是全链数值化。
- **装置保护与材料响应：** `2609.40132` 用 Geant4 数据库和一维热扩散做全 ITER 壁面筛查，并以 MEMENTO 标出熔点前后适用边界。
- **聚变 alpha 粒子输运：** `2609.39376` 用 WBA 相空间图显示 QS 误差与多谐波 Alfvén 模的耦合，不把混沌比例直接升级成损失功率。
- **正式来源优先：** APS `10.1103/79h1-q62n` 已有 DOI 与 Accepted Paper 页面；本地全文明确使用同作品 arXiv v1 作者预印本，不把它当作 VOR。
- **结构化重试：** IOP `10.1088/1612-202x/aeab55` 的主题高度相关，但官方 PDF、DOI 和文章页均返回 HTML，且无同题 arXiv/合法作者稿，因此只进入重试队列。

## 共同证据边界

四篇入库内容均以作者理论/模拟为主：Sytov 串联 FBPIC、Wake-T 与 Geant4；Svensson 使用 JOREK 场景、Geant4 库和 MEMENTO 基准；Lachmann 使用 FIRM3D/AE3D 无碰撞轨道；Xia 使用解析模理论与三维 OSIRIS PIC。本地只做 PDF/正文/图表核验与 close reading，没有重跑物理、Monte Carlo、热响应、轨道或 PIC 计算。峰值瞬时率不等于平均源强，混沌比例不等于壁损失，达到熔点不等于熔池预测，激光质心阻尼也不等于电子束品质已稳定。

## PDF 与解析

4 份 PDF 都通过文件头、类型、字节数、SHA-256、页数和非空布局文本检查，共 16 个抽样页完成渲染和人工查看。MinerU API 接受上传后四个批次均约 10 分钟保持 `pending 0/?`，本地轮询因无超时上限被中止；本轮据技能允许使用 `pdftotext -layout` 与页面渲染 fallback，未把 MinerU 写成成功。
