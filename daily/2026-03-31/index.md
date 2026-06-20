# 2026-03-31 论文索引

## 今日概览

- 运行日期：2026-03-31
- 新增论文数：0（未满足“成功下载并可打开正文 PDF”的入库条件）
- 检索主题：激光等离子体、强场 QED、高能量密度物理、PIC、机器学习/先进算法在相关方向中的应用
- 去重基线：`state/processed_articles.json` + 历史 `daily/*/index.md`（按 DOI、规范化标题、来源链接去重）
- 去重结果：以下 3 篇为“历史未收录 DOI”的新增候选

## 今日候选（均因下载失败未入库）

### 候选 A
- 标题：Time-resolved X-ray imaging of the current filamentation instability in solid-density plasmas
- 作者：Christopher Schoenwaelder et al.
- 期刊/平台：Nature Communications（正式期刊）
- DOI：https://doi.org/10.1038/s41467-025-67160-2
- 真实发表日期：2026-01-09
- 来源链接：https://www.nature.com/articles/s41467-025-67160-2
- PDF 文件名（目标）：`Schoenwaelder et al. - 2026 - Time-resolved X-ray imaging of the current filamentation instability in solid-density plasmas.pdf`
- 影响因子分：9/10（Nature Communications，HEDP/激光等离子体相关实验影响力高）
- 专业相似度分：8/10（固体密度等离子体丝化不稳定性与激光等离子体/HEDP 直接相关）
- 推荐理由：提供高时空分辨率成像与动力学演化信息，对激光固体相互作用与不稳定性建模校验价值高。
- 一句话总结：该工作直接解析了固体密度等离子体中电流丝化不稳定性演化，为 HEDP 实验-模拟闭环提供关键观测。

### 候选 B
- 标题：Batch Bayesian optimization of attosecond betatron pulses from laser wakefield acceleration
- 作者：Dominika Maslarova et al.
- 期刊/平台：Communications Physics（正式期刊）
- DOI：https://doi.org/10.1038/s42005-026-02542-6
- 真实发表日期：2026-02-18
- 来源链接：https://www.nature.com/articles/s42005-026-02542-6
- PDF 文件名（目标）：`Maslarova et al. - 2026 - Batch Bayesian optimization of attosecond betatron pulses from laser wakefield acceleration.pdf`
- 影响因子分：7/10（Communications Physics，物理方向较高质量开放期刊）
- 专业相似度分：9/10（AI/Bayesian 优化 + LWFA betatron 辐射，命中“机器学习+等离子体加速”优先方向）
- 推荐理由：把批量贝叶斯优化引入激光尾场加速参数搜索，对实验设计与 PIC 参数调优具有可迁移性。
- 一句话总结：文章展示通过密度尖峰与批量贝叶斯优化可显著提升阿秒 betatron 辐射产额。

### 候选 C
- 标题：Kinetic Structure of Strong-Field QED Showers in Crossed Electromagnetic Fields
- 作者：M. Pouyez et al.
- 期刊/平台：Physical Review Letters（正式期刊）
- DOI：https://doi.org/10.1103/PhysRevLett.134.135001
- 真实发表日期：2025-04-04
- 来源链接：https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.134.135001
- PDF 文件名（目标）：`Pouyez et al. - 2025 - Kinetic Structure of Strong-Field QED Showers in Crossed Electromagnetic Fields.pdf`
- 影响因子分：9/10（PRL，强场 QED 方向高影响力）
- 专业相似度分：10/10（强场 QED shower 动力学核心理论，直接匹配研究主题）
- 推荐理由：给出 SFQED shower 的动力学结构与解析标度律，对高强激光-粒子级联建模具有基础价值。
- 一句话总结：该文建立了跨场型可用的强场 QED shower 动力学解析框架，强化了实验可预测标度关系。

## 今日检索与下载执行记录

- 目录创建：`daily/2026-03-31/pdfs/`、`daily/2026-03-31/notes/`。
- 新候选去重检查：上述 3 篇 DOI、规范化标题、来源链接均未出现在历史索引或 `processed_articles.json`。
- 已严格按约束执行 PDF 下载（均使用指定脚本）：
  - `python scripts/safe_pdf_download.py --url https://www.nature.com/articles/s41467-025-67160-2 --doi 10.1038/s41467-025-67160-2 --output daily/2026-03-31/pdfs/Schoenwaelder et al. - 2026 - Time-resolved X-ray imaging of the current filamentation instability in solid-density plasmas.pdf`
  - `python scripts/safe_pdf_download.py --url https://www.nature.com/articles/s42005-026-02542-6 --doi 10.1038/s42005-026-02542-6 --output daily/2026-03-31/pdfs/Maslarova et al. - 2026 - Batch Bayesian optimization of attosecond betatron pulses from laser wakefield acceleration.pdf`
  - `python scripts/safe_pdf_download.py --url https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.134.135001 --doi 10.1103/PhysRevLett.134.135001 --output daily/2026-03-31/pdfs/Pouyez et al. - 2025 - Kinetic Structure of Strong-Field QED Showers in Crossed Electromagnetic Fields.pdf`
- 失败原因一致：
  - 代理模式失败：`127.0.0.1:1087` 不可达（`Operation not permitted`）
  - 直连模式失败：`www.nature.com`、`journals.aps.org`、`doi.org` DNS 解析失败（`NameResolutionError`）
- 下载与校验结果：0/3 成功。
- `research-paper-explainer` 工作流状态：
  - `MINERU_API_KEY` 未配置，且无成功下载的 PDF。
  - 因此未执行 `convert_mineru.py`，今日无新笔记输出。

## 当日综合总结

- 今天论文的共同趋势：
  - 高能量密度与激光等离子体实验持续向“高分辨诊断 + 动力学可解释”推进。
  - 强场 QED 研究继续强化可解析标度律，服务于高功率激光实验参数预估。
  - 机器学习方法从离线分析走向实验设计/参数优化（如批量贝叶斯优化）。
- 关键理论/算法/实验方向：
  - 理论：SFQED shower 的动力学结构与短/长时标解析近似。
  - 实验：固体密度等离子体电流丝化不稳定性的超快成像。
  - 算法：LWFA-betatron 辐射的批量贝叶斯优化。
- 本仓库方向下最值得优先阅读的 1-3 篇论文及原因：
  - 1) `10.1103/PhysRevLett.134.135001`：强场 QED 理论框架完整，直接支撑 SFQED 参数区判定与模型对比。
  - 2) `10.1038/s42005-026-02542-6`：机器学习优化与激光尾场加速深度结合，适合迁移到 PIC 参数寻优与实验调参。
  - 3) `10.1038/s41467-025-67160-2`：HEDP 关键不稳定性得到高时空分辨实验证据，可用于验证模拟与输运模型。
- 机器学习结合点：
  - 今日候选中，`10.1038/s42005-026-02542-6` 是明确的新结合点，强调 batch Bayesian optimization 在激光等离子体辐射增强上的实用潜力。

## 状态文件更新

- `state/processed_articles.json`：未追加新条目（0 篇成功下载并完成笔记）。
