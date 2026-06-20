# 每日论文雷达（2026-04-12）

## 检索与去重说明

- 检索日期：2026-04-12
- 优先方向：激光等离子体、强场 QED、高能量密度物理、PIC、AI for plasma/HEDP/SFQED
- 检索来源：Nature Portfolio（Communications Physics、Scientific Reports）正式论文页面与 DOI 页面
- 去重基线：`state/processed_articles.json` + 历史 `daily/*/index.md`
- 去重规则：DOI > 规范化标题 > 来源链接/PDF 链接
- 结果：筛得 2 篇“历史未收录 DOI”的高相关正式论文（均为 Open Access）

## 今日新增论文索引

### 1) A procedure for rule extraction from a Self-Organising plasma disruption predictor for JET

- 标题：A procedure for rule extraction from a Self-Organising plasma disruption predictor for JET
- 作者：Samuele Setzu, Enrico Aymerich, Alessandra Fanni, Fabio Pisano, Giuliana Sias, Barbara Cannas, The JET contributors, WPTE Team
- 期刊/平台：Scientific Reports
- DOI：10.1038/s41598-026-38318-9
- 真实发表日期：2026-04-10
- 来源链接：https://www.nature.com/articles/s41598-026-38318-9
- PDF 文件名：`Setzu et al. - 2026 - A procedure for rule extraction from a Self-Organising plasma disruption predictor for JET.pdf`
- 下载状态：失败（网络限制，见下）
- 影响因子分：6.5/10（依据：Scientific Reports 为综合 OA 期刊，影响力中等）
- 专业相似度分：7.5/10（AI + 等离子体破裂预测，直接对应“AI for plasma”）
- 推荐理由：工作重点在可解释 AI（规则提取）用于托卡马克破裂预测，兼顾模型性能与物理可解释性，对等离子体控制策略和数据驱动诊断流程有参考意义。
- 一句话总结：该文提出从自组织破裂预测器中提取规则的方法，提升了聚变等离子体破裂预警模型的可解释性。

### 2) Accelerating atomic fine structure determination with graph reinforcement learning

- 标题：Accelerating atomic fine structure determination with graph reinforcement learning
- 作者：Minghui Ding, V.-A. Darvariu, A. N. Ryabtsev, et al.
- 期刊/平台：Communications Physics
- DOI：10.1038/s42005-026-02582-y
- 真实发表日期：2026-03-19
- 来源链接：https://www.nature.com/articles/s42005-026-02582-y
- PDF 文件名：`Ding et al. - 2026 - Accelerating atomic fine structure determination with graph reinforcement learning.pdf`
- 下载状态：失败（网络限制，见下）
- 影响因子分：7.5/10（依据：Communications Physics 领域声誉较高、方法学影响力较强）
- 专业相似度分：6.5/10（AI + 原子结构反演，对高能密度/等离子体光谱诊断有方法迁移价值）
- 推荐理由：将图强化学习用于复杂原子精细结构反演，属于“先进算法赋能等离子体相关诊断”的代表路径，可为 HEDP 光谱反演与参数估计提供可迁移思路。
- 一句话总结：该文用图强化学习显著加速原子精细结构确定流程，为复杂谱学问题提供了数据驱动求解框架。

## 下载执行记录（严格使用 safe_pdf_download.py）

- 执行命令 1：
  - `python scripts/safe_pdf_download.py --url 'https://www.nature.com/articles/s41598-026-38318-9.pdf' --doi '10.1038/s41598-026-38318-9' --output 'daily/2026-04-12/pdfs/Setzu et al. - 2026 - A procedure for rule extraction from a Self-Organising plasma disruption predictor for JET.pdf'`
- 结果 1：失败
- 失败原因 1：
  - 代理链路不可达（`127.0.0.1:1087` 被沙箱阻止）
  - 直连 DNS 解析失败（`www.nature.com`、`doi.org`）

- 执行命令 2：
  - `python scripts/safe_pdf_download.py --url 'https://www.nature.com/articles/s42005-026-02582-y.pdf' --doi '10.1038/s42005-026-02582-y' --output 'daily/2026-04-12/pdfs/Ding et al. - 2026 - Accelerating atomic fine structure determination with graph reinforcement learning.pdf'`
- 结果 2：失败
- 失败原因 2：
  - 代理链路不可达（`127.0.0.1:1087` 被沙箱阻止）
  - 直连 DNS 解析失败（`www.nature.com`、`doi.org`）

## 笔记生成状态（research-paper-explainer）

- 今日成功下载 PDF：0
- 今日成功生成笔记：0
- 说明：按 `research-paper-explainer` 工作流，仅对“成功下载并可读取全文”的论文执行 PDF→Markdown 转换与中文结构化笔记生成；本次未满足前置条件。

## 当日综合总结

- 今天论文的共同趋势：
  - 今日新增论文集中在“AI/先进算法与等离子体相关问题结合”，从可解释破裂预测到图强化学习反演，体现出“物理约束 + 数据驱动”的方法演进。
- 关键理论/算法/实验方向：
  - 可解释机器学习（rule extraction）在聚变破裂预测中的落地；
  - 图强化学习用于高维谱学参数/精细结构求解，服务等离子体诊断与反演。
- 对你当前研究最值得优先阅读的 1-3 篇论文及原因：
  - `10.1038/s41598-026-38318-9`：直接对应等离子体控制与可解释预测，利于方法迁移到实验在线预警；
  - `10.1038/s42005-026-02582-y`：在“先进算法加速物理反演”上有代表性，可迁移到 HEDP/SFQED 光谱诊断场景。
- AI/机器学习方法新结合点：
  - 出现了“可解释 AI + 等离子体控制”和“图强化学习 + 原子谱学反演”两条可迁移路线，但尚未看到直接面向 SFQED/PIC 主流程的端到端新框架。
