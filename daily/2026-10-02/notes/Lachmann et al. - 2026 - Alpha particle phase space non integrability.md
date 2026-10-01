# 近全向性 stellarator 中 alpha 粒子的相空间非可积性

> A. L. Lachmann、A. R. Knyazev 与 E. J. Paul，arXiv:2609.39376v1（2026-09-30，稿件标注 under consideration for *Journal of Plasma Physics*）。以下基于官方 arXiv PDF、布局文本与 4 个抽样渲染页；MinerU 批次长时间停留在 `pending 0/?` 后使用 fallback。全文是无碰撞 guiding-centre 数值轨道研究，不是 alpha 诊断实验或反应堆实测约束。

## 一句话结论

作者用加权 Birkhoff 平均（WBA）把单个 Poincaré 截面扩展为覆盖径向—俯仰角的混沌图；在两类优化 stellarator 中，多谐波 Alfvén 本征模和全向性误差的共同作用远强于最大单谐波，且“混沌相空间比例”不能直接等同于“alpha 损失比例”，因为规则输运屏障仍可截断损失通道。

## 1. 方法：用收敛速度识别混沌

对轨道上的平滑观测量 `p(t)`，作者计算带端点抑制权重的时间平均：

$$
\mathrm{WBA}_T(p)=\int_0^T C\exp\!\left[-\frac{T}{t(T-t)}\right]p(t)\,dt.
$$

准周期轨道的加权平均会超收敛，混沌轨道则收敛慢。作者比较 `T/2` 与 `T` 的结果，把相对“有效数字数”低于 `3` 定义为混沌，并用传统 Poincaré 岛链/破碎分离器校准。轨道由 FIRM3D 积分，背景含近准轴对称 LBQA 与高剪切准等动力 SQuID，Alfvén 模结构来自 AE3D。

## 2. 无波时的相空间结构

- LBQA 中，混沌开始位置几乎贴着 passing/trapped 边界；barely trapped、ripple trapped 和多数 banana trapped 轨道的数字收敛度较低。
- 按 `10,000` 个 fusion-born、固定 `3.5 MeV` alpha marker 的轨道分类，大多数被俘获粒子是混沌的，只有约 `28%` banana-trapped 粒子被判为规则。
- passing 粒子总体规则，但在漂移有理共振附近会出现岛链、分离器破裂和局域混沌。

## 3. QS 误差、多谐波与损失

作者用相同背景比较“严格 QS”与“保留 QS 误差”。单个最大能量谐波下，严格 QS LBQA 的混沌比例/出生损失比例仅 `0.007/0.003`；保留误差后增至 `0.36/0.01`，说明背景非全向性会显著拓宽共振混沌层。

更重要的是，多谐波结果远强于最大单谐波：

- LBQA 的 `35` 谐波波场给出混沌比例 `0.80`、fusion-born 损失 `0.41`；
- 高剪切 SQuID 的 `20` 谐波波场给出混沌比例 `0.76`、损失 `0.22`；
- 两者混沌比例接近，但 SQuID 损失约为 LBQA 的一半。图中 `s0≈0.65` 附近的较规则带可能充当输运屏障，说明局部波幅、共振重叠和屏障拓扑共同决定最终损失。

## 4. 证据边界

- **作者数值证据：** FIRM3D guiding-centre 轨道、AE3D 模结构、WBA 分类及无碰撞 marker 损失；本地没有重跑。
- **方法边界：** WBA 依赖准周期运动；随机 pitch-angle scattering 等碰撞会破坏其适用前提。结果还依赖 marker 密度、积分时长、容差和阈值 `3`。
- **物理边界：** `chaotic fraction` 是采样相空间的分类，不是装置 alpha 功率损失；`fusion-born loss fraction` 也来自指定平衡、指定波幅和无碰撞初始分布，不能直接外推到反应堆热负荷。
- **尚未验证：** 非线性 Alfvén 模演化、碰撞、微湍流与真实诊断观测的耦合。

论文最有用的提醒是：只看最大谐波或单个 Poincaré 截面会低估多谐波共振重叠；但只报混沌比例也会高估实际损失，因为规则带和几何边界可切断到壁面的通路。
