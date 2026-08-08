# Building a Start-to-End Model of the CESR Injector Linac

## 基本信息

- 作者：Ryland Goldman；Adam Bartnik；Jared Maxson
- 期刊/平台：arXiv preprint（physics.acc-ph）
- DOI：https://doi.org/10.48550/arXiv.2608.05094
- 发表时间：2026-08-05
- 来源链接：https://arxiv.org/abs/2608.05094
- 本地 PDF：`daily/2026-08-09/pdfs/Goldman et al. - 2026 - CESR injector linac start to end model.pdf`

## 研究问题与方法

作者把 CESR 正电子注入器的阴极、枪、预聚束、四段电子直线加速器、钨转换靶和四段正电子加速器连成 Python 端到端模型。低能电子段使用二维轴对称 WarpX 电磁静态 PIC；转换靶用 Geant4/QGSP_BERT_EMZ 与 G4beamline；正电子后段用 Impact-T。阶段间以 openPMD/HDF5/YAML 交接，自动相位搜索，并预留 Xopt 的 23 参数多目标遗传优化。

## 主要结论

- 模型中电子束以平均 145.7 MeV、59.3 pC 入射 6.35 mm 钨靶；Geant4 给出 `0.386 e+/e-`、`1.04 e-/e-` 和 `11.2 gamma/e-`，生成 22.9 pC、平均 17.1 MeV 且高发散的正电子。
- `0.7022 T` 捕获螺线管将正电子中位角发散由 478 mrad 降至 361 mrad；后续 RF 段把核心加速到约 250 MeV。
- 但从阴极发射的 1.36 nC 最终仅 0.37 pC 到达第八段末端；主损失在转换靶后，原因是大角发散撞壁和大能散导致的相位失配，正电子加速段存活率约 1.6%。

## 与本仓库方向的关系

- 主题关键词：electron beam；converter；bremsstrahlung；gamma；positron；WarpX；Geant4；openPMD；machine learning optimization。
- 这是电子束打钨转换靶、韧致辐射--电磁级联、二次正电子束与束线捕获的端到端范例，直接可借鉴到激光加速电子束的转换靶/二次源研究。
- WarpX--Geant4--openPMD 的跨代码衔接及“优化电荷、发射度、能散、束斑”的目标定义，也适合推广到 LPA 电子束、光核或辐射防护源项链条。
- 相关性评分：4/5。

## 局限与注意事项

这是传统热阴极注入器而非 LPA 或光核实验。第 2--8 段复用并缩放 SLAC 场图，只保证大致能量增益，作者明确指出场图/CAD 缺失使横向与传输结果尚不能视为最终精度；优化仅做过探索性运行，单次评估约 40 分钟，未报告优化后性能。
