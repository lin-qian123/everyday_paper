# 2026-11-06 每日论文索引

## 今日概览

- 新增 **2 篇独立作品**，另将既有 DPF 作品原位升级至正式接收稿并补写此前缺失的笔记；台账 **534→536**。未重复计数 arXiv／期刊身份，原 DPF 入库日期 2026-06-11 保留。
- 新增水窗 FEL 为 Nature Communications **Article in Press**；DPF 是 Nuclear Fusion **Accepted Manuscript**，均未称最终 VOR。PGTI 以 11-04 投稿、11-05 公告的作者预印本补充。
- 三篇主文加一份补充材料，共 **4 份 PDF／74 页**；文件头、类型、SHA、独立页数与全页文本通过。**34 个关键页、12 幅原图／表摘录**已目视核查，见 [PDF 核验](./pdf_validation.json)、[视觉清单](./research/visual-validation.json)。PDF／文本本地保存并按既有规则 Git 忽略，中文笔记和证据纳入版本控制。
- MinerU 一次真实公开 URL 请求仍返回 **401/A0211 令牌过期**，0 次解析成功；其余三份 PDF 未重复提交，采用本地全文／布局／渲染回退，见[解析记录](./research/mineru-attempts.json)。
- APS 两篇新候选仅“已接收”，普通 PDF 403、官方 harvest 404，进入精确重试；未把 Crossref 日期称正式 VOR 发表日，未写摘要替代全文笔记。重试 **53→55**；此前 53 对象保持，未全队列重复探测。

## 全文与中文笔记

| 论文 | 版本、日期与主要证据 |
| --- | --- |
| [水窗强增益 FEL](./notes/Berman%20et%20al.%20-%202026%20-%20Strong%20gain%20water%20window%20X%20ray%20laser.md) | [Nature Communications](https://doi.org/10.1038/s41467-026-78880-4)，11-05 在线、10-04 接收，Article in Press。FBPIC→Elegant→Puffin 贯通模拟；切片与全束统计、平均／时间峰值功率及独立扰动扫描分别说明。 |
| [复杂解剖中的瞬发伽马时间成像 PGTI](./notes/Kavrigin%20et%20al.%20-%202026%20-%20Prompt%20gamma%20time%20imaging%20complex%20anatomy.md) | [arXiv 2611.06683v1](https://arxiv.org/abs/2611.06683v1)，11-04 投稿。100 MeV 质子、八模块、RANDO 头模实验；0.55／1.44 mm 是两向阈值位置差，材料／剂量依赖模型及外推。 |
| [DPF 中子混合模型：原条目升级](./notes/Zhao%20et%20al.%20-%202026%20-%20Hybrid%20PIC%20fluid%20dense%20plasma%20focus%20accepted.md) | [Nuclear Fusion](https://doi.org/10.1088/1741-4326/aebda4)，Crossref 接收稿在线日 11-04；NF-108657.R2 接收稿。合并原 arXiv 2604.09032；二维轴对称、指定末段初态，源端中子率与数值／闭合限制分别核查。 |

## 检索、版本及去重

Crossref 十主题、2026-11-04 至 11-06、每主题相关性前 40 行，共 **400 行／336 唯一 DOI**；两次初始 429 经顺序重试恢复。官方 arXiv 十类最新 11-05 公告块共 **181 行／170 ID**；cs.LG 仅前 100/214。检索非穷尽，公告日不等于投稿日。

去重比较 DOI／arXiv 别名、规范化标题、作者、摘要和物理场景。旧台账 **533 个对象原值保持、1 个 DPF 对象更新**，新增两项。DPF 原 note_path 为空，本轮补齐，历史 PDF 线索保留。版本核对见 [version-checks.json](./research/version-checks.json)，检索结果见 [discovery.json](./research/discovery.json)，逐项来源见 [sources.jsonl](./research/sources.jsonl)。

## 全文待恢复

| 候选 | 状态与本轮实际失败 |
| --- | --- |
| [薄膜中等强度激光相互作用](https://journals.aps.org/pre/accepted/10.1103/3dkl-vphp) | PRE 11-05 接收；普通 PDF HTTP403 验证页、harvest HTTP404。未获得相应全文，不建笔记。 |
| [DREAM 可微核反应贝叶斯校准](https://journals.aps.org/prc/accepted/10.1103/9szm-dgtr) | PRC 11-04 接收；普通 PDF HTTP403、harvest HTTP404。相关 arXiv 2605.30980v2 为 06-01 版本，题目和推断表述不同，未验证为该接收稿，未替代入库。 |

具体下载记录见 [download_report.json](./download_report.json) 与 [重试台账](../../state/daily_retry_candidates.json)。VHEE 空气屏、BC8 碳、LG 正电子、稳定性代理与高变换比 afterburner 保留为[未精读线索](./research/next-leads.json)，不能当作本轮科学结论。

## 证据边界与接续

水窗 FEL 尚是模拟，独立扰动样本汇总不代表联合误差测试；PGTI 尚是单头模低强度实验，一阶剂量和低能外推不等于临床验收；DPF 总产额是不同阳极几何间的数量级比较，空间加密未覆盖主要产额窗口、Hall／压强扩展不稳定。DPF 粒子力印刷式和 Debye 长数量级问题，以及 PGTI 截断／配色图注差异均在笔记中保留，未擅改原文。

本轮未运行作者 PIC、FEL、Geant4、核反应模型、机器学习或实验，仅做来源核验、静态公式／简单算术检查和文献解读；没有新增激光转换靶—光核核素端到端、患者临床或辐射防护验收。优先恢复两篇 APS 接收稿，等待最终版本及作者原始输出澄清上述问题。

运行与验证见 [run_results.json](./run_results.json) 和 [verification.json](./research/verification.json)。
