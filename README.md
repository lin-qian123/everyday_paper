# everyday_paper

一个持续更新的高功率激光、等离子体物理与相关应用论文索引仓库。按天搜集、去重、下载并分析本仓库研究方向相关论文，并将已入库论文整理为分类索引。

## 目录

- [项目定位](#项目定位)
- [关注主题](#关注主题)
- [索引文件](#索引文件)
- [仓库结构](#仓库结构)
- [分类索引](#分类索引)
- [当前状态](#当前状态2026-06-20)
- [去重规则](#去重规则)
- [PDF 下载稳健性](#pdf-下载稳健性)
- [维护约定](#维护约定)

## 项目定位

仓库内容包括：

- 每日跟踪激光等离子体、强场 QED、高能量密度物理、PIC、机器学习等方向的新论文。
- 优先从正式发表来源检索，必要时补充高质量 arXiv 预印本。
- 为新增论文下载并校验 PDF，生成中文结构化笔记。
- 维护分类索引、论文页、每日索引和 GitHub 同步记录。

## 关注主题

- 激光等离子体（laser plasma）
- 强场 QED（strong-field QED）
- 高能量密度物理（high energy density physics）
- PIC 及相关计算方法
- 机器学习 / 数据驱动方法 / 先进算法在上述方向中的应用与结合
- 激光加速电子束、离子束及其应用：包括电子束打转换靶产生韧致辐射 / 伽马源、光核反应、中子 / 同位素产生、核诊断、辐照、诊疗、材料研究，以及相关束流品质、靶设计、转换效率和辐射防护问题

## 索引文件

- 总索引：[`INDEX.md`](./INDEX.md)
- 分类索引：[`categories/`](./categories/)
- 单篇论文索引：[`papers/<paper>/README.md`](./papers/)
- 每日索引：[`daily/README.md`](./daily/README.md)
- 中文笔记：`daily/YYYY-MM-DD/notes/`

## 仓库结构

- `daily/`：按日期归档的每日论文索引、下载报告、中文笔记和运行结果。
- `papers/`：按单篇论文生成的索引页，由 `scripts/build_indexes.py` 自动维护。
- `categories/`：按主题生成的分类索引，由 `scripts/build_indexes.py` 自动维护。
- `state/processed_articles.json`：已处理论文去重台账和索引数据源。
- `state/daily_retry_candidates.json`：下载失败或待重试候选台账。
- `scripts/`：下载、重试和索引构建脚本。
- `templates/`：每日索引模板。
- `yearly/`：历史年度回填索引。
- `AGENTS.md`：自动化执行规则。
- `TODO.md`：待办、阶段记录、阻塞点和接续线索。

## 分类索引

完整索引见 [`INDEX.md`](./INDEX.md) 与 [`categories/README.md`](./categories/README.md)。当前分类包括：

- [激光等离子体与束流加速](./categories/laser-plasma-acceleration.md)
- [激光加速电子/离子束应用](./categories/laser-accelerated-beam-applications.md)
- [强场 QED 与辐射反作用](./categories/strong-field-qed-radiation.md)
- [高能量密度物理、ICF 与实验室天体](./categories/hedp-icf-laboratory-astrophysics.md)
- [PIC、动理学与数值模拟](./categories/pic-and-plasma-simulation.md)
- [机器学习与等离子体物理](./categories/ai-ml-plasma-physics.md)
- [磁约束聚变与 alpha 粒子](./categories/magnetic-fusion-and-alpha-particles.md)
- [实验平台、靶设计与诊断](./categories/experimental-platforms-diagnostics.md)
- [综合等离子体与交叉方法](./categories/general-plasma-and-methods.md)

## 目录约定

- `daily/YYYY-MM-DD/`: 每日运行输出目录
- `daily/YYYY-MM-DD/pdfs/`: 当天新发现论文 PDF
- `daily/YYYY-MM-DD/notes/`: 逐篇中文笔记
- `daily/YYYY-MM-DD/index.md`: 当天论文索引与汇总
- `papers/<paper>/README.md`: 单篇论文索引页
- `categories/*.md`: 主题分类索引
- `INDEX.md`: 总索引
- `state/processed_articles.json`: 已处理论文去重台账
- `templates/daily-index-template.md`: 每日索引模板

## 当前状态（2026-06-20）

- 已连续维护到 `daily/2026-06-20/`。
- 关注主题已扩展到激光加速电子束与离子束应用方向，后续每日检索纳入转换靶韧致辐射、伽马源、光核反应、中子/同位素产生、激光离子加速应用和相关靶/诊断/防护问题。
- `2026-06-20` 新增 3 条高相关论文并完成 PDF 校验与中文笔记，均为 arXiv 高相关补充，分别覆盖波导去相位 LWFA、数据驱动 stellarator alpha-particle confinement Bayesian optimization，以及用于高重复频 HEDP 的流体微透镜 caustic 增强方案。
- 已处理论文总数增至 126 条；`state/daily_retry_candidates.json` 维持 12 条。
- 当前重试队列只剩已明确的来源侧限制：10 条 ScienceDirect / Elsevier `HTTP 403`、1 条 Nature `cookies_not_supported`、1 条 IOP / New Journal of Physics Radware/Perfdrive 验证页。
- 2026-06-11 配置级诊断显示当前 Codex shell 已是 `danger-full-access` 且 network enabled；`127.0.0.1:1087` 代理路径可下载 arXiv PDF。此前 06-09 到 06-11 的 9 条 runtime-blocked 候选已通过 `retry_download_queue.py` 全部恢复。
- 当前有 65 条已补到 PDF 但尚未补中文结构化笔记的历史条目。
- 已新增自动索引脚本 `scripts/build_indexes.py`，可从 `state/processed_articles.json` 重建 `INDEX.md`、`papers/`、`categories/` 与 `daily/README.md`。
- `scripts/safe_pdf_download.py` 已支持 HTML 落地页自动提取官方 PDF、失败分类输出和 `curl` 传输回退；其中 `curl` 回退下的代理不可连 / DNS 失败也已单独归类。`scripts/retry_download_queue.py` 可批量重试并自动更新 processed/retry 台账。今天再次验证：Cambridge 文章页/DOI 到官方 PDF 的自动跟进仍可正常完成下载；但对来源侧长期受限的 12 条旧队列，全量重试仍会在无效来源上耗时过长，后续更适合按来源分组或限额运行。

## 去重规则

默认以 DOI 为第一去重键；没有 DOI 时，使用规范化标题；仍无法稳定识别时，结合源链接与 PDF 文件名判断。已经记录在 `state/processed_articles.json` 或已出现在历史 `daily/` 目录中的论文，不应重复下载和重复分析。

## 评分规则

- 影响因子分：`1-10`
- 专业相似度分：`1-10`

影响因子分优先依据期刊影响力、领域声誉和发表平台层级；若是预印本，则明确标注为预印本并给出保守评分。专业相似度分衡量该论文与本仓库关注方向的直接相关程度。

## PDF 下载稳健性

为避免自动化因本地代理失效（常见于 `http_proxy/https_proxy/all_proxy` 指向 `127.0.0.1` 但代理未启动）导致下载失败，统一使用：

```bash
python scripts/safe_pdf_download.py --url <候选URL> --doi <DOI> --output <目标pdf路径>
```

该脚本会自动两阶段重试：
- 先按当前环境代理下载
- 若失败，自动绕过环境代理直连重试
- 若 DOI 存在且出版社链接不可得，会自动查询 Unpaywall 的合法开放获取链接再重试
- 若候选链接先返回 HTML 文章页（例如 Cambridge Core），会自动解析页面中的官方 PDF 链接并继续尝试
- 若 `urllib` 传输层失败，会自动回退到 `curl`

并会校验下载结果是否为真实 PDF（`Content-Type` 或 `%PDF-` 文件头）。

需要批量消化历史重试队列时，可使用：

```bash
python scripts/retry_download_queue.py --source-family cambridge
python scripts/retry_download_queue.py --source-family nature
python scripts/retry_download_queue.py --source-family elsevier
python scripts/retry_download_queue.py --source-family iop
```

重试脚本会自动在队列条目上写入 `retry_count`、`last_retry_at`、`source_family` 与 `last_failure_class`，并在成功时把 PDF 转入 `state/processed_articles.json`。

说明：仅使用合法来源（出版社站点、DOI 跳转、Unpaywall 收录的 OA 地址）；不使用侵权镜像站。

## 年度回填目录（历史）

- `yearly/YYYY/pdfs/`: 对应年份回填论文 PDF
- `yearly/YYYY/notes/`: 对应年份回填中文笔记
- `yearly/YYYY/index.md`: 对应年份索引
- `yearly/index.md`: 年度回填总索引

## 维护约定

- 默认直接在当前分支更新，不新建分支。
- 每日新增论文后，同步更新 `state/processed_articles.json`、当天 `daily/YYYY-MM-DD/index.md` 和中文笔记。
- 每次更新台账后运行：

```bash
python scripts/build_indexes.py
```

- 索引脚本会重建 `papers/`、`categories/`、`daily/README.md` 与 `INDEX.md`；这些文件构成 GitHub 论文索引。
- GitHub 仓库默认不跟踪 PDF 文件，避免仓库过大；PDF 本地路径仍保留在元数据与论文页中。
- 自动化成功完成后，默认提交并推送到 `origin/master`。
