# 每日论文雷达 - 2026-06-09

## 今日新增论文索引

- 初始运行时未发现满足“新增且可完成 PDF 下载校验”的论文入库条目；2026-06-11 后续重试已恢复本日 3 条 PDF，并写入 `state/processed_articles.json`，中文结构化笔记仍待补。

## 今日高相关候选（已去重，PDF 已于后续重试恢复）

### 1) Data-driven model order reduction for accelerating boundary plasma turbulence simulations
- 作者：Andreas Solheim, Kyungtak Lim, Simone Deparis, Paolo Ricci
- 期刊/平台：Journal of Plasma Physics（正式期刊，Open Access）
- DOI：https://doi.org/10.1017/S0022377825101050
- 真实发表日期：2026-02-05（Published online by Cambridge University Press）
- 来源链接：https://www.cambridge.org/core/product/D2265426E60D45572203017E81913120
- 与方向关系：用 POD 与神经网络加速边界等离子体湍流模拟，直接对应 AI/ML 加速等离子体数值计算这一主线，对 PIC/输运建模方法论也有参考价值。

### 2) Design of experiments characterising heat conduction in magnetised, weakly collisional plasma
- 作者：T. A. Vincent, P. Ariyathilaka, L. Creaser, C. Danson, D. Lamb, J. Meinecke, C.A.J. Palmer, S. Pitt, H. Poole, C. Spindloe, P. Thomas, E. Tubman, L. Wilson, W. Garbett, G. Gregori, P. Tzeferacos, T. Hodge, A. F. A. Bott
- 期刊/平台：High Power Laser Science and Engineering（Accepted manuscript，官方已接收）
- DOI：https://doi.org/10.1017/hpl.2026.10152
- 真实发表日期：2026-05-12（Published online by Cambridge University Press）
- 来源链接：https://www.cambridge.org/core/journals/high-power-laser-science-and-engineering/accepted-manuscripts
- 与方向关系：聚焦磁化弱碰撞等离子体热传导实验平台设计，面向 HEDP/ICF 中的输运物理与 FLASH 类辐射流体模拟验证，和你的高能量密度主线高度相关。

### 3) Suppression and Enhancement of Electromagnetic Pulses from Laser-Target Interactions by Strong Magnetic Fields
- 作者：P. V. Heuer, J. L. Peebles, J. R. Davies, D. H. Barnak, B. Stanley, N. Pelepchan, M. Cufari, J. A. Frenje, C. Niemann, N. A. Rongione, C. Constantin, E. Cisneros, P. Pribyl, H. Sio, H. Chen
- 期刊/平台：High Power Laser Science and Engineering（Accepted manuscript，官方已接收）
- DOI：https://doi.org/10.1017/hpl.2026.10147
- 真实发表日期：2026-05-05（Published online by Cambridge University Press）
- 来源链接：https://www.cambridge.org/core/journals/high-power-laser-science-and-engineering/accepted-manuscripts
- 与方向关系：围绕强磁场条件下激光靶相互作用产生的 EMP 抑制与增强机制，直接关系到高功率激光设施诊断、靶室电磁环境和激光等离子体实验平台稳定性。

## 检索与去重执行记录

- 检索日期：2026-06-09。
- 重点检索方向：激光等离子体、强场 QED、高能量密度物理、PIC，以及 AI/机器学习在上述方向中的应用。
- 优先来源：Cambridge Core 官方 HPL accepted manuscripts、JPP 正式论文页与 DOI 页面。
- 去重基线：`state/processed_articles.json` 与 `state/daily_retry_candidates.json`（运行前唯一 DOI/标题键合计 190 条）。
- 本次新增候选：3 条，均未命中现有 processed/retry 台账；追加后唯一 DOI/标题键合计 196 条。
- 说明：本次三条均来自正式出版社来源，其中 1 条为正式期刊 OA，2 条为 HPL 官方 accepted manuscript。

## 下载与校验状态

- 当日初始执行了 3 条候选论文 PDF 下载尝试，详见 `daily/2026-06-09/run_results.json`。
- 初始结果：三条候选均因当时运行环境外网阻塞失败，错误模式一致：
  - 走环境代理时 `curl` 连接本地代理 `127.0.0.1:1087` 失败：`Couldn't connect to server`
  - 直连时 DNS 解析失败：`Could not resolve host`
- 后续恢复：2026-06-11 12:32 +0800 重试后，本日 3 条 Cambridge/JPP PDF 均下载成功并通过 PDF 文件识别。
- 结论：初始阻塞是运行环境侧问题，不是出版社侧 `403` / cookie wall / bot wall。

## 笔记产出

- 今日无新增中文结构化笔记（无校验通过的 PDF）。

## 状态更新

- 初始运行：`state/processed_articles.json` 无新增，保持 86 条；`state/daily_retry_candidates.json` 已追加今日 3 条新增候选，累计 15 条。
- 后续重试恢复（2026-06-11 12:32 +0800）：本日 3 条 Cambridge/JPP 候选 PDF 均已下载校验并转入 `state/processed_articles.json`。

## 当日总结

- 今天补入了 3 条新的 Cambridge/JPP 高相关候选，分别覆盖 AI/ML 加速等离子体湍流模拟、磁化弱碰撞等离子体热传导实验设计，以及强磁场下的激光靶 EMP 行为。
- 额外修复了 `scripts/safe_pdf_download.py` 的失败分类回归：`curl` 回退路径下的“代理不可连”和“DNS 失败”现在不再落到 `unknown`，而会正确标记为运行环境阻塞。
