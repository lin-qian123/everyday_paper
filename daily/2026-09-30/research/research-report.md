# 2026-09-30 定向论文研究报告

## 检索覆盖

本轮先运行安装的多来源搜索层，3 个定向查询返回 0 条可用结果；随后使用官方 arXiv Atom/API 检索 `physics.plasm-ph`、`physics.acc-ph`、`physics.ins-det`、`physics.comp-ph`、`nucl-ex`、`nucl-th` 和 `hep-ph` 的 2026-09-28 投稿增量，并用 Crossref 2026-09-29 至 30 元数据检查正式来源。覆盖是定向的，不宣称穷尽全部期刊。

## 选择逻辑

- **强场 QED 实验准备：** `2609.35519` 有 ARES/FACET-II 真实束测，且明确给出低通量、本底和辐照限制。
- **强场 QED / γ 源理论：** `2609.35208` 直接连接非线性 Compton、多光子通道、MeV γ 和 spin–OAM 相干。
- **束流诊断与 AI：** `2609.34350` 用真实二极管衰减数据比较脉宽，再以 AI 方法反演能谱。
- **聚变控制算法：** `2609.34076` 给出状态降阶、观测器、受限优化、鲁棒场景和实时计时的闭环链路。

## 共同证据边界

LUXE 是原型束测而不是 LUXE 物理数据；AEE 的异常能比例来自滤片衰减反演；vector-vortex γ 是条件化强场 QED 模式计算；EXL-50U 是作者 FGE 闭环仿真而不是装置实验。本轮未重跑 Ptarmigan/Geant4、Fredholm 反演、强场 QED 振幅或 MEQ/FGE/OSQP。
