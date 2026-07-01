# 每日论文索引 - 2026-07-02

## 今日新增论文索引

- 今日新增并完成 PDF 校验入库 3 条：2 条 Journal of Plasma Physics 正式论文，1 条高相关 arXiv 预印本。
- 3 条论文均已下载通过 PDF 文件头校验，并已生成中文结构化笔记。
- 今天先复查 Cambridge `Journal of Plasma Physics` 当前期与 `High Power Laser Science and Engineering` accepted manuscripts；JPP 当前期有若干未入库正式论文，其中优先补入与聚变反应/中性束、无碰撞磁场生成和 HEDP stopping power 更相关的条目。此前已入库的 JPP 高相关 DOI 已按台账跳过，避免重复处理。

## 今日高相关候选（已去重，已完成 PDF 与笔记）

### 1) Extension of MIDAS-1D2V model: fusion reactions and neutral beam capture
- 作者：Vadim Prikhodko
- 期刊/平台：Journal of Plasma Physics
- DOI：https://doi.org/10.1017/S0022377826101901
- 真实发表日期：2026-06
- 来源链接：https://www.cambridge.org/core/journals/journal-of-plasma-physics/article/extension-of-midas1d2v-model-fusion-reactions-and-neutral-beam-capture/BFAB5F26EACA47C19DFFC1A8C5DFB551
- 与方向关系：这篇补强开放磁阱动理学模拟、聚变反应源项与中性束俘获，对束流-等离子体反应率、反应产物和中子源建模有方法参考价值。

### 2) From Weibel seeds to dynamo beyond pair-plasmas
- 作者：Lise Hanebring, James Juno, Ammar Hakim, Jason TenBarge, István Pusztai
- 期刊/平台：Journal of Plasma Physics
- DOI：https://doi.org/10.1017/S0022377826101780
- 真实发表日期：2026-06
- 来源链接：https://www.cambridge.org/core/journals/journal-of-plasma-physics/article/from-weibel-seeds-to-dynamo-beyond-pairplasmas/FA0D98C97FE4C4DD04C644424A3729FB
- 与方向关系：这篇覆盖无碰撞等离子体、Weibel 磁场种子和 dynamo 放大，可补强 HEDP/实验室天体物理中的磁场生成、多尺度模拟和 kinetic-to-MHD 连接。

### 3) An Enhanced RPA-LDA Model for Ion Stopping Power from Cold Matter to High-Energy Density Plasmas: A Unified, Open-Source Framework
- 作者：Thomas A. Mehlhorn, Ming Feng Gu, Igor Golovkin
- 期刊/平台：arXiv 预印本
- DOI：https://doi.org/10.48550/arXiv.2606.30978
- 真实发表日期：2026-06-29
- 来源链接：https://arxiv.org/abs/2606.30978
- 与方向关系：这篇直接覆盖离子 stopping power、温稠密物质、高能量密度等离子体和 ICF/激光离子束能量沉积，是扩展应用方向中的高价值补充。

## 检索与去重执行记录

- 检索日期：2026-07-02。
- 重点检索方向：Journal of Plasma Physics 当前期、High Power Laser Science and Engineering accepted manuscripts、HEDP stopping power、无碰撞磁场生成、动理学模拟、束注入与聚变反应源项。
- 优先来源：Cambridge `Journal of Plasma Physics` 当前期；随后补查 Cambridge HPL accepted manuscripts 与 arXiv `physics.plasm-ph`、`physics.comp-ph`、`physics.acc-ph`、`nucl-ex` 近期列表。
- 去重基线：`state/processed_articles.json` 与 `state/daily_retry_candidates.json`。
- 本次新增候选：3 条，均未命中现有 processed/retry 台账。

## 下载与校验状态

- 当日执行了 3 条候选论文 PDF 下载尝试，详见 `daily/2026-07-02/run_results.json`。
- 结果：3 条候选均通过环境代理路径下载，并通过 PDF 文件头校验。
- 今日没有重新运行 `scripts/retry_download_queue.py`，因为旧重试队列仍是 12 条明确来源侧限制条目，继续全量重试收益很低。

## 笔记产出

- 已生成 3 份中文结构化笔记：
  - `daily/2026-07-02/notes/Vadim Prikhodko - 2026 - Extension of MIDAS-1D2V model fusion reactions and neutral beam capture.md`
  - `daily/2026-07-02/notes/Lise Hanebring et al. - 2026 - From Weibel seeds to dynamo beyond pair-plasmas.md`
  - `daily/2026-07-02/notes/Thomas A. Mehlhorn et al. - 2026 - An Enhanced RPA-LDA Model for Ion Stopping Power.md`

## 状态更新

- `state/processed_articles.json`：从 156 条增至 159 条。
- `state/daily_retry_candidates.json`：保持 12 条，无新增来源失败重试记录。
- 当前“已补回 PDF 但尚无中文结构化笔记”的历史条目仍为 65 条。

## 当日总结

- 今天优先补入正式 JPP 来源，使索引从近期 arXiv 主线回到正式期刊增量；同时用 HEDP stopping power 预印本补强激光离子束与能量沉积应用线。
- 如果只优先读一篇，建议先看 `10.48550/arXiv.2606.30978`，因为它最直接连接激光离子束应用、ICF alpha 沉积、材料辐照和 HEDP 靶设计。
