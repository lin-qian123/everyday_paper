# 每日论文索引 - 2026-10-09

## 今日概览

- 运行日期：2026-10-09
- 新增论文数：5（2 篇正式 version of record、3 篇官方 arXiv 预印本）；另将 1 篇既有预印本合并升级为 APS 正式 VOR，不重复计数。
- 最新性：官方 arXiv 目标分类已出现 2026-10-07 投稿；Crossref 对 2026-10-07 至 10-09 的 5 组主题查询各取前 100 条，经 DOI 去重和关键词过滤得到 196 条候选。安装的多来源搜索层对 3 个定向查询返回 0 条，故转用官方 arXiv、Crossref 与出版社来源。
- 主题：铝等离子体高次谐波、辐射反作用俘获、tokamak 合成预训练、全向 γ 探测与机器学习定位、可微离子束输运，以及 10 GeV 级 LWFA 联合诊断。
- 去重：按 DOI/arXiv、规范化标题、425 条完成台账、27 条重试队列、来源 URL、正式版关系、摘要和物理场景检查；5 篇为新作品，Tang 等只做版本升级。
- PDF / 正文：6 份 PDF 均通过 `%PDF-`、`file`、`pdfinfo`、SHA-256 与非空 `pdftotext -layout`；共 89 页、27,224,520 字节，人工核查 12 个关键页并解码 6 幅保留图。MinerU 对 6 个公开 URL 均失败，故明确使用已验证本地 PDF、布局文本和渲染回退。
- 重试：IOP 正式论文 `10.1088/1741-4326/aeb1db` 的 PDF/DOI/正文路线都返回 HTML 验证页，未生成笔记，进入结构化重试；队列 `27 → 28`。
- 覆盖边界：定向增量筛选，不宣称穷尽所有期刊、预印本或数据库。

## 论文清单

### 1. High-order harmonic generation in ion- and nanoparticle-containing aluminum laser-induced plasma

- 标识符：[DOI: 10.1063/5.0350047](https://doi.org/10.1063/5.0350047)
- 发表：2026-10-06；*Physics of Plasmas* 33, 103302；AIP 正式 version of record
- 中文笔记：[Ganeev - 2026 - High-order harmonic generation in aluminum plasma.md](notes/Ganeev%20-%202026%20-%20High-order%20harmonic%20generation%20in%20aluminum%20plasma.md)
- 来源影响力分：8/10；专业相似度分：8/10
- 推荐理由：把块材/纳米铝靶、延迟、烧蚀通量、等离子体长度和单双色驱动放在同一套 HHG 实验中比较。
- 一句话总结：纳米颗粒可把第 15 阶增强约 6 倍却降低截止；组分和局域场机理仍缺少时间分辨质谱证据。

### 2. Novel radiative trapping mechanism in ultra-intense laser–plasma interactions

- 标识符：[DOI: 10.1063/5.0341085](https://doi.org/10.1063/5.0341085)
- 发表：2026-09-17；*Matter and Radiation at Extremes* 11, 065201；AIP 正式 VOR
- 中文笔记：[Zhou et al. - 2026 - Novel radiative trapping mechanism.md](notes/Zhou%20et%20al.%20-%202026%20-%20Novel%20radiative%20trapping%20mechanism.md)
- 来源影响力分：8/10；专业相似度分：10/10
- 推荐理由：给出辐射反作用把电子层速度锁定到孔钻界面的 PIC 机制，并补充量子和三维检查。
- 一句话总结：`5×10^23 W/cm²` 模拟形成约 `270 n_c` 电子层及可诊断角峰；目前是单代码预测，无实验或跨代码闭合。

### 3. Real-time Tokamak Equilibrium Reconstruction Under Limited Experimental Data via Physics-Grounded Synthetic Pre-training

- 标识符：[arXiv:2610.09674](https://arxiv.org/abs/2610.09674)
- 版本：2026-10-07，官方 arXiv v1
- 中文笔记：[He et al. - 2026 - Tokamak equilibrium reconstruction via synthetic pretraining.md](notes/He%20et%20al.%20-%202026%20-%20Tokamak%20equilibrium%20reconstruction%20via%20synthetic%20pretraining.md)
- 来源影响力分：7/10；专业相似度分：8/10
- 推荐理由：系统比较同分布、形状 OOD 和时间 OOD，量化合成预训练在真实数据稀缺时的收益与负迁移边界。
- 一句话总结：MAST 时间 OOD 的 `1%` 数据误差从约 `6.42%` 降到 `2.31%`；仍是同装置、EFIT 标签和离线 GPU 测试。

### 4. Omnidirectional Radiation Detector with Perpendicular Dual Silicon Photomultiplier Readout

- 标识符：[arXiv:2610.08195](https://arxiv.org/abs/2610.08195)
- 版本：2026-10-06，官方 arXiv v1
- 中文笔记：[Kozuljevic et al. - 2026 - Omnidirectional gamma detector with ML positioning.md](notes/Kozuljevic%20et%20al.%20-%202026%20-%20Omnidirectional%20gamma%20detector%20with%20ML%20positioning.md)
- 来源影响力分：7/10；专业相似度分：8/10
- 推荐理由：把小型 GAGG 阵列的近全向几何与 XGBoost 距离定位结合，适合作为 γ 诊断设计参考。
- 一句话总结：Geant4 内 MAE 约 `4.5–5.1 mm`，但无样机、背景、宽谱、EMP 或 sim-to-real 验收。

### 5. A Differentiable Surrogate for Loss-Dominated Ion Beam Transport

- 标识符：[arXiv:2610.08877](https://arxiv.org/abs/2610.08877)
- 版本：2026-10-06，官方 arXiv v1
- 中文笔记：[Munoz-Arias et al. - 2026 - Differentiable ion beam transport surrogate.md](notes/Munoz-Arias%20et%20al.%20-%202026%20-%20Differentiable%20ion%20beam%20transport%20surrogate.md)
- 来源影响力分：7/10；专业相似度分：8/10
- 推荐理由：用存活 hazard 与 conditional flow 同时建模强孔径损失和六维相空间，并支持梯度束线优化。
- 一句话总结：SIMION 回代透过率达到 `19.2%`、高于黑盒最好 `16.7%`；尚无实验场图、失准或源漂移闭环。

### 6. Revealing Laser and Electron Beam Evolution in 10-GeV-class Laser-Plasma Accelerators

- 标识符：[DOI: 10.1103/qqcv-f29q](https://doi.org/10.1103/qqcv-f29q)
- 版本：*Physical Review Research* 8, 033352 正式 VOR；由已入库 arXiv:`2604.25823` 合并升级，不增加台账数量
- 中文笔记：[Tang et al. - 2026 - 10-GeV laser-plasma accelerator evolution.md](notes/Tang%20et%20al.%20-%202026%20-%2010-GeV%20laser-plasma%20accelerator%20evolution.md)
- 来源影响力分：9/10；专业相似度分：10/10
- 推荐理由：BELLA 同步纵向测量电子最高能量和激光红移，用双观测量约束 40 cm 等离子体通道及激光耗尽。
- 一句话总结：高密通道实测 `10.2 GeV`；通道参数反演和 `15–20 GeV` 扩展仍依赖 INF&RNO 模拟。

## 当日综合总结

- 本轮只有 Ganeev 的核心 HHG 光谱和 Tang 的电子/激光纵向演化属于直接激光实验；Zhou 是纯 PIC，He、Kozuljevic 和 Muñoz-Arias 是合成数据或模拟器上的机器学习/代理验证。
- 辐射与诊断主线覆盖“源机制—探测—定位”：Zhou 的角分布和 Kozuljevic 的定位都还是模拟预测，不能合并为已验证的激光 γ 诊断链。
- 束流主线把 Tang 的直接 10.2 GeV 实验与可微离子束输运方法并列，但后者没有实验束线，不能据此声称激光离子束已完成在线优化。
- 本轮没有运行 KLAPS、INF&RNO、FreeGSNKE、Geant4、SIMION 或网络训练；所有参数、拟合和物理归因均按作者证据及本地全文核读处理。
