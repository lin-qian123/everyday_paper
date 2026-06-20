# 2026-03-26 论文索引

## 今日概览

- 运行日期：2026-03-26
- 新增论文数：0（未满足“成功下载并可打开正文 PDF”的入库条件）
- 检索主题：激光等离子体、强场 QED、高能量密度物理、PIC、机器学习/先进算法在相关方向中的应用
- 检索来源：Nature/Communications Physics 官方论文页、DOI 页面、arXiv 当日列表页
- 总体判断：今天筛到 3 篇高质量新候选（2 篇正式期刊 + 1 篇高相关预印本），但当前环境网络限制导致 PDF 下载全部失败，因此未进入“已处理入库”。

## 今日高质量候选（未纳入）

### 1) Super light-by-light scattering in vacuum induced by intense vortex lasers

- 类型：正式期刊
- 作者：Zhigang Bu, Lingang Zhang, Shiyu Liu, et al.
- 期刊 / 平台：Communications Physics
- DOI：https://doi.org/10.1038/s42005-026-02556-0
- 真实发表日期：2026-03-10
- 来源链接：https://www.nature.com/articles/s42005-026-02556-0
- PDF 文件名（目标）：`Bu et al. - 2026 - Super light-by-light scattering in vacuum induced by intense vortex lasers.pdf`
- 影响因子分：`8/10`（Communications Physics 正式发表，物理方向同行评审可靠）
- 专业相似度分：`9/10`（强场 QED + 超强激光 + 真空非线性效应，与强场主线高度相关）
- 推荐理由：提出利用涡旋超强激光与 XFEL 碰撞实现真空光-光散射增强，直接面向强场 QED 可观测性。
- 一句话总结：该文给出“超光-光散射”机制与可实验化方案，提升真空极化信号可探测性。
- 未纳入原因：`safe_pdf_download.py` 在代理与直连模式均失败（代理不可达 + DNS 解析失败）。

### 2) High average-flux laser-driven neutron source

- 类型：正式期刊
- 作者：Simon Vallieres, Francois Fillion-Gourdeau, Sylvain Fourmaux, et al.
- 期刊 / 平台：Nature Communications
- DOI：https://doi.org/10.1038/s41467-025-66535-9
- 真实发表日期：2025-11-20
- 来源链接：https://www.nature.com/articles/s41467-025-66535-9
- PDF 文件名（目标）：`Vallieres et al. - 2025 - High average-flux laser-driven neutron source.pdf`
- 影响因子分：`9/10`（Nature Communications 正式发表，HEDP/激光等离子体交叉影响力高）
- 专业相似度分：`8/10`（LWFA 电子束 + 光核反应中子源，贴合高能量密度与激光等离子体应用）
- 推荐理由：报告高重复频率下的高平均通量激光驱动中子源，并与 TNSA 路线同台比较，工程参考价值高。
- 一句话总结：该文将 LWFA 电子束驱动光核反应推进到高通量稳定运行区间，显著提升应用可行性。
- 未纳入原因：`safe_pdf_download.py` 在代理与直连模式均失败（代理不可达 + DNS 解析失败）。

### 3) CMA-Unfold: A Covariance Matrix Adaptation unfolding algorithm for stacked calorimeter detectors

- 类型：预印本
- 作者：G. Fauvel, A. Arefiev, M. Manuel, et al.
- 期刊 / 平台：arXiv (physics.plasm-ph)
- DOI：https://doi.org/10.48550/arXiv.2603.22930
- 真实发表日期：2026-03-25（arXiv 提交日期）
- 来源链接：https://arxiv.org/abs/2603.22930
- PDF 文件名（目标）：`Fauvel et al. - 2026 - CMA-Unfold A Covariance Matrix Adaptation unfolding algorithm for stacked calorimeter detectors.pdf`
- 影响因子分：`6/10`（预印本，尚未正式同行评审）
- 专业相似度分：`8/10`（面向 ICF/超强激光实验诊断反演，属于先进算法在 HEDP 问题的直接应用）
- 推荐理由：以 CMA-ES 做堆叠量热探测器谱反演，兼顾噪声鲁棒性与模型灵活性，对实验数据反演流程有直接价值。
- 一句话总结：该预印本提供了面向激光等离子体高能辐射诊断的稳健谱反演算法框架。
- 未纳入原因：`safe_pdf_download.py` 在代理与直连模式均失败（代理不可达 + DNS 解析失败）。

## 当日综合总结

- 今天论文的共同趋势：
  - 一条主线是“更可观测的极端场物理信号”（真空非线性 QED）；另一条主线是“更可用的激光驱动粒子/中子源”；同时出现“面向实验诊断反演的先进优化算法”。
- 关键理论/算法/实验方向：
  - 理论与方案：强场 QED 真空效应的可探测几何与动量分离设计。
  - 实验与装置：LWFA 驱动高重复频中子源，强调平均通量与稳定性指标。
  - 算法与计算：CMA-ES 用于高能诊断反演，体现“先进算法 + HEDP 实验链路”的结合。
- 本仓库方向下最值得优先阅读的 1-3 篇论文及原因：
  - 1) `10.1038/s42005-026-02556-0`：最直接对应强场 QED 与超强激光实验可观测性。
  - 2) `10.1038/s41467-025-66535-9`：对激光等离子体驱动二次源的工程化路线最具参考意义。
  - 3) `10.48550/arXiv.2603.22930`：在本仓库关注的“机器学习/先进算法 + 等离子体/HEDP”交叉点上最实用。
- 机器学习方法新结合点：
  - 今日候选中，`CMA-Unfold` 显示了演化优化（CMA-ES）在激光等离子体实验反演中的直接落地，属于方法学层面的新结合点。

## 执行记录

- 已创建目录：`daily/2026-03-26/pdfs/`、`daily/2026-03-26/notes/`
- 下载执行：严格使用 `python scripts/safe_pdf_download.py --url <候选URL> --doi <DOI> --output <pdf路径>`。
- 下载结果：3/3 失败（环境网络限制：代理不可达 + 直连 DNS 失败）。
- `research-paper-explainer` 流程状态：未触发（无 PDF 成功下载）；`MINERU_API_KEY` 当前为未设置。
- `state/processed_articles.json`：未修改（无新增可入库条目）。
