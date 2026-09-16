# 每日论文索引 - 2026-09-17

## 今日概览

- 运行日期：2026-09-17
- 新增论文数：3
- 最新性：官方 arXiv 目标分类本轮可见的最新批次为 2026-09-16；三篇入选稿均于 2026-09-15 提交，并在该批次公开列出。正式来源复查发现 *Physics of Plasmas* `10.1063/5.0347124`，但其预印本 `arXiv:2606.04887` 已于 2026-06-14 入库，按标题硬去重不重复收录。
- 主题分布：透明可扩展的电磁 PIC 代码与分层验证；LAPD 强非线性 Alfvén 波实验—Hall-MHD—混合 PIC 机制链；面向 bump-on-tail/ITG 的非线性精确响应与等变神经闭合。
- 检索范围：检查官方 arXiv `physics.plasm-ph`、`physics.acc-ph`、`physics.comp-ph`、`nucl-ex`、`physics.ins-det`、`physics.optics`、`physics.atom-ph`、`astro-ph.HE`、`nucl-th` 与 `hep-ph` 新增/交叉列表，并用 Crossref、出版商落地页定向复查近期正式论文。本地多源聚合器返回 0 条可用记录，故采用官方分类页、DOI 元数据和文章页核验，不宣称穷尽所有数据库。
- 去重：按 DOI/arXiv identifier、规范化标题、历史 `daily/`、354 条完成台账、16 条重试队列、摘要和物理场景核对；三篇入选稿均未入库，AIP 正式版因预印本已存在而排除，重试队列不变。
- PDF / 正文：三份官方 arXiv PDF 均通过 `%PDF-`、`file`、`pdfinfo`、SHA-256 和非空 `pdftotext -layout`；全部完成 MinerU 转换，保留并逐张查看 12 张关键图。完整记录见 [pdf_validation.json](pdf_validation.json)。

## 论文清单

### 1. KEMPIC-3D: A transparent and extensible electromagnetic Particle-in-Cell framework for kinetic plasma simulations

- 标识符：[arXiv:2609.16575](https://arxiv.org/abs/2609.16575)；归档 DOI `10.48550/arXiv.2609.16575`
- 提交日期：2026-09-15
- 期刊 / 平台：arXiv 预印本
- 本地 PDF：`daily/2026-09-17/pdfs/Lopez et al. - 2026 - KEMPIC-3D PIC framework.pdf`
- 中文笔记：[Lopez et al. - 2026 - KEMPIC-3D PIC framework.md](notes/Lopez%20et%20al.%20-%202026%20-%20KEMPIC-3D%20PIC%20framework.md)
- 来源影响力分：6/10
- 专业相似度分：9/10
- 推荐理由：把 Yee、Boris、CIC 与 ZigZag 电流沉积的离散契约、逐层验证和短程 LWFA 示范集中写清楚，适合审计一个教学/研究型电磁 PIC 实现应如何从部件验证走到耦合验证。
- 一句话总结：作者恢复 Boris/Yee 二阶收敛、$10^{-13}$ 量级离散连续性和低于 $7.5\times10^{-4}$ 的冷等离子体总能量变化；但 LWFA 示例是 `Ny=2` 的准二维短程算例、不含注入或束流品质，源码也仍是“正式发表后公开”的承诺而非本轮可复现资产。

### 2. Strong Nonlinear Alfvén Wave Interactions in a Laboratory Plasma

- 标识符：[arXiv:2609.17162](https://arxiv.org/abs/2609.17162)；归档 DOI `10.48550/arXiv.2609.17162`
- 提交日期：2026-09-15；正文日期：2026-09-16
- 期刊 / 平台：arXiv 预印本
- 本地 PDF：`daily/2026-09-17/pdfs/Chen et al. - 2026 - Strong nonlinear Alfven wave interactions.pdf`
- 中文笔记：[Chen et al. - 2026 - Strong nonlinear Alfven wave interactions.md](notes/Chen%20et%20al.%20-%202026%20-%20Strong%20nonlinear%20Alfven%20wave%20interactions.md)
- 来源影响力分：8/10
- 专业相似度分：8/10
- 推荐理由：用可重复 LAPD 波幅扫描区分天线谐波与双波二次互调，再用 Hall-MHD 标度和三维混合 PIC 检验同向波在有限 $k_\perp d_i$ 下的耦合，是实验—理论—数值证据链较完整的基础等离子体工作。
- 一句话总结：反向和同向 `75/100 kHz` 波都产生宽频新模，同向 `175 kHz` 和频模的实测比值 `0.12` 与理论量级 `0.15` 接近，降低 $k_\perp d_i$ 后模拟峰约弱一个数量级；空间谱向更高 $k_\perp$ 移动支持小尺度传能，但尚未测得充分发展湍流的稳态惯性区或恒定能通量。

### 3. Nonlinear kinetic closures for linear instabilities

- 标识符：[arXiv:2609.17209](https://arxiv.org/abs/2609.17209)；归档 DOI `10.48550/arXiv.2609.17209`
- 提交日期：2026-09-15；正文日期：2026-09-16
- 期刊 / 平台：arXiv 预印本
- 本地 PDF：`daily/2026-09-17/pdfs/Paul et al. - 2026 - Nonlinear kinetic closures.pdf`
- 中文笔记：[Paul et al. - 2026 - Nonlinear kinetic closures.md](notes/Paul%20et%20al.%20-%202026%20-%20Nonlinear%20kinetic%20closures.md)
- 来源影响力分：7/10
- 专业相似度分：9/10
- 推荐理由：不仅给出 EKR 和等变 NN 的精度结果，还用 $N\ge2M-1$ 说明只读瞬时矩的闭合最多能辨认多少叠加模，并把神经闭合的等变性、Padé 的因果性和多模失败案例摆在同一框架中。
- 一句话总结：在 bump-on-tail 与 slab-ITG 线性模型中，EKR/$N=4$ NN 的增长率中位误差约达 $5\times10^{-5}$/$10^{-5}$，比 Hammett–Perkins 的百分比级误差低至多三阶；但训练真值来自解析线性矩层级，NN 没有一般因果保证，也未在非线性 Vlasov/PIC、湍流或生产流体代码中验证长期稳定性。

## 未入库候选与取舍

- `arXiv:2609.17151`（JC-PIC）给出约一百个低温等离子体 PIC-MCC 测试案例和 Windows 图形界面，资源价值较高，但与本轮 KEMPIC 的通用代码验证主题接近，且原创新物理密度低于入选三篇，保留为后续工具/教学线索。
- `arXiv:2609.16328`（Vlasov–Poisson–BGK characteristic mapping）展示三阶收敛和细尺度放大，方法扎实，但当前主题匹配与物理应用链弱于三篇入选稿。
- `arXiv:2609.17425` 讨论 drift-reduced Braginskii 能量守恒并以 GBS 量化常用近似，值得跟踪；本轮因与既有流体/数值守恒条目重合较多而不为凑数入库。
- `10.1063/5.0347124` 是 `arXiv:2606.04887`（方位角 Fourier 降阶 PIC）的正式 *Physics of Plasmas* 版本；规范化标题与 2026-06-14 台账条目完全相同，因此不作为新论文重复下载、记账或生成第二份笔记。
- `10.1364/OE.612056`（short-wavelength laser–nanofoil 产生阿秒电子束）与主题高度相关，但 Optica 官方页当前仍明确标注论文已接收、正式文章尚未上线，且没有官方 PDF；不从题名或元数据生成全文笔记，待正式全文发布后再核验。
- `10.1007/s10444-026-10364-x`（autoencoder + Hamiltonian NN 降阶 Vlasov–Poisson PIC）与本轮 Paul 的学习型闭合及既有降阶 PIC 条目重合，未优先于已取得全文的三篇。
- `10.1088/1361-6595/aea24a`（不同激光入射角下 Sn 等离子体 EUV/离子碎屑分离）是实验—辐射流体正式论文，但与近期已入库的 Sn/EUV 与辐射流体主题重叠较高，留作后续专题回看。
- 本批次没有发现同时闭合“激光加速电子/离子束 → 转换靶/捕获器 → γ/中子/光核或活化产额 → 剂量/屏蔽”的新实验论文；仍不以普通核物理、单纯束流模拟或相邻辐射方法替代端到端证据。

## 当日综合总结

- 三篇共同强调“结构约束比单张漂亮结果更重要”：PIC 需要离散连续性，Alfvén 波机制需要幅度/尺度控制，神经闭合需要等变性和可辨识度计数。
- 最强实验增量来自 LAPD 工作；KEMPIC 是实现验证稿，非线性闭合是线性解析真值上的方法稿。三者的 `PIC`、`实验` 和 `ML` 标签不能互相替代。
- 推荐阅读顺序：先看 Chen 图 1/3/5 理解观测—机制—级联边界；再看 Paul 图 2 理解单模精确为何不等于多模正确；最后看 KEMPIC 图 2/7/8 区分代码耦合验证与应用示范。
