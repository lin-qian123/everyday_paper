# 每日论文索引 - 2026-07-21

## 今日新增论文索引

- 今日新增并完成 PDF 校验入库 3 条：1 条 HPL 正式 accepted manuscript，2 条 arXiv 高相关预印本。
- 3 条论文均已通过官方来源下载，并通过 `%PDF-` 文件头校验。
- 今天先加载 `processed_articles.json`、`daily_retry_candidates.json` 和历史 daily 索引做硬去重；随后复查 Cambridge HPL/JPP 可见正式来源，并使用 arXiv 官方 Atom API 检索近期 `physics.plasm-ph`、`physics.acc-ph`、`physics.comp-ph`、`nucl-ex` 与 `physics.ins-det` 条目。按台账、重试队列和历史 daily 去重后，优先选择与激光驱动次级源、LWFA 辐射源和机器学习等离子体湍流代理模型相关的未入库条目。

## 今日高相关候选（已去重，已完成 PDF 与笔记）

### 1) Nonlinear Enhancement of Laser-Foil Coupling and Secondary Sources under Irradiation by Dual Picosecond Petawatt Pulses

- 作者：Zitao Wang; Zhigang Deng; Wei Qi; Zhi-meng Zhang; Yonghong Yan; Bo Cui; Shukai He; Bo Zhang; Lan Xu; Aihui Niu; Jingjing Li; Jieru Ren; Weimin Zhou
- 期刊/平台：High Power Laser Science and Engineering accepted manuscript
- DOI：https://doi.org/10.1017/hpl.2026.10182
- 真实发表日期：2026-07-14
- 来源链接：https://www.cambridge.org/core/journals/high-power-laser-science-and-engineering/article/nonlinear-enhancement-of-laserfoil-coupling-and-secondary-sources-under-irradiation-by-dual-picosecond-petawatt-pulses/FCCED31921F53973000E0D29A190E407
- 与方向关系：论文在 SG-II Upgrade 上研究双皮秒 PW 脉冲打金属箔，给出快电子、EMP 和中子产额增强结果，直接补强激光驱动次级源、靶前等离子体控制和转换效率优化方向。

### 2) Experimental demonstration of Flying-Focus enhanced Thomson scattering

- 作者：E. Gerstmayr; C. Mariani; R. Fitzgarrald; M. VanDusen-Gross; C. Berger; Q. Chen; A. Di Piazza; M. S. Formanek; D. H. Froula; C. G. R. Geddes; A. J. Gonsalves; B. Greenwood; R. Jacob; A. Lu; A. McIlvenny; K. Nakamura; L. Obst-Huebl; J. P. Palastro; A. Picksley; K. Poder; D. Ramsey; H. G. Rinderknecht; G. Sarri; A. G. R. Thomas; J. van Tilborg; M. J. V. Streeter
- 期刊/平台：arXiv preprint
- DOI：https://doi.org/10.48550/arXiv.2607.15805
- 真实发表日期：2026-07-17
- 来源链接：https://arxiv.org/abs/2607.15805
- 与方向关系：论文实验展示 Flying-Focus 时空整形激光增强 LWFA 电子束 Thomson scattering X 射线源，直接关联激光加速电子束应用、紧凑高亮度辐射源和束激光同步控制。

### 3) Surrogate modeling of drift-reduced Braginskii turbulence with resistivity-conditioned Koopman neural operators

- 作者：Ameir Shaa; Kyungtak Lim; Long Shan Chan; Claude Guet
- 期刊/平台：arXiv preprint
- DOI：https://doi.org/10.48550/arXiv.2607.15857
- 真实发表日期：2026-07-17
- 来源链接：https://arxiv.org/abs/2607.15857
- 与方向关系：论文把 Koopman neural operator 用于三维边界等离子体湍流代理建模，补强机器学习、等离子体数值模拟加速和诊断代理模型方向。

## 检索与去重执行记录

- 检索日期：2026-07-21。
- 重点检索方向：HPL/JPP 正式来源可见增量，以及 arXiv `physics.plasm-ph`、`physics.acc-ph`、`physics.comp-ph`、`nucl-ex`、`physics.ins-det` 中与激光等离子体、HEDP、PIC/数值模拟、激光加速束流应用、实验诊断和机器学习模拟相关的最新条目。
- 去重基线：`state/processed_articles.json`、`state/daily_retry_candidates.json` 与历史 `daily/` 全文检索。
- 去重结果：`10.1017/hpl.2026.10182`、`10.48550/arXiv.2607.15805`、`10.48550/arXiv.2607.15857` 均未出现在处理台账、重试队列或历史 daily 中。
- 正式来源复查：Cambridge HPL accepted manuscripts 中 `10.1017/hpl.2026.10182` 为本轮最强非重复正式来源；HPL 其他可见未入库 DOI 多偏激光器件或光学元件，JPP 新 DOI 多偏磁约束基础与校正条目，未优先于本轮三条候选。
- 跳过记录：`10.48550/arXiv.2607.15805` 同主题邻近条目 `10.48550/arXiv.2607.15788` 也与 inverse Compton source 相关，但本轮优先选择已有实验展示的 Flying-Focus Thomson scattering；`10.48550/arXiv.2607.15921` 与 SpinPIC2D 重联相关但主题更偏空间/天体 pair plasma，未进入今日三条。

## 下载与校验状态

- 当日执行了 3 条候选论文 PDF 下载尝试，详见 `daily/2026-07-21/*.download_report.json`。
- 结果：1 条通过 Cambridge 官方 PDF 链路下载成功，2 条通过官方 arXiv PDF 链路下载成功，均通过 `%PDF-` 文件头校验。
- 今日没有重新运行 `scripts/retry_download_queue.py`，因为旧重试队列仍是 12 条明确来源侧限制条目，继续全量重试收益很低。

## 笔记产出

- 已生成 3 份中文结构化笔记：
  - `daily/2026-07-21/notes/Zitao Wang et al. - 2026 - Dual picosecond petawatt secondary sources.md`
  - `daily/2026-07-21/notes/E Gerstmayr et al. - 2026 - Flying-Focus enhanced Thomson scattering.md`
  - `daily/2026-07-21/notes/Ameir Shaa et al. - 2026 - Braginskii turbulence Koopman neural operators.md`

## 状态更新

- `state/processed_articles.json`：从 211 条增至 214 条。
- `state/daily_retry_candidates.json`：保持 12 条，无新增来源失败重试记录。
- 当前“已补回 PDF 但尚无中文结构化笔记”的历史条目仍需后续专项清理；本轮不扩展旧重试队列。

## 当日总结

- 今天补强了激光驱动多类次级源、LWFA 电子束辐射源和 ML 等离子体湍流代理建模三条主线。
- 如果只优先读一篇，建议先读 `10.1017/hpl.2026.10182`，因为它是正式来源且与激光-靶耦合、快电子增强和中子/EMP 次级源优化直接相关。
