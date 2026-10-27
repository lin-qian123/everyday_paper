# 每日论文索引：2026-10-28

新增 **6 篇独立作品**，台账 **500 → 506**：1 篇正式 VOR、1 篇 PRL 正式记录对应作者稿、1 篇 PRE 接受记录对应作者稿，以及3篇近期预印本。6份PDF共 **96页、27,304,912字节**，布局文本 **530,304字节**；MinerU pipeline全部成功，已交叉检查 **33个身份/关键页、11幅原图摘录**。PDF、布局文本和MinerU全文保留本地并Git忽略。

## 阅读顺序与证据

| 作品 | 结果与限制 | 笔记 |
|---|---|---|
| [Operator Formalism for Laser–Plasma Mode Coupling](https://doi.org/10.3390/axioms15110800) | Axioms10-27正式VOR；算符/截断理论与简化PDE基准；省略较大相对论项，二模域及计时图文差异保留。 | [中文全文笔记](notes/Behtouei%20et%20al.%20-%202026%20-%20Operator%20laser%20plasma%20mode%20coupling.md) |
| [Available Energy and Ground States of Convective Hydrodynamic and Hydromagnetic Instabilities](https://doi.org/10.1103/bp24-s332) | PRL10-27正式记录，实际读2月作者稿；重排—松弛求受约束基态/可用能量，非失稳时间或全部能量转化。 | [中文全文笔记](notes/Fan%20and%20Zhou%20-%202026%20-%20Available%20energy%20convective%20instabilities.md) |
| [Identification of rippling interface between laser-ablated plasma and ambient uniform plasma at rest](https://doi.org/10.1103/mhz4-f54x) | PRE10-23接受，作者稿10-25；恢复旧重试。实测Al–N亮界面与2D MHD解释，界面不等于冲击前沿。 | [中文全文笔记](notes/Yamazaki%20et%20al.%20-%202026%20-%20Rippling%20laser%20ablated%20plasma%20interface.md) |
| [Bright Compton source based on the interaction of an ultraintense laser pulse with a relativistically transparent foil and a plasma mirror](https://doi.org/10.48550/arXiv.2610.35039) | 10-26预印本；2D透明薄箔+镜Compton，10–250keV谱产额潜力；第三维换算与大立体角限制。 | [中文全文笔记](notes/Chekmareva%20and%20Korzhimanov%20-%202026%20-%20Transparent%20foil%20Compton%20source.md) |
| [Laser wakefield acceleration and x-ray emission in plasma produced by the electrical explosion of an aluminum wire](https://doi.org/10.48550/arXiv.2610.34859) | 10-26预印本；电爆剖面作为初态的3D/2D电离PIC；近GeV尾和X射线，非端到端新实验。 | [中文全文笔记](notes/Wang%20et%20al.%20-%202026%20-%20Exploded%20aluminum%20wire%20wakefield%20X%20rays.md) |
| [Accelerating high-fidelity gyrokinetic fusion simulations with iGENE](https://doi.org/10.48550/arXiv.2610.33561) | 10-24预印本；JAX可微回旋动理学/作者GPU基准；FFT、单步、总时间与降阶误差口径分开。 | [中文全文笔记](notes/Merlo%20et%20al.%20-%202026%20-%20iGENE%20JAX%20gyrokinetic%20acceleration.md) |

## 检索、版本与去重

- Crossref对 **10-26至28** 作10组有界主题查询，各最多75行，最终 **750行、536个唯一DOI**；首轮5个请求受限/出错，降为顺序查询后全部恢复，原失败与恢复记录均保留。大量同名医学plasma、引力韧致辐射等词面无关结果排除；本检索不是穷尽检索。
- 官方arXiv两组五分类各300条，并集 **575条**，最新可见提交 **2026-10-26T17:59:02Z**。覆盖等离子体、加速器、计算、核实验/仪器，以及高能理论、医学物理、核理论、光学、应用物理；APS最近目录补充发现PRL可用能量论文。
- 按DOI、arXiv别名、规范化标题、源URL、作者组和物理场景去重。最新arXiv:2610.35507与昨日Onofrio正式VOR是同一作品，只在既有记录补arXiv别名；旧500条除这一别名外不变。iGENE JAX与其TensorFlow先导研究有版本/方法关系，本篇是新的完整重写、误差修复和基准研究，未重复引用旧性能。
- 模耦合VOR标题与旧arXiv:2512.04982v2的Wakefield Acceleration不同，但作者/方法对应，保留单篇正式DOI。主站PDF代理/直连403，由官方mdpi-res开放CDN取得VOR；没有使用旧稿代替正式全文。
- Fan/Zhou PRL10-27正式发表，但官方全文401，实际读官方arXiv:2602.23983v1；2月提交与3月打印日期、未取得的独立补充材料均明确，未声称VOR逐项对照。
- **重试46→45，恢复1条，无新增重试。** 界面作品10.1103/mhz4-f54x的公开作者稿现可得；官方APS明确10-23是接受日期，Crossref的published-online不当成VOR出版。目录沿预印本口径使用10-25日期，并另存accepted_date/publication_date_type。其余45条对象不变，含JCP114707与完成台账PDF=null的历史交集；旧来源受限/embargo项无新信号，不重复空跑。
- 未选的非理想相对论镜、宽带中子索引、热工反馈中子MC、空气偶次谐波等仅为元数据线索，没有全文阅读/入库声明。

## 科学边界与接续

1. 模耦合计算省略的相对论项在测试条件下可大于保留项；有限温度适定性定理不覆盖冷数值测试；宽带二模误差与秒数图文不一致均待澄清。
2. 可用能量限定守恒约束/几何；模拟势能损失与动能峰不是同量，作者稿未附完整补充材料，不宣称装置稳定性阈值已验证。
3. 界面亮边缘不是氮冲击前沿；主GOI时间序列跨炮，微观厚度未分辨。密度设置字面正值问题、上游密度口径和CTS模型失配需作者材料核实，不将静态疑点写成实跑负密度。
4. Compton谱产额、亮度、带宽、前向全角与局部角密度分开；硬谱的二维到三维换算可能高估约两倍。电爆铝丝为规定初态的PIC，光子积分>1keV并非仅图示1–100keV，二维电子数是窗口内权重。
5. iGENE的86%为无碰撞2→32H100强缩放；FFT3.97×、无诊断单步2.63×与整次运行不是同分母，低阶矩速度以显著观测量偏差为代价。
6. 本轮未运行作者PIC、Dedalus、MHD、PDE、回旋动理学求解器、训练或实验；未新增激光转换靶—光核中子/核素端到端实测、临床或防护验收。

## 核验与可追溯记录

[PDF/哈希](pdf_validation.json) · [下载与回退](download_report.json) · [来源元数据](research/sources.jsonl) · [有界检索](research/research-run.json) · [版本与接受状态](research/version-checks.json) · [MinerU](research/mineru-attempts.json) · [原图来源](research/figure-manifest.json) · [运行结果](run_results.json)
