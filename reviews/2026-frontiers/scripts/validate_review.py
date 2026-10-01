#!/usr/bin/env python
"""Structural audit. This does not validate scientific correctness."""
import hashlib
import json
import re
import subprocess
from pathlib import Path
from urllib.parse import unquote

BASE = Path(__file__).resolve().parents[1]
ROOT = BASE.parents[1]
corpus=json.loads((BASE/'data/corpus.json').read_text())
refs={r['ref'] for r in corpus['articles']}
errors=[]
files=list(BASE.rglob('*.md'))
files=[p for p in files if '.build' not in p.parts]
counts={}
def link_targets(node):
    if isinstance(node, dict):
        if node.get('t') in ('Link', 'Image'):
            yield node['c'][2][0]
        for value in node.values():
            yield from link_targets(value)
    elif isinstance(node, list):
        for value in node:
            yield from link_targets(value)
for p in files:
    t=p.read_text()
    unknown=set(re.findall(r'R\d{3}',t))-refs
    if unknown:errors.append(f'{p.name}: unknown references {sorted(unknown)}')
    ast=json.loads(subprocess.check_output(['pandoc',str(p),'--from=markdown+tex_math_dollars','-t','json']))
    for target in link_targets(ast):
        if re.match(r'^(https?://|mailto:|#)',target):continue
        target=target.split('#',1)[0]
        if not target:continue
        path=(p.parent/unquote(target)).resolve()
        if not path.exists():errors.append(f'{p.relative_to(BASE)}: missing link {target}')
    if p.parent.name=='chapters':
        counts[p.name]={'chinese_characters':len(re.findall(r'[\u4e00-\u9fff]',t)),
                        'unique_references':len(set(re.findall(r'R\d{3}',t)))}
        if t.count('$$')%2:errors.append(f'{p.name}: odd display math delimiters')
live_ledger=(ROOT/'state/processed_articles.json').read_bytes()
snapshot_ledger=live_ledger
ledger_validation='live ledger matches snapshot'
if hashlib.sha256(live_ledger).hexdigest()!=corpus['summary']['ledger_sha256']:
    commit=corpus['summary'].get('ledger_git_commit')
    if commit and re.fullmatch(r'[0-9a-f]{40}',commit):
        try:
            snapshot_ledger=subprocess.check_output(
                ['git','show',f'{commit}:state/processed_articles.json'],cwd=ROOT)
            ledger_validation=f'archived ledger verified at {commit}; live repository has advanced'
        except subprocess.CalledProcessError:
            errors.append('archived ledger commit is unavailable')
    else:
        errors.append('ledger changed after corpus snapshot without an archived commit')
if hashlib.sha256(snapshot_ledger).hexdigest()!=corpus['summary']['ledger_sha256']:
    errors.append('snapshot ledger hash mismatch')
snapshot_items=json.loads(snapshot_ledger)
source_items={(r.get('doi'),r['title']):r for r in snapshot_items}
if len(snapshot_items)!=len(refs):errors.append('snapshot ledger count mismatch')
for row in corpus['articles']:
    source=source_items.get((row.get('doi'),row['title']))
    if source is None or any(row.get(k)!=v for k,v in source.items()):
        errors.append(f'{row["ref"]}: corpus metadata differs from snapshot ledger')
for row in corpus['articles']:
    if row.get('note_sha256'):
        path=ROOT/row['note_path']
        if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest()!=row['note_sha256']:
            errors.append(f'{row["ref"]}: source note changed after snapshot')
catalog=(BASE/'appendices/reference-catalog.md').read_text()
if len(re.findall(r'<a id="r\d{3}"></a>',catalog))!=len(refs):errors.append('reference catalogue does not cover corpus exactly')
coverage=json.loads((BASE/'data/coverage-summary.json').read_text())
if coverage['total_articles']!=len(refs):errors.append('coverage count mismatch')
for p in ('综述合订本.pdf','综述合订本.html'):
    if not (BASE/p).exists():errors.append(f'missing edition {p}')
summary={'status':'passed' if not errors else 'failed','articles':len(refs),
         'ledger_validation':ledger_validation,
         'chapter_statistics':counts,'errors':errors,
         'scope':'reference IDs, local paths, corpus hash, material coverage and derived edition presence; not scientific validation'}
(BASE/'data/validation.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
