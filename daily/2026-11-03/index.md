# 每日论文索引：2026-11-03

新增 **3 篇独立作品**：1 篇正式接收早期版（Article in Press，尚非最终 VOR）和 2 篇近期预印本；台账 **524→527**。四篇新正式候选全文受限，重试 **47→51**，旧对象保持不变。三份经验证 PDF 共 **45 页**，中文笔记、22 个关键页目视核验和 5 幅原始图表／公式摘录已保存。

## 阅读顺序与证据

| 作品与版本 | 重点及边界 | 中文笔记 |
|---|---|---|
| [d–α 辐射俘获热核反应率](https://doi.org/10.1038/s41598-026-78629-5)，11-02 正式接收早期版 | NLO 两体 CEFT 与热平均，非新实验；印刷式(25)与 Table 1 的四点算术不符，图 2 图例／图注交换颜色，等待最终版。 | [Nazari 等](notes/Nazari%20et%20al.%20-%202026%20-%20Deuteron%20alpha%20capture%20reaction%20rate.md) |
| [DHW 弱耦合电子—正电子约化](https://arxiv.org/abs/2610.41623v1)，10-30 提交 | 16→8 相空间分量、BMT 极限；弱场慢尺度解析推导，一般三维电磁真空响应未完成全部积分／重整化，无数值性能结果。 | [Brodin、Lundström](notes/Brodin%20and%20Lundstrom%20-%202026%20-%20Weakly%20coupled%20electron%20positron%20DHW.md) |
| [BO-T 动理学色散求解器](https://arxiv.org/abs/2610.41450v1)，10-30 提交 | 相同极点残差降阶与围道根界；最高 144 倍计时只含矩阵与特征值计算，完整筛选更贵，并有阻尼段／不稳定峰漏选。BO 在此不是贝叶斯优化。 | [Tian 等](notes/Tian%20et%20al.%20-%202026%20-%20BO%20Tian%20kinetic%20dispersion%20solver.md) |

## 检索、版本与去重

- Crossref 十主题，发表日期窗口 **11-01—11-03**，每组前 60 条，共 **600 行／517 唯一 DOI**；七组初次 429 均经顺序补查恢复。只有年月的 11 月卷期日期不当作新在线发表证据。
- 官方 arXiv 十分类 recent 页的首个日期块均为 **11-02**，共 **222 行／205 唯一 ID**；cs.LG 仅覆盖前 100／198 条。公告日期与实际提交日期分开记录，不声称全库穷尽。
- DOI、arXiv ID／别名、规范化标题、作者和物理任务与旧 524 篇及 47 条重试比对；本轮无同作升级或重复入库。两篇预印本精确标题 Crossref 前三未核实正式版。
- 三篇 AIP 受限候选的正确引号短语／题名作者 Atom 查询均为零；最初未加引号的宽 OR 查询已弃用，不作为全文缺失证据。SEB 作者会议页有海报，未将海报冒充期刊全文。
- FLUCS、EDGE2D–EIRENE 代理与 EAST 多任务学习等保留为未读元数据线索，没有生成全文笔记或写入完成台账。

## 全文下载与重试

新增四条，均未取得有效期刊全文、未写摘要笔记：

| 正式候选 | 本轮失败与接续 |
|---|---|
| [直接驱动激光不对称概率模型](https://doi.org/10.1063/5.0349325) | AIP 官方 PDF 代理／直连 403，curl 传输回退仍 403；未核实合法作者全文。 |
| [电子—离子弛豫与尺寸标度](https://doi.org/10.1063/5.0351973) | 同上；检索命中的同作者热传导／能量学旧论文不是这一作品。 |
| [对等离子体通道纵场加速](https://doi.org/10.1063/5.0359075) | 同上；保留正式 DOI 和准确失败，等待作者稿。 |
| [刀口狭缝 SEB 碳离子射程诊断](https://doi.org/10.1088/1748-0221/21/11/C11001) | IOP 代理返回 HTML、直连进入 Radware 验证页；[作者会议海报入口](https://indico.cern.ch/event/1579489/contributions/7084274/)不能替代期刊文章。 |

以上在线日期 11-02 来自 Crossref，尚未用对应 PDF 核实。旧 47 个重试对象完全不变，本轮没有重复全队列探测。Nazari 的常规 `.pdf` 返回 HTML，但页面实际 Download PDF 指向 `_reference.pdf`，通过该公开入口恢复了正式早期全文，不计为重试。

## 核验、发现与接续

三份 PDF 通过 `%PDF-`、文件类型、SHA-256、pdfinfo／pypdf／PyMuPDF 页数一致与全页非空文本检查。MinerU 三项均失败，原因是 **API 401 / A0211 / user token expired**，不属于 PDF 内容或出版商访问失败；本轮明确采用本地全文、独立布局文本与原页渲染回退。早期版公式的提取占位符已回到页面核对，原 PDF 正常显示。

Nazari 的印刷式(25)在四个指定表点与 Table 1 差约 **8.56%、18.10%、98.85%、61.29%**，与文中 1.29% 拟合精度声明不一致；这是印刷式算术核对，未重算 CEFT 积分，也未断言作者实际使用了错误公式。保留[可复现算术脚本](research/check_printed_rate_fit.py)和[记录](research/printed-rate-fit-check.json)，等待作者／最终 VOR 澄清，不自行改系数。

下一轮优先恢复四篇正式全文、确认早期版图例／拟合式，续查 MinerU 凭据状态；BO-T 需完整围道成本与漏模追踪，DHW 需同阶 Maxwell 源与一般电磁场重整化验证。本轮没有复跑作者物理、求解器、训练或实验，未新增激光转换靶—光核中子／核素端到端实测、临床或防护验收。

[PDF 核验](pdf_validation.json) · [下载](download_report.json) · [检索覆盖](research/research-run.json) · [候选快照](research/discovery-candidates.json) · [版本](research/version-checks.json) · [来源](research/sources.jsonl) · [解析失败与回退](research/mineru-attempts.json) · [原图清单](research/figure-manifest.json) · [运行结果](run_results.json)
