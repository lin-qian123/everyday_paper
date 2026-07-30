# Calibration of scintillator-based X-ray detectors for broadband laser-driven X-ray radiation

## 基本信息

- 作者：Orsolya Morvai; Benoit Lefebvre; Marcel Lamač 等
- 期刊/平台：arXiv preprint（physics.optics）
- DOI：https://doi.org/10.48550/arXiv.2607.25856
- 发表时间：2026-07-28
- 来源链接：https://arxiv.org/abs/2607.25856
- 本地 PDF：`daily/2026-07-31/pdfs/Luis A. Padilla-Lecuna et al. - 2026 - Calibration of scintillator X-ray detectors.pdf`

## 研究问题

宽谱、强烈 shot-to-shot 波动的激光驱动 X 射线源，如何把闪烁体探测器信号可靠转换为光子注量与谱信息，从而服务于定量诊断？

## 方法与模型

- 用 ISO 4037-1 N 系列多色参考 X 射线场，在捷克 SÚRO 进行受控标定。
- 研究互补的 CsI:Tl Varex XRD 0822 平板与 CMOS 读出的塑料闪烁体滤片堆栈谱仪（FSS）。
- 平板响应采用 Beer--Lambert 吸收，加上 FLUKA 对非局域沉积的修正；FSS 以逐层沉积响应重建入射谱。

## 主要结论

- 全谱正向重建给出平板 CsI:Tl 有效厚度约 `680 μm`，并能在受控参考场下描述其能量相关响应。
- 标定把大面积成像平板和可重建宽谱的 FSS 组合起来，面向 ELI L3Gammatron 的 LWFA betatron X 射线实验。
- 结果提供从相机计数到光子注量、再到谱反演的探测器响应链，而不是直接给出某一激光等离子体源的绝对产额。

## 与本仓库方向的关系

- 直接关联激光等离子体加速电子束产生的 betatron X 射线，以及 HEDP 成像、断层与瞬态谱诊断。
- 对转换靶/次级辐射实验也有可迁移价值：需先以已知参考场标定响应，才可比较束流或靶参数导致的产额变化。
- 主题关键词：LWFA；betatron X-ray；scintillator；filter-stack spectrometer；FLUKA；detector calibration。
- 相关性评分：5/5。

## 局限与注意事项

标定参考场最高至 `150 keV` 左右，真实激光驱动源的更高能尾部、剂量率、空间非均匀性和单发饱和仍需在目标束线条件下交叉验证；有效闪烁体厚度是响应模型参数，并非器件制造厚度的独立测量。
