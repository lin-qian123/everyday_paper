# 每日论文索引 - 2026-09-01

## 今日概览

- 运行日期：2026-09-01
- 新增论文数：3
- 重点来源：3 篇官方 arXiv 预印本；其中 `2608.26313` 使用 2026-08-28 更新的 v2。
- 主题分布：flying-focus 强场 QED 对产生、MAST-U 神经网络实时虚拟电路主动控制、强化学习控制简化等离子体湍流—zonal-flow 转换。
- 检索范围：复查 Cambridge HPL 最新/accepted manuscripts；检查官方 arXiv `physics.plasm-ph`、`physics.acc-ph`、`physics.comp-ph`、`nucl-ex`、`physics.ins-det`，并对 `hep-ph` 强场 QED 与激光束流应用关键词定向检索。截至本轮官方 API 可见的新提交最新日期为 2026-08-28。
- 去重：按 DOI、规范化标题、历史 daily、重试队列和摘要/实验语境核对 `state/processed_articles.json`。`2608.28468` 是昨日 PCS 集成论文 `2608.26216` 的主动实验续篇，保留；`2608.28301` 与已入库的 plasma-bubble vortex-electron 理论内容接近，本轮跳过。
- PDF/正文：3 份官方 arXiv PDF 均通过 `%PDF-` 文件头、`file` 类型、`pdfinfo` 页数/元数据、SHA-256、非空 `pdftotext -layout` 和 MinerU Markdown 转换。字节数、页数、哈希与解析结果见 [`pdf_validation.json`](pdf_validation.json)。

## 论文清单

### 1. Enhancement of nonlinear pair production in a flying-focus pulse

- DOI：[10.48550/arXiv.2608.26313](https://doi.org/10.48550/arXiv.2608.26313)
- 提交/修订日期：2026-08-26 / 2026-08-28（v2）
- 来源：[arXiv 摘要页](https://arxiv.org/abs/2608.26313)
- 期刊 / 平台：arXiv preprint v2
- 本地 PDF：`daily/2026-09-01/pdfs/Rahman et al. - 2026 - Enhancement of nonlinear pair production in a flying-focus pulse.pdf`
- 中文笔记：[Rahman et al. - 2026 - Enhancement of nonlinear pair production in a flying-focus pulse.md](notes/Rahman%20et%20al.%20-%202026%20-%20Enhancement%20of%20nonlinear%20pair%20production%20in%20a%20flying-focus%20pulse.md)
- 专业相似度分：`5/5`
- 推荐理由：直接连接 flying-focus 光场设计、强场 QED 标度和 NCS→NBWPP 少代级联，并在等激光能量条件下给出可比较的对产额提升。
- 一句话总结：Ptarmigan/LCFA 模拟给出 1 J FF 对 10/20/50 GeV 理想单能光子的最大对产额相对 SFG 提高 `12%/29%/76%`；这是数值方案，不是对产生观测或完整真实束流容差结果。

### 2. Real-time virtual circuits for plasma shape control via neural network emulators: experimental demonstration on MAST Upgrade

- DOI：[10.48550/arXiv.2608.28468](https://doi.org/10.48550/arXiv.2608.28468)
- 提交日期：2026-08-28；稿件日期：2026-08-31
- 来源：[arXiv 摘要页](https://arxiv.org/abs/2608.28468)
- 期刊 / 平台：arXiv preprint
- 本地 PDF：`daily/2026-09-01/pdfs/Amorisco et al. - 2026 - Real-time virtual circuits experimental demonstration on MAST-U.pdf`
- 中文笔记：[Amorisco et al. - 2026 - Real-time virtual circuits experimental demonstration on MAST-U.md](notes/Amorisco%20et%20al.%20-%202026%20-%20Real-time%20virtual%20circuits%20experimental%20demonstration%20on%20MAST-U.md)
- 专业相似度分：`4/5`
- 推荐理由：把昨日的 RTVC 软件/piggyback 验证推进到真实 MAST-U 主动闭环炮次，并同时暴露七参数伪逆病态和状态缺失边界。
- 一句话总结：同一 emulator 在四组炮次上完成常规形状、扰动、divertor-leg 和强演化控制；但本文没有传统 VC 性能优越性对照，54002/54168 仍出现 nose interaction 与病态放大。

### 3. Reinforcement-learning control of turbulence transition in the modified Hasegawa–Wakatani system

- DOI：[10.48550/arXiv.2608.27845](https://doi.org/10.48550/arXiv.2608.27845)
- 提交日期：2026-08-28；稿件日期：2026-08-31
- 来源：[arXiv 摘要页](https://arxiv.org/abs/2608.27845)
- 期刊 / 平台：arXiv preprint
- 本地 PDF：`daily/2026-09-01/pdfs/Sun et al. - 2026 - Reinforcement-learning control of turbulence transition in modified Hasegawa-Wakatani system.pdf`
- 中文笔记：[Sun et al. - 2026 - Reinforcement-learning control of turbulence transition in modified Hasegawa-Wakatani system.md](notes/Sun%20et%20al.%20-%202026%20-%20Reinforcement-learning%20control%20of%20turbulence%20transition%20in%20modified%20Hasegawa-Wakatani%20system.md)
- 专业相似度分：`4/5`
- 推荐理由：把有限控制预算、输运积分、reward hacking、物理独立诊断和 physics-informed warm buffer 同时纳入等离子体 RL 研究。
- 一句话总结：在二维改写 MHW 模型中，SAC schedule 同预算下的平均 return `−573` 优于两基线，TD3 找到 `[-9,-9,+9,+9]` 反对称 forcing；两者都接近开环且未在真实装置验证。

## 当日综合总结

- 共同趋势：三篇都在优化“强度以外的结构”——FF 用相互作用时间换产额，RTVC 用实时局部响应替代离线 phase schedule，RL 用时序/空间 actuator 结构优化累计输运。
- 实验与模拟边界：Amorisco 是真实 MAST-U 主动控制实验；Rahman 是解析标度加 Ptarmigan Monte Carlo；Sun 是改写 MHW 的 JAX/RL 数值实验。三者不可混写为同等级实验证据。
- 值得跟进的问题：把真实 γ 光子谱/同步误差卷入 FF 对产生；为 RTVC 加 passive-current/profile 状态和正则伪逆；将 MHW RL 推进到 3D edge model、真实 actuator、噪声和时延。
- 对当前研究最值得优先阅读的论文：强场 QED 方向先读 Rahman；实验控制链先连读昨日 Marshall 与今日 Amorisco；希望设计 physics-informed RL 验证协议时再读 Sun。
