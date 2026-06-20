# 2026-03-28 论文索引

## 今日概览

- 运行日期：2026-03-28
- 新增论文数：0（未满足“成功下载并可打开正文 PDF”的入库条件）
- 检索主题：激光等离子体、强场 QED、高能量密度物理、PIC、机器学习/先进算法在相关方向中的应用
- 去重基线：已读取 `state/processed_articles.json` 与历史 `daily/` 目录

## 今日候选（均因下载失败未入库）

### 候选 A
- 标题：Super light-by-light scattering in vacuum induced by intense vortex lasers
- 作者：Yihe Bu et al.
- 期刊/平台：Communications Physics
- DOI：https://doi.org/10.1038/s42005-026-02556-0
- 真实发表日期：2026-03-10
- 来源链接：https://www.nature.com/articles/s42005-026-02556-0
- 目标 PDF 文件名：`Bu et al. - 2026 - Super light-by-light scattering in vacuum induced by intense vortex lasers.pdf`
- 影响因子分：8/10（依据：Nature Portfolio 子刊 Communications Physics，领域认可度高）
- 专业相似度分：9/10（强场 QED + 高强激光真空非线性过程）
- 推荐理由：直接对接强场 QED 主线，且实验/理论参数窗口与超强激光平台相关。
- 一句话总结：研究强涡旋激光驱动下真空光-光散射增强机制，指向可实验验证的 SFQED 非线性效应。

### 候选 B
- 标题：Multi-messenger dynamic imaging of laser-driven shocks in water using a plasma wakefield accelerator
- 作者：Mario D. Balcazar et al.
- 期刊/平台：Nature Communications
- DOI：https://doi.org/10.1038/s41467-025-67224-3
- 真实发表日期：2026-02-14
- 来源链接：https://www.nature.com/articles/s41467-025-67224-3
- 目标 PDF 文件名：`Balcazar et al. - 2026 - Multi-messenger dynamic imaging of laser-driven shocks in water using a plasma wakefield accelerator.pdf`
- 影响因子分：9/10（依据：Nature Communications 综合影响力高）
- 专业相似度分：8/10（激光驱动冲击波 + 等离子体尾场加速诊断）
- 推荐理由：对 HEDP 冲击动力学诊断和激光等离子体实验方法学都有直接参考价值。
- 一句话总结：将 PWFA 作为超快探针用于激光驱动冲击成像，强化了 HEDP 多信使诊断路线。

### 候选 C
- 标题：Growth Rate of Self-Sustained QED Cascades Induced by Intense Lasers
- 作者：A. Mercuri-Baron et al.
- 期刊/平台：Physical Review X
- DOI：https://doi.org/10.1103/PhysRevX.15.011062
- 真实发表日期：2025-03-18
- 来源链接：https://journals.aps.org/prx/abstract/10.1103/PhysRevX.15.011062
- 目标 PDF 文件名：`Mercuri-Baron et al. - 2025 - Growth Rate of Self-Sustained QED Cascades Induced by Intense Lasers.pdf`
- 影响因子分：9/10（依据：PRX 为 APS 顶级综合期刊）
- 专业相似度分：10/10（强场 QED 级联增长率核心问题）
- 推荐理由：对 SFQED 级联可观测性、参数扫描与 QED-PIC 设计有直接指导。
- 一句话总结：给出强激光诱导自持 QED 级联增长率的一般解，能直接指导实验窗口优化。

## 今日检索与下载执行记录

- 目录创建：`daily/2026-03-28/pdfs/`、`daily/2026-03-28/notes/`。
- 已按要求使用下载命令（3 次）：
  - `python scripts/safe_pdf_download.py --url https://www.nature.com/articles/s42005-026-02556-0.pdf --doi 10.1038/s42005-026-02556-0 --output daily/2026-03-28/pdfs/Bu et al. - 2026 - Super light-by-light scattering in vacuum induced by intense vortex lasers.pdf`
  - `python scripts/safe_pdf_download.py --url https://www.nature.com/articles/s41467-025-67224-3.pdf --doi 10.1038/s41467-025-67224-3 --output daily/2026-03-28/pdfs/Balcazar et al. - 2026 - Multi-messenger dynamic imaging of laser-driven shocks in water using a plasma wakefield accelerator.pdf`
  - `python scripts/safe_pdf_download.py --url https://journals.aps.org/prx/pdf/10.1103/PhysRevX.15.011062 --doi 10.1103/PhysRevX.15.011062 --output daily/2026-03-28/pdfs/Mercuri-Baron et al. - 2025 - Growth Rate of Self-Sustained QED Cascades Induced by Intense Lasers.pdf`
- 失败原因一致：
  - 代理链路失败：`127.0.0.1:1087` 不可达（`Operation not permitted`）
  - 直连失败：`doi.org` / `nature.com` / `journals.aps.org` DNS 解析失败（`NameResolutionError`）
- PDF 实际下载结果：0/3 成功。
- `research-paper-explainer` 流程：未触发（无可用 PDF 输入）。

## 当日综合总结

- 今天论文的共同趋势：
  - 候选均围绕“超强激光驱动下的高场非线性过程 + 高时空分辨诊断/建模”。
- 关键理论/算法/实验方向：
  - 理论：SFQED 级联增长率与真空非线性散射。
  - 实验：激光驱动冲击与多信使动态成像。
  - 方法：面向 QED-PIC 参数优化的可计算增长率模型。
- 对我当前研究最值得优先阅读的 1-3 篇论文及原因：
  - 1) `10.1103/PhysRevX.15.011062`：SFQED 级联理论主干，最直接服务强场 QED/PIC 建模。
  - 2) `10.1038/s42005-026-02556-0`：强激光真空非线性前沿，契合高场实验可验证问题。
  - 3) `10.1038/s41467-025-67224-3`：HEDP 诊断与加速器结合路径，对实验设计参考价值高。
- 机器学习方法是否在相关方向出现新的结合点：
  - 今日候选未出现新增 机器学习 主体论文；更偏向高场理论与诊断实验。

## 状态文件更新

- `state/processed_articles.json`：未追加新条目（因 0 篇成功下载并生成笔记）。
