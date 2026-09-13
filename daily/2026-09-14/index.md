# 每日论文索引 - 2026-09-14

## 今日概览

- 运行日期：2026-09-14
- 新增论文数：2
- 最新性：周一早间运行时，官方 arXiv 目标分类已更新到 2026-09-11 批次，尚无 2026-09-14 批次；本轮只收录其中两篇证据完整、尚未入库且互补性强的工作，没有用相邻主题论文凑数。
- 主题分布：空心阴极羽流的实验诊断—静电 WarpX—粒子追踪链，以及 $^{50}$Ti M1 强度的实光子/电子/质子/单中子转移多探针核结构实验。
- 检索范围：检查官方 arXiv `physics.plasm-ph`、`physics.acc-ph`、`physics.comp-ph`、`physics.ins-det`、`physics.med-ph`、`nucl-ex`、`physics.app-ph`、`physics.optics` 与 `astro-ph.HE` 近期列表，并复查 APS/HPLSE 与激光等离子体、PIC、HEDP、强场 QED、ML、核诊断和 beam application 定向检索。多源聚合器本轮没有返回可用记录，因此不宣称覆盖全部数据库。
- 去重：按正式 DOI/arXiv identifier、规范化标题、历史 `daily/`、347 条完成台账、17 条重试队列、摘要及物理场景核对，两篇均为新记录。
- PDF / 正文：2 份官方 arXiv PDF 通过 `%PDF-`、`file`、`pdfinfo`、SHA-256 和非空 `pdftotext -layout`；两篇均完成 MinerU 正文/图件转换，保留并逐张查看 13 张关键图。完整记录见 [pdf_validation.json](pdf_validation.json)。

## 论文清单

### 1. Particle-resolved pathways to energetic-ion formation in a fluctuating low-current hollow-cathode plume

- DOI：[10.48550/arXiv.2609.10958](https://doi.org/10.48550/arXiv.2609.10958)
- arXiv v1：2026-09-10
- 来源：[arXiv 摘要页](https://arxiv.org/abs/2609.10958)
- 期刊 / 平台：arXiv 预印本
- 本地 PDF：`daily/2026-09-14/pdfs/Wang et al. - 2026 - Energetic ions in fluctuating hollow-cathode plume.pdf`
- 中文笔记：[Wang et al. - 2026 - Energetic ions in fluctuating hollow-cathode plume.md](notes/Wang%20et%20al.%20-%202026%20-%20Energetic%20ions%20in%20fluctuating%20hollow-cathode%20plume.md)
- 来源影响力分：7/10
- 专业相似度分：9/10
- 推荐理由：把 RPA/双探针实验、二维轴对称静电 WarpX、自洽源标记、被动粒子场对照和轨迹积分功接成粒子级机制链，同时主动写出相位折叠、不同统计分母和实验—模拟不匹配。
- 一句话总结：实验确认高能 Xe 离子与宽带涨落共存；代表性 PIC 中 96.93% 的分类高能外流来自域内电离，同一 KDE 出生队列在完整时变场/平均场/冻结场中超过 50 eV 的条件份额为 73.0%/7.2%/8.4%，但这些是模拟机制敏感性结果，不能当成实验离子声归因或绝对高能占比。

### 2. A detailed view at magnetic dipole strengths: The case of semi-magic $^{50}$Ti

- DOI：[10.1103/82y9-svrd](https://doi.org/10.1103/82y9-svrd)
- 正式发表：2026-09-11
- 开放全文：[arXiv 摘要页](https://arxiv.org/abs/2609.10843)
- 期刊 / 平台：Physical Review Letters
- 本地 PDF：`daily/2026-09-14/pdfs/Kelly et al. - 2026 - Magnetic dipole strengths in 50Ti.pdf`
- 中文笔记：[Kelly et al. - 2026 - Magnetic dipole strengths in 50Ti.md](notes/Kelly%20et%20al.%20-%202026%20-%20Magnetic%20dipole%20strengths%20in%2050Ti.md)
- 来源影响力分：10/10
- 专业相似度分：8/10
- 推荐理由：用新 $^{50}$Ti$(\gamma,\gamma')$ 和 $^{49}$Ti$(d,p)$ 联合既有 $(e,e')$、$(p,p')$，在逐态层面同时约束总 M1、主要自旋分量和中子 $1f_{5/2}$ 谱因子，是“多探针比单一总强度更能检验微观模型”的正式实验范例。
- 一句话总结：牢固指认的 $1^+$ 态总 $B(M1)=4.9(9)\,\mu_N^2$，但八个 $(d,p)$ 牢固态只承载 $1.9(5)\,\mu_N^2$；三个模型经淬灭后能大致匹配累计强度，却都错误预言大谱因子与大 M1 同位出现，说明总和相符不等于逐态波函数正确。

## 未入库候选与取舍

- 2026-09-11 `physics.plasm-ph` 中的 KOBRA ELM 自适应 Vlasov–Poisson 稿件与 2026-09-12 已入库的 `kobra` 代码/benchmark 属同一主线，内容增量不足以支撑再次入库；继续跳过以避免近重复。
- 一篇核物理问题的 physics-guided Gaussian-process 方法稿件具有方法学价值，但与本轮两篇直接实验/PIC 证据相比相关性更弱，未用于扩充数量。
- 5 条高优先级 APS 阻塞候选已用项目安全下载器重试，accepted/article 与 DOI 的代理/直连路径仍全部返回 `HTTP 403`；重试计数已更新，队列总数保持 17 条，没有用摘要代替全文笔记。
- 扩展的 laser-accelerated beam → converter/catcher → γ/中子/活化 → 剂量/屏蔽链仍是优先方向。Kelly 使用激光 Compton 背散射光束做核结构诊断，但不是激光尾场电子束打转换靶的端到端应用验证。

## 当日综合总结

- 两篇论文共同强调“可观测量与机制变量不能一一等同”：Wang 的双探针表观波数不能唯一还原真实模式，Kelly 的总 M1 强度不能唯一还原微观组态。
- Wang 最值得借鉴的是显式分开自洽瞬时份额与被动队列条件份额，并用同初始粒子做场历史敏感性；Kelly 最值得借鉴的是用互补探针逐态交叉，而不是只让模型拟合积分总量。
- 推荐阅读顺序：先读 Wang 的 Eqs. 5–8 和图 11，建立“诊断混叠 + 条件队列”边界；再读 Kelly 的图 1 与图 3，看同一个态的多探针约束怎样推翻仅凭累计强度得出的结构判断。
