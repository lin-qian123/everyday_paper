# 每日论文索引 - 2026-06-16

## 今日新增论文索引

- 今日新增并完成 PDF 校验入库 4 条，其中 1 条为 Cambridge HPL 正式来源，3 条为高相关 arXiv 预印本补充。
- 4 条论文均已下载通过 PDF 校验，并已生成中文结构化笔记。

## 今日高相关候选（已去重，已完成 PDF 与笔记）

### 1) Equation of state measurements of boron nitride under laser-driven compression at the Prague Asterix Laser System facility
- 作者：Hanna Marchenko, Agnieszka Zaras-Szydlowska, Dimitri Batani, Donaldi Mancelli, Diluka Singappuli, Yair Ferber, Eran Greenberg, Artem S. Martynenko, Noaz Nissim, Roman Dudzak, Shubham Agarwal, Pooja Devi, David Ettel, Pavel Gajdoš, Simon Jelinek, Michal Krupka, Miroslav Krus, Libor Juha, Sushil Singh, Katarzyna Liliana Batani
- 期刊/平台：High Power Laser Science and Engineering（正式来源）
- DOI：https://doi.org/10.1017/hpl.2026.10115
- 真实发表日期：2026-02-06（Cambridge online）
- 来源链接：https://www.cambridge.org/core/journals/high-power-laser-science-and-engineering/article/equation-of-state-measurements-of-boron-nitride-under-laserdriven-compression-at-the-prague-asterix-laser-system-facility/9B71874D6F9DB182D74372D40E442618
- 与方向关系：直接覆盖 HEDP / ICF 相关材料在激光驱动压缩下的状态方程测量，对极端条件材料模型和靶设计都相关。

### 2) PIConGPU modeling of nanoplasma formation in helium nanodroplets irradiated by intense femtosecond laser pulses
- 作者：Cristian Medina, Klaus Steiniger, Brian Edward Marre, Marcel Mudrich, Asbjørn Ø. Lægdsmand, SivaRama Krishnan, Keshav Sishodia, Martin Albrecht, Eva Klimešová, Maria Krikunova, Jakob Andreasson, Weiyu Zhang, Deepthy Mootheril, Nikolas Rapp, Serge A. Krasnokutski, Robert Moshammer, Thomas Pfeifer
- 期刊/平台：arXiv 预印本（高相关补充）
- DOI：https://doi.org/10.48550/arXiv.2606.14300
- 真实发表日期：2026-06-12（arXiv submitted）
- 来源链接：https://arxiv.org/abs/2606.14300
- 与方向关系：用大规模 GPU PIC 模拟强场激光驱动氦纳米液滴纳米等离子体形成，是 laser-plasma + PIC + 强场动力学的直接交叉样本。

### 3) Kinetic Theory for Electronic Transport Properties of Warm Dense Matter: Chapman-Enskog Solution of the Uehling-Uhlenbeck Equation
- 作者：Lucas J. Babati, Nathaniel R. Shaffer, Louis Jose, Scott D. Baalrud
- 期刊/平台：arXiv 预印本（高相关补充）
- DOI：https://doi.org/10.48550/arXiv.2606.02890
- 真实发表日期：2026-06-01（arXiv submitted）
- 来源链接：https://arxiv.org/abs/2606.02890
- 与方向关系：直接面向 warm dense matter / HEDP 传输系数建模，把强耦合、简并和量子散射统一到一套动理学框架。

### 4) Radiation-induced electron spin polarization in ultrarelativistic kinetic turbulence
- 作者：Peng Liu, Karen Z. Hatsagortsyan, Christoph H. Keitel, Zheng Gong
- 期刊/平台：arXiv 预印本（高相关补充）
- DOI：https://doi.org/10.48550/arXiv.2606.04332
- 真实发表日期：2026-06-04（arXiv v2）
- 来源链接：https://arxiv.org/abs/2606.04332
- 与方向关系：虽然问题偏天体，但主题直接命中强场 / 辐射主导等离子体、超相对论 PIC 与自旋效应，可作为 strong-field QED 相关数值方法参考。

## 检索与去重执行记录

- 检索日期：2026-06-16。
- 重点检索方向：激光等离子体、强场 QED、高能量密度物理、PIC，以及 机器学习在上述方向中的应用。
- 优先来源：先检查 Cambridge HPL 最新卷；确认 1 条高相关且未重复的正式来源增量。随后从 arXiv `physics.plasm-ph` 当前列表与相关检索结果补入 3 条高相关预印本。
- 去重基线：`state/processed_articles.json` 与 `state/daily_retry_candidates.json`（运行前唯一 DOI/标题键合计按既有记法为 222 条）。
- 本次新增候选：4 条，均未命中现有 processed/retry 台账；追加后唯一 DOI/标题键合计按既有记法为 226 条。

## 下载与校验状态

- 当日执行了 4 条候选论文 PDF 下载尝试，详见 `daily/2026-06-16/run_results.json`。
- 结果：4 条候选均通过环境代理路径下载，并通过 PDF 文件头校验。
- 今日尝试启动 `scripts/retry_download_queue.py --source-family all` 先消化积压，但该全量命令在来源受限条目上耗时过长，已中断，未对现有重试台账产生变更。
- 当前旧重试队列维持 12 条，仍全部属于来源侧限制：
  - 10 条 Elsevier / ScienceDirect `publisher_http_403`
  - 1 条 Nature `publisher_cookie_wall`
  - 1 条 IOP `publisher_bot_wall`

## 笔记产出

- 已生成 4 份中文结构化笔记：
  - `daily/2026-06-16/notes/Hanna Marchenko et al. - 2026 - Equation of state measurements of boron nitride under laser-driven compression at the Prague Asterix Laser System facility.md`
  - `daily/2026-06-16/notes/Cristian Medina et al. - 2026 - PIConGPU modeling of nanoplasma formation in helium nanodroplets irradiated by intense femtosecond laser pulses.md`
  - `daily/2026-06-16/notes/Lucas J. Babati et al. - 2026 - Kinetic Theory for Electronic Transport Properties of Warm Dense Matter Chapman-Enskog Solution of the Uehling-Uhlenbeck Equation.md`
  - `daily/2026-06-16/notes/Peng Liu et al. - 2026 - Radiation-induced electron spin polarization in ultrarelativistic kinetic turbulence.md`

## 状态更新

- `state/processed_articles.json`：从 109 条增至 113 条。
- `state/daily_retry_candidates.json`：保持 12 条，无新增来源失败重试记录。
- 当前“已补回 PDF 但尚无中文结构化笔记”的历史条目仍为 43 条。

## 当日总结

- 今天补入 4 条高相关论文，主题覆盖激光驱动 BN 状态方程测量、PIConGPU 强场纳米等离子体模拟、warm dense matter 电子输运动理学，以及辐射主导超相对论湍流中的自旋极化。
- 正式来源今天仍能筛到有价值增量，但整体密度不高；实践上继续维持“正式来源优先，若无更强非重复增量则快速切到高质量 arXiv”的节奏更稳妥。
