# 每日论文索引 - 2026-09-27

## 今日概览

- 运行日期：2026-09-27
- 新增论文数：3（1 篇 2026-09-25 新正式开放论文，2 篇 2026-09-25 官方 arXiv 批次中的高质量预印本）
- 最新性：周末没有新的 arXiv 公告批次，官方目标分类最新仍为 2026-09-25；同时核对 Crossref 2026-09-25 至 27 新正式元数据和单篇来源。
- 主题分布：LUXE 电子/伽马—激光强场 QED 实施更新；二维电阻 MHD 重联 PINO 代理；VAMOS++ MWPPAC 的物理约束自监督校准。
- 去重：按 DOI/arXiv identifier、规范化标题、382 条完成台账、17 条重试队列、历史 `daily/` 及正式版—预印本/物理场景核对；3 篇为独立作品。LUXE 新文与库内既有路线图文章主题重叠，但 DOI、作者、稿件和实施更新均不同。
- PDF / 正文：3 份官方 PDF 均通过 `%PDF-`、`file`、`pdfinfo`、SHA-256 和非空 `pdftotext -layout`；LUXE 完成 MinerU，2 篇 arXiv 的 MinerU 任务失败后使用本地布局文本、页面渲染和逐图检查。共保留并人工查看 12 张关键图。
- 重试：正式 *Nuclear Fusion* `10.1088/1741-4326/aeac6a` 的官方 PDF、DOI 与文章路由均返回 HTML/Radware，未从摘要生成笔记，加入结构化重试队列。
- 覆盖边界：本轮是官方来源的定向增量筛选，不宣称穷尽全部期刊或跨学科数据库。

## 论文清单

### 1. LUXE: a high-precision experiment to study non-perturbative QED in electron–laser and photon–laser collisions

- 标识符：[10.1140/epjp/s13360-026-08312-1](https://doi.org/10.1140/epjp/s13360-026-08312-1)
- 发表日期：2026-09-25
- 期刊 / 平台：*The European Physical Journal Plus*（CC BY 4.0 正式论文）
- 本地 PDF：`daily/2026-09-27/pdfs/Zarnecki - 2026 - LUXE high-precision nonperturbative QED.pdf`
- 中文笔记：[Zarnecki - 2026 - LUXE high-precision nonperturbative QED.md](notes/Zarnecki%20-%202026%20-%20LUXE%20high-precision%20nonperturbative%20QED.md)
- 来源影响力分：8/10
- 专业相似度分：10/10
- 推荐理由：正式更新强场 QED 实验的电子/伽马两模式、转换靶、探测器原型、ELBEX 选址和实施时间线。
- 一句话总结：`16.5 GeV` 电子束配 `40→350 TW` 激光，目标 `ξ=O(10)、χ=O(1)`；全部谱/产额仍是设计预测，LUXE 安装计划从 2029 年开始。

### 2. Physics-Informed Neural Operator Surrogate for 2D Magnetohydrodynamic Reconnection

- 标识符：[arXiv:2609.29514](https://arxiv.org/abs/2609.29514)；归档 DOI `10.48550/arXiv.2609.29514`
- 提交日期：2026-09-24（2026-09-25 官方新论文列表）
- 期刊 / 平台：arXiv 预印本
- 本地 PDF：`daily/2026-09-27/pdfs/Pothula and Kumar - 2026 - PINO MHD reconnection.pdf`
- 中文笔记：[Pothula and Kumar - 2026 - PINO MHD reconnection.md](notes/Pothula%20and%20Kumar%20-%202026%20-%20PINO%20MHD%20reconnection.md)
- 来源影响力分：7/10
- 专业相似度分：9/10
- 推荐理由：同时给出留出 `S`、电流二阶导数误差、网格迁移、加速比和 plasmoid burst 失败区，边界比单纯平均误差完整。
- 一句话总结：低至中等 `S` 的重联率误差低于约 `3%`，单 A100 的 `2049²×41` 轨迹约 30 秒；高 `S` 晚期 burst 未覆盖时误差升至 `32–42%`。

### 3. Physics-Informed Self-Supervised Learning for Joint Wire Calibration and Interaction Position Reconstruction in Multi-Wire Parallel Plate Avalanche Counters

- 标识符：[arXiv:2609.28604](https://arxiv.org/abs/2609.28604)；归档 DOI `10.48550/arXiv.2609.28604`
- 提交日期：2026-09-23（2026-09-25 官方新论文列表）
- 期刊 / 平台：arXiv 预印本
- 本地 PDF：`daily/2026-09-27/pdfs/Lemasson and Rejmund - 2026 - Self-supervised MWPPAC calibration.pdf`
- 中文笔记：[Lemasson and Rejmund - 2026 - Self-supervised MWPPAC calibration.md](notes/Lemasson%20and%20Rejmund%20-%202026%20-%20Self-supervised%20MWPPAC%20calibration.md)
- 来源影响力分：7/10
- 专业相似度分：9/10
- 推荐理由：在真实 VAMOS++ 核谱仪数据上把物理冗余转成自监督信号，并用未进入训练的参考丝验证位置分辨率。
- 一句话总结：400 万事件训练约半分钟收敛，参考丝分辨率从 `0.09 mm` 改善到前/后 `0.06/0.05 mm`；跨装置、非线性响应和长期漂移仍未验证。

## 未入库候选与取舍

- 正式 *Nuclear Fusion* `10.1088/1741-4326/aeac6a` 报道 DIII-D 中 TAE 驱动的快离子密度涨落和能量交换直接测量，优先级高；但 IOP 路径只返回 HTML/Radware 且未找到合法作者全文，故只入重试队列。
- 正式 PST `10.1088/2058-6272/aeacb3` 是负离子源抽取区 Mach probe 实验，正文同受 IOP 页面限制；与本轮强场 QED、等离子体 ML 和核诊断相比优先级较低，未加入重试队列。
- `arXiv:2609.29336` 的 PQLS/Bayesian 饱和闭合有方法价值，但本轮已收录一个具有明确失败区的等离子体 ML 代理，留待回旋动理学专题。
- `arXiv:2609.29277` 的 DBD 再点火预测、`2609.30155` 的低密度 ICRF 冷等离子体奇点和 `2609.29849` 的 ITER 准对称误差场校正均相关，但优先级低于三篇入选作品。

## 当日综合总结

- LUXE 的关键新增是实施路线而非物理结果：转换靶伽马模式、ELBEX 新位置与探测器原型把强场 QED 从设计向装置推进，但模拟产额不能写成已观测。
- PINO 工作最有价值的不是两数量级加速本身，而是明确展示二阶导数、电流片相位和高 `S` burst 会比体平均场更早失效。
- MWPPAC 工作用独立参考丝把“自监督残差更小”连接到真实位置分辨率；仍需跨运行期、跨探测器和非线性增益检验。
- 推荐阅读顺序：先看 LUXE 图 3/6 理解可观测量与产额跨度，再看 PINO 图 8 的适用域，最后看 MWPPAC 图 5/7 区分训练内残差和外部参考验证。
