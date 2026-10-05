# 每日论文索引 - 2026-10-06

## 今日概览

- 运行日期：2026-10-06
- 新增论文数：6（2 篇 *Review of Scientific Instruments* 正式 version of record，4 篇官方 arXiv 预印本）
- 最新性：官方 arXiv 目标分类已出现 2026-10-02 投稿的新批次；从其中筛出 5 篇高相关全文，并从 AIP 正式最新期补入 1 篇激光 X 射线照相背光源实验。Crossref 对 2026-10-05 至 10-06 的 6 组主题查询读取 568 条元数据、473 条去重作品。
- 主题：激光驱动 X 射线背光源、热致密等离子体谱学、3D 相对论磁重联、PIC 平滑带宽、张量网络 Vlasov–Maxwell、LLM 中子仪器设计。
- 去重：按 DOI/arXiv、规范化标题、409 条完成台账、21 条重试队列、来源 URL、正式版关系、摘要和物理场景检查；6 篇均为新作品。
- PDF / 正文：6 份 PDF 均通过 `%PDF-`、`file`、`pdfinfo`、SHA-256 与非空 `pdftotext -layout`；共 97 页，选定 36 页人工核查，6 幅关键图裁切后解码。MinerU 的本地路径不受支持，公开 URL 任务全部失败，故明确使用已验证本地 PDF、布局文本和渲染回退。
- 重试：新增 IOP 正式论文 `10.1088/1741-4326/aeb037`；官方 PDF/DOI/article 路径均返回 HTML 验证页，未从摘要生成笔记。重试队列 `21 → 22`。
- 覆盖边界：定向增量筛选，不宣称穷尽所有期刊、预印本或数据库。

## 论文清单

### 1. Characterization and optimization of a laser-produced x-ray source for x-ray radiography

- 标识符：[DOI: 10.1063/5.0323034](https://doi.org/10.1063/5.0323034)
- 发表：2026-10-02 online；*Review of Scientific Instruments* 97, 103510；AIP 正式 version of record
- 本地 PDF：`daily/2026-10-06/pdfs/Benkadoum et al. - 2026 - Laser X-ray radiography source.pdf`
- 中文笔记：[Benkadoum et al. - 2026 - Laser X-ray radiography source.md](notes/Benkadoum%20et%20al.%20-%202026%20-%20Laser%20X-ray%20radiography%20source.md)
- 来源影响力分：9/10
- 专业相似度分：10/10
- 推荐理由：同一实验把背光材料、丝径、脉宽、入射角、承载膜、滤片、宽带韧致辐射和成像分辨率放在一条可审计链中。
- 一句话总结：单根细丝、近 `90°` 入射最利于高分辨照相；增大丝径/高 Z 会提高光子数，却增强连续本底、热电子分量和几何模糊。

### 2. X-ray spectroscopy of hot dense plasmas using LLNL’s upgraded Titan 2ω short-pulse laser

- 标识符：[DOI: 10.1063/5.0350551](https://doi.org/10.1063/5.0350551)
- 发表：2026-10-02 online；*Review of Scientific Instruments* 97, 103506；AIP 正式 version of record
- 本地 PDF：`daily/2026-10-06/pdfs/Fairchild et al. - 2026 - Titan hot dense plasma X-ray spectroscopy.pdf`
- 中文笔记：[Fairchild et al. - 2026 - Titan hot dense plasma X-ray spectroscopy.md](notes/Fairchild%20et%20al.%20-%202026%20-%20Titan%20hot%20dense%20plasma%20X-ray%20spectroscopy.md)
- 来源影响力分：9/10
- 专业相似度分：10/10
- 推荐理由：升级 Titan `2ω` 的首轮多谱仪实验直接面向近固体密度原子物理和 HEDP 谱模型验证。
- 一句话总结：5 台时间积分谱仪获得 Cl/K 多通道校准谱；`T_e≈1 keV、n_e≈10^23 cm^-3` 仍是 Orion/MERL 辅助的初步解释，尚非最终基准值。

### 3. Guide field effects on particle acceleration in three-dimensional relativistic magnetic reconnection

- 标识符：[arXiv:2610.03427](https://arxiv.org/abs/2610.03427)
- 版本：2026-10-02，官方 arXiv v1
- 本地 PDF：`daily/2026-10-06/pdfs/Karavola et al. - 2026 - 3D guide-field relativistic reconnection.pdf`
- 中文笔记：[Karavola et al. - 2026 - 3D guide-field relativistic reconnection.md](notes/Karavola%20et%20al.%20-%202026%20-%203D%20guide-field%20relativistic%20reconnection.md)
- 来源影响力分：8/10
- 专业相似度分：8/10
- 推荐理由：用同参 2D/3D PIC 与开放 outflow 隔离三维自由加速通道，并显式扫描强导引场。
- 一句话总结：快速加速通道到 `B_g=B_0` 仍存在，但参与比例持续下降，伴随重联率降低、能谱变陡和 cutoff 下移。

### 4. Dynamics-aware bandwidth selection for smoothed charge deposition in 2D electrostatic particle-in-cell

- 标识符：[arXiv:2610.03230](https://arxiv.org/abs/2610.03230)
- 版本：2026-10-02，官方 arXiv v1
- 本地 PDF：`daily/2026-10-06/pdfs/Agrawal et al. - 2026 - Dynamics-aware PIC smoothing.pdf`
- 中文笔记：[Agrawal et al. - 2026 - Dynamics-aware PIC smoothing.md](notes/Agrawal%20et%20al.%20-%202026%20-%20Dynamics-aware%20PIC%20smoothing.md)
- 来源影响力分：7/10
- 专业相似度分：9/10
- 推荐理由：把 PIC 降噪与物理模保持放进同一验收，不再用密度 MSE 单独决定滤波强度。
- 一句话总结：选中 Gaussian 令密度/场 MSE 降 `7.40%/3.70%`，增长率比 `0.9556 [0.9453,0.9640]`；结论限于二维静电、指定线性模。

### 5. Quantum approaches for particle-in-cell codes

- 标识符：[arXiv:2610.03254](https://arxiv.org/abs/2610.03254)
- 版本：2026-10-02，官方 arXiv v1
- 本地 PDF：`daily/2026-10-06/pdfs/Connor et al. - 2026 - Quantum approaches for PIC.pdf`
- 中文笔记：[Connor et al. - 2026 - Quantum approaches for PIC.md](notes/Connor%20et%20al.%20-%202026%20-%20Quantum%20approaches%20for%20PIC.md)
- 来源影响力分：7/10
- 专业相似度分：8/10
- 推荐理由：给张量网络 Vlasov–Maxwell 增加任意位置 TFSF 激光注入，是从算法原型走向受驱动等离子体的必要一步。
- 一句话总结：MPS 中的双向激光注入可工作且保留测试范围内的近对数标度，但没有等精度 PIC 成本/误差对照，不能宣称普遍加速。

### 6. NeutronGym: Physics-Graded Neutron Instrument Design for LLM Agents

- 标识符：[arXiv:2610.03631](https://arxiv.org/abs/2610.03631)
- 版本：2026-10-02，官方 arXiv v1
- 本地 PDF：`daily/2026-10-06/pdfs/Ding and Do - 2026 - NeutronGym instrument design.pdf`
- 中文笔记：[Ding and Do - 2026 - NeutronGym instrument design.md](notes/Ding%20and%20Do%20-%202026%20-%20NeutronGym%20instrument%20design.md)
- 来源影响力分：7/10
- 专业相似度分：8/10
- 推荐理由：把 LLM 中子仪器设计绑定到 McStas 和物理分级 reward，并主动审计 shortcut/no-model 基线。
- 一句话总结：GRPO 使 guide-match held-out 通过率从 `11.3%` 到 `76.7%`，但任务只调固定布局的少量参数，且多数训练只有单 seed。

## 当日综合总结

- 两篇正式实验共同覆盖“源—谱—诊断”：Benkadoum 研究激光背光源的产额/分辨率权衡，Fairchild 建立近固体密度 K 壳谱平台；前者的两温韧致辐射拟合和后者的 `T_e/n_e` 均需与直接测量分开。
- 两篇 PIC 方法工作分别处理物理机制和数值误差：Karavola 的 3D 高能尾不能由 2D 替代；Agrawal 说明降噪必须保护目标模的动力学。
- Connor 是短篇能力原型，不提供成熟 PIC 替代证据；NeutronGym 是可执行软件/RL 实验，不是束线上机或真实中子装置设计。
- 本轮没有运行 PIC、MERL、GEANT4、PrismSPECT、McStas、张量网络代码或 RL 训练；所有模型结果均按作者数值证据处理。
