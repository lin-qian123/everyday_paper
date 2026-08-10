# Effect of nonuniform density structure on burn-up ratio of multi-shock-compressed DT fuel in fast ignition

## 基本信息

- 作者：Tomoyuki Johzaki；Hideo Nagatomo；Yasuhiko Sentoku；Shinsuke Fujioka
- 期刊/平台：*Nuclear Fusion*，开放接受稿（in press）
- DOI：https://doi.org/10.1088/1741-4326/ae96c1
- 发表时间：2026-08-07
- 来源链接：https://iopscience.iop.org/article/10.1088/1741-4326/ae96c1
- 本地 PDF：`daily/2026-08-11/pdfs/Multi shock DT fast ignition.pdf`

## 研究问题与方法

多冲击压缩实心 DT 球可降低流体不稳定性，却会形成局域超高密度核心和承载大部分燃料质量的低密度外层。作者把一维内爆得到的时变密度剖面映射到二维轴对称燃烧模拟，在圆柱加热区以规定比功率沉积建立快点火热点；比较最大面密度和更晚点火时刻，并在保持燃料质量不变时人为提高外层密度，以分离总面密度与点火周围密度结构的影响。

## 主要结论

- 最大面密度时 `rho R_DT,max = 2.27 g/cm^2`，超过一半面密度集中于只含约 10% 燃料质量的中心高密度区；其余质量留在低密度尾部。中心点火后燃烧波进入外层即衰减，`12.4 kJ` 加热情形难以形成自持传播。
- 晚点火虽使高密区空间范围变宽，但所需点火能量约增加 39%，饱和聚变产额仅增约 22%，燃耗率约 11%，仍约为同面密度、均匀压缩燃料的一半。
- 将外层密度参数从约 50 提升至约 500 `g/cm^3` 会提高产额和燃耗率，结果逐渐接近 Fraley `Phi = rho R_DT/(rho R_DT + 7)` 曲线；但即使最高外层密度，局域核心仍令性能略低于同面密度均匀燃料。

## 与本仓库方向的关系

- 主题关键词：fast ignition；DT fuel；multi-shock compression；burn wave；density profile；ICF；two-dimensional burn simulation。
- 工作把靶设计由单一总面密度指标推进到“点火区沿燃烧波传播路径的密度”约束，对 HEDP/ICF 靶设计、激光点火能量预算与燃烧诊断解释有直接参考价值。
- 该研究未建模激光--等离子体耦合、快电子产生/输运和自生电磁场，因此不是完整激光驱动快点火方案的性能证明。
- 相关性评分：4/5。

## 局限与注意事项

计算使用一维内爆剖面映射后的二维轴对称燃烧模型，并以规定外部电子加热替代真实能量沉积；真实快点火的耦合效率仍受激光--等离子体相互作用、快电子输运与自生场控制。外层密度扫描同时改变总 `rho R_DT`，不能解释为在所有其他靶参数不变时的独立工程增益；结果应作为密度结构设计准则，而非已验证的反应堆增益预测。
