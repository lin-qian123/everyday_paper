# 每日论文索引 - 2026-09-23

## 今日概览

- 运行日期：2026-09-23
- 新增论文数：3（2 篇 2026-09-22 正式 APS 论文，1 篇 2026-09-20 提交并于 2026-09-22 列出的 arXiv 预印本）
- 最新性：官方 arXiv 目标分类已更新到 2026-09-22 批次；正式来源检索覆盖 Crossref 2026-09-21 至 2026-09-23 元数据，并核对 APS、DOI 与 arXiv 页面。没有把 9 月 20 日提交的预印本写成 9 月 23 日新投稿。
- 主题分布：锥形导引靶对激光质子束能散/发散的动态控制；辐射相对论 Alfvén 湍流中的粒子—光子各向异性；受物理约束、可回滚的机器学习时间跳跃。
- 检索范围：官方 arXiv `physics.plasm-ph`、`physics.acc-ph`、`physics.comp-ph`、`nucl-ex`、`physics.ins-det`、`physics.optics` 与相关交叉列表；Crossref、APS 和 DOI 元数据；通用 Web 检索与本地多源搜索器。本地搜索器返回 0 条，最终选择不依赖聚合器排序，也不宣称穷尽全部数据库。
- 去重：按 DOI/arXiv identifier、规范化标题、369 条完成台账、18 条结构化重试队列和历史 `daily/` 核对。`10.1103/d45l-hsgg` 曾因 APS 常规路径受阻而只列为候选，本轮 APS harvest 正式全文恢复可达后首次入库。
- PDF / 正文：3 份全文均通过 `%PDF-`、`file`、`pdfinfo`、SHA-256 和非空 `pdftotext -layout`；3 份均完成 MinerU 转换，共保留并逐张查看 14 张关键图。详见 [pdf_validation.json](pdf_validation.json)。
- 来源边界：两篇 APS 都是作者 PIC 模拟而非实验；PhySKIP 是一维流体放电求解器的预印本，不是 PIC 加速，也没有通用长时稳定性证明。

## 论文清单

### 1. Cone-guided phase-space control of laser-driven proton beams

- 标识符：[DOI: 10.1103/d45l-hsgg](https://doi.org/10.1103/d45l-hsgg)
- 发表日期：2026-09-22
- 期刊 / 平台：*Physical Review E* **114**, 035212（正式期刊论文）
- 本地 PDF：`daily/2026-09-23/pdfs/Chintalwad and Stark - 2026 - Cone-guided proton beam control.pdf`
- 中文笔记：[Chintalwad and Stark - 2026 - Cone-guided proton beam control.md](notes/Chintalwad%20and%20Stark%20-%202026%20-%20Cone-guided%20proton%20beam%20control.md)
- 来源影响力分：9/10
- 专业相似度分：10/10
- 推荐理由：直接对应激光离子束品质、靶设计和输运；同时用锥坍缩—质子飞行时间匹配解释为什么最小发散和最窄能谱出现在不同锥长，而不只是报告参数扫描。
- 一句话总结：作者 EPOCH 模拟显示约 `10 μm` 锥长最利于聚焦，`25–30 μm` 更利于谱压缩；最佳相对能散较平面基线降低约 `63%`，三维弹道外推中 25% 能量半径从 `29.2 μm` 降至 `15.8 μm`，但没有实验和真实束线输运验证。

### 2. Anisotropy and energy distribution of leptons and photons in radiative relativistic Alfvénic turbulence

- 标识符：[DOI: 10.1103/f9xt-jpd1](https://doi.org/10.1103/f9xt-jpd1)
- 发表日期：2026-09-22
- 期刊 / 平台：*Physical Review D* **114**, 063021（正式期刊论文）
- 本地 PDF：`daily/2026-09-23/pdfs/Liu et al. - 2026 - Radiative relativistic Alfvenic turbulence.pdf`
- 中文笔记：[Liu et al. - 2026 - Radiative relativistic Alfvenic turbulence.md](notes/Liu%20et%20al.%20-%202026%20-%20Radiative%20relativistic%20Alfvenic%20turbulence.md)
- 来源影响力分：9/10
- 专业相似度分：9/10
- 推荐理由：把辐射反作用、相对论 pair-plasma PIC、粒子俯仰角和光子方向分布连接成一条可检查的机制链，并明确给出弱/强冷却和系统尺度对拐点的影响。
- 一句话总结：二维 EPOCH 结果给出弱冷却低能 `sinθ∝γ⁻¹`、强冷却低能 `sinθ∝(γ−1)⁻¹ᐟ²` 等分段标度及其光子映射；这些指数依赖二维、衰减、弱激发 pair-plasma 设置，尚无观测或实验对照。

### 3. Machine Learning Accelerated Plasma Simulation through Physics Guided Time Jumps

- 标识符：[arXiv:2609.23358](https://arxiv.org/abs/2609.23358)；归档 DOI `10.48550/arXiv.2609.23358`
- 提交日期：2026-09-20（2026-09-22 官方新论文列表）
- 期刊 / 平台：arXiv 预印本
- 本地 PDF：`daily/2026-09-23/pdfs/Iqbal and Zhang - 2026 - ML accelerated plasma simulation.pdf`
- 中文笔记：[Iqbal and Zhang - 2026 - ML accelerated plasma simulation.md](notes/Iqbal%20and%20Zhang%20-%202026%20-%20ML%20accelerated%20plasma%20simulation.md)
- 来源影响力分：7/10
- 专业相似度分：9/10
- 推荐理由：相比只预测等离子体状态，PhySKIP 把神经网络限制为可验收的时间跳跃提议，并保留 Poisson/电路重建、周期重锚和失败回滚，适合评估 ML 加速的稳定性成本。
- 一句话总结：一维氮气漂移—扩散基准在单逻辑 CPU 上由约 `156 s` 降到最低 `33.3 s`，最高 `4.70×`；计时不含加载/诊断，`500 ns` 完成率不是长期稳定性证明，也没有实现 PIC 加速。

## 未入库候选与取舍

- `arXiv:2609.23141` 的 FPGA reservoir-prediction 平台有实时性价值，但本轮选择的 PhySKIP 直接量化了求解器内时间跳跃、重锚和回滚；另两个名额优先给 9 月 22 日正式发表的 APS 论文。
- `arXiv:2609.22627` 的相互作用 filament 实验属于高质量等离子体物理，但与当前激光束流、PIC、辐射和 ML 主线的联系较弱，未挤入前三篇。
- `arXiv:2609.23437` 的 PIC debris localization 是理想冷离子条件下的 proof of principle，工程与实验闭环弱于今天的束流品质和辐射湍流论文。
- 本轮没有发现同等新鲜、全文可验证且未入库的激光转换靶—韧致辐射/光核/中子应用论文；没有用较旧或低相关条目填满主题配额。

## 当日综合总结

- Chintalwad–Stark 的核心是定时而非静态几何：质子到达锥尖和锥壁坍缩的相对时间决定聚焦窗与谱压缩，因此束流品质指标之间存在结构性权衡。
- Liu–Wei–Gong 展示了辐射反作用如何选择性耗散垂直动量，使粒子分布和辐射方向都带有能量依赖；解析指数必须与二维 pair-plasma 假设一起引用。
- Iqbal–Zhang 展示了“网络提议、物理重建、守卫验收、周期重锚”的保守加速架构；当前证据只支持一维流体基准中的速度—精度折中。
- 推荐阅读顺序：先看质子论文图 1/6 理解能散—发散权衡，再看辐射湍流图 2/4 跟踪粒子到光子的各向异性映射，最后看 PhySKIP 图 1/9/10 检查加速比和稳定性口径。
