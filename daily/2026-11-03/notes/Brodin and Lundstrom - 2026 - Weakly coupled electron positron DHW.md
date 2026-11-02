# DHW 的弱耦合电子—正电子约化：八个相空间分量与真空响应

## 0. 身份与证据

- 原题：*An approximate separation of the electron and positron degrees of freedom in the Dirac-Heisenberg-Wigner formalism*；Gert Brodin、Sebastian Lundström，Umeå University。
- [官方 arXiv 2610.41623v1](https://arxiv.org/abs/2610.41623v1)，**2026-10-30 12:00:17 UTC 提交**，11-02 recent 公告；13 页。[本地 PDF](../pdfs/Brodin%20and%20Lundstrom%20-%202026%20-%20Weakly%20coupled%20electron%20positron%20DHW.pdf)。精确标题 Crossref 前三未核实同作正式版，因此保留预印本身份。
- 证据为 **解析推导与已知极限的一致性比较**，没有数值收敛、运行时间、PIC、激光实验或真空双折射测量。本文无原始数据图，笔记保留可编辑公式，不制造数值曲线。

## 1. 为什么要保留两种粒子的弱耦合

等时、规范不变的 Dirac–Heisenberg–Wigner（DHW）Wigner 矩阵展开为 16 个实相空间函数：四个标量 $f_0,f_1,f_2,f_3$ 与四个三维矢量 $\mathbf g_0,\ldots,\mathbf g_3$。其中 $f_0$ 与电荷、$\mathbf g_1$ 与电流有关，单个原始分量并不等于电子或正电子概率分布。

传统 Foldy–Wouthuysen 单能区约化便于只保留一个粒子种类；本文的 WCEP（weakly coupled electron–positron）目标则是消去快的辅助变量，同时保留正负能区之间的量子源项，使真实粒子与真空响应能在同一框架中处理。

模型采用经典电磁平均场／Hartree 近似，使用 SI 单位。前提是场相对 Schwinger 临界场弱、时间和空间变化慢于／长于相应 Compton 尺度。**动量依赖保持全相对论，没有以 $p/(mc)\ll1$ 作为总模型前提。** 显式低阶推导另取弱自旋极化 $\mathbf g_0,\mathbf g_3=O(\hbar)$；这是本次截断的假设，不是任意自旋态的验证。

## 2. 从 16 到 4＋4 的具体含义

首先对非局域算子做梯度展开，并迭代消去 $f_1,f_2,\mathbf g_1,\mathbf g_2$ 的独立快演化。留下 $f_0,f_3,\mathbf g_0,\mathbf g_3$，共八个实标量分量。标量变化为

$$
f_\pm=\frac{\gamma_p f_3\pm f_0}{2},\qquad
\gamma_p=\sqrt{1+p^2/(m^2c^2)},\quad
\mathbf v_p=\frac{\mathbf p}{m\gamma_p}.
$$

式(30)给出

$$
D_{v,\pm}f_\pm=\frac12\left(\frac{Q_3}{\gamma_p}\pm Q_0\right),\quad
D_{v,\pm}=\partial_t\pm\mathbf v_p\cdot\nabla_r
+e(\mathbf E\pm\mathbf v_p\times\mathbf B)\cdot\nabla_p.
$$

$Q_0,Q_3$ 为所保留的二阶量子项；将它们置零才得到经典输运。DHW 的两分支动量约定有差别：同向运动的电子和正电子在这里的 $\mathbf p$ 符号相反。不能直接把“±速度”误读成两个物种必须反向传播。

矢量变化不是简单相加：

$$
F_{\pm i}=g_{0i}\pm A_{ij}g_{3j},\qquad
A_{ij}=\frac{1}{\gamma_p}\left(\delta_{ij}+\frac{p_ip_j}{m^2c^2}\right).
$$

其动量导数必须参与变换；式(52)得到每物种一条三分量矢量输运／进动方程，共 **每种 1＋3、两种 8 分量**。这不是已证实的二倍加速：相空间维度没有减少，源项、重构和导数成本仍需实现后测量。

推导中必须按照原方程的 $1/\hbar$ 因子决定保留阶数，例如 $\mathbf g_1$ 的二阶项可在矢量方程产生一阶贡献。仅按辅助量本身的阶数删项可能丢失所需自旋耦合。Maxwell 源也必须与演化方程同阶重构；第 7 页为简洁给出的输运＋极化＋磁化电流，明确又省略了自旋无关的 $O(\hbar^2)$ 项，不能直接当作完整二阶自洽电流。

## 3. 已检查的极限与未完成的真空响应

| 检查 | 论文结果 | 适用边界 |
|---|---|---|
| 非相对论单物种 | 磁梯度力与自旋方程同既有半经典模型一致 | 还舍去了轨道梯度量子项、真空和另一物种耦合；不是只取 $\gamma=1$ 即可 |
| 相对论自旋进动 | 先设 $\mathbf a=\gamma\mathbf F$，再变换到静止系 $\boldsymbol\zeta$，恢复 $g=2$ BMT | 去源项的比较；弱相对论电项含 Thomas 因子 1/2 |
| 高阶扩展 | 对 $(1+\tau^2D_t^2)^{-1}$ 作慢时间形式级数，$\tau=\hbar/(2mc^2)$ | 给出任意微扰阶的构造，不是级数全域收敛或强场非微扰有效性证明 |
| 真空极化 | 原始 DHW 真空分量非零，$f_{\pm,\rm vac}=-1$；重构并积分电流后需要电荷重整化 | 完整三维一般电磁场的动量积分／重整化并未在本文逐项完成 |

$\mathbf F$ 本身不是通常的静止系自旋；其长度一般不守恒。无源经典轨道上，真正保持的是式(88)对应的

$$
|\boldsymbol\zeta|^2=\gamma^2\left[|\mathbf F|^2-(\mathbf v\cdot\mathbf F)^2/c^2\right].
$$

真空的 $f_\pm=-1$ 提醒我们它们不是非负的经典粒子分布；场致变化也不自动表示真实粒子产生。第 11 页列出的弱场 Euler–Heisenberg 与导数修正是应恢复的已知综合响应，并引用前作纵向静电情形的显式验证。作者明确说本文没有完整执行一般电磁场的相空间重构、积分和重整化。需要同一调节量保持规范不变性、电流守恒及发散项的抵消，不能在正则化前任意丢弃边界项。

## 4. 与强场 QED／PIC 的联系及接续

它适合为含自旋与真空响应的动理学模型建立机制与阶次账本。本文所说强场环境仍必须满足其**相对临界场弱、慢变化**条件；不能用这套有限阶展开直接预测非微扰 Schwinger 对产生、QED 级联或激光伽马产额。辐射反作用也在本文 DHW 模型之外。

后续实现应先做无场／均匀场与单物种 BMT 测试，明确 $e$、动量及归一化约定，核验同阶 Maxwell 电流与守恒，再比较完整 DHW 的受控弱场算例；一般三维真空响应应独立完成积分与重整化。八分量与四分量 FW 模型的成本／精度比较尚未给出，不能仅按变量数认定优势。

## 5. 本轮核验

目视 PDF 第 4、5、6、7、9、11、12 页；文件头、哈希、三种页数与全页文本核验见[记录](../pdf_validation.json)。MinerU 返回 `HTTP 401 / A0211 / user token expired`，未产生有效转换，使用本地全文、布局文本和渲染。按 DOI／arXiv ID／规范化标题／作者／任务与旧 524 条去重；与既有真空对产生或辐射反作用模拟不是同作。见[版本核对](../research/version-checks.json)、[来源](../research/sources.jsonl)。未运行作者求解器或实验。
