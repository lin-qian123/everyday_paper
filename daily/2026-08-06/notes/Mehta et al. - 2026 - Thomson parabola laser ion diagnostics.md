# Development of Thomson parabola spectrometer for diagnostics of ions driven by ultrahigh intensity laser: Simulations and numerical analysis

## 基本信息

- 作者：Kavil Mehta；Jatin Parashar；Shivangi Bidoliya；Prashant Kumar；Muhammad Tayyab；Anand Moorti；Juzer Ali Chakera
- 期刊/平台：arXiv preprint（physics.plasm-ph）
- DOI：https://doi.org/10.48550/arXiv.2608.03969
- 发表时间：2026-08-04
- 来源链接：https://arxiv.org/abs/2608.03969
- 本地 PDF：`daily/2026-08-06/pdfs/Manohar et al. - 2026 - Thomson parabola laser ion diagnostics.pdf`

## 研究问题与方法

汤姆孙抛物线谱仪须在能量覆盖、离子种类分离与空间分辨之间折中，而传统恒定电、磁场近似会忽略入口/出口的 fringe field。作者以 COMSOL 得到实际空间场分布，推导包含上升—平台—下降段的离子偏转解析式；再制造可调漂移段 TPIS，以磁场测量和 PW 激光铝箔靶实验验证。

- 仪器采用 0.25 mm 入射孔、150 mm 电极和磁铁、4.7 kV 最大电压、轴上约 0.2 T 磁场、75 mm MCP + 荧光屏；漂移段可调，示例为 80 mm。
- 实验为 800 nm、42 fs、靶上 0.8 J、约 `6.8×10^19 W/cm²` 的 Ti:sapphire 激光，45 度入射 0.8 或 10 µm Al 箔。

## 主要结论

- 实测轴向磁场与模拟的 NRMSE 为 1.75%，场区 `R²=0.9870`；采用非均匀场公式后，质子抛物线在整个偏转范围内与实测一致，而恒定场会低估低能端偏转。
- 单发图像中分辨出 `H+`、`C4+`、`C5+`、`C6+` 与 `Al10+`；对 1 MeV 质子给出 2.5% 能量分辨率。
- 薄箔（0.8 µm）质子截止能为 8.5 MeV，高于 10 µm 箔的 6 MeV；这支持较短热电子输运距离和再循环可加强后鞘场的解释。

## 与本仓库方向的关系

- 直接覆盖激光离子加速的束流能谱、物种鉴别和单发诊断，是辐照、核反应或二次源实验中的上游计量环节。
- 可变漂移段明确展示“高能量覆盖”与“离子轨迹分离/能量分辨”的工程折中，适合用于后续转换靶或剂量研究的输入束流标定。
- 相关性评分：5/5。

## 局限与注意事项

该装置只在一个 PW 条件、两种 Al 箔厚度下展示，测得的是谱仪分辨与离子截止能，不是绝对电荷、束流发射度、靶后输运或辐照剂量验证。将其用于更高能/更重离子或高重复频实验，仍须重新匹配漂移长度、探测器动态范围、几何接受角和标定链。
