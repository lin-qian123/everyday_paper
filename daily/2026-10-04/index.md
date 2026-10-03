# 每日论文索引 - 2026-10-04

## 今日概览

- 运行日期：2026-10-04
- 新增论文数：1（Springer 正式 version of record）
- 最新性：官方 arXiv 目标分类最新仍为 2026-10-02 公告批次；Crossref 2026-10-03 至 10-04 的 6 组主题检索共返回 422 条元数据、336 条去重作品，新增 1 篇高相关正式论文。
- 主题：CSNS Back-n 白中子源上的 ¹⁹⁷Au(n,γ) 俘获产额、共振参数、截面与 Maxwell 平均截面（MACS）。
- 去重：按 DOI、规范化标题、407 条完成台账、21 条重试队列、历史 `daily/`、摘要和物理场景检查；本篇为新作品，未引入重复。
- PDF / 正文：Springer 正式 PDF 通过 `%PDF-`、`file`、`pdfinfo`、SHA-256 与非空 `pdftotext -layout`；11 页全部渲染并人工查看。MinerU 完成 11/11 页解析，仅结果 ZIP 因服务端 CDN 证书过期改用 `curl` 传输回退，ZIP 完整性通过。
- 重试：21 条既有来源受限记录无新的合法全文信号，队列不变。
- 覆盖边界：这是定向增量筛选，不宣称穷尽所有期刊或数据库。

## 论文清单

### 1. New measurement of the 197Au(n, γ) cross section at the CSNS Back-n white neutron facility

- 标识符：[DOI: 10.1007/s41365-026-02072-4](https://doi.org/10.1007/s41365-026-02072-4)
- 在线发表：2026-10-03
- 期刊 / 版本：*Nuclear Science and Techniques* 37, 233 (2026)；Springer 正式 version of record
- 本地 PDF：`daily/2026-10-04/pdfs/Cui et al. - 2026 - Au197 neutron capture cross section.pdf`
- 中文笔记：[Cui et al. - 2026 - Au197 neutron capture cross section.md](notes/Cui%20et%20al.%20-%202026%20-%20Au197%20neutron%20capture%20cross%20section.md)
- 来源影响力分：8/10
- 专业相似度分：8/10
- 推荐理由：直接白中子俘获实验，把 TOF、双束团展开、PHWT、分项本底、R-matrix 和 MACS 连成可审计的诊断链，对激光驱动宽谱中子的 Au 活化/俘获诊断有方法学参考。
- 一句话总结：`0.5 eV–300 keV` 俘获产额的平均总不确定度约 `5.9%`，`30 keV` MACS 为 `628±38 mb`；但俘获截面借用 ENDF/B-VIII.1 总截面，不能写成完全独立的绝对截面测量。

## 当日综合总结

- 本轮优先收录可验证的正式新文，没有为填充数量重复处理 2026-10-02 已筛选的 arXiv 批次。
- 论文对 `151.4、534.2、738.7、1822.7 eV` 等共振给出超过 `30%` 的俘获核偏差，说明 eV–keV 慢化谱诊断需显式传播评价库版本和核数据不确定度。
- 本文不是激光驱动中子实验；没有激光—靶、pitcher/catcher、EMP 或逐发源波动数据，因此只能作为核数据与诊断方法基准。
