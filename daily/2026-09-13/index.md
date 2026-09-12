# 每日论文索引 - 2026-09-13

## 今日概览

- 运行日期：2026-09-13
- 新增论文数：3
- 最新性：周日运行时，官方 arXiv 目标分类的最新提交批次仍为 2026-09-10；本轮从该窗口中选择三个尚未入库、且证据类型互补的高相关工作。
- 主题分布：TJ-II 实验剖面约束的 inverse PINN 输运反演、结构化光阴极的 WarpX/IMPACT-T 多尺度束流模拟、同步辐射冷却等离子体的解析—PIC—流体交叉验证。
- 检索范围：检查官方 arXiv `physics.plasm-ph`、`physics.acc-ph`、`physics.comp-ph`、`physics.ins-det`、`physics.med-ph` 与 `nucl-ex` 近期列表，并按 laser plasma、PIC、radiation reaction、HEDP、ML 与 beam application 做定向检索。多源聚合器本轮没有返回可用记录，因此不宣称覆盖全部数据库。
- 去重：按 DOI/arXiv identifier、规范化标题、历史 `daily/`、344 条完成台账、17 条重试队列、摘要及物理场景核对，三篇均为新记录。
- PDF / 正文：3 份官方 arXiv PDF 通过 `%PDF-`、`file`、`pdfinfo`、SHA-256 和非空 `pdftotext -layout`；三篇均完成 MinerU 正文/图件转换，保留并逐张查看 12 张关键图。完整记录见 [pdf_validation.json](pdf_validation.json)。

## 论文清单

### 1. Physics-Informed Neural Networks to Infer the Perpendicular Energy Conductivity in the Scrape-Off Layer of Stellarator Devices

- DOI：[10.48550/arXiv.2609.11628](https://doi.org/10.48550/arXiv.2609.11628)
- arXiv v1：2026-09-10
- 来源：[arXiv 摘要页](https://arxiv.org/abs/2609.11628)
- 期刊 / 平台：arXiv 预印本
- 本地 PDF：`daily/2026-09-13/pdfs/Gallego et al. - 2026 - PINN inference of SOL perpendicular conductivity.pdf`
- 中文笔记：[Gallego et al. - 2026 - PINN inference of SOL perpendicular conductivity.md](notes/Gallego%20et%20al.%20-%202026%20-%20PINN%20inference%20of%20SOL%20perpendicular%20conductivity.md)
- 来源影响力分：7/10
- 专业相似度分：9/10
- 推荐理由：把 TJ-II 真实稀疏温度/密度剖面、一维 SOL 能量守恒、LCFS 功率边界和 bootstrap 不确定度接成可审计的输运反问题。
- 一句话总结：同族合成数据的有约束区中 $\kappa_\perp$ 通常恢复到约 10% 内，而 TJ-II 实验的物理一致性分数仅约 0.82；所得系数是受一维简化模型约束的有效反演量，不是直接输运测量或跨装置标度律。

### 2. Coupling periodic-cell and finite-bunch dynamics for structured photocathodes

- DOI：[10.48550/arXiv.2609.11844](https://doi.org/10.48550/arXiv.2609.11844)
- arXiv v1：2026-09-10
- 来源：[arXiv 摘要页](https://arxiv.org/abs/2609.11844)
- 期刊 / 平台：arXiv 预印本
- 本地 PDF：`daily/2026-09-13/pdfs/Bazyl and Zagorodnov - 2026 - Structured photocathode multiscale coupling.pdf`
- 中文笔记：[Bazyl and Zagorodnov - 2026 - Structured photocathode multiscale coupling.md](notes/Bazyl%20and%20Zagorodnov%20-%202026%20-%20Structured%20photocathode%20multiscale%20coupling.md)
- 来源影响力分：7/10
- 专业相似度分：9/10
- 推荐理由：用周期单胞 WarpX 响应修正有限平坦载体束团，在可承担的 41×41 阵列上给出相空间和切片量的直接数值对照，再扩展到 100 pC 注入器。
- 一句话总结：同一 WarpX 模型内，局部组合把切片能散轮廓误差由 30.7% 降至 2.0%；52 万孔注入器结果没有全分辨率真值，且 WarpX/IMPACT-T 载体基线已有 2.5%–9.4% 偏差，不能写成实验束流或通用精度保证。

### 3. Two-Phase Structure of Synchrotron-Cooling-Unstable Relativistic Plasma

- DOI：[10.48550/arXiv.2609.07793](https://doi.org/10.48550/arXiv.2609.07793)
- arXiv v1：2026-09-07
- 来源：[arXiv 摘要页](https://arxiv.org/abs/2609.07793)
- 期刊 / 平台：arXiv 预印本
- 本地 PDF：`daily/2026-09-13/pdfs/Wierzchucka et al. - 2026 - Two-phase synchrotron-cooling-unstable relativistic plasma.pdf`
- 中文笔记：[Wierzchucka et al. - 2026 - Two-phase synchrotron-cooling-unstable relativistic plasma.md](notes/Wierzchucka%20et%20al.%20-%202026%20-%20Two-phase%20synchrotron-cooling-unstable%20relativistic%20plasma.md)
- 来源影响力分：7/10
- 专业相似度分：10/10
- 推荐理由：把同步辐射产生的负压强各向异性、firehose 阈值与宏观磁场—密度冷却反馈连成解析机制，并明确比较 OSIRIS 辐射 PIC、线性理论和两相流体。
- 一句话总结：早期 $t\lesssim2.2\tau_0$ 的 PIC 与流体/理论约在 7% 内一致；之后低温区被有限宏粒子数造成的人工各向同性化污染，长期约 $10\tau_0$ 饱和来自流体延拓，且 $\chi_{\mathrm{QED}}\sim7\times10^{-4}$，不是强场 QED 验证。

## 未入库候选与取舍

- 本轮没有出现晚于 2026-09-10 的官方 arXiv 分类批次，因此没有用较旧或相关性较弱的论文凑数。
- 一篇与 2026-09-12 已入库 `kobra` 工作同属近期 Vlasov/plasma-wall 数值主线的候选因内容增量较小被跳过；优先保留三种不同证据类型。
- 17 条结构化重试候选没有变化。本轮未对长期 Elsevier/Nature/IOP 墙重复空跑，也没有把 APS `HTTP 403` 摘要扩写成全文笔记。
- 扩展的 laser-accelerated beam → converter/catcher → γ/中子/活化/剂量链仍是优先方向，但本轮没有发现比当前三篇更直接且可获取的非重复新全文。

## 当日综合总结

- Gallego 给出“真实诊断 + 简化守恒方程 + inverse PINN”的实验约束反演范式，但真实残差同时暴露约化方程的不充分性；这比单独展示平滑拟合更有价值。
- Bazyl–Zagorodnov 给出局部高分辨率响应库与全局低分辨率载体的组合思路；可信区来自小阵列全分辨率对照，注入器尺度仍是近似外推。
- Wierzchucka 的强项是把数值伪效应写进主结论：冷却会持续恶化每 Debye 面积宏粒子数，早期收敛不等于晚期可信。
- 推荐阅读顺序：先读 Wierzchucka 建立辐射 PIC 的误差警觉，再读 Gallego 看实验反问题怎样用残差审计模型，最后读 Bazyl 比较多尺度响应组合的验证层级。
