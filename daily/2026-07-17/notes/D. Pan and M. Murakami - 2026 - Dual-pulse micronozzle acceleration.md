# Dual-pulse micronozzle acceleration of sub-GeV-class protons

## 基本信息

- 作者：D. Pan; M. Murakami
- 期刊/平台：arXiv preprint
- DOI：https://doi.org/10.48550/arXiv.2607.13672
- 发表时间：2026-07-15
- 来源链接：https://arxiv.org/abs/2607.13672
- 本地 PDF：`daily/2026-07-17/pdfs/D. Pan and M. Murakami - 2026 - Dual-pulse micronozzle acceleration.pdf`

## 研究问题

激光驱动质子加速常面临最高能量和激光到质子转换效率之间的折中。论文提出的问题是：是否可以通过双脉冲和微喷嘴几何，实现质子束与加速场的相位锁定，从而同时提高截止能量、转换效率和高能质子占比。

## 方法与模型

- 提出双脉冲 micronozzle 方案：预脉冲形成紧凑质子前沿，延迟主脉冲在微喷嘴腔体内驱动准静态轴向电场。
- 通过调节双脉冲延迟，使质子束与加速场保持相位同步，延长有效加速时间。
- 使用二维 PIC 模拟比较微喷嘴、非受限双脉冲氢棒等几何。
- 使用三维 PIC 模拟验证 slit-nozzle 几何中相位锁定和能谱硬化是否仍然保持。
- 构建解析同步模型解释最佳延迟窗口。

## 主要结论

- 在主脉冲强度约 `10^21 W/cm^2` 条件下，方案可获得 sub-GeV 质子截止能量。
- 总激光到质子转换效率约为 20%，其中 100 MeV 以上质子效率超过约 13%。
- 微喷嘴几何通过维持长寿命轴向加速通道，抑制热化退束并提高高能质子装载。
- 三维模拟显示 slit-nozzle 中截止能量比非受限氢棒高约 60%，说明几何约束和时间同步是核心增益来源。

## 与本仓库方向的关系

- 论文直接关联激光离子加速、靶设计、束流品质、转换效率和高能质子应用。
- sub-GeV 高效率质子束对辐照、材料研究、核反应、次级中子/同位素产生和诊疗方向都有潜在价值。
- 主题关键词：laser-driven proton acceleration；TNSA；micronozzle target；dual-pulse synchronization；PIC simulation；secondary-particle applications。
- 相关性评分：5/5。

## 阅读价值

适合关注激光离子加速靶设计和高能质子应用的读者。论文的核心价值在于把“相位锁定”作为可工程化的靶-脉冲协同设计原则，并给出二维、三维 PIC 支持。

## 局限与注意事项

当前为预印本，主要基于数值模拟。实验实现还需要评估微喷嘴制备、双脉冲时间抖动、预等离子体、重复频率、靶更新、辐射防护和真实三维激光聚焦误差对高能尾部的影响。
