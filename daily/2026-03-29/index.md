# 2026-03-29 论文索引

## 今日概览

- 运行日期：2026-03-29
- 新增论文数：0（未满足“成功下载并可打开正文 PDF”的入库条件）
- 检索主题：激光等离子体、强场 QED、高能量密度物理、PIC、AI/先进算法在相关方向中的应用
- 去重基线：已读取 `state/processed_articles.json`（23 条）与历史 `daily/` 索引（额外提取 DOI/标题/来源链接）
- 去重后候选策略：仅保留历史索引未出现的新 DOI，优先正式期刊页面与 DOI 页面

## 今日候选（均因下载失败未入库）

### 候选 A
- 标题：Revisiting self-seeding mechanism by generating vector ultraviolet N2+ lasing
- 作者：Jingsong Gao et al.
- 期刊/平台：Communications Physics（正式期刊）
- DOI：https://doi.org/10.1038/s42005-026-02535-5
- 真实发表日期：2026-02-11（Version of record: 2026-03-20）
- 来源链接：https://www.nature.com/articles/s42005-026-02535-5
- PDF 文件名（目标）：`Gao et al. - 2026 - Revisiting self-seeding mechanism by generating vector ultraviolet N2+ lasing.pdf`
- 影响因子分：8/10（Nature Portfolio 子刊 Communications Physics，正式同行评审）
- 专业相似度分：7/10（强激光场驱动等离子体/离子激光过程，贴近强场方向但非直接 SFQED 主问题）
- 推荐理由：聚焦强场驱动下的分子离子增益与矢量紫外激光机制，对强场光物理与激光等离子体诊断有参考价值。
- 一句话总结：文章重新审视强场空气激光的自播种机理，并给出矢量紫外 N2+ 激光的实验与模型框架。

### 候选 B
- 标题：Generation of vacuum ultraviolet vortex beams via near-threshold harmonics in argon gas driven by infrared Laguerre-Gaussian lasers
- 作者：Jiaxin Han et al.
- 期刊/平台：Communications Physics（正式期刊）
- DOI：https://doi.org/10.1038/s42005-026-02579-7
- 真实发表日期：2026-03-10
- 来源链接：https://www.nature.com/articles/s42005-026-02579-7
- PDF 文件名（目标）：`Han et al. - 2026 - Generation of vacuum ultraviolet vortex beams via near-threshold harmonics in argon gas.pdf`
- 影响因子分：8/10（Nature Portfolio 子刊正式发表）
- 专业相似度分：7/10（强场高次谐波与超快源方向相关，间接服务强场实验平台）
- 推荐理由：在强场驱动的近阈值谐波与轨道角动量光场耦合方面提供了可转移方法，对超快强场诊断光源设计有启发。
- 一句话总结：该文提出台式真空紫外涡旋光束生成方案，结合强场驱动与时频分析揭示谐波形成机制。

### 候选 C
- 标题：Laser-driven annular shock waves as laboratory analogues of wCDM cosmologies and cosmological gravitational waves
- 作者：Felipe A. Asenjo et al.
- 期刊/平台：Communications Physics（正式期刊）
- DOI：https://doi.org/10.1038/s42005-026-02570-2
- 真实发表日期：2026-03-04
- 来源链接：https://www.nature.com/articles/s42005-026-02570-2
- PDF 文件名（目标）：`Asenjo et al. - 2026 - Laser-driven annular shock waves as laboratory analogues of wCDM cosmologies.pdf`
- 影响因子分：8/10（Nature Portfolio 子刊正式发表）
- 专业相似度分：8/10（激光驱动冲击波与 HEDP 实验路径直接相关）
- 推荐理由：虽然应用场景偏类宇宙学模拟，但核心实验对象是激光驱动等离子体冲击波，对 HEDP 冲击动力学与诊断仍具方法学价值。
- 一句话总结：利用激光驱动环形冲击波构建实验类比系统，展示了可映射到多组分宇宙学演化的冲击动力学行为。

## 今日检索与下载执行记录

- 目录创建：`daily/2026-03-29/pdfs/`、`daily/2026-03-29/notes/`。
- 已严格按约束执行 PDF 下载（3 次）：
  - `python scripts/safe_pdf_download.py --url https://www.nature.com/articles/s42005-026-02535-5 --doi 10.1038/s42005-026-02535-5 --output daily/2026-03-29/pdfs/Gao et al. - 2026 - Revisiting self-seeding mechanism by generating vector ultraviolet N2+ lasing.pdf`
  - `python scripts/safe_pdf_download.py --url https://www.nature.com/articles/s42005-026-02579-7 --doi 10.1038/s42005-026-02579-7 --output daily/2026-03-29/pdfs/Han et al. - 2026 - Generation of vacuum ultraviolet vortex beams via near-threshold harmonics in argon gas.pdf`
  - `python scripts/safe_pdf_download.py --url https://www.nature.com/articles/s42005-026-02570-2 --doi 10.1038/s42005-026-02570-2 --output daily/2026-03-29/pdfs/Asenjo et al. - 2026 - Laser-driven annular shock waves as laboratory analogues of wCDM cosmologies.pdf`
- 失败原因一致：
  - 代理模式失败：`127.0.0.1:1087` 不可达（`Operation not permitted`）
  - 直连模式失败：`www.nature.com` / `doi.org` DNS 解析失败（`NameResolutionError`）
- PDF 下载与校验结果：0/3 成功。
- `research-paper-explainer` 工作流状态：未触发（无可用 PDF 输入）；当前环境 `MINERU_API_KEY` 未设置。

## 当日综合总结

- 今天论文的共同趋势：
  - 候选集中在“强激光驱动下的非线性辐射/增益机制”与“激光驱动冲击波高能量密度实验”两条线。
- 关键理论/算法/实验方向：
  - 理论与机制：强场谐波与涡旋光场耦合、空气激光自播种增益机制。
  - 实验方向：激光驱动冲击波时空演化与实验类比平台。
  - 计算/算法：本轮候选未出现新的 AI/PIC 主体方法论文（相较前几日已检索过的 Bayesian/PIC 方向，今天无新增未重复条目）。
- 对我当前研究最值得优先阅读的 1-3 篇论文及原因（在网络恢复后建议优先）：
  - 1) `10.1038/s42005-026-02570-2`：与激光驱动冲击波和 HEDP 直接相关，实验可借鉴性强。
  - 2) `10.1038/s42005-026-02579-7`：强场驱动谐波与超快光源设计，对高场诊断工具链有潜在价值。
  - 3) `10.1038/s42005-026-02535-5`：强场离子激光增益机理可为强场实验诊断提供补充视角。
- AI / 机器学习方法是否在相关方向出现新的结合点：
  - 今日新增未重复候选中未出现明确 AI/ML 主体方法论文。

## 状态文件更新

- `state/processed_articles.json`：未追加新条目（0 篇成功下载并生成笔记）。
