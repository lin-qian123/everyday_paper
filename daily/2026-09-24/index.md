# 每日论文索引 - 2026-09-24

## 今日概览

- 运行日期：2026-09-24
- 新增论文数：3（1 篇 2026-09-23 正式 APS 论文，2 篇 2026-09-22 提交并于 2026-09-23 列出的 arXiv 预印本）
- 最新性：官方 arXiv 目标分类已更新到 2026-09-23 批次；正式来源检索覆盖 Crossref 2026-09-21 至 2026-09-24 元数据，并核对 APS、DOI 与 arXiv 单篇页。
- 主题分布：一维 PIC 中非热尾场电子的 Lévy 型能量跳跃；100 Hz OPCPA-LWFA 的 10,000 发束流稳定性；LCS 伽马束下 Ho/Tm 的多重性分辨光中子截面。
- 去重：按 DOI/arXiv identifier、规范化标题、372 条完成台账、18 条结构化重试队列和历史 `daily/` 核对。`10.1103/nc7w-yr34` 从 accepted 阶段的 APS 阻塞项升级为正式发表记录，并由 APS harvest 正式全文端点恢复，重试队列相应减少 1 条。
- PDF / 正文：3 份全文均通过 `%PDF-`、`file`、`pdfinfo`、SHA-256 和非空 `pdftotext -layout`。MinerU 对 3 份官方 PDF URL 均解析失败；APS 替代 URL只解析出机器人验证页，因此没有把该返回记作成功。改用本地文本、页面渲染和人工检查，共保留 17 张关键图。详见 [pdf_validation.json](pdf_validation.json)。
- 来源边界：第一篇是作者 `1D-3V` EPOCH 与分数输运模型；第二篇直接测得 100 Hz LWFA 束流，但 `1 kHz`/FLASH 是展望且最佳 FBPIC 的 Ar 比例与实验差 10 倍；第三篇是 NewSUBARU 储存环 LCS 光核实验，不是 LPA 转换靶中子源。

## 论文清单

### 1. Nonthermal electron acceleration and transition probability density in turbulent wakefields driven by an intense laser pulse

- 标识符：[DOI: 10.1103/nc7w-yr34](https://doi.org/10.1103/nc7w-yr34)
- 发表日期：2026-09-23
- 期刊 / 平台：*Physical Review E* **114**, 035213（正式期刊论文）
- 本地 PDF：`daily/2026-09-24/pdfs/Liu et al. - 2026 - Nonthermal electron acceleration in turbulent wakefields.pdf`
- 中文笔记：[Liu and Kuramitsu - 2026 - Nonthermal wakefield acceleration.md](notes/Liu%20and%20Kuramitsu%20-%202026%20-%20Nonthermal%20wakefield%20acceleration.md)
- 来源影响力分：9/10
- 专业相似度分：9/10
- 推荐理由：把粒子轨迹、能量跳跃 TPD、Lorentzian 重尾和 `α=1` 分数 Fokker–Planck 解连成一条可检查链，并明确区分 Brownian、中能间歇和高能弹道分支。
- 一句话总结：作者的一维 EPOCH 结果在 `200<γ<2000` 形成近 `γ⁻²` 能谱，中能 TPD 在 `|Δγ|≈10²–10³` 近似 `|Δγ|⁻²`；该解释压制横向物理、没有本文新实验，也没有公开数据或二维/三维复现。

### 2. Stable 50 MeV Beams from a 100 Hz Laser-Wakefield Accelerator Driven by an OPCPA Laser

- 标识符：[arXiv:2609.26390](https://arxiv.org/abs/2609.26390)；归档 DOI `10.48550/arXiv.2609.26390`
- 提交日期：2026-09-22（2026-09-23 官方新论文列表）
- 期刊 / 平台：arXiv 预印本
- 本地 PDF：`daily/2026-09-24/pdfs/Smartsev et al. - 2026 - Stable 100 Hz LWFA beams.pdf`
- 中文笔记：[Smartsev et al. - 2026 - Stable 100 Hz LWFA beams.md](notes/Smartsev%20et%20al.%20-%202026%20-%20Stable%20100%20Hz%20LWFA%20beams.md)
- 来源影响力分：8/10
- 专业相似度分：10/10
- 推荐理由：给出连续 10,000 发的真实束流稳定性、仪器分辨率受限的能散上限、慢漂移 PCA，以及与 FBPIC 局域电离注入的机制对照。
- 一句话总结：`70 mJ、8.1 fs` OPCPA 在 `100 Hz` 下产生 `47 MeV、15 pC` 束流，峰值能量 `1.4% rms`、电荷 `12% rms`、本征能散 `95%` 上限 `10% FWHM`；`1 kHz` 未运行，最佳模拟需 `0.1%` Ar 而实验为 `1%`。

### 3. Photoneutron reactions on 165Ho and 169Tm in the giant dipole resonance region

- 标识符：[arXiv:2609.25984](https://arxiv.org/abs/2609.25984)；归档 DOI `10.48550/arXiv.2609.25984`
- 提交日期：2026-09-22（2026-09-23 官方新论文列表）
- 期刊 / 平台：arXiv 预印本
- 本地 PDF：`daily/2026-09-24/pdfs/Gheorghe et al. - 2026 - Ho and Tm photoneutron reactions.pdf`
- 中文笔记：[Gheorghe et al. - 2026 - Ho and Tm photoneutron reactions.md](notes/Gheorghe%20et%20al.%20-%202026%20-%20Ho%20and%20Tm%20photoneutron%20reactions.md)
- 来源影响力分：8/10
- 专业相似度分：9/10
- 推荐理由：直接提供 GDR 区多重性分辨光中子截面与平均中子能，可用于校核伽马谱—核反应—中子产额链中的核数据和探测器响应。
- 一句话总结：NewSUBARU LCS 实验首次系统给出 `¹⁶⁹Tm` 的 `1nX–4nX` 数据，并发现 Ho 旧 Saclay 结果需约 `+0.35 MeV` 移能、Livermore 仍有约 `10%` 强度差；光源不是激光等离子体转换靶，EMPIRE/TALYS 对平均中子能仍有系统偏差。

## 未入库候选与取舍

- `arXiv:2609.25554` 提出以富集 `¹⁵⁰Gd` 两阶段生产医用 `¹⁴⁹Tb`，主题高度相关，但关键 `¹⁵⁰Gd(p,2n)¹⁴⁹Tb` 截面尚待实验测量，剂量与聚变中子供给均为条件化场景；本轮优先收录直接光中子数据。
- `arXiv:2609.25073` 的 PICLas 稀有痕量组分权重对 DSMC/再入电离建模有方法价值，但与激光高能束流、强场和 HEDP 主线较远。
- `arXiv:2609.26070` 是 ECR 源膨胀氢等离子体实验与理论，属于可靠基础等离子体工作，但本轮的正式 PRE、LWFA 束流品质和光核实验与仓库重点更贴近。
- 本轮未发现同等新鲜、全文可验证且未入库的强场 QED 正式论文；没有用低相关条目填满主题配额。

## 当日综合总结

- Liu–Kuramitsu 给出的是“为什么一维湍流尾场会出现 `γ⁻²`”的统计解释：中能电子的 Lorentzian 跳跃可映射到 `α=1` 分数扩散，高能准单能粒子则保留定向加速记忆。
- Smartsev 等把高重复率 LWFA 的讨论从单发峰值推进到 100 秒、10,000 发的完整数据集；当前最可用的工程线索是主导漂移低于 `1 Hz`，适合慢反馈，而不是已经完成 kHz/FLASH。
- Gheorghe 等补齐了 Ho/Tm 光核核数据和旧实验系统学，可作为未来激光电子束—转换靶伽马谱—光中子模拟的独立 benchmark，但不能替代实际 LPA 源项与厚靶输运验证。
- 推荐阅读顺序：先看 LWFA 图 2/3 把握可直接用的束流稳定性，再看光中子图 5–8 了解核反应数据链，最后看 PRE 图 4–6 区分随机重尾和弹道高能分支。
