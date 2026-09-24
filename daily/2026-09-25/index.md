# 每日论文索引 - 2026-09-25

## 今日概览

- 运行日期：2026-09-25
- 新增论文数：3（2 篇 2026-09-23/24 正式期刊论文，1 篇 2026-09-23 提交并于 2026-09-24 列出的 arXiv 预印本）
- 最新性：官方 arXiv 目标分类已核对到 2026-09-24 批次；正式来源检索覆盖 Crossref 2026-09-22 至 2026-09-25 元数据，并核对 PST、Optica、DOI 与 arXiv 单篇页。
- 主题分布：焦点位置调谐的 GeV LWFA 实验与 FBPIC；短波激光—纳米箔阿秒电子束二维 EPOCH 方案；二维钙钛矿在 D–D 中子混合场中的 n/γ 脉冲形状甄别。
- 去重：按 DOI/arXiv identifier、规范化标题、375 条完成台账、17 条结构化重试队列和历史 `daily/` 核对。正式 PRL `10.1103/qqcv-f29q` 与已有同题作者稿重复，`arXiv:2609.27995` 与已入库正式 PRD `10.1103/f9xt-jpd1` 同题，均未重复入库。
- PDF / 正文：3 份全文均通过 `%PDF-`、页数、SHA-256 和非空 `pdftotext -layout`。PST 完成 MinerU；Optica 的公开 URL 解析受 JavaScript gate 限制，arXiv 远程任务长时间未完成，后两篇使用本地文本、页面渲染和逐图核对 fallback。共保留并人工检查 12 张关键图，详见 [pdf_validation.json](pdf_validation.json)。
- 来源边界：第一篇含真实 LWFA 实验，但 `2.2 GeV` 是准三维 FBPIC；第二篇全部是二维 EPOCH 与解析标度；第三篇直接测得 D–D 混合场 PSD，但绝对效率相关数字来自作者输运模型。

## 论文清单

### 1. Experimental tuning of electron energy gain via laser focus shift in a laser-driven plasma wakefield accelerator

- 标识符：[DOI: 10.1088/2058-6272/aeabfd](https://doi.org/10.1088/2058-6272/aeabfd)
- 发表日期：2026-09-24
- 期刊 / 平台：*Plasma Science and Technology*（正式期刊元数据；本地全文为带 DOI 的 accepted manuscript）
- 本地 PDF：`daily/2026-09-25/pdfs/Chang et al. - 2026 - Plasma telescope LWFA focus tuning.pdf`
- 中文笔记：[Chang et al. - 2026 - Plasma telescope LWFA focus tuning.md](notes/Chang%20et%20al.%20-%202026%20-%20Plasma%20telescope%20LWFA%20focus%20tuning.md)
- 来源影响力分：8/10
- 专业相似度分：10/10
- 推荐理由：把真实焦点扫描、磁谱与准三维 FBPIC 连成可核对机制链，同时清楚暴露实验与理想模型在最优位置、最高能量和注入窗口上的差异。
- 一句话总结：`15.22 J、54 fs` CoReLS 激光在 `z_f=-1.6 mm` 获得约 `1.4 GeV`，实验自注入窗口为 `-2.2<z_f<2.4 mm`；FBPIC 的 `-1.0 mm/2.2 GeV` 支持等离子体再聚焦机制，但不是实验值。

### 2. High-energy high-density attosecond electron bunch from short-wavelength laser–nanofoil interaction

- 标识符：[DOI: 10.1364/OE.612056](https://doi.org/10.1364/OE.612056)
- 发表日期：2026-09-23
- 期刊 / 平台：*Optics Express* **34**(20), 37393–37407（开放 VOR）
- 本地 PDF：`daily/2026-09-25/pdfs/Li et al. - 2026 - Attosecond electron bunch from laser nanofoil.pdf`
- 中文笔记：[Li et al. - 2026 - Attosecond electron bunch from laser nanofoil.md](notes/Li%20et%20al.%20-%202026%20-%20Attosecond%20electron%20bunch%20from%20laser%20nanofoil.md)
- 来源影响力分：8/10
- 专业相似度分：9/10
- 推荐理由：正式全文补齐了此前仅有 accepted 元数据的高相关条目，并明确给出二维 PIC 网格、波长扫描、相空间压缩机制和实验功率门槛。
- 一句话总结：二维 EPOCH 最优构型 `10 nm、a₀=40、l=3λ、d=1 nm` 形成约 `305 MeV`、`0.5%` 能散、`1–10 as` 和 `10²⁴ cm⁻³` 的电子束；三维效应、数百 TW 软 X 光源和纳米靶控制均未验证。

### 3. Fast-Neutron Scintillation with Multi-Quantum-Well 2D Perovskites

- 标识符：[arXiv:2609.28468](https://arxiv.org/abs/2609.28468)；归档 DOI `10.48550/arXiv.2609.28468`
- 提交日期：2026-09-23（2026-09-24 官方新论文列表）
- 期刊 / 平台：arXiv 预印本
- 本地 PDF：`daily/2026-09-25/pdfs/Tan et al. - 2026 - Fast neutron scintillation in 2D perovskites.pdf`
- 中文笔记：[Tan et al. - 2026 - Fast neutron scintillation in 2D perovskites.md](notes/Tan%20et%20al.%20-%202026%20-%20Fast%20neutron%20scintillation%20in%202D%20perovskites.md)
- 来源影响力分：7/10
- 专业相似度分：9/10
- 推荐理由：提供真实 `2.45 MeV` D–D 混合场的事件级中子/γ 双带，而不是只报告材料光致发光或纯输运模拟；同时把阈值依赖和模型效率边界写得可审计。
- 一句话总结：毫米厚多量子阱二维钙钛矿在 `662 keV` 下能量分辨率为 `5.4%`，D–D 混合场 PSD 最高 `FoM=3.51`；该值是在积分电荷阈值 `2515` 后取得，`10.1%/3.6%` 是 5 mm 样品约 2 MeV 条件下的模型交互/沉积量。

## 未入库候选与取舍

- 正式 PRL `10.1103/qqcv-f29q`（*Revealing Laser and Electron Beam Evolution in 10-GeV-class LPAs*）与历史台账中的同题作者稿规范化标题完全相同，按“同一作品正式版—预印本”硬去重，不建立第二条记录。
- `arXiv:2609.27995` 与 2026-09-23 已入库正式 PRD `10.1103/f9xt-jpd1` 同题，按正式版本优先去重。
- `arXiv:2609.28422` 的 dHybridR exascale hybrid-PIC、`2609.27501` 的隐式能量/电荷守恒 PIC、`2609.28116` 的 SOLPS 几何感知概率代理都有方法价值；本轮优先直接 LWFA 实验、正式高相关激光—靶方案和真实快中子诊断。
- `arXiv:2609.28204` 的可持续屏蔽材料方向相关，但与本轮三项的物理证据链相比更偏一般辐射工程，留作后续专题筛选。

## 当日综合总结

- Chang 等给出最直接的束流工程旋钮：在焦斑小于匹配尺寸时，把真空焦点放在密度平台前可由等离子体再聚焦延长稳定加速；定性机制成立，但理想 FBPIC 明显高估能量和注入窗口。
- Li 等的关键不是“短波自动得到窄谱”，而是短波剥离/相位锁定、偏置靶横向注入与穿轴后的梯度反转共同完成谱压缩；所有最佳指标仍处于二维数值证据层。
- Tan 等把快中子材料工作推进到真实混合场 PSD，适合作为未来激光驱动中子诊断的候选材料依据；在源项、EMP、高通量和绝对效率验证前，不能直接写成激光中子诊断器已就绪。
- 推荐阅读顺序：先看 LWFA 图 2/3 区分实验窗口与模拟窗口，再看钙钛矿图 3 理解阈值—FoM 权衡，最后看阿秒方案图 6/7 判断相空间压缩与单参数稳健性。
