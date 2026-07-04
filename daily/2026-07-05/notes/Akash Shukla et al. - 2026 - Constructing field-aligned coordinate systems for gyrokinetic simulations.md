# Constructing field-aligned coordinate systems for gyrokinetic simulations of tokamaks in X-point geometries

## 基本信息

- 作者：Akash Shukla; Ammar Hakim; James Juno; Gregory W. Hammett; Manaure Francisquez
- 期刊/平台：Journal of Plasma Physics
- DOI：https://doi.org/10.1017/S0022377826101779
- 发表时间：2026-06
- 本地 PDF：`daily/2026-07-05/pdfs/Akash Shukla et al. - 2026 - Constructing field-aligned coordinate systems for gyrokinetic simulations.pdf`

## 研究问题

Tokamak 等离子体扰动通常沿磁场方向拉长、垂直磁场方向尺度短，因此 gyrokinetic 代码常使用 field-aligned coordinates 降低数值成本。但在 X-point 附近，极向磁场趋零，传统场线跟随坐标会出现奇异性，阻碍 core 与 scrape-off layer (SOL) 的统一模拟。

## 方法与模型

- 提出一种在标准场线跟随坐标下生成网格并计算几何量的算法。
- 目标是在 X-point 几何中避开坐标奇异性，使二维轴对称 gyrokinetic 模拟可以覆盖更完整的 tokamak 区域。
- 通过平流问题、边值问题和几何量收敛测试检验算法。
- 特别检查 X-point 附近的数值收敛和几何一致性。

## 主要结论

- 所提算法可在 X-point 附近保持大于一阶的收敛表现。
- 方法保留了 field-aligned 坐标对强各向异性等离子体结构的数值优势，同时缓解了 X-point 奇异性问题。
- 论文展示了算法的几何一致性，为 core/SOL 一体化 gyrokinetic 模拟提供更稳健的网格基础。

## 与本仓库方向的关系

- 属于 PIC/动理学与磁约束模拟基础设施方向。
- 对 tokamak 边界、SOL、divertor 以及 core-edge coupled simulations 有直接方法价值。
- 可与本仓库关注的高保真 plasma simulation、数值算法和 fusion application 主题衔接。

## 阅读价值

- 适合关注 gyrokinetic 代码、tokamak X-point/SOL 模拟、场线跟随网格和几何离散的读者。
- 如果后续比较 Gkeyll、GENE、GX 或其他动理学代码的边界几何处理，这篇可作为坐标构造参考。

## 局限与注意事项

- 论文重点是二维轴对称几何下的算法与收敛验证，真实三维扰动、复杂壁面和全装置工程边界仍需额外处理。
- 方法价值主要体现在数值基础设施，对具体物理输运预测还需结合完整模拟案例评估。
