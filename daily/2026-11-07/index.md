# 2026-11-07 每日论文索引

## 今日概览

- 新增 **4 篇独立作品**，台账 **536→540**，此前 536 个完成对象保持不变。两篇 11-06 正式 VOR 为等离子体光栅数值与实验研究；两篇 11-05 投稿／11-06 公告的作者预印本补充 hosing 与束流机器学习。
- **4 份 PDF／86 页**（束流 PDF 内嵌 22 页补充）通过文件头、类型、SHA、`pdfinfo`／pypdf／PyMuPDF 页数一致性和全页非空文本核验。全文阅读之外，**37 个关键页与 12 幅原图摘录**经目视核查，见 [PDF 记录](./pdf_validation.json)、[视觉清单](./research/visual-validation.json)。PDF／文本本地保留并沿用 Git 忽略规则，中文笔记、图和来源记录纳入版本控制。
- MinerU 一次公开 URL 请求返回 **401/A0211 令牌过期**，其他三份不重复提交，采用本地布局文本与原页渲染回退，见[实际请求结果](./research/mineru-attempts.json)。认证失败不等于 PDF 损坏，0 次 MinerU 解析成功。
- 重试 **55→58**：PRE 光栅全文恢复，删除该旧候选；Mo 同质异能态条目更正为 11-06 正式发表，但 harvest401／普通 PDF403；新增四项全文受限候选，其余 53 个旧对象保持。没有摘要替代全文笔记，也没有购买或绕过访问限制。

## 全文与中文笔记

| 论文 | 版本、主要内容及证据边界 |
| --- | --- |
| [有限脉宽有质动力光栅](./notes/lehmann-2026-finite-pulse-plasma-gratings.md) | [PRE 114, 055205](https://doi.org/10.1103/9237-5stj)，10-22 接收、11-06 VOR。14 页，APS 官方 harvest 恢复旧重试，首次计入完成库。预电离氢的 Vlasov 模拟与有限带宽近似；泵浦撤去后的离子惯性、首周期持续时间与再形成分开，近似模型主要解释趋势。 |
| [场电离光栅衍射效率实验](./notes/wang-2026-experimental-plasma-grating-diffraction.md) | [PRApplied 26, 054022](https://doi.org/10.1103/9q15-5b5w)，09-29 接收、11-06 VOR，11 页。CO₂ 场电离的等离子体—中性气体条纹；效率按气室后透射信号归一化。35% 均值与最高强度不属于同一工作点，98 μm 通光孔径与毫米传播长度、模型密度与直接观测分别说明。 |
| [抛物通道中的激光 hosing](./notes/jogiya-2026-hosing-parabolic-channel.md) | [arXiv 2611.07475v1](https://arxiv.org/abs/2611.07475v1)，24 页。弱相对论变分／线性色散及二维 a0=2 PIC；印刷式候选截止是简单根，未构成一般重根判稳证明。整脉冲离轴摆动与内部 hosing 不同，图注时间差异保留。 |
| [MeV γγ 束线的传输映射与机器学习](./notes/zhang-2026-transfer-maps-ml-gamma-collider.md) | [arXiv 2611.08036v1](https://arxiv.org/abs/2611.08036v1)，37 页含补充。200 MeV Elegant 模拟、二阶映射与 ExtraTrees；89 个共同留出工况、22 例可测输入测试、20 例计时分开。集体效应关闭、固定归一化磁铁、历史截断、能量标定敏感性及输入集成差异均保留。 |

## 检索、去重和版本

Crossref 十主题、2026-11-05 至 11-07、每主题相关性前 40 行，共 **400 行／324 唯一 DOI**；三项初始非 JSON 响应顺序恢复。官方 arXiv 十类 11-06 公告块共 **215 行／197 ID**；cs.LG 仅前 100/224，非穷尽。医学类首轮429、次轮超时，后由官方规范 URL 成功取回；不把失败响应计入覆盖。

当前 HTML 把日期标题放在对应 `dl` 内，已按父 `dl` 解析并核对标题条数；初次错误选到下一日期块的结果已丢弃，不计入最终统计。按 DOI／arXiv 别名、规范化标题、作者与物理场景去重；两种光栅分别为预电离介质有质动力再分布与中性气体场电离，不是重复作品。两篇预印本的精确标题 Crossref 前三项只有相关旧作，未核到同作品期刊 VOR，不将有限检索说成绝不存在正式版本。

详见 [检索记录](./research/discovery.json)、[预印本版本检查](./research/version-checks.json)、[逐项来源](./research/sources.jsonl)。本次未改项目规则，保留并排除用户既有 `AGENTS.md` 编辑。

## 正式全文待恢复

| 候选 | 版本与本次实际结果 |
| --- | --- |
| [多 PW 泡沫靶大电荷电子／EMP](https://doi.org/10.1063/5.0348878) | MRE，Crossref 在线 11-06；AIP PDF403 验证 HTML，精确标题检索未核到可用作者全文。不据摘要生成科学笔记。 |
| [LWFA 纵向相空间 CTR 诊断](https://doi.org/10.1088/1402-4896/aeaeb6) | Physica Scripta，官方页标在线 11-06；PDF URL200 但返回订阅预览 HTML，页面明确无订阅。 |
| [气喷 Z 箍缩初态与中子产生](https://doi.org/10.1063/5.0329733) | Journal of Applied Physics，Crossref 在线 11-06；AIP PDF403 验证 HTML。 |
| [DIII-D 弥散强化钨损伤](https://doi.org/10.1088/1741-4326/aebe49) | Nuclear Fusion，Crossref 接收稿在线 11-05；PDF URL200 为 Radware/CAPTCHA，不称最终 VOR，也不解验证码。 |
| [Mo 同质异能态耗尽：旧候选更新](https://journals.aps.org/prc/abstract/10.1103/rds9-9p7r) | PRC 114, 054603，10-07 是接收日、11-06 才是正式发表日。官方 harvest401 未授权、普通 PDF403；记录状态变化，未获得正文。 |

[下载报告](./download_report.json)保存具体响应；[重试台账](../../state/daily_retry_candidates.json)保留接续信息。新隐式混合 PIC、低秩 Vlasov、ELBEX QED 束线和非轴对称 MHD 仅为[未读线索](./research/next-leads.json)，没有科学结论或完成计数。

## 当日综合判断与接续

光栅两篇提供了不同机制的数值与实验参考，不能直接以场电离的实验效率“验证”有质动力模型；效率分母、延时拟合寿命和密度模型各有边界。Hosing 截止式和图注问题属于静态核查；ML 高决定系数针对关闭下游集体效应的固定模拟标签，未来数字孪生尚未接入真机。本轮未运行作者 Vlasov、OSIRIS、ASTRA、Elegant、机器学习或实验，也未重新分析原始实验数据；没有新增光核核素端到端、患者临床或防护验收。

优先恢复正式全文；随后核光栅密度图注、入射／透射效率与孔径放大，重做严格 hosing 全根判稳，并为束流代理补集体效应和独立真机标定。运行与完成检查见 [run_results.json](./run_results.json)及 [verification.json](./research/verification.json)。
