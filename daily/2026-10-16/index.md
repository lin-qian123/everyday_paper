# 每日论文索引 - 2026-10-16

## 今日概览

- 新增 **6 篇**：2 篇 2026-10-15 正式 VOR、4 篇高相关官方 arXiv v1 作者预印本；完成台账 **453 → 459**。
- 正式论文优先：微管内爆离子增能、脉冲质子治疗机的场外中子测量；预印本补充 GaN 质子探测器、CNN 湍流 LES、WarpX 束束 QED 基准与激光 Compton 硬 X 射线频梳。
- 检索：搜索层 3 个定向查询返回 0；官方 arXiv 五个目标分类最近 300 条最新提交为 2026-10-14。Crossref 2026-10-14 至 16 的 10 组主题查询中，6 组初次遇到 HTTP 429，降低并发后全部补查成功，合计 820 条返回、662 个唯一 DOI；另查正式版关系、出版商、APS accepted 与精确标题。
- 去重：对 453 条完成台账、37 条重试项和历史日更检查 DOI/arXiv、规范化标题、来源、近似标题和物理场景；未创建正式版与预印本的双重条目。
- 全文：6 份 PDF 共 **116 页、23,262,368 字节**，文件头、类型、SHA-256、页数、全页可读性和 499,692 字节布局文本通过；6 篇均由 MinerU 显式 `pipeline` 成功解析，并与原 PDF 交叉检查。目视核查 13 个身份/关键页，保留 7 幅直接裁取的原图。
- 阻塞：APS 核衰变 accepted paper 与 IOP 二十面体束布局 accepted manuscript 的 PDF 分别返回 403/404 和 HTML 验证页；只存候选与失败记录，重试队列 **37 → 39**。
- 覆盖边界：定向增量筛选，未穷尽所有期刊或 arXiv 学科；没有把检索空结果当成无论文，也没有从摘要生成未读全文笔记。

## 论文清单

### 1. Path-integrated electrostatic energization in laser-driven collisionless cylindrical convergence

- 标识符：[10.1103/8jqr-lcb3](https://doi.org/10.1103/8jqr-lcb3)
- 日期与来源：2026-10-15，*Physical Review E*，正式 VOR
- 中文笔记：[Pan et al. - 2026 - Electrostatic energization in cylindrical convergence](notes/Pan%20et%20al.%20-%202026%20-%20Electrostatic%20energization%20in%20cylindrical%20convergence.md)
- 来源影响力分：8/10；专业相似度分：10/10（阅读优先级主观评分，不是期刊影响因子）
- 推荐理由：用逐轨道功预算识别靶几何与离子增能的因果关系，可帮助避免把强磁场峰值当作源性能。
- 一句话总结：径向静电通道主导增能，0.89 GeV 是中心局部平均动能峰值；二维机制结果未给出可抽取束流或效率。

### 2. Practical considerations in measuring out-of-field neutron dose for pulsed and gantry-mounted proton therapy machines

- 标识符：[10.1088/1361-6560/aeaf3e](https://doi.org/10.1088/1361-6560/aeaf3e)
- 日期与来源：2026-10-15，*Physics in Medicine &amp; Biology*，正式 VOR
- 中文笔记：[Zhang et al. - 2026 - Pulsed proton therapy neutron dose](notes/Zhang%20et%20al.%20-%202026%20-%20Pulsed%20proton%20therapy%20neutron%20dose.md)
- 来源影响力分：8/10；专业相似度分：10/10（阅读优先级主观评分，不是期刊影响因子）
- 推荐理由：直接关联脉冲束流、中子测量、治疗与防护，适合优先建立探测器单脉冲响应检查。
- 一句话总结：特定体模计划中 WENDI 相对 LUPIN 低报约 1.7–2.7 倍；H*(10) 是操作量，不能当作个体胎儿吸收剂量。

### 3. A single radiation hard pixel detector for proton dosimetry, imaging, energy resolution and beam monitoring

- 标识符：[10.48550/arXiv.2610.20304](https://doi.org/10.48550/arXiv.2610.20304)
- 日期与来源：2026-10-14，*arXiv preprint*，官方 arXiv v1 作者预印本
- 中文笔记：[Brosda et al. - 2026 - GaN proton detector](notes/Brosda%20et%20al.%20-%202026%20-%20GaN%20proton%20detector.md)
- 来源影响力分：8/10；专业相似度分：9/10（阅读优先级主观评分，不是期刊影响因子）
- 推荐理由：同一器件结合剂量、二维结构、能量与实时监测，含辐照损伤和 Monte Carlo 解释。
- 一句话总结：GaN 实测 MGy 后仍可标定工作；优化楔形的亚 10 keV 是峰位变化分辨，单帧 7 mGy 与 FLASH 存在外推条件。

### 4. Learning to reconstruct Germano Differential Filtered Fields with Convolutional Neural Networks for Large Eddy Simulation of Plasma Turbulence

- 标识符：[10.48550/arXiv.2610.20204](https://doi.org/10.48550/arXiv.2610.20204)
- 日期与来源：2026-10-14，*arXiv preprint*，官方 arXiv v1 作者预印本
- 中文笔记：[Castagna and Williams - 2026 - Filtered plasma turbulence CNN](notes/Castagna%20and%20Williams%20-%202026%20-%20Filtered%20plasma%20turbulence%20CNN.md)
- 来源影响力分：7/10；专业相似度分：9/10（阅读优先级主观评分，不是期刊影响因子）
- 推荐理由：把解析滤波与学习补偿分开，并报告错误输运和真实成本，适合审查物理代理模型。
- 一句话总结：最粗 32²→256² 可出现错误通量；最高墙钟加速 1.55×，49.45× 是 MPI task-time 指标。

### 5. A modern particle-in-cell code for beam-beam simulations of future colliders

- 标识符：[10.48550/arXiv.2610.17557](https://doi.org/10.48550/arXiv.2610.17557)
- 日期与来源：2026-10-13，*arXiv preprint*，官方 arXiv v1 作者预印本
- 中文笔记：[Formenti et al. - 2026 - WarpX beam beam benchmark](notes/Formenti%20et%20al.%20-%202026%20-%20WarpX%20beam%20beam%20benchmark.md)
- 来源影响力分：9/10；专业相似度分：10/10（阅读优先级主观评分，不是期刊影响因子）
- 推荐理由：提供 WarpX/旧代码、QED/次级对和网格收敛的逐观测量基准，能直接指导 PIC 验收。
- 一句话总结：多个中等场案例一致，但最强 LWFA 总亮度/高能亮度仍差约 78%/40%，不能宣布全参数精密一致。

### 6. Programmable Hard-X-Ray Spectral Comb Generation via Laser-Compton Scattering

- 标识符：[10.48550/arXiv.2610.17166](https://doi.org/10.48550/arXiv.2610.17166)
- 日期与来源：2026-10-12，*arXiv preprint*，官方 arXiv v1 作者预印本
- 中文笔记：[Zhang et al. - 2026 - Programmable hard X ray spectral comb](notes/Zhang%20et%20al.%20-%202026%20-%20Programmable%20hard%20X%20ray%20spectral%20comb.md)
- 来源影响力分：8/10；专业相似度分：10/10（阅读优先级主观评分，不是期刊影响因子）
- 推荐理由：联系实际束流输运、相位、发散和辐射探针，明确频谱调制与时间锁模的不同要求。
- 一句话总结：激光间隔与相位独立调谱齿；10 μm 束可保留频梳，而 13.9 as 时间锁模需要亚纳米束长。

## 当日综合总结

优先读中子剂量测量与微管增能机制，两篇分别约束“读数是否可信”和“能量来自哪里”。WarpX 基准则给出精度尚未闭环的强场案例，适合与本地 PIC 验收标准对照。

- **实测与估算分开：** 中子体模读数、GaN 读出是直接测量；剂量累加、GATE 局部沉积、单帧成像估算和 FLASH 前景各有条件。
- **物理量定义先行：** 峰值局部均能、可抽取束流能量、亮度阈值积分、谱齿和时间锁模不可互换。
- **计算性能保留硬件口径：** WarpX 的多 GPU 周转时间不等于同硬件代码加速；CNN 的 MPI task-time 也不等于墙钟加速。
- **本地核验边界：** 只完成来源、全文、图表与文档验证；未运行 EPOCH、治疗 TPS、GATE/Geant4、BOUT++、神经网络训练、WarpX、GUINEA-PIG、CAIN、ImpactX 或辐射计算。

## 维护与证据记录

- [全文校验](pdf_validation.json)
- [运行与验收记录](run_results.json)
- [检索/限流补查/正式版关系](research/research-run.json)
- [入库元数据](research/import-manifest.json)
- [来源与受阻候选](research/sources.jsonl)
- [MinerU 任务结果](research/mineru-attempts.json)
- [图像出处与裁框](research/figure-manifest.json)

PDF 与两种提取正文保存在本地 `pdfs/` 并按仓库规则被 Git 忽略；GitHub 同步笔记、元数据、原图裁片和核验记录。
