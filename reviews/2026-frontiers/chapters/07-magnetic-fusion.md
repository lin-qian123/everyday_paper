# 07 磁约束聚变与快粒子：从磁面平衡到可验证的实时控制

> 截至 **2026-09-30**。仓库的“磁约束聚变与 alpha 粒子”路由有 43 条，全部在台账中标为 2026；部分只是出现 fusion/alpha 等关键词的 ICF 或束靶论文。本章人工围绕磁面、输运、快粒子、边界和控制选文，不把 43 条当 43 项磁聚变验证。本库对 AI 与算法论文有明显取样偏好，不能据此认定磁聚变前沿只剩机器学习。

## 1. 入门：磁场为什么能约束，为什么又总会漏

带电粒子在磁场中绕磁力线回旋，垂直运动半径 $\rho_s=m_sv_\perp/(|q_s|B)$，角频率 $\Omega_s=|q_s|B/m_s$。磁场不会对粒子直接做功，因为 $\mathbf v\cdot(\mathbf v\times\mathbf B)=0$。它能限制运动方向，却不能自动阻止沿场方向逃逸，也不能让所有粒子永远停在同一磁面。托卡马克把磁场线绕成螺旋闭合体系，环向电流产生极向场；恒星器主要用复杂外线圈建立螺旋磁场，少依赖等离子体电流，但三维轨道和工程几何更复杂。[R141](../appendices/reference-catalog.md#r141) [R231](../appendices/reference-catalog.md#r231)

磁聚变的燃料温度可达 keV，壁面则承受有限热负荷；核心越能保存能量，边缘越必须有受控排热路径。闭合磁面之外是刮削层（SOL），场线通向偏滤器。X 点是极向磁场为零的鞍点，分离面穿过它，把闭合与开放场线分开。核心约束、边界热流、线圈控制和快粒子不能分别做到“最好”就保证全装置可行：例如更窄热流剖面可能带来更高局部材料负荷，更强快粒子模可能一边损失 alpha、一边激发剪切流降低微湍流。[R234](../appendices/reference-catalog.md#r234) [R239](../appendices/reference-catalog.md#r239) [R142](../appendices/reference-catalog.md#r142)

读本章时把四个问题分开：**磁场几何能否平衡压力；在该几何中粒子和热如何输运；高能粒子是否改变稳定性；诊断和控制能否在实际时间预算内感知并执行。** “平衡预测准确”不等于“输运准确”，“网络推理快”不等于“装置闭环已经运行”。今年本库文章最值得关注的进展，正是把这些层次接得更紧，同时也暴露层与层之间的空白。

## 2. 单位与能量账本：读快粒子论文以前要懂的量

这里 $n$ 是总 DT 离子数密度，单电离时 $n_e\simeq n$，$T$ 用能量单位；当文献以 keV 写温度，代入 SI 要转换成 J。$\beta=2\mu_0p/B^2$ 比较热压与磁压，不是效率。安全因子 $q$ 描述场线绕环向与极向的相对圈数，不是电荷。归一化半径 $r/a$、$\rho$（磁通半径）和质量密度 $\rho$ 在不同论文中可重名，阅读时必须先看定义。约束时间 $\tau_E=W/P_{\rm loss}$ 是储能除能量损失率，不能和某个粒子从中心逃逸的飞行时间互换。[R142](../appendices/reference-catalog.md#r142) [R342](../appendices/reference-catalog.md#r342)

**教学推导：最简 DT 自热条件。** 等摩尔 DT 时反应率为 $n^2\langle\sigma v\rangle/4$，alpha 功率密度为该率乘 3.5 MeV。等温电子与离子的热能密度约 $W/V=3nT$。忽略辐射、杂质和外加热，要求 alpha 加热补偿损失：

$$
\frac{n^2}{4}\langle\sigma v\rangle E_\alpha
\gtrsim\frac{3nT}{\tau_E}
\quad\Rightarrow\quad
n\tau_E\gtrsim\frac{12T}{\langle\sigma v\rangle E_\alpha}.
$$

左右单位均为 $\mathrm{s/m^3}$。这解释了 Lawson 型条件为什么出现 $n\tau_E$ 或 $nT\tau_E$；真实阈值随温度、辐射和 alpha 沉积改变。等离子体增益 $Q=P_{\rm fusion}/P_{\rm aux}$ 只把聚变热与辅助加热比较，尚未扣线圈、低温、泵、RF 墙插效率和热电转换。即使达到某个 $Q$，也不能直接宣称净电站功率。alpha 要在内部停住是必要条件，但高能粒子轨道与激发模式会改变它是否做到。[R141](../appendices/reference-catalog.md#r141) [R278](../appendices/reference-catalog.md#r278)

## 3. Grad–Shafranov：不是一张磁通图，而是一组平衡假设

**教学推导，静态、轴对称、标量压强理想 MHD。** 柱坐标为 $(R,\phi,Z)$，令 $\partial_\phi=0$。引入每弧度极向磁通 $\psi$（习惯单位 Wb），并写

$$
\mathbf B=\frac1R\nabla\psi\times\mathbf e_\phi+
\frac{F}{R}\mathbf e_\phi.
$$

这样自动满足 $\nabla\cdot\mathbf B=0$，且 $B_R=-\partial_Z\psi/R$、$B_Z=\partial_R\psi/R$。磁面就是 $\psi$ 常数面。力平衡 $\nabla p=\mathbf J\times\mathbf B$ 沿磁场点乘，右侧为零，所以 $\mathbf B\cdot\nabla p=0$，可取 $p=p(\psi)$；环向分量同样给 $F=F(\psi)$。由 Ampère 定律算环向电流，

$$
J_\phi=-\frac{1}{\mu_0R}\Delta^*\psi,
\qquad
\Delta^*=R\partial_R\left(\frac1R\partial_R\right)+\partial_Z^2.
$$

代回横向力平衡就得到

$$
\Delta^*\psi=-\mu_0R^2\frac{dp}{d\psi}-F\frac{dF}{d\psi}.
$$

这是一类非线性椭圆方程。固定边界问题给定磁面形状；自由边界还要解线圈、真空场、等离子体边界和容器响应的匹配。正问题从线圈/剖面求磁通；逆问题从目标形状或诊断反推线圈/内部状态。二者输入不同，不能把正向代理的测试误差拿来证明诊断重建可靠。[R268](../appendices/reference-catalog.md#r268) [R308](../appendices/reference-catalog.md#r308) [R324](../appendices/reference-catalog.md#r324)

大纵横比近圆截面时 $q\simeq rB_\phi/(RB_\theta)$，更一般需沿磁面积分场线螺距。$q=1$ 面与锯齿、鱼骨等模式有关；不同剖面即使边界形状相同也可能有不同 $q$。因此只给轮廓不能唯一恢复电流密度与稳定性。流、各向异性、三维扰动或快速瞬态明显时，静态 GS 需要推广，不能把方程残差小当成全物理成立。[R239](../appendices/reference-catalog.md#r239) [R149](../appendices/reference-catalog.md#r149)

**重点 1：毫秒级双零位 GS 代理到底学了什么。** R268 的最佳 FNO 在 500 个测试平衡上的平均相对 $L_2$ 误差约 0.052%，GPU 单算例约 2.77 ms。它是一个壁面、受控双零位拓扑、固定 65×65 网格的 FreeGS 标签代理；X 点位置是输入条件，不能称从磁诊断独立预测 X 点。该研究同时报告磁通、几何和离散残差，值得借鉴，但约 640 倍速度是相对其 FreeGS 配置，不能普遍替代生产求解器的真实实时比较。更低磁通误差也不自动给更好 $q$、边界和线圈请求。[R268](../appendices/reference-catalog.md#r268)

**重点 2：EXL-50U 架构比较中，插值赢家未必外推赢家。** R305 的 IID 测试里 Transformer 更准，CNN 在推理与 OOD 鲁棒性间更均衡；不同架构在规定几何外推下的退化差别很大。标题中“validation on EXL-50U”主要是代理、GS 与参考平衡的装置关联数值对照，不是网络驱动电源的放电证据。对实验选型，误差分布、计算延迟、拓扑变化与传感器噪声比只报平均 $L_2$ 更重要。[R305](../appendices/reference-catalog.md#r305)

**重点 3：没有磁诊断的平衡挑战是一种有意提高难度的反问题。** R324 从外 PF 电流和 Thomson $T_e,n_e$ 剖面恢复磁通，要求 DIII-D 到 MAST 零样本迁移。它是开放数据/竞赛协议文章，尚无获胜系统或装置闭环结果。摘要总 shots 与正文发布 shots 不同，具体 release 应按正文约 11,208 shots 口径；本章不自行补出过滤原因。非磁输入难以约束内部状态，既有诊断重建标签也可能有偏差。它把跨装置、炮次隔离和从磁通导出一致几何量纳入评估，价值在把泛化问题变成可测问题。[R324](../appendices/reference-catalog.md#r324)

## 4. 漂移、碰撞与湍流：从轨道到热流要跨几层

**教学推导。** 把匀强场回旋平均后，横向电力与磁力平衡给 $q\mathbf E_\perp+q\mathbf v_E\times\mathbf B=0$，这里仅求垂直分量，沿场电场仍可加速粒子；由横向方程解得

$$
\mathbf v_E=\frac{\mathbf E\times\mathbf B}{B^2}.
$$

电荷约掉了，所以理想 $E\times B$ 漂移对不同物种同方向、同速度；它可形成流剪切，却不是电子和离子自然分离的机制。缓变磁场还给

$$
\mathbf v_{\nabla B}=\frac{m v_\perp^2}{2qB^2}\mathbf b\times\nabla B,
\qquad
\mathbf v_c=\frac{m v_\parallel^2}{qB}\mathbf b\times\boldsymbol\kappa,
\quad\boldsymbol\kappa=(\mathbf b\cdot\nabla)\mathbf b.
$$

这里 $m,q$ 为所考察物种的质量与电荷，$\mathbf b$ 为磁场单位向量，$\boldsymbol\kappa$ 为场线曲率向量。这两项随电荷符号改变。环形磁场的不均匀与曲率会使轨道偏离单条场线；被困粒子形成香蕉轨道，碰撞不断把粒子换到不同轨道，产生新经典输运。恒星器三维场更容易引入轨道损失，所以设计既要平衡，也要看轨道与碰撞率。[R231](../appendices/reference-catalog.md#r231) [R141](../appendices/reference-catalog.md#r141)

新经典输运并非“新发现的经典”，而是环形/三维几何下的碰撞输运；湍流输运则来自涨落相关，例如径向粒子通量 $\Gamma_r=\langle\widetilde n\widetilde v_{E,r}\rangle$。只有涨落幅度不够，密度与电势的相位关系才决定净通量。局部热扩散系数有时便于全剖面计算，但它可能吸收有限轨道宽度、几何和非局域效应，不能都称为普适材料常数。[R074](../appendices/reference-catalog.md#r074) [R349](../appendices/reference-catalog.md#r349)

**陀螺动理学的教学推导。** 当 $\rho/L\ll1$、$\omega/\Omega\ll1$，可平均掉快速回旋相位，把六维位置速度压成五维回旋中心相空间。粒子在半径 $\rho$ 的圆上看到的 Fourier 电势平均为

$$
\frac1{2\pi}\int_0^{2\pi}e^{ik_\perp\rho\cos\theta}d\theta
=J_0(k_\perp\rho).
$$

所以有限 Larmor 半径效应以 Bessel 因子进入耦合，高波数扰动被回旋平均削弱。这个降维保留慢湍流和共振，但不覆盖所有电子回旋频率、Debye 尺度或任意强激光过程。ITG 的自由能来自离子温度梯度；漂移波、波粒共振、$E\times B$ 非线性和 zonal flow 共同决定饱和，单看线性增长率不能直接给出热流。[R330](../appendices/reference-catalog.md#r330) [R074](../appendices/reference-catalog.md#r074)

**重点 4：yancc 加速的是明确近似下的新经典求解。** R231 采用 GPU/可微路线，在其 MONKES/SFINCS 对照范围内约到 1% 一致，速度和内存有明显收益。这有助于高维几何优化和灵敏度计算，但小归一化回旋半径、局部径向处理仍是模型边界；GPU 更快不表示已经包含全轨道或湍流。它应作为可靠碰撞基线，与非线性 GK 互补，而不是拿一种输运机制替另一种。[R231](../appendices/reference-catalog.md#r231)

**重点 5：分钟级 GTC 通过保留相关频谱来降成本。** R330 的 hybrid spectral PIF 仍推进五维回旋中心粒子，却将场用有限环向模、径向有限差分与相关极向谐波表示，减少完整环向网格和通信。单模 2000 步在笔记本 RTX 4090 约 78.2 s 的数字是特定模型和较小有效问题规模，不能表述成任意三维全电磁 GK 均到分钟级。线性频率/增长率、非线性热流与 zonal flow 检验比标题更能说明保留了什么。X 点几何的 R106 和 XGC 环向谱求解的 R157 处理另一种基础瓶颈，三者不能简单按一个加速比排名。[R330](../appendices/reference-catalog.md#r330) [R106](../appendices/reference-catalog.md#r106) [R157](../appendices/reference-catalog.md#r157)

**重点 6：AI-GX 恒星器优化的负结果应和正结果一起读。** R379 从超过 20 万次局域、静电、绝热电子 GX 非线性计算训练 CNN 集成，并接入平衡与输运优化。作者报告特定循环约 72 倍加速，有效构型的高保真后处理支持离子温度提升；但最高代理打分曾落到训练分布外、非嵌套磁面的非法解，还污染遗传搜索后代。教训不是“AI 不可用”，而是物理可行性、集成不确定性和高保真回退必须进入目标函数。此数据不覆盖动理学电子、有限 beta 全电磁或全局效应；代理提升只适用于它真正学过的物理层。[R379](../appendices/reference-catalog.md#r379)

## 5. alpha、鱼骨与逃逸电子：高能尾既是资源也是风险

**重点 7：ARC-class alpha 的湍流反馈。** R142 用线性与非线性 CGYRO 对比真实快 alpha 与人为热化 alpha，指向内核 $r/a\le0.5$ 的湍流通量降低和非线性 ITG 阈值移动。机制涉及快粒子模、zonal flow 与背景湍流，不只是把 beta 增加造成线性稳定。它是 ARC-class 参数下的局部模拟，不是未来装置的实测增益；真实 alpha 分布、全剖面功率平衡和电磁模式损失仍应一起检查。高能 alpha 可能稳定微湍流，同时又通过 Alfvén 本征模向壁损失，两个结论可同时成立。[R142](../appendices/reference-catalog.md#r142)

**重点 8：恒星器 alpha 约束从“优化器”转向“可行设计空间”。** R141 用数据分位变换和边界点 PCA，把几何搜索空间重新组织，再做异步 Bayesian optimization 与 guiding-center 轨道跟踪。创新不只在采样算法，而在减少边界自交和平衡失败、让优化变量尺度更合理。良好轨道约束可以出现在偏离传统准对称范式的候选上，但轨道目标不等于线圈可制造、低湍流、良好边界和整机稳定都成立。与 R379 并读可以看到：一项优化减少 alpha 损失，另一项压低离子湍流，下一步应是共同约束而非独立报最优值。[R141](../appendices/reference-catalog.md#r141) [R379](../appendices/reference-catalog.md#r379)

**重点 9：EAST 鱼骨驱动 zonal flow 的证据层次。** R239 用鱼骨 burst、低频流、多普勒反射计和双相干分析，支持鱼骨自耦合产生细径向反向流；GTC 给出热离子与电子反号贡献抵消的机制解释。同步出现只是第一层，相位耦合比纯时间相关更有力；早期流增长早于鱼骨峰更支持 beat-driven，但不能排除晚期快离子外逸附加贡献。真实测到流，不等于已经证明长期约束改善或 alpha 自热增加。它为 R142 的多尺度反馈提供相关实验参照，尚不是同一条件的验证。[R239](../appendices/reference-catalog.md#r239)

快粒子输运代理 R278 学的是指定 ITER 工况、已非线性饱和的 FAR3d 响应，不是完整模增长时间过程。R255 从变分结构构造全动理学离子/陀螺电子混合框架，提供守恒设计背景。R109 给开放磁阱加聚变产物和中性束俘获源项；R244 讨论自旋极化燃料的 alpha channeling。它们都涉及快粒子，物理层次和证据成熟度却不同，不宜因 alpha 关键词并成一条性能增长曲线。[R278](../appendices/reference-catalog.md#r278) [R255](../appendices/reference-catalog.md#r255) [R109](../appendices/reference-catalog.md#r109) [R244](../appendices/reference-catalog.md#r244)

**教学推导：逃逸电子的阈值为何不是单一温度。** 高能电子的碰撞摩擦随速度变化；相对论极限的临界电场常写为

$$
E_c\simeq\frac{n_e e^3\ln\Lambda}{4\pi\epsilon_0^2m_ec^2}.
$$

它是理想完全电离、无额外损失的量级式。外电场的加速 $eE_\parallel$ 超过有效摩擦时，某些电子进入 runaway 区；同步辐射、部分屏蔽、俯仰角散射与轨道损失会改变实际阈值。一次高能电子与低能电子的大角碰撞还能产生新的逃逸种子，造成 avalanche，因此“初始尾很少”也未必安全。[R243](../appendices/reference-catalog.md#r243) [R128](../appendices/reference-catalog.md#r128)

**重点 10：全 $f$ PIC 雪崩不是只加一个指数源。** R243 在 3D 相对论电子模型中加入 knock-on 碰撞与重采样，保留高俯仰角、受困和逆电场传播二次电子，并检查能量动量与三维结构。全局守恒表现好不等于每个局部 cell 严格守恒；JET-like 终止计算也不是 ITER 长时间反馈验证。R128 的伴随/PINN 层级代理可加速电流、均能和能谱预测，R175 的 Aditya-U 薄靶硬 X 射线系统试图隔离受限快电子与壁上厚靶辐射；计算和诊断应该相互约束，不能用总 HXR 增大唯一推 runaway 数增加。[R243](../appendices/reference-catalog.md#r243) [R128](../appendices/reference-catalog.md#r128) [R175](../appendices/reference-catalog.md#r175)

## 6. 波加热与启动：射线轨迹正确还不够

射频波要先进入等离子体，再在合适位置把能量与动量传给粒子。几何光学射线近似要求波长远小于背景变化尺度；遇到 cutoff、模式转换、反射或强非局域区应另用全波/动理学。R269 的 BORAY-3D 覆盖三维磁构型中的多个频段，适合比较传播与吸收；它并不自动完成壁反射、非 Maxwell 分布或全部电流驱动模块。[R269](../appendices/reference-catalog.md#r269)

**重点 11：螺旋波电流驱动的实验与残差反演。** R342 在 DIII-D 用 476 MHz 行波天线，ECE 调制响应支持核心功率沉积；MSE 约束平衡与已知电流源模型之差给中心螺旋波电流约 $20\pm10$ kA。它包含真实放电和“只加热”对照，但电流不是独立电流探头读数。共振条件 $v_\parallel=\omega/k_\parallel=c/n_\parallel$，解释波把平行动量交给电子；约 $n_\parallel=3$ 对应相速度 $c/3$。实验处于较低 beta 原理验证，单侧天线未做方向反转，所以反应堆效率仍需专门检验。本次官方核查首次 arXiv 提交为 09-11，台账 09-08 不宜当已确认首次公开日期。[R342](../appendices/reference-catalog.md#r342)

**重点 12：宽带下混合波改变的是边带结构。** R228 的理论结合 Alcator C-Mod 边带，指出有限带宽可把非共振连续谱重组到离子回旋谐波附近，且增长率仍可较大。它和 ICF 的宽带 TPD 一样提醒：带宽既改变相干，也改变共振结构，不能只看“失相干所以稳定”。R367 的 BREAK 启动模拟还将 EC 非线性吸收、电离、碰撞随机运动与开场线损失连接起来；作者 ITER 级气体击穿预测不等于 burn-through、闭合磁面或电流爬升全部成功。[R228](../appendices/reference-catalog.md#r228) [R367](../appendices/reference-catalog.md#r367)

## 7. 边界热流与控制：今年最应认真分级的进展

**重点 13：ST40 双诊断纠正热流解释。** R234 以 Langmuir 探针电流与红外热像比较宽/窄 SOL 热流剖面，强调电子电流贡献对解释窄热流重要。探针和红外的相符并非两台仪器都直接测同一量：一台测收集电流，一台通过表面温升与热传导反演热流；几何、鞘层与材料响应都在中间。应检查绝对标定、空间映射和功率守恒，然后才谈热流宽度标度。[R234](../appendices/reference-catalog.md#r234)

**重点 14：SafeDivertor 重建标签也继承红外反演误差。** R270 从宏观状态信号重建时空热流，在 77 炮数据上采用炮次隔离、频谱监督和物理先验；其意义在兼顾形态、时间谱与高频误差，而非仅小 MSE。标签仍来自放电后 IR—导热分析，网络不能越过绝对标定链，亦未展示跨装置或完整闭环。R235 的 SOLPS-ITER 循环一致性代理和 R349 的 TJ-II inverse PINN 也一样：内部循环自洽、方程残差小与真实未观测机制正确，是三个不同问题。[R270](../appendices/reference-catalog.md#r270) [R235](../appendices/reference-catalog.md#r235) [R349](../appendices/reference-catalog.md#r349)

**教学推导：虚拟电路怎样实现形状解耦。** 对线圈电流附近作一阶展开，$\Delta\mathbf P\simeq S\Delta\mathbf I$，$S=\partial\mathbf P/\partial\mathbf I$ 是形状响应矩阵。目标通道与线圈数不同或耦合强时，用伪逆得 $\Delta\mathbf I=S^+\Delta\mathbf P$。这就是把“只动某个形状量”翻译成多个线圈协调动作。平衡变化会让 $S$ 变，离线查表需要阶段切换；实时代理可以更新局部 $S$，但伪逆条件数、剖面不确定性和执行器饱和仍需经典保护。[R318](../appendices/reference-catalog.md#r318)

**重点 15：MAST-U 的主动闭环是明确跨过的一道门槛。** R318 是前篇 PCS 集成/非驱动测试的实验续篇，本次官方摘要与本地全文均确认它实际发出线圈请求，完成若干形状扰动、偏滤器腿扫描和强演化任务。形状控制器 10 kHz，RTVC 响应矩阵每约 5–5.6 ms 更新，两个频率不是同一个刷新速度。它保留现有控制架构与保护，使用规定剖面参数且未把被动结构电流全部纳入网络；没有足够传统 VC 对照机器时间，故证明可部署完成任务，尚不能证明所有情景全面优于传统方法。[R318](../appendices/reference-catalog.md#r318) [R312](../appendices/reference-catalog.md#r312)

R308 的 TCV inverse-GS 网络采取另一接口：目标形状先变成 PF 电流请求，再由低层 RZIP 执行。真实成形实验存在，但初始实验没有显式实时形状反馈，完整适应主要在 FGE 仿真。它与 R318 并非“谁更先进”的单轴比较，而是逆映射与局部正向响应两种可审计分层方式。[R308](../appendices/reference-catalog.md#r308)

**重点 16：EXL-50U MPC 的毫秒求解仍是作者仿真。** R390 将 538 状态降到 40，Kalman 观测器加电压约束 MPC；在 FGE 非线性 plant 的噪声、延迟和构型失配测试中比同模型上的 PID/LQR 更好，控制进程平均约 0.413–0.441 ms。尚未包含真实平衡重建、通信、电源和装置闭环，个别最大计时超过 1 ms；不能只靠均值称硬实时保证。这是模型降阶和优化控制，不能因同在先进算法章节就称为 ML 已上机。[R390](../appendices/reference-catalog.md#r390)

## 8. 今年动态、比较与经验

本库 2026 年动态可分三条。第一条是 **平衡与输运计算可调用化**：从 R074 的线性 GK 饱和规则、R231 的可微新经典，到 R330 的谱粒子压缩、R379 的非线性 GX 代理。它们加速了不同层，取值范围、电子模型与几何近似各不相同，不能把速度倍数相乘声称已做整机数字孪生。[R074](../appendices/reference-catalog.md#r074) [R231](../appendices/reference-catalog.md#r231) [R330](../appendices/reference-catalog.md#r330) [R379](../appendices/reference-catalog.md#r379)

第二条是 **从单一稳定性到快粒子—湍流反馈**：R142、R239、R278 分别代表燃烧条件模拟、实验多尺度耦合和快速输运预测。第三条是 **从离线精度到部署证据**：R268/R305 是代理求解，R324 是评测协议，R308 是部分实机成形，R318 是主动闭环，R390 仍是作者 plant 仿真。层次越后，越必须计入诊断、状态估计、延迟尾、约束和失败处理。[R142](../appendices/reference-catalog.md#r142) [R239](../appendices/reference-catalog.md#r239) [R278](../appendices/reference-catalog.md#r278) [R318](../appendices/reference-catalog.md#r318)

| 证据层 | 典型条目 | 能说什么 | 仍缺什么 |
|---|---|---|---|
| 方程/代码基准 | R106、R157、R231、R330 | 特定离散与物理模型更准/更快 | 装置全条件与全模型验证 |
| 同模型标签代理 | R268、R305、R379 | 训练范围内近似标签，部分高保真回退 | 真实物理偏差与 OOD 保障 |
| 历史实验数据预测 | R291、R270 | 规定测试集上的预测统计 | 前瞻放电与闭环收益 |
| 部分装置演示 | R308、R342 | 指定形状/波驱动的实验证据 | 完整反馈、反应堆参数与长期可靠性 |
| 主动装置闭环 | R318 | 指定 MAST-U 任务实际执行成功 | 全情景传统对照与跨装置 |
| 作者非线性 plant 闭环 | R390、R197 | 在所建 plant 下优化/控制表现 | 实机诊断、电源、未建模模式 |

工程材料同样是前沿约束。R365 的 IFMIF/EVEDA 概述区分 LIPAc 已有 5 MeV 高流脉冲与 9 MeV CW 目标，提醒中子辐照和连续束流仍有完整工程链；R153 的中子外逸碳-14、R340 的核素发生器、R377 的快中子闪烁涉及应用或监测，不能作为核心磁约束性能证据。R079 的激光纳米线 p–B alpha 与 R056/R062 的 ICF AI/驱动也应放回相应主章节，只在方法联系上交叉阅读。[R365](../appendices/reference-catalog.md#r365) [R153](../appendices/reference-catalog.md#r153) [R340](../appendices/reference-catalog.md#r340) [R377](../appendices/reference-catalog.md#r377) [R079](../appendices/reference-catalog.md#r079) [R056](../appendices/reference-catalog.md#r056) [R062](../appendices/reference-catalog.md#r062)

还有一个常被忽略的判断：物理残差必须与标签用同一离散口径比较。粗网格有限差分给出的残差有截断误差，代理与标签残差接近只说明二者在该诊断下相当，既不说明连续方程被精确满足，也不替代网格收敛和装置诊断。

最值得带走的经验有三点。首先 **不要用一个网络的场误差代替最终任务误差**：磁通、X 点、$q$、线圈电流、壁热流和丢失粒子各自要测。其次 **按炮次与装置隔离验证**，同一炮滑窗或同一模型族中随机分割可能只是在测试插值。再次 **优化必须允许拒绝候选并回退**，R379 已给出具体非法最优解例子；没有失败机制的优化流程很可能主动放大代理误差。

## 9. 初学学习路线

第一轮只做磁面和平衡：画托卡马克、X 点和 SOL，把本章 GS 推导手算到 $J_\phi$，读 R268 并列出输入、输出、边界。第二轮做轨道：算一个 3.5 MeV alpha 的回旋半径与机器尺度之比，区分 $E\times B$、梯度与曲率漂移，再读 R141/R231。第三轮做输运：从涨落相关解释净热流，再读 R330/R142/R239，区分线性增长、非线性饱和和约束反馈。第四轮做控制：手算一个 2×2 响应矩阵，理解条件数与伪逆，然后对照 R308/R318/R390 的真实接口与证据层。

若只选五篇深入阅读，可用 R231（碰撞基线）、R330（GK 物理与算力）、R142（alpha 反馈）、R318（实机闭环）、R379（优化失败与回退）。它们共同解释这个方向为什么同时需要物理、算法、诊断和工程，而不只是一套更大的神经网络。

## 10. 本章证据来源与覆盖

本次清点原路由 43 条的标题、日期与路径，正文串联超过 30 篇，16 个重点单元。对于同标签的 ICF、核素与闪烁材料明确作分类噪声/跨方向关联处理，未把它们算成磁约束实测提升。现有笔记阅读覆盖 R106/R109/R128/R141/R142/R157/R175/R197/R228/R231/R234/R235/R239/R243/R255/R268/R269/R270/R278/R291/R305/R308/R318/R324/R330/R342/R349/R359/R365/R367/R379/R390；未有新读全文支撑的条目仅作主题关联，不摘录强定量结论。

本次重新用本地 `pdftotext -layout` 定位复核 **R268、R318、R342、R379** 的定量与证据口径；R330/R324/R308/R390 等细节主要复用现有深入笔记，未重跑代码、下载开放数据集或审阅原始放电信号。

2026-09-30 成功打开 [R318 官方 arXiv](https://arxiv.org/abs/2608.28468) 和 [R342 官方 arXiv](https://arxiv.org/abs/2609.12474) 核对摘要/版本与提交历史。R318 首次提交 **08-28**、仓库入库 **09-01**；R342 官方首次提交 **09-11**、仓库入库 **09-15**，台账 publication_date **09-08** 与官方历史不一致。本章采用官方首次提交日期并记录差异，未自行修改共享台账。访问与 PDF 复核记录见 [来源核查表](../data/hedp-source-checks.json)。

历史基础部分是为理解方程补写的教学背景，不是对托卡马克和恒星器历史文献的穷尽综述；本库没有覆盖全部重要机器与全年全部成果。对反应堆状态、商业时间表、外部项目里程碑未作系统调查。本次没有独立复现 GK、RE、平衡代理、装置控制或净电计算。
