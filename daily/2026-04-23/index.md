# 每日论文索引 - 2026-04-23

## 今日新增论文索引

- 无（本次候选均未通过下载与 PDF 校验，未执行入库）

## 今日高相关候选（已去重，未入库）

### 1) Efficient generation of a 100 nC electron beam via self-mode transition from LWFA to PWFA
- 作者：Huitong Zhai et al.
- 期刊/平台：High Power Laser Science and Engineering（正式期刊）
- DOI：https://doi.org/10.1017/hpl.2025.10093
- 真实发表日期：2026-03-05
- 来源链接：https://www.cambridge.org/core/journals/high-power-laser-science-and-engineering/article/efficient-generation-of-a-100-nc-electron-beam-via-selfmode-transition-from-lwfa-to-pwfa/CCC856732A1F652E97B889DB2C0CE823
- 与方向关系：LPWFA（LWFA→PWFA 自模式过渡）+ PIC，直接对应激光等离子体加速与束流品质优化。

### 2) Generation of polarization-tunable hybrid cylindrical vector gamma rays from rotating electron beams
- 作者：Si-Man Liu et al.
- 期刊/平台：High Power Laser Science and Engineering（正式期刊）
- DOI：https://doi.org/10.1017/hpl.2026.10121
- 真实发表日期：2026-03-02
- 来源链接：https://www.cambridge.org/core/journals/high-power-laser-science-and-engineering/article/generation-of-polarizationtunable-hybrid-cylindrical-vector-gamma-rays-from-rotating-electron-beams/7ECAA9BDB454ACF208755F225D47B86E
- 与方向关系：强场辐射（非线性康普顿）+ 三维自旋分辨 PIC，连接强场 QED 与结构化 γ 源。

### 3) Properties of well isolated warm dense matter produced by collision of high-speed plasma jets
- 作者：Gaoyang Liu et al.
- 期刊/平台：High Power Laser Science and Engineering（正式期刊，Accepted Manuscript）
- DOI：https://doi.org/10.1017/hpl.2026.10108
- 真实发表日期：2026-01-12
- 来源链接：https://www.cambridge.org/core/journals/high-power-laser-science-and-engineering/article/properties-of-well-isolated-warm-dense-matter-produced-by-collision-of-highspeed-plasma-jets/7ADB5354A376261FD82BD6E1BA8DEBF1
- 与方向关系：高速喷流碰撞制备温稠密物质，属于 HEDP 关键实验问题。

## 检索与去重执行记录

- 已读取 `state/processed_articles.json`（50 条）并按 DOI + 规范化标题 + source_url 执行去重。
- 本次筛选得到 3 篇高相关正式论文，均未命中 state 去重键。
- 本次仍未入库，原因是下载校验失败（见下）。

## 下载与校验状态

- `scripts/safe_pdf_download.py` 已对 3 篇候选执行“环境代理 + 直连 + DOI 回退”流程。
- 失败原因一致：
- 代理模式：`127.0.0.1:1087` 不可达（ProxyError）。
- 直连模式：`www.cambridge.org`/`doi.org` 解析失败（NameResolutionError）。
- 本次未产生通过校验的新 PDF。

## 笔记产出

- 无（未下载并校验 PDF，不生成逐篇笔记）。

## 状态更新

- `state/processed_articles.json`：未变更（仍为 50 条）。

## 当日总结

- 今日候选覆盖 LPWFA、强场辐射偏振调控与温稠密物质三条主线，相关性高。
- 受网络解析与代理不可用影响，今天未形成可入库增量。
