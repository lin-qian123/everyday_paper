# 2026 等离子体与强激光研究：按主题的入门到前沿综述

**阅读入口：** 先读 [共同基础](chapters/00-foundations.md)，再按下面的主题选择章节。所有主题都按“背景与物理问题 → 原理和推导 → 历史脉络 → 2026文章 → 方法比较 → 经验与未解决问题”展开。

本版截止 **2026-09-30**，以本仓库393篇文献为范围，其中365篇的仓库发表日期属于2026年，28篇为2016—2025年的背景文献。现有中文笔记328篇，本地PDF路径存在356篇，65篇缺少中文笔记。重点论文结合本地全文片段与官方来源复核；全库条目都进入可追溯目录，但**目录覆盖不等于393篇全文精读，也不是全世界2026文献的穷尽检索**。

2026-10-01图文增补版：正文共11章，约8.3万汉字，引用290篇不同文献；其余103篇保留在全库目录和覆盖矩阵中。新增54幅关键论文原图摘录，来自45篇论文，九个主题各6幅；结合10幅教学图（其中8幅本次新增）讲清机制、性能、误差与证据链。各图放在相应内容首次详细讨论处，逐子图解释坐标、单位、归一化、趋势、论证作用与局限。当前合订PDF为144页，含正文与393条精简书目；内容范围仍截止2026-09-30。

## 按主题阅读

| 章 | 主题 | 原分类关联篇数 | 先解决的问题 |
| --- | --- | ---: | --- |
| [00](chapters/00-foundations.md) | 共同基础与阅读地图 | 全库 | 等离子体、关键尺度、a₀、能量交换与证据判断 |
| [01](chapters/01-laser-plasma-acceleration.md) | 激光等离子体与束流加速 | 126 | LWFA、PWFA、DLA及离子加速怎样产生可用束流 |
| [02](chapters/02-beam-applications.md) | 束流、辐射与核应用 | 90 | 从电子/离子到X/γ、中子、同位素和成像的完整链 |
| [03](chapters/03-strong-field-qed.md) | 强场QED与辐射反作用 | 67 | χ、量子辐射、对产生与可测信号 |
| [04](chapters/04-hedp-icf-astrophysics.md) | HEDP、ICF与实验室天体 | 105 | 物性、冲击、不稳定性、压缩和燃烧 |
| [05](chapters/05-pic-kinetic-simulation.md) | PIC、动理学与数值模拟 | 163 | 如何把方程变成可信的离散计算 |
| [06](chapters/06-ai-ml-plasma.md) | AI与等离子体物理 | 64 | 代理、闭合、反演和控制何时能真正工作 |
| [07](chapters/07-magnetic-fusion.md) | 磁约束聚变与快粒子 | 43 | 平衡、输运、驱动、alpha和失控电子 |
| [08](chapters/08-platforms-diagnostics.md) | 实验平台、靶与诊断 | 112 | 响应函数、绝对标定与工程稳定性 |
| [09](chapters/09-general-plasma.md) | 综合等离子体与交叉方法 | 75 | 波、重联、开放系统与跨尺度方法 |
| [10](chapters/10-outlook-learning.md) | 跨方向趋势、经验与学习路线 | 综合 | 研究进展到哪一步，下一步怎样补齐证据 |

篇数采用仓库分类路由，一个条目可以跨类。关键词分类包含噪声，正文按科学问题重新组织；合计不能当成独立篇数。

## 完整目录与核查材料

- [393篇参考文献与原始路径](appendices/reference-catalog.md)：R编号、发表日期、来源状态、分类、笔记和全文路径。
- [按主题的覆盖矩阵](appendices/coverage-by-topic.md)：每个条目在哪些正文章中被引用，哪些仅作目录覆盖。
- [材料缺口](appendices/reading-gaps.md)：65篇无笔记条目及本版的阅读优先级。
- [方法、日期和证据边界](appendices/methodology.md)：如何使用旧笔记、全文与联网核查。
- [旧笔记与原文的差异](appendices/source-discrepancies.md)：本次复核发现的参数、公式或日期问题。
- [术语表](appendices/glossary.md)：缩写、中文含义与阅读位置。
- [图像导航与原图出处](appendices/figure-guide.md)：64幅图的阅读位置、原图号、PDF页码及原尺寸图像；`data/figure-assets/`保留逐图裁框、来源和哈希。
- `data/corpus.json`：可重建的文献快照；`data/*-source-checks.json`：来源核查记录。

## 连续阅读与重建

[综述合订本PDF](综述合订本.pdf)方便离线阅读，末尾附精简全库书目；[浏览器阅读版](综述合订本.html)可点击图片打开原尺寸图像，数学渲染需要联网加载MathJax。分章Markdown和附录是可维护的源文件，完整笔记和全文链接优先从上述附录进入。PDF编译与排版检查见`data/render-validation.json`，图像核查见`data/figure-validation.json`，核心教学推导的协作复核范围见`data/editorial-audit.md`。

在仓库根目录执行：

```bash
python reviews/2026-frontiers/scripts/build_coverage.py
python reviews/2026-frontiers/scripts/build_figure_index.py
python reviews/2026-frontiers/scripts/build_book.py
python reviews/2026-frontiers/scripts/validate_review.py
```

`build_corpus.py`复用原索引分类方法；若台账改变，R编号可能随排序改变，因此本版重建使用已保存的`data/corpus.json`，不能把它当作滚动自动更新。当前快照的台账SHA-256和Git提交记录在该文件中；验证程序核对固定快照与全部条目元数据，允许日更仓库继续增加文献。2026-10-01日更已另增5篇，本图文版仍覆盖截至2026-09-30的393篇。建立新版本并修订引用编号时才运行`build_corpus.py --refresh-snapshot --cutoff YYYY-MM-DD`。重建不改`state/`、`daily/`、`yearly/`或原始论文页。

合订本构建需要`python`、Pandoc、XeLaTeX与xeCJK；当前字体配置使用macOS系统中文字体和TeX的Latin Modern文件。概念图已随本版提供，重新绘图可运行`scripts/build_figures.py`，需要Matplotlib。临时合订源与原文提取放在本版`.build/`，不随Git发布。

论文原图按章放在`figures/papers/chXX/`，使用本地PDF指定区域的250 dpi渲染，保留原数据、图例和所选子图。新增教学图在`figures/teaching/`，以`scripts/build_teaching_figures.py`重建，提供PNG/PDF/SVG；教学曲线均标明解析或自拟示例。重新绘图或改变裁框后应重新检查图像与侧录，不把脚本执行成功当作视觉复核。逐主题选图理由见`data/figure-selection-*.md`。

## 如何使用这份综述

首次阅读不必推导所有公式。每章先看物理问题和机制图景，再选择两三篇重点文章。第二遍检查变量、假设和证据来源，第三遍回到仓库笔记与原文。正文里的“我们建议”“值得关注”是综述判断；直接实验、诊断反演、作者模拟和条件化理论分别说明。本版没有重跑PIC、核输运、神经网络训练、聚变控制或探测器绝对标定。
