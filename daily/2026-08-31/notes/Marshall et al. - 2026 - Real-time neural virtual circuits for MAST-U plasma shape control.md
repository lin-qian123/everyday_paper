# Real-time virtual circuits for plasma shape control via neural network emulators: integration and testing in the MAST-U PCS 笔记

## 0. 论文信息

- 作者：Matthew J. Marshall；Edward Jones；Graham J. McArdle；Alasdair Ross；Kamran Pentland；Nicola C. Amorisco；Charles Vincent；Martin Kochan；Colin Hogben；Graham Jones；Adam Stephen；George K. Holt；Adriano Agnello
- 期刊/平台：arXiv preprint；文中标注 submitted to *Fusion Engineering and Design*
- DOI：[10.48550/arXiv.2608.26216](https://doi.org/10.48550/arXiv.2608.26216)
- 发表时间：2026-08-26
- 来源链接：[arXiv 摘要页](https://arxiv.org/abs/2608.26216)
- 本地 PDF：`daily/2026-08-31/pdfs/Marshall et al. - 2026 - Real-time neural virtual circuits for MAST-U plasma shape control.pdf`

## 1. 摘要与文章定位

本文不是提出新的等离子体物理模型，而是把已训练的神经网络形状 surrogate 接入 MAST-U plasma control system（PCS）。模型根据实时等离子体电流、PF 线圈电流和电流密度剖面参数预测形状及 Jacobian，再实时构造 virtual circuit（VC），将目标形状变化转换为 PF 线圈电流请求。

文章贡献是完整的软件集成、固定内存和低延迟通信设计、PCS mock/replay 测试，以及在真实 MAST-U 炮次中与常规 VC 的 piggyback 对照。论文结论是该实现已达到实验测试所需的延迟和一致性条件；并非“神经网络已经取代所有形状控制”，也不是激光等离子体实验。

## 2. Introduction：从离线 VC 到 state-aware VC

传统 VC 通常从预先选定的一组 Grad–Shafranov（GS）平衡有限差分得到，并按预设时间区间使用。当等离子体形状偏离预定轨迹时，VC 灵敏度会变差。本文的思路是：使用神经网络近似形状灵敏度，在实时测量状态下更新 VC，使控制器能够响应毫秒尺度的未知轨迹变化。

作者把真正的困难归纳为完整部署链：仿真测试、实时执行、诊断与执行器接口、机器保护约束、通信和实验验证，而不是单一的网络结构。

## 3. MAST-U PCS 中的形状控制

MAST-U PCS 使用 LEMUR 从磁诊断得到局部形状描述向量 $\vec P$，包含内/外中平面半径、X 点位置、divertor nose 半径、strike-point 半径和 squareness gap 等。形状控制器产生目标变化率，再由 VC 转换为 PF 线圈电流变化率。

### 3.1 灵敏度矩阵与虚拟电路

$$
S=\frac{\partial\vec P}{\partial\vec I_{\mathrm{shape}}},\qquad
\frac{\partial\vec I_{\mathrm{shape}}}{\partial t}=S^{+}\frac{\partial\vec P}{\partial t}
$$

**变量说明：** $\vec P$ 为等离子体形状参数向量，$\vec I_{\mathrm{shape}}$ 为 PF 线圈电流向量，$S$ 为形状对线圈电流的灵敏度矩阵，$S^+$ 为 Moore–Penrose 伪逆。

**推导过程：**

1. 在当前等离子体状态附近，对形状参数关于线圈电流线性化，得到 $d\vec P\approx S\,d\vec I$。
2. 线圈数量和受控形状量通常不完全相等，因此不能直接求普通逆矩阵。
3. 用伪逆 $S^+$ 找到最小二乘意义下实现目标形状变化的线圈电流变化，再在输出端施加机器保护限制。

**物理直觉：**

VC 是一个局部“方向盘”：它告诉 PCS 要把每个 PF 线圈电流怎样组合，才能尽量只改变指定形状量而不扰动其它受控量。NN 的作用是快速给出随状态变化的 $S$，不是替代 PCS 的保护逻辑。

**关键点/物理意义：**

- 该线性化只在训练和验证覆盖的状态域附近可靠。
- 伪逆病态、输入校准差异和输出限幅都会影响最终线圈请求。
- 论文保留常规 VC Algorithm 在后台运行，用于覆盖/替换选定条目。

## 4. Real-time Virtual Circuit Server：数值循环与工程约束

TensorFlow/Keras 原生推理的延迟抖动和运行期内存分配不适合 PCS。作者选择 TensorFlow Lite for Microcontrollers（现称 LiteRT for Microcontrollers）作为推理引擎，将 Keras 模型转为 flatbuffer，配合描述文件装载到 PCS。

RTVC Server 分为初始化、内存分配和 server mode。server mode 使用共享内存获取输入、执行推理/有限差分 Jacobian，再返回输出；用共享标志而非 OS semaphore，避免常规 syscall。支持 shape-only、单线程 Jacobian 和多线程 Jacobian 三种模式，也支持由 8 个模型组成的 ensemble。

### 4.1 延迟与资源

表 1 的开发机全链路测试显示：无推理平均约 `650 ns`、约 `1.5 MHz`；单模型平均 `50 μs`，p99 为 `190 μs`；8 模型 ensemble 平均 `590 μs`、p99 `930 μs`。8 模型结果使用固定约 `1 GB` 模型缓冲区和每模型 `100 kB` 中间缓冲区，总内存低于 `1.1 GB`。

这些结果是在类似 PCS 的开发硬件上测得，不能直接写成所有 PCS 硬件上的保证值。作者也计划后续生成针对硬件架构优化的二进制。

## 5. PCS Integration and Testing：从推理到线圈请求

RTVC Algorithm 将实时输入送入服务器，获取 ensemble 平均 Jacobian $S$，在 PCS 侧用 CBLAS 求伪逆，再覆写常规 VC 的相应条目。计算分到两个 PCS 核：CPU2 以 `10 kHz/0.1 ms` 处理 VC 覆写和 PF 请求，CPU5 以 `2 kHz/0.5 ms` 处理服务器信号、输入/输出和伪逆；服务器在独立绑定线程上异步运行。

首次伪逆调用约需 `80 μs`，主要是 worker 初始化；之后约 `8–12 μs`。在 shot replay 和 FPDT closed-loop 对照中，多数测试的累计 PF 线圈电流请求达到 $R^2\ge 0.95$。偏移主要归因于真实 PCS 每个输入通道具有独立 ADC offset/scaling，而仿真回放使用统一校准值。RTVC 更新周期保持在 `5–5.6 ms`。

图 1 展示初始化/运行分层和共享内存；图 2 展示 53000、53010 两个历史炮次的 7 种软件测试情形。这里的图和数值支持“软件实现与参考 emulator 一致”，不直接证明新的闭环物理性能。

## 6. MAST-U commissioning shots：真实数据上的 piggyback

在炮次 `53974`、`53975`、`53976` 中，RTVC 与常规 VC 并行运行，但真正控制 PF 线圈的是常规 VC；RTVC 记录它如果被启用会发出的请求，再与 TensorFlow emulator 对照。未通过机器安全限幅的请求呈现近乎完全一致，完成了集成验证。

对于约 `1 s` 炮次，`5–5.6 ms` 的更新周期对应约 `130–144` 个 state-dependent VC。论文结论称 RTVC 已为实验测试做好准备；文中另引的“已主动控制多种 MAST-U 等离子体”属于单独工作，不应把本文 piggyback 结果写成本文完成的全闭环主动控制性能。

## 7. 结论、局限与应用关系

### 7.1 已验证内容

- 模型可转换为固定内存的实时推理格式。
- 共享内存和绑定线程通信能满足所考虑的 PCS 延迟要求。
- 完整 RTVC Algorithm 在 replay、mock PCS 和真实 MAST-U piggyback 炮次中与参考 emulator 保持高一致性。

### 7.2 未完成或需继续验证

- 当前使用通用 Linux binary，PCS 硬件特定的 vectorization 和更低抖动尚待实现。
- 真实 ADC 独立校准与仿真统一校准之间的差异会积累到线圈请求，需要在主动控制前持续审计。
- NN 泛化、超出训练域的等离子体形状、安全限幅与故障恢复仍是部署风险。

### 7.3 与本仓库方向的关系

- 主题关键词：magnetic fusion；MAST-U；plasma shape control；neural network emulator；real-time inference；Jacobian；PCS。
- 相关性评分：4/5。
- 可借鉴处：把 surrogate、Jacobian、伪逆、固定内存、通信延迟和硬件在环测试作为一个可复现实验控制链，而不是只报告离线模型误差。
- 证据边界：这是磁约束聚变 PCS 软件集成与验证，不是激光等离子体/PIC 运行结果，也没有给出激光加速束流、转换靶 γ 或核反应数据。

## 8. 复习用速记

RTVC 的关键不是“NN 预测形状”本身，而是把 NN Jacobian 可靠地接入伪逆 VC、固定内存服务器、共享内存通信和 PCS 安全链。本文证明了软件一致性与延迟可行性，真实炮次主要是 piggyback commissioning，主动控制性能需看另文。
