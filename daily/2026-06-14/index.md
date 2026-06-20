# 每日论文雷达 - 2026-06-14

## 今日新增论文索引

- 今日新增并完成 PDF 校验入库 4 条，其中 1 条来自 Cambridge 正式来源，3 条为在更强正式增量不足时补入的高相关 arXiv 预印本。
- 4 条论文均已下载通过 PDF 校验，并已生成中文结构化笔记。

## 今日高相关候选（已去重，已完成 PDF 与笔记）

### 1) Supersonic gas jet catcher system for differential pumping in laser plasma interaction experiments
- 作者：S. Lorenz, C.M. Lazzarini, I. Zymak, F. Baffigi, F. Brandi, M. Ezzat, A. Fregosi, L.A. Gizzi, M. Jech, P. Koester, L. Labate, M. Nevrkla, D. Palla, A. Spadova, J. Sisma, L.V. Goncalves, F. Vitha, P. Voboril, S. V. Bulanov, G. Grittani
- 期刊/平台：High Power Laser Science and Engineering（Accepted manuscript，正式来源）
- DOI：https://doi.org/10.1017/hpl.2026.10148
- 真实发表日期：2026-05-11
- 来源链接：https://www.cambridge.org/core/journals/high-power-laser-science-and-engineering/article/supersonic-gas-jet-catcher-system-for-differential-pumping-in-laser-plasma-interaction-experiments/53E0393B43AA9806F71CF144966C07F5
- 与方向关系：直接面向高重复频 LWFA 的气体靶与 differential pumping 工程问题，属于激光等离子体实验基础设施方向的正式增量。

### 2) Electron injection and acceleration into laser-driven wakefield from a solid overdense plasma target
- 作者：M. Caetano de Sousa, S. Marini, M. Grech, S. Brunner, C. Riconda, M. Raynaud
- 期刊/平台：arXiv 预印本（高相关补充）
- DOI：https://doi.org/10.48550/arXiv.2606.02454
- 真实发表日期：2026-06-01（arXiv submitted）
- 来源链接：https://arxiv.org/abs/2606.02454
- 与方向关系：提出把过密等离子体界面电子抽取和欠密等离子体 wakefield 加速串起来的两段式方案，直接落在 LWFA 注入与电子束品质优化上。

### 3) A Reduced-Order Particle-in-Cell Method with Azimuthal Fourier-Decomposed Fields for Nominally Axisymmetric Plasmas
- 作者：Shaun Andrews
- 期刊/平台：arXiv 预印本（高相关补充）
- DOI：https://doi.org/10.48550/arXiv.2606.04887
- 真实发表日期：2026-06-03（arXiv submitted；v2 on 2026-06-08）
- 来源链接：https://arxiv.org/abs/2606.04887
- 与方向关系：针对具有低阶方位角不稳定性的圆柱等离子体提出 reduced-order PIC，核心贡献是把 3D 场求解压成少模态 2D 问题，直接对应你关注的 PIC 算法加速。

### 4) A Surrogate Model for Proton Spectrum Prediction to Map Transitions in Laser-Ion Acceleration
- 作者：Chengqi-Zhang, Yang He, Mamat Ali Bake, Xilin-Wang, Bai-Song Xie
- 期刊/平台：arXiv 预印本（高相关补充）
- DOI：https://doi.org/10.48550/arXiv.2606.06210
- 真实发表日期：2026-06-04（arXiv submitted）
- 来源链接：https://arxiv.org/abs/2606.06210
- 与方向关系：把 β-VAE、MLP 和不确定性量化用于 laser-ion acceleration 的连续质子谱预测，直接覆盖 AI/ML + 激光等离子体加速。

## 检索与去重执行记录

- 检索日期：2026-06-14。
- 重点检索方向：激光等离子体、强场 QED、高能量密度物理、PIC，以及 AI/机器学习在上述方向中的应用。
- 优先来源：先检查 Cambridge HPL 正式来源 / accepted manuscripts 与 arXiv 近期 plasma / accelerator 方向列表。今天确认到 1 条新的高相关 Cambridge 正式来源；其余正式来源未筛出更强且未重复的新增条目，因此补入 3 条高相关 arXiv 预印本。
- 去重基线：`state/processed_articles.json` 与 `state/daily_retry_candidates.json`（运行前唯一 DOI/标题键合计按既有记法为 214 条）。
- 本次新增候选：4 条，均未命中现有 processed/retry 台账；追加后唯一 DOI/标题键合计按既有记法为 218 条。

## 下载与校验状态

- 当日执行了 4 条候选论文 PDF 下载尝试，详见 `daily/2026-06-14/run_results.json`。
- 结果：1 条 Cambridge 正式来源与 3 条 arXiv 预印本均通过下载与 PDF 文件头校验。
- Cambridge 那篇通过直接抽取官方 `citation_pdf_url` / Save PDF 链接后完成下载，说明来源本身可达，只是 `safe_pdf_download.py` 当前在该链接上的 Python 读取路径存在卡住现象；今天先以 `curl` 直链完成闭环，不把它记入 retry 队列。
- 当前旧重试队列维持 12 条，仍全部属于来源侧限制：
  - 10 条 Elsevier / ScienceDirect `publisher_http_403`
  - 1 条 Nature `publisher_cookie_wall`
  - 1 条 IOP `publisher_bot_wall`

## 笔记产出

- 已生成 4 份中文结构化笔记：
  - `daily/2026-06-14/notes/S. Lorenz et al. - 2026 - Supersonic gas jet catcher system for differential pumping in laser plasma interaction experiments.md`
  - `daily/2026-06-14/notes/M. Caetano de Sousa et al. - 2026 - Electron injection and acceleration into laser-driven wakefield from a solid overdense plasma target.md`
  - `daily/2026-06-14/notes/Shaun Andrews - 2026 - A Reduced-Order Particle-in-Cell Method with Azimuthal Fourier-Decomposed Fields for Nominally Axisymmetric Plasmas.md`
  - `daily/2026-06-14/notes/Chengqi-Zhang et al. - 2026 - A Surrogate Model for Proton Spectrum Prediction to Map Transitions in Laser-Ion Acceleration.md`

## 状态更新

- `state/processed_articles.json`：从 101 条增至 105 条。
- `state/daily_retry_candidates.json`：保持 12 条，无新增来源失败重试记录。
- 当前“已补回 PDF 但尚无中文结构化笔记”的历史条目仍为 43 条。

## 当日总结

- 今天补入了 1 条正式来源和 3 条高相关预印本，分别覆盖高重复频 LWFA 气体靶工程、两段式注入 LWFA、新型 reduced-order PIC 方法，以及 AI 驱动的 laser-ion 质子谱预测。
- 运行环境中的 arXiv 下载链路继续稳定，Cambridge 来源也可用，但暴露出 `safe_pdf_download.py` 在个别 Cambridge PDF 直链上的传输卡住问题，值得后续单独修补。
