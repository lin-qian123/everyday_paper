# Quasi-static transverse electric field driven electron acceleration in relativistic laser matter interaction

## 基本信息

- 作者：Ameya Parab；Bhooshan Paradkar；Aparajit C. Anandam；Sk Rakeeb；Sagar Dam；Prashant Kumar Singh
- 期刊/平台：arXiv preprint（physics.plasm-ph）
- DOI：https://doi.org/10.48550/arXiv.2607.26252
- 发表时间：2026-07-28
- 来源链接：https://arxiv.org/abs/2607.26252
- 本地 PDF：`daily/2026-08-02/pdfs/Parab et al. - 2026 - Transverse field electron acceleration.pdf`

## 研究问题

在相对论激光驱动电子加速中，电子与激光场的退相位会限制净能量增益。能否利用横向准静态电场延长相位锁定，同时保持束流指向性？

## 方法与模型

- 先用测试粒子方程分析横向准静态电场对相位滑移和直接激光加速（DLA）的影响。
- 提出双激光构型：一束激光在靶后建立横向鞘层场，另一束负责电子加速；通过相对几何和延迟实现相位锁定。
- 用 SMILEI 2D3V PIC 模拟验证，基准参数包括 p 偏振、`a0=3`、12 个光学周期脉宽和约 `3λ` 焦斑；同时比较单激光、不同延迟和 `a0=10` 情况。

## 主要结论

- 当横向场与激光偏振面同向时，可降低退相位并使电子持续从激光场获得能量。
- 在文中给定的双激光 2D PIC 参数下，正确同步使电子截止能量增加约 `5–6 MeV`，高于 `5 MeV` 的电子能量耦合增加约 `34%`。
- 在 `a0=3` 下，约 `2–8` 个周期（`5.5–22 fs`）的延迟窗口给出约两倍的电子温度增强，表明同步容差是实现该方案的关键实验变量。

## 与本仓库方向的关系

- 直接关联激光加速电子束的束流品质与能量转换，可为紧凑辐射源和转换靶二次源前端的电子束优化提供机制参考。
- 以 PIC 为核心验证手段，适合作为研究横向场、靶后鞘层和 DLA 耦合时的可复现建模案例。
- 主题关键词：laser-driven electron acceleration；direct laser acceleration；phase locking；quasi-static field；dual laser；PIC。
- 相关性评分：5/5。

## 局限与注意事项

结果目前来自理想化二维 PIC 和测试粒子分析，尚未给出三维、预等离子体、靶面粗糙度、激光抖动或实验束流发散度的系统扫描；`34%` 耦合增益与 `5–6 MeV` 截止能量提升只能视为文中参数点的模拟结果，不能直接外推为通用实验性能。
