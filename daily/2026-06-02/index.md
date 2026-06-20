# 每日论文索引 - 2026-06-02

## 今日新增论文索引

- 今日未发现满足“新增且可完成 PDF 下载校验”的论文入库条目。

## 今日高相关候选（已去重，待重试）

### 1) Quasi-monoenergetic deuteron acceleration via boosted coulomb explosion by reflected picosecond laser pulse
- 作者：Tianyun Wei, Zechen Lan, Akifumi Yogo et al.
- 期刊/平台：Nature Communications（正式期刊）
- DOI：https://doi.org/10.1038/s41467-026-73196-9
- 真实发表日期：2026-05-29
- 来源链接：https://www.nature.com/articles/s41467-026-73196-9
- 与方向关系：激光离子加速 + 惯性约束聚变相关离子源 + 激光等离子体实验

### 2) Multi-PW laser-driven proton acceleration using a plasma-lens target
- 作者：Vojtěch Horný, Domenico Doria
- 期刊/平台：Scientific Reports（正式期刊）
- DOI：https://doi.org/10.1038/s41598-025-29793-7
- 真实发表日期：2025-12-06
- 来源链接：https://www.nature.com/articles/s41598-025-29793-7
- 与方向关系：多 PW 激光质子加速 + 近临界等离子体透镜 + HEDP 应用

## 检索与去重执行记录

- 检索日期：2026-06-02。
- 重点检索方向：激光等离子体、强场 QED、高能量密度物理、PIC，以及 机器学习在这些方向中的应用。
- 优先来源：Nature Portfolio 正式论文页面与对应 DOI。
- 去重基线：`state/processed_articles.json` 与 `state/daily_retry_candidates.json`（唯一 DOI/标题键合计 77 条）。
- 本次新增候选：2 条，均未命中现有 processed/retry 台账。
- 说明：候选元数据通过官方网页检索确认，但当前本地运行时外网出站仍受限，无法完成 PDF 下载与文件校验。

## 下载与校验状态

- 当日执行了 2 条正式论文 PDF 下载尝试，详见 `daily/2026-06-02/run_results.json`。
- 结果：两条候选均因本地运行环境网络受限失败，错误模式一致：
  - 走环境代理时返回 `Operation not permitted`
  - 直连时返回 DNS 解析失败 `nodename nor servname provided, or not known`
- `daily/2026-06-02/pdfs/` 无新增可校验 PDF。

## 笔记产出

- 今日无新增中文结构化笔记（无校验通过的 PDF）。

## 状态更新

- `state/processed_articles.json`：无新增（继续避免写入未校验论文）。
- `state/daily_retry_candidates.json`：已追加今日 2 条新增正式论文候选，待网络恢复后重试。

## 当日总结

- 今天补回了新的正式来源候选，不再只是空跑占位。
- 当前主阻塞仍是本地运行时的网络出站；网络恢复后应优先重试今天这 2 篇正式论文。
