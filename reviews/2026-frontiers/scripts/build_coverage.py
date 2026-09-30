#!/usr/bin/env python
"""Build exact, non-inflated chapter citation coverage and material gaps."""
import csv
import json
import re
from collections import Counter
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
corpus = json.loads((BASE / 'data/corpus.json').read_text())
rows = corpus['articles']
chapter_refs = {}
for path in sorted((BASE / 'chapters').glob('*.md')):
    chapter_refs[path.name] = set(re.findall(r'R\d{3}', path.read_text()))
records = []
for row in rows:
    rec = {k: row.get(k) for k in ('ref', 'title', 'publication_date', 'note_exists', 'pdf_exists')}
    rec['categories'] = ';'.join(row['categories'])
    rec['cited_chapters'] = ';'.join(p for p, refs in chapter_refs.items() if row['ref'] in refs)
    rec['coverage'] = '正文引用' if rec['cited_chapters'] else '目录覆盖'
    records.append(rec)
with (BASE / 'data/coverage.csv').open('w', newline='', encoding='utf-8') as out:
    writer = csv.DictWriter(out, fieldnames=list(records[0]), lineterminator='\n')
    writer.writeheader()
    writer.writerows(records)
cat_titles = {
    'laser-plasma-acceleration': '激光等离子体与束流加速',
    'laser-accelerated-beam-applications': '束流、辐射与核应用',
    'strong-field-qed-radiation': '强场QED与辐射反作用',
    'hedp-icf-laboratory-astrophysics': 'HEDP、ICF与实验室天体',
    'pic-and-plasma-simulation': 'PIC、动理学与数值模拟',
    'ai-ml-plasma-physics': 'AI与等离子体',
    'magnetic-fusion-and-alpha-particles': '磁约束聚变与快粒子',
    'experimental-platforms-diagnostics': '实验平台、靶与诊断',
    'general-plasma-and-methods': '综合等离子体与交叉方法',
}
def clean(text):
    return text.replace('|', '\\|').replace('\n', ' ')

lines = ['# 按主题的逐条覆盖矩阵', '',
    '“正文引用”表示该条目在某章有明确R编号引用，可能是重点讲解，也可能是历史/对比串联；它不等于整篇全文精读。“目录覆盖”表示纳入全库目录但未在正文章展开。笔记/PDF列只表示当前路径存在。', '',
    f'全库{len(rows)}条；正文引用{sum(bool(r["cited_chapters"]) for r in records)}条；其余为目录覆盖。分类可交叉，下面会重复显示同一条目。', '']
for slug, title in cat_titles.items():
    subset = [(row, rec) for row, rec in zip(rows, records) if slug in row['categories']]
    lines += [f'## {title}', '',
        f'原路由{len(subset)}条；其中{sum(bool(rec["cited_chapters"]) for _, rec in subset)}条在正文有引用。类别保留原仓库路由，不代表全部均是此领域的核心研究。', '',
        '| 编号 | 发表年 | 文章 | 材料 | 正文位置 |', '| --- | --- | --- | --- | --- |']
    for row, rec in subset:
        chapters = [f'[{p[:2]}](../chapters/{p})' for p in rec['cited_chapters'].split(';') if p]
        lines.append(f'| [{row["ref"]}](reference-catalog.md#{row["ref"].lower()}) | {row["publication_date"][:4]} | {clean(row["title"])} | {"笔记" if row["note_exists"] else "缺笔记"} / {"PDF在" if row["pdf_exists"] else "PDF路径缺"} | {"、".join(chapters) or "仅目录"} |')
    lines.append('')
(BASE / 'appendices/coverage-by-topic.md').write_text('\n'.join(lines))
gap_count = sum(not row['note_exists'] for row in rows)
gaplines = ['# 阅读缺口与补读顺序', '',
    f'当前{gap_count}条缺少中文笔记，均保留在参考目录。本版没有仅凭标题给这些文章生成结果性总结。部分条目有PDF但未形成笔记，部分没有可用的台账PDF路径；与下载重试队列的候选不是同一集合。', '',
    '优先补读：能补齐同shots束流—转换—产额链的实验；可用来检验闭合/代理的实机或留出数据；能减少HED模型依赖的多诊断物性；重要算法的原始格式与收敛证明。其次补背景综述和比较基线。优先级需要结合实际全文，不按标题或期刊机械排名。', '',
    '| 编号 | 发表日期 | 文章 | PDF路径存在 |', '| --- | --- | --- | --- |']
for row in rows:
    if not row['note_exists']:
        gaplines.append(f'| [{row["ref"]}](reference-catalog.md#{row["ref"].lower()}) | {row["publication_date"]} | {clean(row["title"])} | {"是" if row["pdf_exists"] else "否"} |')
gaplines += ['', '## 现有笔记也有质量缺口', '',
    '有笔记不等于达到逐式/逐图可复现解读。少数早期笔记使用通用模板，公式与实际研究机制未必匹配。本版用标准教学推导和关键原文复核绕开这些问题；已识别差异见[source-discrepancies.md](source-discrepancies.md)。后续应按科学编辑流程修订原笔记，并记录原文页码、图号、版本及修订依据。', '',
    '## 全文访问与版本', '',
    '合法作者稿、arXiv、正式版和机器排版替代文本的证据能力不同。比如同作品机器排版文本没有原始图，不能用于原图视觉判读。网页访问受限不等于论文不存在；保持重试记录，并在可达时补核对。当前综述不改变原仓库下载队列。', '']
(BASE / 'appendices/reading-gaps.md').write_text('\n'.join(gaplines))
summary = {
    'total_articles': len(rows),
    'unique_articles_cited_in_chapters': sum(bool(r['cited_chapters']) for r in records),
    'catalogue_only': sum(not r['cited_chapters'] for r in records),
    'missing_notes': sum(not r['note_exists'] for r in rows),
    'chapters': {p: {'unique_refs': len(refs)} for p, refs in chapter_refs.items()},
}
(BASE / 'data/coverage-summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2)+'\n')
print(json.dumps(summary, ensure_ascii=False, indent=2))
