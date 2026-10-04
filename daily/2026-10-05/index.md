# 每日论文索引 - 2026-10-05

## 今日概览

- 运行日期：2026-10-05
- 新增论文数：1（Springer 正式 version of record）
- 最新性：官方 arXiv 目标分类的最新可见提交仍为 2026-10-01、公告批次为 2026-10-02；Crossref 对 2026-10-04 至 10-05 的 6 组主题查询返回 338 条元数据、260 条去重作品，新增 1 篇高相关正式论文。
- 主题：p 型 HPGe γ 谱效率标定、死层优化、源距转移、近场真符合求和（TCS）和 PHITS/Efftran 模型边界。
- 去重：按 DOI、规范化标题、408 条完成台账、21 条重试队列、历史 `daily/`、正式版关系和物理场景检查；本篇为新作品，未引入重复。
- PDF / 正文：Springer 正式 PDF 通过 `%PDF-`、`file`、`pdfinfo`、SHA-256 与非空 `pdftotext -layout`；10 页全部渲染并人工查看，5 张关键嵌图解码。MinerU 对官方 URL 返回 `parsing failed`，故使用本地布局文本和逐页渲染回退。
- 重试：21 条既有来源受限记录无新的合法全文信号，队列不变。
- 覆盖边界：这是定向增量筛选，不宣称穷尽所有期刊或数据库。

## 论文清单

### 1. Precise efficiency calibration of a p-type HPGe detector: dead layer optimization and near-field TCS analysis via PHITS simulation

- 标识符：[DOI: 10.1140/epjp/s13360-026-08383-0](https://doi.org/10.1140/epjp/s13360-026-08383-0)
- 在线发表：2026-10-04
- 期刊 / 版本：*The European Physical Journal Plus* 141, 1130 (2026)；Springer 正式 version of record
- 本地 PDF：`daily/2026-10-05/pdfs/Badague et al. - 2026 - HPGe efficiency calibration PHITS.pdf`
- 中文笔记：[Badague et al. - 2026 - HPGe efficiency calibration PHITS.md](notes/Badague%20et%20al.%20-%202026%20-%20HPGe%20efficiency%20calibration%20PHITS.md)
- 来源影响力分：8/10
- 专业相似度分：7/10
- 推荐理由：把 HPGe 死层、绝对全能峰效率、源距、近场级联符合和模拟残差放到同一条可审计链中，可直接提醒激光驱动 γ / 中子活化诊断不能只搬用厂家几何或远场效率曲线。
- 一句话总结：`1.2 mm` 死层模型在 `≥10.4 cm` 的远场多数达到 `≤5%`；`3.8 cm` 处 Efftran TCS 修正后仍有 `6.51–8.46%` 残差，尚未达到同一准则。

## 当日综合总结

- 本轮优先收录可验证的正式新文，没有重复处理 2026-10-02 已筛选的 arXiv 批次。
- 论文的直接实验是标准源能谱和多距离峰效率；PHITS 几何/死层与 Efftran 符合修正均为模型辅助。本地未运行 PHITS 或 Efftran。
- 表 2 和正文支持的近场未修正最大偏差约为 `14.7%`，与结论中的“超过 `20%`”不一致；索引和笔记均采用可复核的表格值。
- 该工作不是激光等离子体或转换靶实验；用于激光核诊断时仍需重新处理脉冲 pile-up、EMP、prompt-γ、样品自吸收、宽谱激活和逐发源波动。
