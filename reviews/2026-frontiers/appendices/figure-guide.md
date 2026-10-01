# 图像导航、出处与复核方法

正文共64幅图，其中54幅论文原图摘录来自45篇论文，另有10幅作者绘制的教学图。图在对应内容首次详细讨论处出现；本表仅作出处导航，不替代逐图讲解。合订图序按分章顺序生成，论文原图号单独保留。

## 论文原图怎么读

先读原始图号与版本，再辨认装置图、直接信号、反演物理量、模拟或理论曲线。检查所有子图的轴、单位、色标、归一化、误差与对照组，最后判断图能支持哪一步结论。正文逐图给出这一解读；来源侧录保留原PDF路径、页码、裁框、DPI与SHA-256。

原图仅从本地PDF渲染指定区域，不重画曲线、不重着色、不更改标签；裁框保留所选图的坐标和图例。原文图注与邻近段落用于解释，但图像视觉检查不自动成为对作者数据/代码的独立复现。摘录用于本综述的来源明确的分析讲解；论文图的权利仍属于相应作者或权利人。

## 教学图怎样与论文结果区分

教学图明确注明解析模型或自拟示例，公式、假设与重建脚本记录在`data/teaching-figures.json`。没有把教学曲线充当新实验、论文仿真数据或数字化原始曲线。PNG方便屏幕阅读，合订PDF优先使用其矢量版本。

| 合订图序 | 位置 | 主题与作用 | 来源 / 原图号 | 原PDF页 | 图像 |
| ---: | --- | --- | --- | ---: | --- |
| 1 | [00章](../chapters/00-foundations.md) | 研究链与专题关系 | 作者教学示意 | — | [查看原尺寸](../figures/research-map.svg) |
| 2 | [00章](../chapters/00-foundations.md) | 界面恢复场与电子振荡 | 作者教学示意 | — | [查看原尺寸](../figures/teaching/plasma-oscillator.png) |
| 3 | [00章](../chapters/00-foundations.md) | 点电荷的屏蔽势 | 作者教学示意 | — | [查看原尺寸](../figures/teaching/debye-screening.png) |
| 4 | [00章](../chapters/00-foundations.md) | 截止频率、临界密度与群速度 | 作者教学示意 | — | [查看原尺寸](../figures/teaching/cold-dispersion.png) |
| 5 | [00章](../chapters/00-foundations.md) | 经典非线性参数与量子参数的区别 | 作者教学示意 | — | [查看原尺寸](../figures/teaching/a0-chi-map.png) |
| 6 | [00章](../chapters/00-foundations.md) | 密度、波长与场强的量级关系 | 作者教学示意 | — | [查看原尺寸](../figures/teaching/density-scales.png) |
| 7 | [00章](../chapters/00-foundations.md) | 观测与反演的证据链 | 作者教学示意 | — | [查看原尺寸](../figures/evidence-chain.svg) |
| 8 | [01章](../chapters/01-laser-plasma-acceleration.md) | 一万发电荷与指向 | [R374](reference-catalog.md#r374) · Fig. 2 | 4 | [查看原尺寸](../figures/papers/ch01/r374-fig-2.png) |
| 9 | [01章](../chapters/01-laser-plasma-acceleration.md) | 一万发能谱 | [R374](reference-catalog.md#r374) · Fig. 3 | 5 | [查看原尺寸](../figures/papers/ch01/r374-fig-3.png) |
| 10 | [01章](../chapters/01-laser-plasma-acceleration.md) | 发射度需要能量分辨测量 | [R314](reference-catalog.md#r314) · Fig. 3 | 4 | [查看原尺寸](../figures/papers/ch01/r314-fig-3.png) |
| 11 | [01章](../chapters/01-laser-plasma-acceleration.md) | 标准与无去相位LWFA | [R144](reference-catalog.md#r144) · Fig. 1 | 3 | [查看原尺寸](../figures/papers/ch01/r144-fig-1.png) |
| 12 | [01章](../chapters/01-laser-plasma-acceleration.md) | 脉宽与纵向相空间旋转 | [R267](reference-catalog.md#r267) · Fig. 4 | 4 | [查看原尺寸](../figures/papers/ch01/r267-fig-4.png) |
| 13 | [01章](../chapters/01-laser-plasma-acceleration.md) | SMLWFA与DLA的能量分工 | [R285](reference-catalog.md#r285) · Fig. 6 | 8 | [查看原尺寸](../figures/papers/ch01/r285-fig-6.png) |
| 14 | [02章](../chapters/02-beam-applications.md) | 双激光逆Thomson实验链 | [R138](reference-catalog.md#r138) · Fig. 1 | 2 | [查看原尺寸](../figures/papers/ch02/r138-fig-1.png) |
| 15 | [02章](../chapters/02-beam-applications.md) | 光子能量、重合与稳定性 | [R138](reference-catalog.md#r138) · Fig. 5 | 7 | [查看原尺寸](../figures/papers/ch02/r138-fig-5.png) |
| 16 | [02章](../chapters/02-beam-applications.md) | 涂层等离子体镜增强ICS | [R230](reference-catalog.md#r230) · Fig. 2 | 6 | [查看原尺寸](../figures/papers/ch02/r230-fig-2.png) |
| 17 | [02章](../chapters/02-beam-applications.md) | 现场LWFA源的涡轮叶片CT | [R287](reference-catalog.md#r287) · Fig. 4 | 17 | [查看原尺寸](../figures/papers/ch02/r287-fig-4.png) |
| 18 | [02章](../chapters/02-beam-applications.md) | Mo/Tc活度的运行假设 | [R286](reference-catalog.md#r286) · Fig. 5 | 10 | [查看原尺寸](../figures/papers/ch02/r286-fig-5.png) |
| 19 | [02章](../chapters/02-beam-applications.md) | 激光驱动缪子透射成像 | [R380](reference-catalog.md#r380) · Fig. 9 | 9 | [查看原尺寸](../figures/papers/ch02/r380-fig-9.png) |
| 20 | [03章](../chapters/03-strong-field-qed.md) | RR实验与三类模型 | [R035](reference-catalog.md#r035) · Fig. 1 | 3 | [查看原尺寸](../figures/papers/ch03/r035-fig-1.png) |
| 21 | [03章](../chapters/03-strong-field-qed.md) | 量子连续与随机模型的证据 | [R035](reference-catalog.md#r035) · Fig. 5 | 6 | [查看原尺寸](../figures/papers/ch03/r035-fig-5.png) |
| 22 | [03章](../chapters/03-strong-field-qed.md) | LUXE可测Compton边 | [R385](reference-catalog.md#r385) · Fig. 5 | 5 | [查看原尺寸](../figures/papers/ch03/r385-fig-5.png) |
| 23 | [03章](../chapters/03-strong-field-qed.md) | LUXE粒种分离布局 | [R393](reference-catalog.md#r393) · Figure 1 | 3 | [查看原尺寸](../figures/papers/ch03/r393-figure-1.png) |
| 24 | [03章](../chapters/03-strong-field-qed.md) | 电子谱决定动态范围 | [R393](reference-catalog.md#r393) · Figure 2 | 4 | [查看原尺寸](../figures/papers/ch03/r393-figure-2.png) |
| 25 | [03章](../chapters/03-strong-field-qed.md) | 椭圆率与spin–OAM相干 | [R392](reference-catalog.md#r392) · Fig. 3 | 4 | [查看原尺寸](../figures/papers/ch03/r392-fig-3.png) |
| 26 | [04章](../chapters/04-hedp-icf-astrophysics.md) | BN 冲击状态方程的两种投影 | [R039](reference-catalog.md#r039) · Fig7 | 6 | [查看原尺寸](../figures/papers/ch04/r039-fig7.png) |
| 27 | [04章](../chapters/04-hedp-icf-astrophysics.md) | 铝Hugoniot高压区的模型分叉 | [R383](reference-catalog.md#r383) · Fig3 | 6 | [查看原尺寸](../figures/papers/ch04/r383-fig3.png) |
| 28 | [04章](../chapters/04-hedp-icf-astrophysics.md) | 相同面密度也可能有不同燃耗 | [R274](reference-catalog.md#r274) · Fig6 | 8 | [查看原尺寸](../figures/papers/ch04/r274-fig6.png) |
| 29 | [04章](../chapters/04-hedp-icf-astrophysics.md) | 碰撞算子与剪切参数怎样改变反应率增强 | [R112](reference-catalog.md#r112) · Fig5 | 7 | [查看原尺寸](../figures/papers/ch04/r112-fig5.png) |
| 30 | [04章](../chapters/04-hedp-icf-astrophysics.md) | 从NIF实验到10 MJ靶设计的证据跳跃 | [R363](reference-catalog.md#r363) · Fig1 | 2 | [查看原尺寸](../figures/papers/ch04/r363-fig1.png) |
| 31 | [04章](../chapters/04-hedp-icf-astrophysics.md) | 四发冲击速度与M-band模型对照 | [R388](reference-catalog.md#r388) · Fig3 | 5 | [查看原尺寸](../figures/papers/ch04/r388-fig3.png) |
| 32 | [05章](../chapters/05-pic-kinetic-simulation.md) | 连续分布如何成为宏粒子 | [R357](reference-catalog.md#r357) · Fig.1 | 6 | [查看原尺寸](../figures/papers/ch05/r357-fig-1.png) |
| 33 | [05章](../chapters/05-pic-kinetic-simulation.md) | Boris磁旋转的轨道与二阶收敛 | [R357](reference-catalog.md#r357) · Fig.3 | 18 | [查看原尺寸](../figures/papers/ch05/r357-fig-3.png) |
| 34 | [05章](../chapters/05-pic-kinetic-simulation.md) | 总能量守恒需要一致轨道积分 | [R131](reference-catalog.md#r131) · Fig.2 | 18 | [查看原尺寸](../figures/papers/ch05/r131-fig-2.png) |
| 35 | [05章](../chapters/05-pic-kinetic-simulation.md) | 谱粒子压缩保留了哪些ITG物理 | [R330](reference-catalog.md#r330) · Fig.5 | 9 | [查看原尺寸](../figures/papers/ch05/r330-fig-5.png) |
| 36 | [05章](../chapters/05-pic-kinetic-simulation.md) | 神经场求解的误差沿时间反馈 | [R139](reference-catalog.md#r139) · Fig.8 | 16 | [查看原尺寸](../figures/papers/ch05/r139-fig-8.png) |
| 37 | [05章](../chapters/05-pic-kinetic-simulation.md) | 时间跳跃仍受物理重建与回滚约束 | [R369](reference-catalog.md#r369) · Fig.1 | 4 | [查看原尺寸](../figures/papers/ch05/r369-fig-1.png) |
| 38 | [06章](../chapters/06-ai-ml-plasma.md) | 固定能量双脉冲的贝叶斯优化地图 | [R133](reference-catalog.md#r133) · Fig.3 | 3 | [查看原尺寸](../figures/papers/ch06/r133-fig-3.png) |
| 39 | [06章](../chapters/06-ai-ml-plasma.md) | 闭合跨越线性阻尼与非线性俘获 | [R256](reference-catalog.md#r256) · Fig.5 | 21 | [查看原尺寸](../figures/papers/ch06/r256-fig-5.png) |
| 40 | [06章](../chapters/06-ai-ml-plasma.md) | 磁通误差与X点几何误差 | [R268](reference-catalog.md#r268) · Fig.5 | 8 | [查看原尺寸](../figures/papers/ch06/r268-fig-5.png) |
| 41 | [06章](../chapters/06-ai-ml-plasma.md) | 神经Jacobian接入已有控制链 | [R318](reference-catalog.md#r318) · Fig.1.1 | 2 | [查看原尺寸](../figures/papers/ch06/r318-fig-1-1.png) |
| 42 | [06章](../chapters/06-ai-ml-plasma.md) | 实时伪逆的病态会放大线圈请求 | [R318](reference-catalog.md#r318) · Fig.4.1 | 6 | [查看原尺寸](../figures/papers/ch06/r318-fig-4-1.png) |
| 43 | [06章](../chapters/06-ai-ml-plasma.md) | TCV的实机成形与已有径向反馈 | [R308](reference-catalog.md#r308) · Fig.4 | 20 | [查看原尺寸](../figures/papers/ch06/r308-fig-4.png) |
| 44 | [07章](../chapters/07-magnetic-fusion.md) | 快alpha改变非线性热流与低波数谱 | [R142](reference-catalog.md#r142) · Fig10 | 16 | [查看原尺寸](../figures/papers/ch07/r142-fig10.png) |
| 45 | [07章](../chapters/07-magnetic-fusion.md) | 鱼骨与低频流的双相干证据 | [R239](reference-catalog.md#r239) · Fig2 | 3 | [查看原尺寸](../figures/papers/ch07/r239-fig2.png) |
| 46 | [07章](../chapters/07-magnetic-fusion.md) | 快粒子输运代理的剖面与不确定性 | [R278](reference-catalog.md#r278) · Fig9 | 19 | [查看原尺寸](../figures/papers/ch07/r278-fig9.png) |
| 47 | [07章](../chapters/07-magnetic-fusion.md) | DIII-D螺旋波电流驱动残差剖面 | [R342](reference-catalog.md#r342) · Fig3 | 4 | [查看原尺寸](../figures/papers/ch07/r342-fig3.png) |
| 48 | [07章](../chapters/07-magnetic-fusion.md) | MAST-U四炮主动形状控制 | [R318](reference-catalog.md#r318) · Fig3.1 | 4 | [查看原尺寸](../figures/papers/ch07/r318-fig3-1.png) |
| 49 | [07章](../chapters/07-magnetic-fusion.md) | EXL-50U作者plant仿真中的PID/LQR/MPC | [R390](reference-catalog.md#r390) · Fig8 | 17 | [查看原尺寸](../figures/papers/ch07/r390-fig8.png) |
| 50 | [08章](../chapters/08-platforms-diagnostics.md) | 气体靶的三种工程几何 | [R067](reference-catalog.md#r067) · Fig.3 | 6 | [查看原尺寸](../figures/papers/ch08/r067-fig-3.png) |
| 51 | [08章](../chapters/08-platforms-diagnostics.md) | 晶体谱仪的绝对通量换算 | [R185](reference-catalog.md#r185) · Fig.11 | 6 | [查看原尺寸](../figures/papers/ch08/r185-fig-11.png) |
| 52 | [08章](../chapters/08-platforms-diagnostics.md) | DRZ屏光输出斜率如何变成电荷 | [R219](reference-catalog.md#r219) · Fig.4 | 3 | [查看原尺寸](../figures/papers/ch08/r219-fig-4.png) |
| 53 | [08章](../chapters/08-platforms-diagnostics.md) | 能窗选择改变所测纵向相空间 | [R275](reference-catalog.md#r275) · Fig.5 | 6 | [查看原尺寸](../figures/papers/ch08/r275-fig-5.png) |
| 54 | [08章](../chapters/08-platforms-diagnostics.md) | 72小时运行的单发与平均稳定性 | [R287](reference-catalog.md#r287) · Fig.2 | 15 | [查看原尺寸](../figures/papers/ch08/r287-fig-2.png) |
| 55 | [08章](../chapters/08-platforms-diagnostics.md) | 束测线性需要同时看拟合残差 | [R393](reference-catalog.md#r393) · Fig.8 | 12 | [查看原尺寸](../figures/papers/ch08/r393-fig-8.png) |
| 56 | [09章](../chapters/09-general-plasma.md) | 磁声波密度与Langmuir探针对照 | [R350](reference-catalog.md#r350) · Fig5 | 5 | [查看原尺寸](../figures/papers/ch09/r350-fig5.png) |
| 57 | [09章](../chapters/09-general-plasma.md) | 同向与反向Alfvén波的二次非线性 | [R358](reference-catalog.md#r358) · Fig2 | 4 | [查看原尺寸](../figures/papers/ch09/r358-fig2.png) |
| 58 | [09章](../chapters/09-general-plasma.md) | 重联率的跨参数与跨网格代理对照 | [R384](reference-catalog.md#r384) · Fig8 | 11 | [查看原尺寸](../figures/papers/ch09/r384-fig8.png) |
| 59 | [09章](../chapters/09-general-plasma.md) | 同出生粒子在四电场控制下的高能尾 | [R347](reference-catalog.md#r347) · Fig11 | 13 | [查看原尺寸](../figures/papers/ch09/r347-fig11.png) |
| 60 | [09章](../chapters/09-general-plasma.md) | Hall推进器近壁净异常电子输运 | [R370](reference-catalog.md#r370) · Fig8 | 13 | [查看原尺寸](../figures/papers/ch09/r370-fig8.png) |
| 61 | [09章](../chapters/09-general-plasma.md) | 射频源双向耦合的周期功率预算 | [R355](reference-catalog.md#r355) · Fig14 | 30 | [查看原尺寸](../figures/papers/ch09/r355-fig14.png) |
| 62 | [10章](../chapters/10-outlook-learning.md) | 同相空间面积不保证相同有效电荷 | 作者教学示意 | — | [查看原尺寸](../figures/teaching/phase-space-acceptance.png) |
| 63 | [10章](../chapters/10-outlook-learning.md) | 响应模型中的非唯一性 | 作者教学示意 | — | [查看原尺寸](../figures/teaching/inverse-ambiguity.png) |
| 64 | [10章](../chapters/10-outlook-learning.md) | 局部误差与滚动误差 | 作者教学示意 | — | [查看原尺寸](../figures/teaching/rollout-error.png) |

## 文件与重建

`data/figure-manifest.json`汇总当前图像，`data/figure-assets/`记录每幅论文摘图，`data/figure-validation.json`记录检查。`scripts/extract_paper_figures.py`提供可追溯的区域渲染；教学图用`scripts/build_teaching_figures.py`重建。新增或替换图后重新执行`scripts/build_figure_index.py`与`scripts/build_book.py`。
