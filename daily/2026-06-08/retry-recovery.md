# 2026-06-08 重试队列恢复记录

## 概览

- 执行时间：2026-06-08
- 目标：修复下载链路并重新消化 `state/daily_retry_candidates.json` 中可恢复的积压 PDF
- 结果：成功补回 6 条 Cambridge / JPP 积压 PDF；重试队列从 18 条降到 12 条；`state/processed_articles.json` 从 80 条升到 86 条

## 本次成功补回

1. `10.1017/hpl.2026.10142` - Neural network-based deconvolution for GeV-Scale Gamma-Ray Spectroscopy
2. `10.1017/hpl.2026.10117` - Generation of X-ray Spatiotemporal Vortices via Nonlinear Thomson Scattering
3. `10.1017/S0022377825101062` - Plasma rotation driven by lasers with zero angular momentum
4. title-key only - Experimental investigation of SRS and SBS growth in thick and exploded foil targets in smoothed and unsmoothed beam interactions
5. title-key only - Shock Breakout Driven by Colliding Plasmas in the Double-Cone Ignition Scheme
6. `10.1017/hpl.2026.10154` - High-repetition-rate, all-reflective optical guiding and electron acceleration in helium using an off-axis axicon

## 剩余阻塞分类

- Elsevier / ScienceDirect：10 条，当前统一复现为 `HTTP 403`
- Nature：1 条，当前复现为 `cookies_not_supported`
- IOP / New Journal of Physics：1 条，当前复现为 Radware / Perfdrive 验证页（bot wall）

## 代码侧改进

- `scripts/safe_pdf_download.py`
  - 新增失败分类 `last_failure_class`
  - 新增 `--report-json` 结构化报告输出
  - 在 `urllib` 失败时自动回退到 `curl`
- `scripts/retry_download_queue.py`
  - 支持按 `source-family` 批量重试
  - 成功时自动把 PDF 从 retry 队列转入 `state/processed_articles.json`
  - 失败时回写 `retry_count`、`last_retry_at`、`source_family`

## 后续动作

- 将每日自动化开头固定为先跑一次 `python scripts/retry_download_queue.py --source-family cambridge`
- 对剩余 12 条来源侧限制项，优先寻找合法 OA/作者稿来源，而不是继续原地址空跑
