# 每日论文雷达 - 2026-04-22

## 今日新增论文索引

- 无（本地网络解析故障导致 PDF 下载与校验失败，未执行入库）

## 今日高相关候选（已去重，未入库）

### 1) All-optically controllable electron and X-ray sources from microchannel-guided direct laser acceleration
- 作者：Chengyu Qin et al.
- 期刊/平台：High Power Laser Science and Engineering（正式期刊，Open Access）
- DOI：https://doi.org/10.1017/hpl.2025.10096
- 真实发表日期：2026-03-19
- 来源链接：https://www.cambridge.org/core/journals/high-power-laser-science-and-engineering/article/alloptically-controllable-electron-and-xray-sources-from-microchannelguided-direct-laser-acceleration/F208F22C7AC66CD2368B45701336A7E8
- 去重结果：未命中 `state/processed_articles.json`
- 与方向关系：激光等离子体电子加速 + X 射线二次源 + 3D PIC 仿真。

### 2) Pushing the frontiers of light: magnetized plasma lenses and chirp tailoring for extreme intensities
- 作者：Trishul Dhalia et al.
- 期刊/平台：High Power Laser Science and Engineering（正式期刊，Open Access）
- DOI：https://doi.org/10.1017/hpl.2025.10101
- 真实发表日期：2026-03-18
- 来源链接：https://www.cambridge.org/core/journals/high-power-laser-science-and-engineering/article/pushing-the-frontiers-of-light-magnetized-plasma-lenses-and-chirp-tailoring-for-extreme-intensities/B06CB5E437556FDFF69156DDBE78E73B
- 去重结果：未命中 `state/processed_articles.json`
- 与方向关系：磁化等离子体透镜 + 脉冲啁啾整形 + OSIRIS PIC，面向极端强场。

### 3) Laguerre–Gaussian pulses for spin-polarized ion beam acceleration
- 作者：Lars Reichwein et al.
- 期刊/平台：High Power Laser Science and Engineering（正式期刊，Open Access，Editors’ Pick）
- DOI：https://doi.org/10.1017/hpl.2025.10098
- 真实发表日期：2026-02-18
- 来源链接：https://www.cambridge.org/core/services/aop-cambridge-core/content/view/C9D2B94D52BA5DE415880F2994166725/S2095471925100984a_hi.pdf/laguerre-gaussian-pulses-for-spin-polarized-ion-beam-acceleration.pdf
- 去重结果：未命中 `state/processed_articles.json`
- 与方向关系：激光等离子体极化离子加速 + 3D PIC，连接强场与高能量密度实验需求。

## 检索与去重执行记录

- 已读取 `state/processed_articles.json`（当前 50 条）作为去重基线。
- 本次优先筛选正式发表来源，并排除历史已处理 DOI。
- 本次候选 3 篇均通过“未处理”筛选，但因网络阻塞未完成 PDF 校验，因此不入库。

## 下载与校验状态

- `scripts/safe_pdf_download.py` 对 3 篇候选均执行了“环境代理 + 直连 + DOI 回退”下载流程。
- 失败原因一致：
- 代理模式：`127.0.0.1:1087` 不可用（Operation not permitted）。
- 直连模式：`www.cambridge.org`、`doi.org` DNS 解析失败（NameResolutionError）。
- 本次未生成有效 PDF 文件。

## 笔记产出

- 无（未下载并校验 PDF，不生成逐篇笔记以避免基于不完整信息写入）。

## 状态更新

- `state/processed_articles.json`：未变更（避免在无 PDF 校验下写入新元数据）。
- 当网络恢复后，优先重试本页 3 篇候选并补齐 `pdfs/`、`notes/` 与 state 入库。
