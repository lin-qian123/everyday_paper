# 历史缺失 PDF 回填记录 - 2026-06-06

## 回填结果概览

- 本次针对 `state/daily_retry_candidates.json` 中的历史缺失 PDF 做了集中补回。
- 成功补回唯一论文 29 篇，并同步更新了 `state/processed_articles.json`。
- 已从重试队列移除 35 条成功记录（含重复旧记录），并额外清理 1 条重复失败记录。
- 当前重试队列剩余 12 条，主要阻塞已收敛为：
  - Elsevier / ScienceDirect 相关条目返回 `HTTP 403`
  - IOP 条目落到反爬验证页
  - 个别 Nature 条目返回 `cookies_not_supported`
- 当前 `state/processed_articles.json` 共 80 条，其中 28 条已补到 PDF 但尚未补中文结构化笔记。

## 本次成功补回的 PDF

### 2026-04-25
- `10.1017/hpl.2025.10093` - Efficient generation of a 100 nC electron beam via self-mode transition from LWFA to PWFA
- `10.1017/hpl.2026.10121` - Generation of polarization-tunable hybrid cylindrical vector gamma rays from rotating electron beams
- `10.1017/hpl.2026.10108` - Properties of well isolated warm dense matter produced by collision of high-speed plasma jets
- `10.1017/hpl.2025.10096` - All-optically controllable electron and X-ray sources from microchannel-guided direct laser acceleration
- `10.1017/hpl.2025.10101` - Pushing the frontiers of light: magnetized plasma lenses and chirp tailoring for extreme intensities
- `10.1017/hpl.2025.10098` - Laguerre-Gaussian pulses for spin-polarized ion beam acceleration

### 2026-04-26
- `10.1038/s41598-026-41516-0` - Beam shape effect on enhanced laser wakefield acceleration of electrons driven by 10-fs mJ-class pulses
- `10.1038/s41598-026-41214-x` - Ponderomotive plasma lenses for holography by Gaussian beams
- `10.1038/s41586-026-10400-2` - Efficiency-optimized relativistic plasma harmonics for extreme fields

### 2026-04-27
- `10.1017/hpl.2026.10111` - Probing Short-Lived Nuclear Isomers in Laser-Induced Plasmas
- `10.1017/hpl.2025.10105` - Efficient plasma-based polarization converter for intense X-ray lasers
- `10.11884/HPLPB202638.250384` - Recent advances in Betatron radiation sources driven by laser-plasma interactions
- `10.11884/HPLPB202638.250382` - Femtosecond laser-driven ultrafast X-ray dynamics experimental station
- `10.1017/hpl.2025.10083` - ARISE: an algorithm for rapid ion spectrum extraction enabling real-time optimisation in high-repetition-rate laser-driven ion acceleration

### 2026-04-28
- `10.1038/s41598-026-47926-4` - X-ray tomography of damage dynamics in advanced materials using a laser wakefield accelerator

### 2026-05-03
- `10.1038/s41467-026-72697-x` - Transversely pumped laser driven particle accelerator

### 2026-05-18
- `10.1038/s41598-026-42431-0` - High-energy gamma-photons and pair electrons generation in polarized ultraintense laser fields

### 2026-05-20
- `10.48550/arXiv.2604.25823` - Revealing Laser and Electron Beam Evolution in 10-GeV-class Laser-Plasma Accelerators
- `10.48550/arXiv.2604.20672` - Attosecond Nonlinear Quantum Electrodynamics in Laser-Driven Plasmas via Two-Photon Synchrotron Emission

### 2026-06-02
- `10.1038/s41467-026-73196-9` - Quasi-monoenergetic deuteron acceleration via boosted coulomb explosion by reflected picosecond laser pulse
- `10.1038/s41598-025-29793-7` - Multi-PW laser-driven proton acceleration using a plasma-lens target

### 2026-06-03
- `10.1038/s42005-026-02689-2` - Explainable tokamak-agnostic forecasting of fusion plasma instability via megahertz turbulent fluctuations
- `10.1038/s42005-026-02674-9` - Ultrafast many-body dynamics of dense Rydberg gases and ultracold plasma
- `10.1038/s42005-026-02626-3` - FusionMAE, a self-supervised pretrained model to optimize and simplify diagnostic and control of fusion plasma

### 2026-06-05
- `10.1038/s41598-025-34221-x` - Influence of plasma, surface, and angle on interlinked X-ray emission dynamics in femtosecond burst pulse ablation
- `10.1017/hpl.2026.10129` - Compensation of Carrier Envelope Phase Slip using Machine Learning

### 2026-06-06
- `10.1038/s41598-026-35800-2` - Enhanced terahertz radiation generation by phase-controlled two-color laser pulses interacting with an under-dense plasma
- `10.1017/hpl.2026.10149` - Multi-pulse and multi-angle ultrafast X-ray imaging driven by petawatt-class ultrafast laser pulses
- title-key only - Dual-picosecond-laser-driven generation of MV/m giant electromagnetic pulses

## 仍待解决的剩余条目

- `10.1038/s41598-026-49116-8` - Nature 返回 `cookies_not_supported`
- `10.1016/j.engappai.2026.114332` - ScienceDirect `HTTP 403`
- `10.1088/1367-2630/ae57cb` - IOP 站点反爬验证页
- `10.1016/j.jcp.2026.114707` - ScienceDirect `HTTP 403`
- `10.1016/j.cpc.2026.110054` - ScienceDirect `HTTP 403`
- `10.1016/j.jcp.2026.114693` - ScienceDirect `HTTP 403`
- `10.1016/j.jcp.2026.114867` - ScienceDirect `HTTP 403`
- `10.1016/j.jcp.2026.114991` - ScienceDirect `HTTP 403`
- `10.1016/j.future.2025.108087` - ScienceDirect `HTTP 403`
- `10.1016/j.hedp.2025.101256` - ScienceDirect `HTTP 403`
- `10.1016/j.cpc.2026.110140` - ScienceDirect `HTTP 403`
- `10.1016/j.fpp.2026.100125` - ScienceDirect `HTTP 403`

## 说明

- 本次优先完成了“PDF 文件缺失”的补回；未承诺同时完成 29 篇的中文结构化笔记批量回填。
- 对已有笔记但此前缺 PDF 的条目，已在 `state/processed_articles.json` 中补上 `pdf_path`。
