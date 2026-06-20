# 每日论文雷达 - 2026-06-08

## 今日新增论文索引

- 今日未发现满足“新增且可完成 PDF 下载校验”的论文入库条目。

## 今日高相关候选（已去重，待重试）

### 1) Experimental investigation of SRS and SBS growth in thick and exploded foil targets in smoothed and unsmoothed beam interactions
- 作者：E. Hume, G. Cristoforetti, P. Koester, S. Atzeni, D. Batani, F. P. Condamine, G. Fauvel, B. Fisher, P.-E. Masson-Laborde, T. Lastovicka, D. Singappuli, R. L. Singh, M. Sokol, W. Theobald, F. Wasser, S. Zahter, N. Woolsey, L. A. Gizzi
- 期刊/平台：High Power Laser Science and Engineering（Accepted manuscript，官方已接收）
- DOI：未在页面摘要中直接给出；本次按标题键去重与入队
- 真实发表日期：2026-06-02（Published online by Cambridge University Press）
- 来源链接：https://www.cambridge.org/core/product/CA8C14175B277DA7154ABAC65E8104BB
- 与方向关系：围绕冲击点火条件下的受激拉曼/布里渊散射增长与厚/爆炸箔靶差异，直接关联高能量密度物理中的激光-等离子体不稳定性与 PIC 诊断。

### 2) Shock Breakout Driven by Colliding Plasmas in the Double-Cone Ignition Scheme
- 作者：Zhijie Qiu, Chuanqi Shi, Ke Fang, Chenglong Zhang, Yihang Zhang, Huigang Wei, Yangyi Lei, Fuyuan Wu, Da-Wei Yuan, Xiaohui Yuan, Zhe Zhang, Yutong Li, Jie Zhang
- 期刊/平台：High Power Laser Science and Engineering（Accepted manuscript，官方已接收）
- DOI：未在页面摘要中直接给出；本次按标题键去重与入队
- 真实发表日期：2026-06-01（Published online by Cambridge University Press）
- 来源链接：https://www.cambridge.org/core/product/ECEF50E08CC72AFBEB8D4149466E094D
- 与方向关系：聚焦双锥点火方案中的碰撞等离子体 shock breakout，与惯性约束聚变、致密高温等离子体形成和实验诊断高度相关。

### 3) High-repetition-rate, all-reflective optical guiding and electron acceleration in helium using an off-axis axicon
- 作者：Jiri Sisma, Michal Nevrkla, Filip Vitha, Sebastian Lorenz, Illia Zymak, Alzbeta Spadova, Andrea Kollarova, Matej Jech, Alexandr Jancarek, Davorin Peceli, Carlo Maria Lazzarini, Leonardo Vila Nova Goncalves, Gabriele Maria Grittani, Sergei Bulanov, Jaron Eugene Shrock, Ela Rockafellow, Ari Joseph Sloss, Bo Miao, Scott Hancock, Howard M. Milchberg
- 期刊/平台：High Power Laser Science and Engineering（Accepted manuscript，官方已接收）
- DOI：https://doi.org/10.1017/hpl.2026.10154
- 真实发表日期：2026-05-12（Published online by Cambridge University Press）
- 来源链接：https://www.cambridge.org/core/product/4BA4AF292507C490FAC79A6DB27C1E34
- 与方向关系：文章直接研究高重复频下的等离子体光导与电子加速，面向 LWFA/PIC 相关实验平台，对激光等离子体主线高度贴合。

## 检索与去重执行记录

- 检索日期：2026-06-08。
- 重点检索方向：激光等离子体、强场 QED、高能量密度物理、PIC，以及 AI/机器学习在上述方向中的应用。
- 优先来源：Cambridge Core 官方 `Accepted Manuscripts` 页面与对应单篇官方 product/PDF 链接。
- 去重基线：`state/processed_articles.json` 与 `state/daily_retry_candidates.json`（运行前唯一 DOI/标题键合计 187 条）。
- 本次新增候选：3 条，均未命中现有 processed/retry 台账；追加后唯一 DOI/标题键合计 190 条。
- 说明：本次继续优先保留正式出版社来源；三条均为 Cambridge HPL 官方 accepted manuscript。

## 下载与校验状态

- 当日执行了 3 条候选论文 PDF 下载尝试，详见 `daily/2026-06-08/run_results.json`。
- 结果：三条候选均因本地运行环境网络受限失败，错误模式一致：
  - 走环境代理时返回 `Operation not permitted`
  - 直连时返回 DNS 解析失败 `nodename nor servname provided, or not known`
- `daily/2026-06-08/pdfs/` 无新增可校验 PDF。

## 笔记产出

- 今日无新增中文结构化笔记（无校验通过的 PDF）。

## 状态更新

- `state/processed_articles.json`：无新增（继续避免写入未校验论文），当前 80 条。
- `state/daily_retry_candidates.json`：已追加今日 3 条新增候选，待网络恢复后重试；当前累计 18 条。

## 当日总结

- 今天补入了 3 条新的 HPL 官方 accepted manuscript，覆盖冲击点火中的 SRS/SBS 不稳定性、双锥点火碰撞等离子体 shock breakout，以及高重复频 LWFA 光导与电子加速。
- 当前主阻塞仍是本地运行时外网出站；网络恢复后应优先重跑今天这 3 条，再与 2026-06-03 至 2026-06-07 的积压项一起完成 PDF 校验与中文笔记。

## 后续回填进展（2026-06-08）

- 当天稍后在网络恢复环境下，以上 3 条候选已全部自动补回 PDF，并从 retry 队列转入 `state/processed_articles.json`。
- 与 `2026-06-07` 一起，本轮共恢复 6 条 Cambridge / JPP 积压项。
- 详见 `daily/2026-06-08/retry-recovery.md`。
