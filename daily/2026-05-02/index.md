# 每日论文索引 - 2026-05-02

## 今日新增论文索引

### 1) Neural network sampling of Bethe-Heitler process in particle-in-cell codes
- 作者：Óscar Amaro, Chiara Badiali, Bertrand Martinez
- 期刊/平台：Journal of Computational Physics（正式期刊）
- DOI：https://doi.org/10.1016/j.jcp.2026.114707
- 真实发表日期：2026-05-15
- 来源链接：https://www.sciencedirect.com/science/article/pii/S0021999126000574
- PDF 文件名：`Oscar Amaro et al. - 2026 - Neural network sampling of Bethe-Heitler process in particle-in-cell codes.pdf`（本次环境网络受限，下载失败，已加入重试队列）
- 影响因子分：9/10
- 专业相似度分：10/10
- 推荐理由：直接作用于PIC中强场QED微观过程采样，属于“机器学习 + 激光等离子体 + PIC”高相关交叉方向。
- 一句话总结：该文用神经网络替代PIC代码中Bethe-Heitler对产生过程的查表采样，在保持物理精度的同时将模型存储需求降低约两个数量级。

## 检索与去重执行记录

- 已重新读取并使用 `state/processed_articles.json` 与 `state/daily_retry_candidates.json` 作为去重基线。
- 今日重点检索方向：激光等离子体、强场QED、高能量密度物理、PIC，以及机器学习在这些方向中的应用。
- 本次新增 1 篇正式期刊论文（JCP, 2026-05-15），此前未在去重台账中出现。

## 下载与校验状态

- 10.1016/j.jcp.2026.114707：受当前运行环境网络解析限制（`doi.org` 无法解析），PDF 下载失败；已记录重试候选。

## 笔记产出

- `notes/Oscar Amaro et al. - 2026 - Neural network sampling of Bethe-Heitler process in particle-in-cell codes.md`

## 状态更新

- `state/processed_articles.json`：新增 1 条（`pdf_path=null`，保留元数据与笔记路径）。
- `state/daily_retry_candidates.json`：新增 1 条下载失败重试记录。

## 当日总结

- 今天新增论文集中在“机器学习替换 PIC中强场QED采样模块”的可工程化路线，与本仓库方向高度一致。
- 一旦网络可用，优先补下该文PDF并细读其网络结构、误差传播和推理性能评测细节。
