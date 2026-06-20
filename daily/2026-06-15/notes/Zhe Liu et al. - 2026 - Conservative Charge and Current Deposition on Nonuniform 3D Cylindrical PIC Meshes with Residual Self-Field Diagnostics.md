# Conservative Charge and Current Deposition on Nonuniform 3D Cylindrical PIC Meshes with Residual Self-Field Diagnostics 笔记

## 0. 论文信息
- 标题: Conservative Charge and Current Deposition on Nonuniform 3D Cylindrical PIC Meshes with Residual Self-Field Diagnostics
- 作者: Zhe Liu, Zhijun Zhou, Yinjian Zhao
- 期刊: arXiv 预印本（高相关补充）
- DOI: 10.48550/arXiv.2606.09168
- 发表日期: 2026-06-08
- 主题关键词: PIC、非均匀圆柱网格、电荷沉积、电流沉积、残余自场、有限体积

## 1. 核心结论
- 论文针对 nonuniform cylindrical PIC mesh 上最容易出问题的 source deposition 环节，提出了 cylindrical-volume-weighted 的电荷/电流沉积方案，把 nodal control volume 和 swept-volume factor 显式纳入沉积权重。
- 测试结果显示，这套做法不仅能在均匀密度和受控输运测试中保持良好的电荷守恒，而且 continuity residual 明显低于对应的 current-density error；更关键的是，作者指出“满足电荷连续性”并不自动等于“自场误差小”，face-centered electric field 布局在 residual self-field 上最稳。

## 2. 方法与技术路线
- 方法上不是简单把 Cartesian deposition 硬搬到柱坐标，而是把圆柱度量因子和非均匀拉伸网格一并纳入离散公式，保证沉积与 finite-volume continuity equation 一致。
- 作者做了三类验证：均匀密度恢复、受控粒子输运、单粒子 self-field 诊断。最后这一项尤其有价值，因为它直接把沉积方案和 field layout 对数值自作用误差的影响分开看清楚了。

## 3. 与当前研究方向的关系
- 相关性评分: 9/10；影响力评分: 6/10。
- 这篇工作非常贴近本仓库关注的 PIC 数值方法。它不直接讨论某个具体激光等离子体器件，但对圆柱几何、非均匀网格、dense plasma focus / Z-pinch / thruster 这类问题都很实用，属于“基础算法改进但能直接影响后续物理可信度”的论文。

## 4. 可复现实验/仿真要点
- 复现时要同时检查三类误差指标：总电荷恢复、连续性残差、单粒子 residual self-field；只看前两个容易高估沉积格式的真实质量。
- 如果后续后面要把它并入现有 PIC 代码，最该优先对比的是 face-centered、cell-centered 和 shifted cell-centered 电场布局对单粒子自场噪声、能量守恒和束流长时间推进稳定性的影响。

## 5. 后续行动项
- 值得把文中的沉积公式和 control-volume 定义整理成实现笔记，尤其是柱坐标半径因子与非均匀步长如何进入 charge/current assignment。
- 如果后续最近在看 cylindrical PIC、reduced-order PIC 或强梯度区局部加密网格，这篇可以和前几天收的 reduced-order / exponential solver 两篇一起读，形成一组“PIC 数值内核更新”材料。
