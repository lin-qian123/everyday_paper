# 每日论文索引 - 2026-09-07

## 今日概览

- 运行日期：2026-09-07
- 新增论文数：3
- 重点来源：3 篇 High Power Laser Science and Engineering 正式开放 accepted manuscripts。
- 主题分布：TNSA 质子谱—同位素产额联合诊断、LFEX 薄箔质子能谱束团化、双锥点火中金污染的时间分辨背光与涂层缓解。
- 检索范围：检查 Cambridge HPLSE accepted manuscripts / latest volume、APS PRResearch / PRE accepted 增量、官方 arXiv 目标分类及 laser–plasma、PIC、strong-field QED、γ / 光核 / 中子 / 同位素、诊断和 radiation protection 关键词。arXiv 最新目标分类记录仍停留在 2026-09-03 批次，因此今天转向未入库的高质量正式全文。
- 去重：按 DOI、规范化标题、历史 daily、重试队列、摘要和物理场景核对 `state/processed_articles.json`；3 篇均未入库且不是近期条目的内容近重复。
- PDF / 正文：3 份 Cambridge 开放全文通过 PDF 文件头、`file` 类型、`pdfinfo` 页数 / 元数据、SHA-256 和非空 `pdftotext -layout`。当前环境没有 `MINERU_TOKEN`，因此未声称完成 MinerU 转换；9 张图由 PDF 页面渲染并人工查看。完整校验见 [pdf_validation.json](pdf_validation.json)。

## 论文清单

### 1. Detailed study of non-equilibrium characteristics of quasi-neutral TNSA plasmas

- DOI：[10.1017/hpl.2026.10188](https://doi.org/10.1017/hpl.2026.10188)
- 在线日期：2026-08-03
- 来源：[Cambridge Core 论文页](https://www.cambridge.org/core/journals/high-power-laser-science-and-engineering/article/detailed-study-of-nonequilibrium-characteristics-of-quasineutral-tnsa-plasmas/EB854A90AE81D74E778949520030BE9E)
- 期刊 / 平台：High Power Laser Science and Engineering accepted manuscript
- 本地 PDF：daily/2026-09-07/pdfs/Zhu et al. - 2026 - Non-equilibrium quasi-neutral TNSA plasmas.pdf
- 中文笔记：[Zhu et al. - 2026 - Non-equilibrium quasi-neutral TNSA plasmas.md](notes/Zhu%20et%20al.%20-%202026%20-%20Non-equilibrium%20quasi-neutral%20TNSA%20plasmas.md)
- 来源影响力分：8/10
- 专业相似度分：10/10
- 推荐理由：少见地把逐发 TNSA 质子谱、HPGe 同位素衰变、反应截面和 SRIM 射程接成 pitcher–catcher 核反应诊断链，直接回应同位素与 $p{}^{11}\mathrm{B}$ 应用。
- 一句话总结：实测 $^{11}\mathrm{C}/{}^{7}\mathrm{Be}=0.37$ 对应 $kT=0.971$ MeV 的等效温度；平均 $8.5\times10^8$、最高 $(1.6\pm0.5)\times10^9$ 个 $\alpha$ 是基于同位素比与截面反演，不是直接 $\alpha$ 计数。

### 2. Experimental Investigation of laser driven proton bunching with plastic foil targets

- DOI：[10.1017/hpl.2026.10184](https://doi.org/10.1017/hpl.2026.10184)
- 在线日期：2026-07-22
- 来源：[Cambridge Core 论文页](https://www.cambridge.org/core/journals/high-power-laser-science-and-engineering/article/experimental-investigation-of-laser-driven-proton-bunching-with-plastic-foil-targets/314E4B697ED3C4331A35C84B7E479AE8)
- 期刊 / 平台：High Power Laser Science and Engineering accepted manuscript
- 本地 PDF：daily/2026-09-07/pdfs/Batani et al. - 2026 - Laser-driven proton bunching with plastic foils.pdf
- 中文笔记：[Batani et al. - 2026 - Laser-driven proton bunching with plastic foils.md](notes/Batani%20et%20al.%20-%202026%20-%20Laser-driven%20proton%20bunching%20with%20plastic%20foils.md)
- 来源影响力分：8/10
- 专业相似度分：10/10
- 推荐理由：两轮 LFEX 实验同时给出质子、碳和热电子谱，直接观察中能质子峰，并用碳电荷态、解析标度和 SMILEI 检查 Coulomb-piston 图景。
- 一句话总结：6 μm CH 箔在 2024 年的峰约 2.7–5 MeV，2025 年代表性发次约 8 MeV；这是 6 发的能谱峰证据，不能直接等同于时间短束团、应用产额或装置重复性。

### 3. Observation and Mitigation of Kelvin–Helmholtz Instability-Driven Gold Contamination in Double-Cone Ignition

- DOI：[10.1017/hpl.2026.10181](https://doi.org/10.1017/hpl.2026.10181)
- 在线日期：2026-07-23
- 来源：[Cambridge Core 论文页](https://www.cambridge.org/core/journals/high-power-laser-science-and-engineering/article/observation-and-mitigation-of-kelvinhelmholtz-instabilitydriven-gold-contamination-in-doublecone-ignition/4E355E2AFD8D14131309D4485CF3E91C)
- 期刊 / 平台：High Power Laser Science and Engineering accepted manuscript
- 本地 PDF：daily/2026-09-07/pdfs/Zhang et al. - 2026 - Kelvin-Helmholtz gold contamination in DCI.pdf
- 中文笔记：[Zhang et al. - 2026 - Kelvin-Helmholtz gold contamination in DCI.md](notes/Zhang%20et%20al.%20-%202026%20-%20Kelvin-Helmholtz%20gold%20contamination%20in%20DCI.md)
- 来源影响力分：8/10
- 专业相似度分：9/10
- 推荐理由：在 SG-II Upgrade 上用 Cu K$\alpha$ 时间分辨背光直接比较无涂层 / 2 μm CH 涂层双锥，并由三维 FLASH 解释 Au pre-plasma 与 KHI 卷吸。
- 一句话总结：涂层提高透射率有实验支撑；Au 质量分数、KHI onset 从 4.1 延迟到 4.6 ns 和 bremsstrahlung 惩罚是模型量，尚无点火增益或中子产额闭环。

## 未入库但需保留的候选

- [Spatiotemporal ionization dynamics in nonthermal copper plasma pumped by femtosecond relativistic laser pulse](https://journals.aps.org/prresearch/accepted/10.1103/sgyf-lrw1)、[Direct observation of saturated heat-flux inhibition by magnetic fields in laser-produced plasmas](https://journals.aps.org/prresearch/accepted/10.1103/2rqf-hq77) 和 [Cone-guided phase-space control of laser-driven proton beams](https://journals.aps.org/pre/accepted/10.1103/d45l-hsgg) 仍高度相关；本轮逐一重试 APS PDF 和 DOI 路径，全部为 HTTP 403，且未找到合法开放作者稿，因此不从摘要扩写笔记。
- HPLSE `10.1017/hpl.2026.10192` 是 3D EPOCH 的 light-spring 螺旋电子束方案，`10.1017/hpl.2026.10191` 是 FBPIC–ELEGANT–GENESIS 的 LWFA-FEL start-to-end 优化；两份 PDF 均可读取，但本轮优先三篇实验实证，后两者不写成已实现束流或 FEL 输出。
- arXiv:2609.03822 的 Geant4 rare-event shielding importance sampling 与辐射防护相关；它是通用模拟方法，相对本轮直接的激光质子—核反应证据链优先级较低。

## 当日综合总结

- Zhu 把“质子谱—同位素活化—反应截面”连在同一分析中，是当前库里更接近端到端激光核应用的一篇；最关键的边界是同位素衰变有实测，逐发核产额与 $\alpha$ 数仍含反演。
- Batani 说明束流优化不能只追求 cutoff：靶厚、脉宽、电子 recirculation 和碳电荷态共同决定能谱峰。但“energy bunch”不自动等于短脉宽、低发散或高重复束团。
- Zhang 的 CH 涂层是可操作的靶设计改进，实验透射率与 FLASH 机制图相互支持；仍不能把污染降低升级为已实现点火、增益或中子产额。
- 推荐阅读顺序：先读 Zhu 看激光质子到同位素 / $p{}^{11}\mathrm{B}$ 的应用链，再读 Batani 理解质子峰如何受多离子前沿控制，最后读 Zhang 看 HED 靶界面污染如何用诊断与材料结构共同约束。
