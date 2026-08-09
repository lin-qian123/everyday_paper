# BORAY-3D: A ray tracing code for three-dimensional magnetized plasma configurations

## 基本信息

- 作者：Yuxuan Wang；Huasheng Xie
- 期刊/平台：arXiv preprint（physics.plasm-ph）
- DOI：https://doi.org/10.48550/arXiv.2608.05667
- 发表时间：2026-08-06
- 来源链接：https://arxiv.org/abs/2608.05667
- 本地 PDF：`daily/2026-08-10/pdfs/Wang et al. - 2026 - BORAY 3D ray tracing code.pdf`

## 研究问题与方法

现有射线追踪工具通常在“宽频但轴对称”与“三维但限电子回旋”之间取舍。BORAY-3D 在柱坐标 `(r, φ, z)` 直接输入磁场、密度和温度，保留环向非对称性使 `nφ` 可变，从而同时覆盖闭合/开放磁力线和任意二维、三维位形。它用冷等离子体色散关系推进几何光学射线；对 IC/helicon/LH 使用原 BORAY 的非相对论热等离子体吸收，对 EC 则加入相对论 Maxwellian 吸收与互易 ECE 辐射输运。

## 主要结论

- 单一框架覆盖 13.56 MHz--220 GHz：MUSE helicon、LHD 50 MHz 快波、tokamak 3.7 GHz LH、HSX/W7-X ECW 与 W7-X ECE。
- 对 tokamak 环向场波纹的 LH 轨迹与 GENRAY、W7-X 140 GHz O 模轨迹与 Raytrax/TRAVIS 比较，对 HSX 28 GHz X2 加热及 W7-X ECE 与公开结果比较，作者报告良好一致性。
- 三维建模消除了原 BORAY 的轴对称和非相对论 EC 限制；直接柱坐标输入适合含开放场线的边界区和非轴对称磁构型。

## 与本仓库方向的关系

- 主题关键词：magnetized plasma；RF heating；lower hybrid；electron cyclotron；ECE；ray tracing；stellarator；tokamak。
- 为磁约束聚变中的 RF 加热、电流驱动和 ECE 诊断提供可复现实用数值工具；可与本仓库的 PIC/数值模拟、实验诊断和机器学习代理工作互补。
- 它不直接研究激光加速或转换靶，但其波--等离子体传播、吸收和诊断链路对多物理耦合建模具有方法学参考价值。
- 相关性评分：3/5。

## 局限与注意事项

代码的核心是几何光学射线近似；当波长不再远小于平衡尺度、出现边界反射、衍射或模式转换时，不能据此做定量预测，需全波模型和实验对照。低频案例本身也被作者标注为需要谨慎使用；当前尚未包含碰撞阻尼、壁反射、电流驱动、非 Maxwellian 分布及 Bernstein 波的完整动理学色散处理。
