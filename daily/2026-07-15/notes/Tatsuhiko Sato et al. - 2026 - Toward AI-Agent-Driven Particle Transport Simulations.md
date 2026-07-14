# Toward AI-Agent-Driven Particle Transport Simulations: Implementation of AI-Assisted Workflows for PHITS

## 基本信息

- 作者：Tatsuhiko Sato; Shintaro Hashimoto; Tatsuhiko Ogawa; Takuya Furuta; Yuho Hirata; Seiki Ohnishi; Tomohiro Yamada; Shinichiro Abe; Yosuke Iwamoto; Kohei Okumura
- 期刊/平台：arXiv preprint
- DOI：https://doi.org/10.48550/arXiv.2607.11309
- 发表时间：2026-07-13
- 来源链接：https://arxiv.org/abs/2607.11309
- 本地 PDF：`daily/2026-07-15/pdfs/Tatsuhiko Sato et al. - 2026 - Toward AI-Agent-Driven Particle Transport Simulations.pdf`

## 研究问题

PHITS 等蒙特卡罗粒子输运程序对输入准备、执行、后处理和结果解释有较高门槛。论文关注的问题是：通过面向 AI assistant 和 AI agent 的知识库、规则和参考材料，能否让 agent 更可靠地参与粒子输运模拟工作流。

## 方法与模型

- 从手册、讲义、样例输入、工具信息和开发者注意事项整理两套 AI-ready 资源：用于 RAG 助手的知识库，以及供 agent 直接使用的紧凑参考。
- 将知识库加载到 NotebookLM 提供交互式 PHITS 支持，并把 agent reference 与 PHITS-specific policies / execution rules 结合。
- 用五类演示任务测试 agent 能力：输入修改、重复模拟、参数优化、程序编译、后处理和结果解释。

## 主要结论

- 在有明确知识边界、规则和执行约束时，AI agent 可以处理较复杂的 PHITS 输入编辑、运行检查和结果分析任务。
- 论文强调代码侧/资料侧准备比直接把通用聊天模型接入模拟更关键，尤其是错误检查、单位、物理卡片和后处理约定。
- 该工作流为核诊断、辐射防护、束流转换靶和粒子输运应用中的自动化建模提供了可迁移范式。

## 与本仓库方向的关系

- 论文不是激光等离子体物理本身，但直接关联机器学习/AI agent 在粒子输运、辐射防护、核诊断和模拟自动化中的应用。
- 对仓库扩展方向有方法价值：激光电子束打转换靶产生韧致辐射、光核反应、中子/同位素产生和材料辐照应用都需要类似的输运模拟闭环。
- 主题关键词：PHITS；AI agent；particle transport；Monte Carlo simulation；radiation shielding；nuclear diagnostics。
- 相关性评分：4/5。

## 阅读价值

适合关注“AI 辅助科学计算工作流”和粒子输运模拟自动化的读者。它的意义在于把 agent 能力落实到可执行规则、知识库和示例任务，而不是停留在泛泛的 AI 应用讨论。

## 局限与注意事项

当前为预印本且偏方法/工作流；与激光等离子体的联系是通过后续辐射输运、转换靶和核应用场景建立的。实际采用时需要严格保留人工审查、基准算例和物理守恒/剂量单位检查。
