# Combined tools for Particle-In-Cell simulations performed with transversely asymmetric chirped lasers

## 基本信息

- 作者：I. Moulanier; F. Massimo; T. L. Steyn; B. Cros
- 期刊/平台：arXiv preprint
- DOI：https://doi.org/10.48550/arXiv.2607.19121
- 发表时间：2026-07-21
- 来源链接：https://arxiv.org/abs/2607.19121
- 本地 PDF：`daily/2026-07-24/pdfs/I Moulanier et al. - 2026 - PIC asymmetric chirped lasers.pdf`

## 研究问题

真实激光脉冲往往同时具有横向非对称性和时间啁啾，而理想化输入会削弱 PIC 对激光尾场加速（LWFA）实验中电子束优化的预测能力。本文给出将这两类特性共同写入 PIC 初始场的工具链。

## 方法与模型

- 提出 Asymmetric Chirped Electric field reconstruction（ACE）工具箱，以模态分解重建横向分布并叠加啁啾时域轮廓。
- 在圆柱与笛卡尔几何的 PIC 中实现该重建；在忽略时空耦合的假设下，对 LWFA 实验进行建模并扫描光谱啁啾。

## 主要结论

- ACE 可将实测或重建的横向非对称激光场与谱啁啾一并导入 PIC，而非分别作理想化处理。
- 示例 LWFA 建模表明，调节脉冲光谱啁啾能够优化产生的电子束。
- 工具链为实验激光表征到 PIC 预测之间提供了可重复的输入接口。

## 与本仓库方向的关系

- 同时覆盖 PIC 数值模拟、激光等离子体耦合和 LWFA 电子束品质优化，可直接服务于实验--模拟闭环设计。
- 主题关键词：PIC；laser wakefield acceleration；chirp；asymmetric laser profile；electron bunch optimization。
- 相关性评分：5/5。

## 局限与注意事项

方法明确假设可忽略时空耦合；对于具有强空间啁啾、脉冲前沿倾斜或复杂像差的系统，应先检验该近似，并与完整时空场诊断交叉验证。
