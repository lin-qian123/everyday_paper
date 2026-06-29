# 每日论文索引 - 2026-06-30

## 今日新增论文索引

- 今日新增并完成 PDF 校验入库 3 条，均为高相关 arXiv 预印本。
- 3 条论文均已下载通过 PDF 文件头校验，并已生成中文结构化笔记。
- 今天先复查 Cambridge `High Power Laser Science and Engineering` accepted manuscripts 与 `Journal of Plasma Physics` 当前页面；高相关 HPL/JPP 新条目要么已入库，要么偏激光器件而非本仓库核心方向，因此本轮转向近期未入库 arXiv 条目，重点补强 ICF 诊断、光子活化和韧致辐射驱动光核反应截面。

## 今日高相关候选（已去重，已完成 PDF 与笔记）

### 1) Single-Shot Intensity-Correlation Diffractive X-ray Imaging of ICF Plasmas
- 作者：Kenan Qu, Daniel Bhatti, Nathaniel J. Fisch
- 期刊/平台：arXiv 预印本
- DOI：https://doi.org/10.48550/arXiv.2606.26198
- 真实发表日期：2026-06-24
- 来源链接：http://arxiv.org/abs/2606.26198v1
- 与方向关系：这篇直接面向 ICF 等离子体 X 射线单发成像诊断，补强 HEDP 实验平台、靶内结构测量和数据反演方法主线。

### 2) Half-Life Measurements of 110Sn, 113Sn, 117mSn, and 123mSn Produced via Photon Activation of Natural Tin
- 作者：O. Nusair et al.
- 期刊/平台：arXiv 预印本（submitted to Nuclear Physics A）
- DOI：https://doi.org/10.48550/arXiv.2606.27064
- 真实发表日期：2026-06-25
- 来源链接：http://arxiv.org/abs/2606.27064v1
- 与方向关系：这篇用 photon activation 产生锡同位素并测量半衰期，服务于光核反应、同位素产生、剂量学和伽马谱核诊断基线。

### 3) Measurements of Bremsstrahlung-Averaged Cross Sections for Reactions on Natural Nickel Targets at Eendpoint = 40MeV
- 作者：O. Nusair et al.
- 期刊/平台：arXiv 预印本
- DOI：https://doi.org/10.48550/arXiv.2606.23966
- 真实发表日期：2026-06-22
- 来源链接：http://arxiv.org/abs/2606.23966v1
- 与方向关系：这篇直接覆盖 40 MeV 电子打钽转换靶产生韧致辐射后的镍靶光核截面测量，是激光加速电子束驱动伽马源、光核反应和同位素生产方向的高价值参考。

## 检索与去重执行记录

- 检索日期：2026-06-30。
- 重点检索方向：ICF/HEDP 诊断、X 射线成像、photon activation、bremsstrahlung converter、光核截面、同位素与核诊断应用。
- 优先来源：Cambridge `High Power Laser Science and Engineering` accepted manuscripts、`Journal of Plasma Physics` 当前页面；随后补查 arXiv `physics.plasm-ph`、`physics.acc-ph`、`nucl-ex` 和 `physics.ins-det` 近期条目。
- 去重基线：`state/processed_articles.json` 与 `state/daily_retry_candidates.json`。
- 本次新增候选：3 条，均未命中现有 processed/retry 台账。

## 下载与校验状态

- 当日执行了 3 条候选论文 PDF 下载尝试，详见 `daily/2026-06-30/run_results.json`。
- 结果：3 条候选均通过环境代理路径下载，并通过 PDF 文件头校验。
- 今日没有重新运行 `scripts/retry_download_queue.py`，因为旧重试队列仍是 12 条明确来源侧限制条目，继续全量重试收益很低。

## 笔记产出

- 已生成 3 份中文结构化笔记：
  - `daily/2026-06-30/notes/Kenan Qu et al. - 2026 - Single-Shot Intensity-Correlation Diffractive X-ray Imaging of ICF Plasmas.md`
  - `daily/2026-06-30/notes/O. Nusair et al. - 2026 - Half-Life Measurements of Sn Isotopes Produced via Photon Activation of Natural Tin.md`
  - `daily/2026-06-30/notes/O. Nusair et al. - 2026 - Measurements of Bremsstrahlung-Averaged Cross Sections for Reactions on Natural Nickel Targets.md`

## 状态更新

- `state/processed_articles.json`：从 150 条增至 153 条。
- `state/daily_retry_candidates.json`：保持 12 条，无新增来源失败重试记录。
- 当前“已补回 PDF 但尚无中文结构化笔记”的历史条目仍为 65 条。

## 当日总结

- 今天的 3 条增量把索引从 HEDP/ICF 诊断延伸到转换靶韧致辐射、光核反应截面和同位素/核诊断数据。
- 如果只优先读一篇，建议先看 `10.48550/arXiv.2606.23966`，因为它最直接对应“电子束打转换靶产生伽马源并驱动光核反应”的应用链条。
