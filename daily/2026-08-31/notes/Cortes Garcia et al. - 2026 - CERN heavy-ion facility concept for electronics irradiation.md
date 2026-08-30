# A European high-energy heavy-ion facility for electronics irradiation based at CERN: Concept Design Report 笔记

## 0. 论文信息

- 作者/编辑：E. C. Cortés García（editor）；R. García Alía；M. A. Fraser；M. Słupecki；M. Widorski
- 文档类型：CERN Yellow Report 预印本/概念设计报告，拟提交出版
- DOI：暂无；arXiv：[10.48550/arXiv.2608.26369](https://doi.org/10.48550/arXiv.2608.26369)
- 版本：Version 1.0，2026-08-28；arXiv 提交 2026-08-26
- 来源链接：[arXiv 摘要页](https://arxiv.org/abs/2608.26369)
- 本地 PDF：`daily/2026-08-31/pdfs/Cortes Garcia et al. - 2026 - CERN heavy-ion facility concept for electronics irradiation.pdf`
- 重要状态说明：报告声明当前版本尚未由贡献专家审查或批准，也尚无 CERN report number、ISBN/ISSN 或正式 DOI。

## 1. 摘要与文章定位

HEARTS@LEIR 提案拟改造 CERN 离子注入链和 LEIR synchrotron，建设面向空间电子学和高能物理 ASIC 的高能重离子单粒子效应（SEE）测试设施。目标是提供约 `1900 h/year` 的额外束流时间、最高约 `100 MeV/nucleon` 的离子能量，以及可调离子种类、LET、通量和均匀照射场。

本文是 `97` 页概念设计和资源/风险估算，不是已建成设施，也不是已经交付的辐照实验。所有“年小时数、产能、成本、屏蔽和通量”均属于设计基线、已有机器数据外推或待技术设计阶段确认的量。

## 2. Executive summary 与项目边界

报告指出现有 cyclotron 测试设施常见能量约 `10–20 MeV/nucleon`，在硅中的穿透深度约 `100–200 μm`，对现代 3D/system-on-chip 器件背面测试不够。HEARTS@LEIR 计划将可用能量扩展至 `20–100 MeV/nucleon`，LET 目标范围约 `0.4–75 MeV·cm²·mg⁻¹`，覆盖 O、Ar、Kr、Xe、Pb 等候选离子。

项目时间表是：`2027–2028` 技术设计，`2029–2032` 采购/制造/测试，`2033` 安装，`2034` 束流 commissioning，`2035` 用户运行。概念设计给出的 funded cost 为 `18.3 MCHF`，另有 `32.5 PY` CERN staff in-kind effort；技术设计阶段需约 `2.062 MCHF` 和 `9.9 PY`。报告明确指出概念阶段成本不确定度约 `±30–50%`。

## 3. Beam specification parameters：从 LET 到照射场

### 3.1 需求和候选离子

基线希望至少提供四种离子，覆盖 `20–100 MeV/nucleon`，候选集合为 O、Ar、Kr、Xe、Pb；具体元素和电荷态需与 Ion Complex Upgrade（ICU）项目协调。LET 目标上限扩展到约 `75 MeV·cm²·mg⁻¹`，穿透硅深度至少 `200 μm`，并要求 LET spread、横向均匀度和时间结构可量化。

表 3.1/3.2 的设计摘要如下：

| 参数 | 目标 |
|---|---:|
| 离子能量 | `20–100 MeV/nucleon` |
| 离子种类 | `16O8+`、`40Ar16+`、`86Kr29+`、`129Xe40+`、`208Pb54+`（候选） |
| LET 范围 | `0.4–75 MeV·cm²·mg⁻¹` |
| LEIR flat-top 粒子数 | `≥10^9 ions/cycle` |
| spill 长度 | `0.5–10 s` |
| spill 强度 | `10^6–10^8 ions/s` |
| 横向均匀度 | 1 cm² bin 的 max/mean `≤1.1` |
| 照射面积 | `2×2` 至 `20×20 cm²` |

注意：`208Pb54+` 在最大 `4.8 Tm` 刚度下约到 `72 MeV/nucleon`，不是 100 MeV/nucleon。辐射防护表 11.1 还写作 `84Kr28+`，而正文基线使用 `86Kr29+`；报告把它列为待协调的 open item，不能擅自抹平。

### 3.2 spill 稳定性系数

$$
c_V=\frac{\sigma}{\mu}
$$

**变量说明：** $\sigma$ 为 spill 粒子计数的 RMS，$\mu$ 为平均粒子计数，$c_V$ 为 coefficient of variation。

**推导过程：**

1. 用 RMS 量化 spill 间或 spill 内的波动尺度。
2. 用平均计数归一化，使该指标不依赖绝对通量单位。
3. 将 $c_V<1$ 作为稳定性规格之一；真正的用户剂量/SEE 测试仍需结合时间结构和束流监测。

**物理直觉：**

同样的平均 fluence，如果每个 spill 波动很大，单粒子效应统计和速率相关效应的误差会变大。$c_V$ 是一个稳定性门槛，不是完整的束流质量指标。

## 4. Ion sources、Linac3 与 LEIR 数值循环

现有 GTS-LHC ECR 源在 afterglow 模式运行，Linac3 选择约 `200–260 μs` 的脉冲片段。报告建议增加第二个同型离子源：保留现源服务 Pb–O 混合物，第二源服务 Ar/Kr/Xe，减少多气体 cocktail 中轻离子占据空间电荷受限区域、抑制 Pb 强度的风险。

表 4.1 的保守估算取 LEIR `3.6 s` 周期并考虑注入次数、stripper 效率、Linac3 传输和 LEIR cooling。代表性 flat-top 强度包括 O `10.2×10^9`、Ar `1.84×10^9`、Kr `0.93×10^9`、Xe `2.35×10^9`、Pb `1.84×10^9` ions/injection；其中既有测量值，也有 Baron 公式缩放和假设，不应全部称为已测结果。

## 5. Beam extraction 与 20×20 cm² 均匀化

报告研究 resonant slow extraction，并比较三种末端照射场方案：

| 方案 | 额外硬件 | 传输效率 | 1 cm² bin max/mean | 关键代价 |
|---|---|---:|---:|---|
| blow-up and scraping（baseline） | 无 | `14.9%` | `1.20` | 简单但效率低 |
| octupole tail folding | 2 个 octupole 等 | `50%` | `1.13` | 光学匹配、孔径和调试更复杂 |
| pencil-beam scanning | 宽孔径扫描 corrector | `63%` | `<1.05` | 真空孔径大，瞬时/平均通量比可超过 10 |

图 7.2–7.4 展示 baseline 传输和 20 cm 场；图 7.5–7.7 展示 octupole tail folding；图 7.8–7.9 展示 pencil-beam spiral scan。所有 tracking 采用 Gaussian transverse distribution，而 extraction plane 的真实分布并非 Gaussian，因此三种效率和均匀度仍需用真实分布量化。

Pencil scan 的另一个问题是剂量时间结构：某一点只在扫描斑经过时接受照射，局部瞬时通量可能是平均值的 1 到大于 10 倍。对只关心积分 fluence 的 SEE 测试影响可能有限，但对 rate-dependent、destructive latch-up、single-event burnout 或与器件 duty cycle 同步的测试可能不可接受。

## 6. Test station、监测与安全

测试站目标包括 beam on/off、离子种类/能量/尺寸/flux/fluence 配置、DUT 电动定位与旋转、在线 beam visualization 和 TTL 时间信号。baseline 仪器是 MWPC（位置/轮廓）、XSEC（二次发射室，用于连续 flux/fluence）和 scintillator screen。

布局按 bending magnet → beam instrumentation → beam stopper → DUT → beam dump 排列，并用两个 CERN Equipment Interlock System 安全区把 beam presence 与人员 access 互锁。墙后需要二次辐射屏蔽。

### 6.1 运行性能估算

在 LEIR 当前 RMS magnet current `1.56 kA`、总周期 `6 s` 的假设下，约束 flat-top duty cycle：O `47.7%`、Ar `24.8%`、Kr `13.1%`、Xe `8.4%`、Pb `8.3%`。表 10.3 以 baseline blow-up/scrape `ηTL=0.15`、extraction efficiency `ηSRE=0.7` 估算，在 `12×12 cm²` 场上累积 `10^7 ions·cm⁻²` 所需约 `8–89 s`，但这是模型化 delivery performance，不是设施实测。

### 6.2 辐射防护边界

LEIR 现有侧向墙约 `160 cm`，缺少顶部屏蔽；新 transfer line 和实验区的初步估计为侧向/顶部约 `80–160 cm` 混凝土。精确厚度须由技术设计阶段的损失分布和 HSE-RP 计算确定。表 11.2 给出从 LEIR flat-top 到 DUT 的暂定强度/损失比例：抽取后 `70–95%`，transfer line 后 `50–67%`，DUT 处仍可能有 `50–67%` 被视为到达/损失相关量。

这些内容是概念阶段 shielding basis，不是人员屏蔽认证或现场剂量许可。辐射剂量对能量和离子种类呈非线性，且顶部 sky-shine、beam loss、DUT 二次粒子和实际几何都需要独立工程审计。

## 7. 结论与项目风险

报告形成了从离子源、Linac3、LEIR 累积冷却、慢抽取、传输线、均匀化、测试站到 interlock/屏蔽的概念闭环。它的价值是把用户需求转成可检查的束流规格、资源包和风险清单，并指出基础设施、孔径、真实抽取分布、成本、采购和安全是 TDR 阶段必须退休的风险。

## 8. 与本仓库方向的关系

- 主题关键词：heavy-ion irradiation；single-event effects；LEIR；beamline；LET；DUT；radiation safety；beam homogenization。
- 相关性评分：4/5。
- 直接价值：为激光离子束/电子束应用研究提供“束流规格—DUT—通量均匀化—在线监测—安全互锁”的系统级对照，尤其提醒不能只看源端粒子数。
- 不应外推：它不是激光离子加速器实验，也不包含激光靶、转换靶韧致辐射、光核、中子或同位素产额；不能把设计年产能写成已运行能力。

## 9. 复习用速记

HEARTS@LEIR 是一个面向高能重离子电子辐照的概念设计：以 LEIR 慢抽取覆盖多离子、多 LET 和大面积均匀照射，代价是新的离子源、传输线、末端均匀化、测试站和屏蔽。最重要的证据边界是：97 页文档尚未最终审查，2034 commissioning、2035 operation、18.3 MCHF 和 `1900 h/year` 都是规划与估算。
