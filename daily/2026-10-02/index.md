# 每日论文索引 - 2026-10-02

## 今日概览

- 运行日期：2026-10-02
- 新增论文数：4（1 篇已分配 DOI 的 APS Accepted Paper，3 篇 2026-09-30 投稿、2026-10-01 官方公告的 arXiv 预印本）
- 最新性：核对官方 arXiv Atom/API 的 2026-10-01 公告批次，并用 Crossref 检查 2026-09-30 至 10-02 正式元数据；正式 *Laser Physics Letters* `10.1088/1612-202x/aeab55` 因全文受限转入重试。
- 主题分布：LWFA—取向晶体 γ/正电子/光核中子源；逃逸电子壁载荷与熔化风险代理；stellarator alpha 粒子多谐波混沌；等离子体通道内相对论激光质心阻尼。
- 去重：按 DOI/arXiv identifier、规范化标题、398 条完成台账、20 条重试队列、历史 `daily/`、摘要和物理场景检查；4 篇均为独立作品。
- PDF / 正文：4 份 PDF 均通过 `%PDF-`、`file`、`pdfinfo`、SHA-256 与非空 `pdftotext -layout`；16 个选定页面完成渲染和人工查看。APS 条目的本地全文是同作品 arXiv 作者预印本，不是 APS VOR。
- 重试：新增 1 条 IOP/HTML 阻塞，队列 `20 → 21`；其他既有来源受限记录未重复空跑。
- 覆盖边界：多来源搜索层返回 0 条可用结果，Crossref 主题检索用于正式元数据核对，arXiv Atom/API 用于公告批次；这是定向增量筛选，不宣称穷尽全部期刊或数据库。

## 论文清单

### 1. Compact ultrafast intense LWFA-driven crystal-based source of γ-radiation, positrons and neutrons

- 标识符：[arXiv:2609.40005](https://arxiv.org/abs/2609.40005)；归档 DOI `10.48550/arXiv.2609.40005`
- 提交日期：2026-09-30（2026-10-01 官方公告批次）
- 期刊 / 平台：arXiv 预印本
- 本地 PDF：`daily/2026-10-02/pdfs/Sytov et al. - 2026 - LWFA crystal gamma positron neutron source.pdf`
- 中文笔记：[Sytov et al. - 2026 - LWFA crystal gamma positron neutron source.md](notes/Sytov%20et%20al.%20-%202026%20-%20LWFA%20crystal%20gamma%20positron%20neutron%20source.md)
- 来源影响力分：8/10
- 专业相似度分：10/10
- 推荐理由：直接覆盖激光电子束—转换靶—γ/正电子/光核中子链，并把晶向、厚度、散角与接受角的效率增益放进同一 Geant4 设计。
- 一句话总结：在 `3 GeV、200 pC` 缩放下，钨 `⟨111⟩` 取向把随机晶向约 `1.9×10^7` 中子/脉冲提高到 `4.3×10^7`，但这是 FBPIC/Wake-T/Geant4 预测，非装置实测平均通量。

### 2. FIREWALL: A surrogate model for the rapid assessment of tokamak wall loading and melting by runaway electrons

- 标识符：[arXiv:2609.40132](https://arxiv.org/abs/2609.40132)；归档 DOI `10.48550/arXiv.2609.40132`
- 提交日期：2026-09-30（2026-10-01 官方公告批次）
- 期刊 / 平台：arXiv 预印本
- 本地 PDF：`daily/2026-10-02/pdfs/Svensson et al. - 2026 - FIREWALL runaway electron wall surrogate.pdf`
- 中文笔记：[Svensson et al. - 2026 - FIREWALL runaway electron wall surrogate.md](notes/Svensson%20et%20al.%20-%202026%20-%20FIREWALL%20runaway%20electron%20wall%20surrogate.md)
- 来源影响力分：7/10
- 专业相似度分：9/10
- 推荐理由：把逃逸电子输运、材料体沉积、热响应和全装置防护筛查连成轻量工作流，适合比较“快速风险定位”和“高保真损伤计算”的边界。
- 一句话总结：最重载 ITER 壁元的熔化时刻可与 Geant4–MEMENTO 接近，但外围/宽能谱场景可差 `0.07–0.12 ms`，且熔点后的相变与熔池演化不在模型内。

### 3. Phase-Space Non-Integrability of Alpha Particles in Near-Omnigeneous Stellarators

- 标识符：[arXiv:2609.39376](https://arxiv.org/abs/2609.39376)；归档 DOI `10.48550/arXiv.2609.39376`
- 提交日期：2026-09-30（2026-10-01 官方公告批次）
- 期刊 / 平台：arXiv 预印本（标注 under consideration for *Journal of Plasma Physics*）
- 本地 PDF：`daily/2026-10-02/pdfs/Lachmann et al. - 2026 - Alpha particle phase space non integrability.pdf`
- 中文笔记：[Lachmann et al. - 2026 - Alpha particle phase space non integrability.md](notes/Lachmann%20et%20al.%20-%202026%20-%20Alpha%20particle%20phase%20space%20non%20integrability.md)
- 来源影响力分：7/10
- 专业相似度分：9/10
- 推荐理由：用 WBA 相空间图量化 QS 误差、多谐波 Alfvén 模和 alpha 损失的非线性关系，并显示单最大谐波会严重低估混沌。
- 一句话总结：LBQA 的 35 谐波波场给出 `0.80` 混沌比例和 `0.41` 出生损失，SQuID 为 `0.76/0.22`；均是无碰撞 guiding-centre marker 结果，不是反应堆诊断。

### 4. Damping dynamics of the centroid oscillation of a relativistic laser pulse in a plasma channel

- 标识符：[DOI:10.1103/79h1-q62n](https://doi.org/10.1103/79h1-q62n)；同作品作者稿 [arXiv:2605.03918](https://arxiv.org/abs/2605.03918)
- 正式发表日期：2026-09-30
- 期刊 / 平台：*Physical Review Applied*；本地 PDF 为对应 arXiv v1 作者预印本，非 APS VOR
- 本地 PDF：`daily/2026-10-02/pdfs/Xia et al. - 2026 - Laser centroid oscillation damping.pdf`
- 中文笔记：[Xia et al. - 2026 - Laser centroid oscillation damping.md](notes/Xia%20et%20al.%20-%202026%20-%20Laser%20centroid%20oscillation%20damping.md)
- 来源影响力分：9/10
- 专业相似度分：10/10
- 推荐理由：APS Accepted Paper 元数据出现后补收，直接讨论长通道 LWFA 对位置/角度抖动的响应，并用解析模分解区分泄漏、walk-off 与相对论 phase mixing。
- 一句话总结：`a0≈2.5` 的三维 OSIRIS PIC 中，切片频率 chirp 使整体质心 phase-mixing 阻尼长度约 `86 mm`；没有 HOFI 通道实验或端到端电子束品质验证。

## 未入库候选与取舍

- 正式 *Laser Physics Letters* `10.1088/1612-202x/aeab55` 研究倾斜非对称薄箔的 TNSA 质子能量与发散控制，主题高度相关；官方 PDF、DOI 和文章页均返回 HTML，且未找到同题 arXiv/合法作者稿，故只加入结构化重试，不从摘要生成笔记。
- `arXiv:2609.38438` 的预训练 VAE 湍流代理与机器学习方向相关，但本轮优先保留新公告批次和与壁防护/alpha 输运更直接的增量。
- `arXiv:2609.36769` 的毛细管液体闪烁体中子探测器为上一批次候选，直接诊断价值较高，但最新性和激光转换靶关联弱于所选晶体光核中子链。
- `arXiv:2609.40318` 的 CBM RICH 前端电子学、`2609.39400` 的地下氩活度测量以及通用核物理 AI 综述 `2609.38711` 距当前激光/HEDP/PIC 主线更远。
- 20 条既有来源受限记录没有新的合法全文线索，继续保留重试状态，不从摘要生成笔记。

## 当日综合总结

- 最直接的应用增量是取向晶体方案：它把高品质 LWFA 电子束的散角控制与 γ、正电子、光核中子产额联系起来，也暴露出峰值瞬时率、逐脉冲产额和平均通量三种指标不能混用。
- FIREWALL 和 alpha 相空间工作分别展示“快速筛查不能替代熔化后高保真模型”和“混沌比例不能替代到壁损失”的同一证据原则：中间代理量必须经过应用端闭合。
- 正式 PRApplied 论文解释了激光质心抖动为何在相对论通道中快速失相，但阻尼不自动等于电子束品质稳定，仍需把入射抖动、注入和束流诊断串起来。
- 推荐阅读顺序：取向晶体 γ/中子链 → PRApplied 通道质心阻尼 → FIREWALL 壁损伤筛查 → stellarator alpha 混沌，依次覆盖束源、传播、材料防护和聚变粒子输运。
