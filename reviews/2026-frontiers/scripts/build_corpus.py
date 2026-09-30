#!/usr/bin/env python
"""Snapshot repository literature and make an auditable review bibliography."""
import hashlib
import importlib.util
import json
from collections import Counter
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
ROOT = BASE.parents[1]
spec = importlib.util.spec_from_file_location('indexes', ROOT / 'scripts/build_indexes.py')
idx = importlib.util.module_from_spec(spec)
spec.loader.exec_module(idx)
items = idx.load_items()
items.sort(key=lambda a: (a.get('publication_date') or '', a.get('doi') or '', a['title']))
rows = []
for i, item in enumerate(items, 1):
    row = {k: v for k, v in item.items() if not k.startswith('_')}
    row['ref'] = f'R{i:03}'
    row['paper_slug'] = item['_paper_slug']
    row['categories'] = item['_categories']
    for kind in ('note', 'pdf'):
        path = ROOT / row[f'{kind}_path'] if row.get(f'{kind}_path') else None
        row[f'{kind}_exists'] = bool(path and path.is_file())
        if row[f'{kind}_exists'] and kind == 'note':
            row['note_sha256'] = hashlib.sha256(path.read_bytes()).hexdigest()
    rows.append(row)
summary = {
    'cutoff': '2026-09-30',
    'ledger_sha256': hashlib.sha256(idx.STATE_PATH.read_bytes()).hexdigest(),
    'total': len(rows),
    'publication_years': dict(sorted(Counter(r['publication_date'][:4] for r in rows).items())),
    'notes_present': sum(r['note_exists'] for r in rows),
    'pdf_paths_present': sum(r['pdf_exists'] for r in rows),
    'category_counts': dict(Counter(c for r in rows for c in r['categories'])),
    'note': 'PDF existence is a path check, not full-text review or PDF health validation. Categories reuse repository routing, not a manual scientific taxonomy.',
}
(BASE / 'data/corpus.json').write_text(json.dumps({'summary': summary, 'articles': rows}, ensure_ascii=False, indent=2) + '\n')
lines = ['# 全库参考文献与阅读覆盖', '',
         '统计截止：2026-09-30。R 编号在此版快照内唯一。发表日期取仓库台账，不取入库日期；预印本与正式版状态按原记录保留。', '',
         '“有笔记”表示复用既有解读素材，不表示本次逐篇重新精读；“PDF 路径存在”不表示本文已逐页审阅。重点讲解请见各主题章。无笔记条目不承担未经原文核实的结果性论断。', '']
titles = {c['slug']: c['title'] for c in idx.all_categories()}
for row in rows:
    ref = row['ref']
    lines += [f'<a id="{ref.lower()}"></a>', '', f'## {ref} · {row["title"]}', '',
              f'- 发表：{row["publication_date"]}；来源状态：{row.get("journal", "未记录")}。',
              f'- 原始来源：[来源页]({row["source_url"]})；标识：`{row.get("doi") or "未记录"}`。',
              f'- 分类：{"；".join(titles[c] for c in row["categories"])}。',
              f'- 仓库论文页：[索引](../../../papers/{row["paper_slug"]}/README.md)。']
    if row['note_exists']:
        lines.append(f'- 阅读材料：[既有中文笔记](<../../../{row["note_path"]}>)。')
    else:
        lines.append('- 阅读材料：缺少中文笔记；本版仅目录覆盖，留待全文补读。')
    if row['pdf_exists']:
        lines.append(f'- 全文路径：[本地 PDF](<../../../{row["pdf_path"]}>)（PDF 通常不随 Git 跟踪）。')
    else:
        lines.append('- 全文路径：台账未指向当前存在的本地 PDF；不可据此断言没有其他全文来源。')
    lines.append('')
(BASE / 'appendices/reference-catalog.md').write_text('\n'.join(lines))
print(json.dumps(summary, ensure_ascii=False, indent=2))
