# 2026-03-24 论文索引

## 今日概览

- 运行日期：2026-03-24
- 新增论文数：0（未满足“成功下载并可打开正文 PDF”的入库条件）
- 检索主题：激光等离子体、强场 QED、高能量密度物理、PIC、机器学习用于 plasma
- 检索来源：Communications Physics 官方论文页、DOI 页面
- 总体判断：今天筛到 3 篇与研究方向高度相关的正式期刊论文（Communications Physics，均含 DOI 与明确发表信息），但受本地沙箱网络限制，PDF 下载全部失败，故本次不新增入库。

## 今日高质量候选（未纳入）

### 1) Batch Bayesian optimization of attosecond betatron pulses from laser wakefield acceleration

- 作者：Dominika Maslarova, Albin Hansson, Ming Luo, et al.
- 期刊 / 平台：Communications Physics
- DOI：https://doi.org/10.1038/s42005-026-02542-6
- 真实发表日期：2026-02-18
- 来源链接：https://www.nature.com/articles/s42005-026-02542-6
- PDF 文件名（目标）：`Dominika Maslarova et al. - 2026 - Batch Bayesian optimization of attosecond betatron pulses from laser wakefield acceleration.pdf`
- 影响因子分：`8/10`（Communications Physics 正式发表，期刊影响力与同行评审可靠）
- 专业相似度分：`10/10`（LWFA + 贝叶斯优化 + 阿秒 betatron 辐射调参与优先方向高度重合）
- 推荐理由：直接展示 机器学习优化在激光等离子体加速与辐射源调参中的实用价值，方法可迁移到 PIC 参数扫描和实验自动调参。
- 一句话总结：该文用批量贝叶斯优化在高维参数空间中高效搜索 LWFA 阿秒 betatron 脉冲最优工作点。
- 未纳入原因：`safe_pdf_download.py` 在代理与直连模式均失败（代理不可达 + DNS 解析失败）。

### 2) Demonstration of scissor-cross ionization injection in laser wakefield accelerators

- 作者：Siyu Chen, Guangwei Lu, Xichen Hu, et al.
- 期刊 / 平台：Communications Physics
- DOI：https://doi.org/10.1038/s42005-025-02440-3
- 真实发表日期：2025-12-11（Version of record：2026-01-07）
- 来源链接：https://www.nature.com/articles/s42005-025-02440-3
- PDF 文件名（目标）：`Siyu Chen et al. - 2025 - Demonstration of scissor-cross ionization injection in laser wakefield accelerators.pdf`
- 影响因子分：`8/10`（Communications Physics 正式发表，实验工作完整）
- 专业相似度分：`9/10`（激光等离子体加速、注入机制控制、与 PIC 模拟结合紧密）
- 推荐理由：针对 LWFA 的关键瓶颈“连续注入导致能散变宽”给出实验可验证方案，对束质优化路径有直接参考意义。
- 一句话总结：该文实验验证了 scissor-cross 电离注入，可在保持较高电荷的同时显著改善电子束能散可控性。
- 未纳入原因：`safe_pdf_download.py` 在代理与直连模式均失败（代理不可达 + DNS 解析失败）。

### 3) Properties of pair plasmas emerging from electromagnetic showers in matter

- 作者：M. Pouyez, G. Nicotera, M. Galbiati, et al.
- 期刊 / 平台：Communications Physics
- DOI：https://doi.org/10.1038/s42005-025-02449-8
- 真实发表日期：2025-12-19（Version of record：2026-01-20）
- 来源链接：https://www.nature.com/articles/s42005-025-02449-8
- PDF 文件名（目标）：`M. Pouyez et al. - 2025 - Properties of pair plasmas emerging from electromagnetic showers in matter.pdf`
- 影响因子分：`8/10`（Communications Physics 正式发表，理论+模拟结合）
- 专业相似度分：`9/10`（对强场 QED/对等离子体对偶喷注与实验可达条件评估高度相关）
- 推荐理由：给出了对靶厚、级联长度、粒子发散与密度的可解析标度关系，便于与现有 LWFA 与多拍瓦平台参数对照。
- 一句话总结：该文建立了电磁级联出射对等离子体的解析判据并给出当前/下一代激光平台的可达性边界。
- 未纳入原因：`safe_pdf_download.py` 在代理与直连模式均失败（代理不可达 + DNS 解析失败）。

## 当日综合总结

- 今天论文的共同趋势：
  - 研究主线集中在“激光等离子体加速可控化 + 极端粒子束/辐射源设计优化 + 强场相关级联可达性判据”。
- 关键理论/算法/实验方向：
  - 算法：批量贝叶斯优化（Batch BO）用于 LWFA 辐射源参数空间快速搜索。
  - 实验：双脉冲/斜交触发注入（scissor-cross ionization injection）提高束流品质与可重复性。
  - 理论：电磁级联在物质中产额、发散与等离子体形成条件的解析标度与 Geant4 对照。
- 对我当前研究最值得优先阅读的 1-3 篇论文及原因：
  - 1) `10.1038/s42005-026-02542-6`：机器学习优化与 LWFA 直接耦合，方法迁移价值最高。
  - 2) `10.1038/s42005-025-02440-3`：注入机制实证突破，直接影响高品质电子束获得。
  - 3) `10.1038/s42005-025-02449-8`：对强场相关 pair plasma 实验条件给出可计算判据。
- 机器学习新结合点：
  - 出现“批量贝叶斯优化 + 激光尾场加速辐射源”这一更贴近实验在线优化与 PIC 联合设计的路线。

## 执行记录

- 已创建目录：`daily/2026-03-24/pdfs/`、`daily/2026-03-24/notes/`
- 下载执行：严格使用 `python scripts/safe_pdf_download.py --url <候选URL> --doi <DOI> --output <pdf路径>`，并完成代理/直连自动重试。
- 本次未生成笔记：无 PDF 成功下载，且环境变量 `MINERU_API_KEY` 未设置，未触发 `research-paper-explainer` 的 PDF→Markdown→中文笔记流程。
- `state/processed_articles.json`：未修改（无新增可入库条目）。
