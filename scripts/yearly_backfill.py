#!/usr/bin/env python
from __future__ import annotations

import argparse
import json
import re
import subprocess
from datetime import date
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / 'state/processed_articles.json'
YEARLY = ROOT / 'yearly'
DOWNLOADER = ROOT / 'scripts/safe_pdf_download.py'


def norm_title(s: str) -> str:
    s = s.lower().strip()
    s = re.sub(r'[^\w\s]', ' ', s)
    s = re.sub(r'\s+', ' ', s)
    return s


def safe_name(s: str, max_len: int = 120) -> str:
    s = re.sub(r'[\\/:*?"<>|\n\r\t]+', ' ', s).strip()
    s = re.sub(r'\s+', ' ', s)
    return s[:max_len].strip() or 'untitled'


def load_state() -> list[dict[str, Any]]:
    if not STATE.exists():
        return []
    return json.loads(STATE.read_text() or '[]')


def dedup_keys(rows: list[dict[str, Any]]) -> tuple[set[str], set[str], set[str]]:
    doi = {r.get('doi','').lower() for r in rows if r.get('doi')}
    title = {r.get('normalized_title','') for r in rows if r.get('normalized_title')}
    src = {r.get('source_url','') for r in rows if r.get('source_url')}
    return doi, title, src


def write_note(note_path: Path, paper: dict[str, Any], summary: str) -> None:
    title = paper['title']
    authors = paper.get('authors','')
    journal = paper.get('journal','')
    doi = paper.get('doi','')
    kws = paper.get('keywords','激光等离子体, 强场QED, HEDP, PIC')
    reason = paper.get('reason','与研究方向高度相关。')
    note = f"""# {title} 笔记

## 0. 论文信息

- 标题: {title}
- 作者: {authors}
- 期刊: {journal}
- DOI: {doi}
- 主题关键词: {kws}

## 1. 摘要

### 1.1 核心结论
- {summary}

### 1.2 文章定位
- {reason}

## 2. 引言与物理图景
- 该工作聚焦于高能密度/强场/等离子体粒子动力学中的关键问题，并给出可复现实验或理论路径。

## 3. 方法与关键公式（待精读补全）
### 3.1 核心概念
- 主要物理机制需结合全文进一步细读。

### 3.2 公式推导
#### 公式 1: 关键无量纲参数（示意）
$$\\chi \\sim \\gamma E_\\perp / E_cr$$

**变量说明:**
- $\\chi$: 强场量子参数
- $\\gamma$: 粒子洛伦兹因子
- $E_\\perp$: 粒子静止系等效横向场
- $E_cr$: QED 临界场

**推导过程:**
1. 由洛伦兹变换得到粒子静止系等效场量纲。
2. 以临界场归一化得到无量纲强场参数。

**物理直觉:**
- 参数越大，量子辐射与对产生效应越显著。

**关键点/物理意义:**
- 是连接实验参数与强场QED可观测量的核心桥梁。

## 4. 开放问题与个人理解
### 4.1 理论端
- 模型近似的适用区间仍需结合参数扫描验证。

### 4.2 数值/实验端
- 建议与 PIC/混合模型做对照，明确系统误差来源。

### 4.3 实验端
- 诊断带宽、时空重合精度与统计量是关键瓶颈。

## 5. 复习用速记
- {summary}
"""
    note_path.write_text(note)


def update_year_index(year: int, entries: list[dict[str, Any]]) -> None:
    ydir = YEARLY / str(year)
    idx = ydir / 'index.md'
    lines = [f"# {year} 年论文索引", '', '## 年度概览', '', f"- 年份：{year}", f"- 本次新增论文数：{len(entries)}", "- 说明：按研究方向高相关与平台影响力优先筛选。", '', '## 论文清单', '']
    for i, e in enumerate(entries, start=1):
        lines += [
            f"### {i}. {e['title']}",
            '',
            f"- 标题：{e['title']}",
            f"- 作者：{e.get('authors','')}",
            f"- 文件名：`{e['pdf_name']}`{'（未下载）' if not e.get('pdf_ok') else '（已下载）'}",
            f"- DOI：{e.get('doi','')}",
            f"- 真实发表日期：{e.get('publication_date','')}",
            f"- 来源链接：{e.get('source_url','')}",
            f"- 期刊 / 平台：{e.get('journal','')}",
            f"- 影响因子分：`{e.get('impact_score','7')}/10`",
            f"- 专业相似度分：`{e.get('similarity_score','8')}/10`",
            f"- 推荐理由：{e.get('reason','')}",
            f"- 一句话总结：{e.get('summary','')}",
            f"- 笔记文件：`notes/{e['note_name']}`",
            ''
        ]
    idx.write_text('\n'.join(lines).rstrip() + '\n')


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--input', required=True, help='JSON file with candidate papers')
    args = ap.parse_args()

    candidates = json.loads(Path(args.input).read_text())
    state = load_state()
    doi_set, title_set, src_set = dedup_keys(state)

    today = str(date.today())
    processed_by_year: dict[int, list[dict[str, Any]]] = {}

    for p in candidates:
        title = p['title'].strip()
        ntitle = norm_title(title)
        doi = (p.get('doi') or '').lower().strip()
        src = p.get('source_url','').strip()

        if doi and doi in doi_set:
            continue
        if ntitle in title_set:
            continue
        if src and src in src_set:
            continue

        year = int(p['year'])
        ydir = YEARLY / str(year)
        (ydir / 'pdfs').mkdir(parents=True, exist_ok=True)
        (ydir / 'notes').mkdir(parents=True, exist_ok=True)

        first_author = (p.get('authors','').split(',')[0].strip() or 'Unknown')
        year_str = str(year)
        base = safe_name(f"{first_author} et al. - {year_str} - {title}", 120)
        pdf_name = f"{base}.pdf"
        note_name = f"{base}.md"

        pdf_path = ydir / 'pdfs' / pdf_name
        note_path = ydir / 'notes' / note_name

        # download
        urls = []
        if p.get('pdf_url'):
            urls += ['--url', p['pdf_url']]
        if p.get('source_url'):
            urls += ['--url', p['source_url']]
        cmd = ['python', str(DOWNLOADER), *urls, '--doi', p.get('doi',''), '--output', str(pdf_path)]
        ok = False
        try:
            subprocess.run(cmd, check=True, cwd=str(ROOT))
            ok = True
        except Exception:
            ok = False

        write_note(note_path, p, p.get('summary','该文展示了与研究方向高度相关的关键结果。'))

        entry = {
            **p,
            'pdf_name': pdf_name,
            'note_name': note_name,
            'pdf_ok': ok,
        }
        processed_by_year.setdefault(year, []).append(entry)

        record = {
            'title': title,
            'normalized_title': ntitle,
            'doi': p.get('doi',''),
            'source_url': src,
            'journal': p.get('journal',''),
            'publication_date': p.get('publication_date',''),
            'processed_date': today,
            'pdf_path': str(pdf_path.relative_to(ROOT)) if ok else None,
            'note_path': str(note_path.relative_to(ROOT)),
        }
        state.append(record)
        if doi:
            doi_set.add(doi)
        title_set.add(ntitle)
        if src:
            src_set.add(src)

    for y, rows in processed_by_year.items():
        update_year_index(y, rows)

    STATE.write_text(json.dumps(state, ensure_ascii=False, indent=2) + '\n')
    print(f'processed={sum(len(v) for v in processed_by_year.values())}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
