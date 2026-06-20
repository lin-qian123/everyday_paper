# 2026-03-30 论文索引

## 今日概览

- 运行日期：2026-03-30
- 新增论文数：0（未满足“成功下载并可打开正文 PDF”的入库条件）
- 检索主题：激光等离子体、强场 QED、高能量密度物理、PIC、AI/先进算法在相关方向中的应用
- 去重基线：`state/processed_articles.json` + 历史 `daily/*/index.md`（按 DOI、规范化标题、来源链接去重）
- 去重结果：以下 3 篇为“历史未收录 DOI”的新增候选

## 今日候选（均因下载失败未入库）

### 候选 A
- 标题：Stable laser-acceleration of high-flux proton beams with plasma collimation
- 作者：M. J. V. Streeter et al.
- 期刊/平台：Nature Communications（正式期刊）
- DOI：https://doi.org/10.1038/s41467-025-56248-4
- 真实发表日期：2024-07-19
- 来源链接：https://www.nature.com/articles/s41467-025-56248-4
- PDF 文件名（目标）：`Streeter et al. - 2025 - Stable laser-acceleration of high-flux proton beams with plasma collimation.pdf`
- 影响因子分：9/10（Nature Communications，领域影响力高）
- 专业相似度分：9/10（激光驱动质子束与激光等离子体加速核心问题高度相关）
- 推荐理由：在高重复频率与低发散质子束稳定产生上给出实验突破，直接关联激光等离子体束流可用性。
- 一句话总结：工作展示了水片靶条件下高稳定、低发散的多 MeV 质子束，为高重复激光质子源应用提供关键路径。

### 候选 B
- 标题：Emittance preservation in a plasma-wakefield accelerator
- 作者：C. A. Lindstrom et al.
- 期刊/平台：Nature Communications（正式期刊）
- DOI：https://doi.org/10.1038/s41467-024-50320-1
- 真实发表日期：2024-07-19
- 来源链接：https://www.nature.com/articles/s41467-024-50320-1
- PDF 文件名（目标）：`Lindstrom et al. - 2024 - Emittance preservation in a plasma-wakefield accelerator.pdf`
- 影响因子分：9/10（Nature Communications，正式同行评审）
- 专业相似度分：8/10（PWFA 束流品质保持与等离子体加速器工程化强相关）
- 推荐理由：聚焦发射度保持这一决定后续光源/高能应用可行性的核心指标，方法对 LPA/PWFA 设计均具参考性。
- 一句话总结：文章证明了在高梯度等离子体尾场加速中可保持束流发射度，推进高品质束流应用落地。

### 候选 C
- 标题：Data-driven beam diagnostics using betatron radiation
- 作者：M. D. Lindstrom et al.
- 期刊/平台：Plasma Physics and Controlled Fusion（正式期刊）
- DOI：https://doi.org/10.1088/1361-6587/ae3eb3
- 真实发表日期：2026-03-23
- 来源链接：https://iopscience.iop.org/article/10.1088/1361-6587/ae3eb3
- PDF 文件名（目标）：`Lindstrom et al. - 2026 - Data-driven beam diagnostics using betatron radiation.pdf`
- 影响因子分：7/10（PPCF 为等离子体领域主流期刊）
- 专业相似度分：8/10（AI/数据驱动诊断与等离子体加速束流表征直接耦合）
- 推荐理由：将数据驱动方法用于 betatron 辐射束诊断，契合“AI + 等离子体加速诊断”优先方向。
- 一句话总结：该文以数据驱动方法提升 betatron 辐射诊断能力，为高重复实验下在线束流表征提供可迁移路线。

## 今日检索与下载执行记录

- 目录创建：`daily/2026-03-30/pdfs/`、`daily/2026-03-30/notes/`。
- 新候选去重检查：上述 3 篇 DOI 未出现在历史索引或 `processed_articles.json`。
- 已严格按约束执行 PDF 下载（均使用指定脚本）：
  - `python scripts/safe_pdf_download.py --url https://www.nature.com/articles/s41467-025-56248-4 --doi 10.1038/s41467-025-56248-4 --output daily/2026-03-30/pdfs/Streeter et al. - 2025 - Stable laser-acceleration of high-flux proton beams with plasma collimation.pdf`
  - `python scripts/safe_pdf_download.py --url https://www.nature.com/articles/s41467-024-50320-1 --doi 10.1038/s41467-024-50320-1 --output daily/2026-03-30/pdfs/Lindstrom et al. - 2024 - Emittance preservation in a plasma-wakefield accelerator.pdf`
  - `python scripts/safe_pdf_download.py --url https://iopscience.iop.org/article/10.1088/1361-6587/ae3eb3 --doi 10.1088/1361-6587/ae3eb3 --output daily/2026-03-30/pdfs/Lindstrom et al. - 2026 - Data-driven beam diagnostics using betatron radiation.pdf`
- 失败原因一致：
  - 代理模式失败：`127.0.0.1:1087` 不可达（`Operation not permitted`）
  - 直连模式失败：`www.nature.com`、`iopscience.iop.org`、`doi.org` DNS 解析失败（`NameResolutionError`）
- 下载与校验结果：0/3 成功。
- `research-paper-explainer` 工作流状态：未触发（无可用 PDF 输入，无法先执行 `convert_mineru.py`）。

## 当日综合总结

- 今天论文的共同趋势：
  - 激光/尾场加速研究继续从“能量提升”向“束流品质可控与稳定运行”转移；
  - 数据驱动方法正在进入等离子体加速诊断环节，强调高重复率实验下的实时可用性。
- 关键理论/算法/实验方向：
  - 实验：高重复率低发散质子束、等离子体尾场中的发射度保持。
  - 诊断与算法：betatron 辐射数据驱动反演/诊断。
  - 方法学：从单次演示转向可重复与可集成的加速器链路指标（稳定性、亮度、发射度）。
- 对你当前研究最值得优先阅读的 1-3 篇论文及原因：
  - 1) `10.1038/s41467-025-56248-4`：激光质子源稳定性和准直性能显著，最贴近激光等离子体应用落地。
  - 2) `10.1038/s41467-024-50320-1`：束流发射度保持是高质量等离子体加速器的核心门槛。
  - 3) `10.1088/1361-6587/ae3eb3`：AI/数据驱动诊断路线直接服务于高通量实验优化闭环。
- AI / 机器学习结合点：
  - 今日新增候选中，`10.1088/1361-6587/ae3eb3` 明确体现了 AI/数据驱动与等离子体加速诊断的实用结合。

## 状态文件更新

- `state/processed_articles.json`：未追加新条目（0 篇成功下载并完成笔记）。
