# A toroidally spectral field solver in the X-point Gyrokinetic Code for accurate simulation of reduced magneto-hydrodynamic modes

## 基本信息

- 作者：Robert Hager; C. S. Chang; Thomas Gade; Eric Held; Seung-Hoe Ku; Alexey Mishchenko; Aaron Scheinberg; Benjamin Sturdevant
- 期刊/平台：arXiv preprint
- DOI：https://doi.org/10.48550/arXiv.2606.25213
- 发表时间：2026-06-23
- 本地 PDF：`daily/2026-07-06/pdfs/Robert Hager et al. - 2026 - A toroidally spectral field solver in the X-point Gyrokinetic Code.pdf`

## 研究问题

XGC 是面向 tokamak 等离子体的全局电磁 total-f gyrokinetic particle-in-cell 代码。常规场求解器适合离子回旋半径量级的微湍流，但对低环向模数的大尺度 reduced MHD 型不稳定性，如 internal kink、tearing 和 peeling modes，需要更高精度的场求解能力。

## 方法与模型

- 在 XGC 中实现新的 toroidally spectral field solver。
- 放弃“大环径比下极向磁场远小于环向磁场”的近似，以提高低模数 MHD 型模式的准确性。
- 在环向方向采用谱离散控制数值复杂度。
- 允许新求解器与常规求解器并行使用，从而覆盖大尺度 MHD 型模式到小尺度微湍流的谱范围。
- 使用解析预测、ORB5 和 NIMROD 进行验证对比。

## 主要结论

- 新场求解器增强了 XGC 对大尺度 reduced MHD 型不稳定性的模拟能力。
- 该方法保留 XGC 对任意纵横比 tokamak 几何的全局 gyrokinetic/PIC 优势，同时提升低环向模数场结构的求解精度。
- 论文为 core-edge/SOL 一体化模拟中同时处理微湍流与宏观模式提供了数值基础设施。

## 与本仓库方向的关系

- 属于 PIC、gyrokinetic、磁约束聚变和高性能等离子体模拟方向。
- 对理解 XGC 这类全局动理学代码如何扩展到 MHD 型大尺度不稳定性很有价值。
- 可与近期 tokamak X-point 坐标构造、core/SOL 一体化模拟和边界等离子体输运主题衔接。

## 阅读价值

- 适合关注 XGC、gyrokinetic PIC、field solver、tokamak MHD instability 和多尺度模拟的读者。
- 如果后续要比较 XGC、ORB5、NIMROD 等代码在大尺度模式上的验证路径，这篇是直接材料。

## 局限与注意事项

- 当前是预印本，工程实现细节和最终期刊版本可能继续调整。
- 论文重点是场求解器和验证，具体装置预测仍需结合完整物理模型、边界条件和实验对照。
