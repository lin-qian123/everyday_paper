#!/usr/bin/env python
"""Join per-figure provenance in chapter reading order and audit local assets."""
import hashlib
import json
import subprocess
from collections import Counter
from pathlib import Path

from PIL import Image

BASE=Path(__file__).resolve().parents[1]
ROOT=BASE.parents[1]


def images(node):
    if isinstance(node,dict):
        if node.get('t')=='Image':yield node['c'][2][0]
        for v in node.values():yield from images(v)
    elif isinstance(node,list):
        for v in node:yield from images(v)


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()


records=[json.loads(p.read_text()) for p in sorted((BASE/'data/figure-assets').glob('*.json'))]
records+=json.loads((BASE/'data/teaching-figures.json').read_text())
for name,title in [('research-map','研究链与专题关系'),('evidence-chain','观测与反演的证据链')]:
    records.append({'asset_id':name,'kind':'original_teaching_illustration','chapter':'00',
        'title':title,'asset_path':f'figures/{name}.svg','vector_pdf':f'figures/{name}.pdf',
        'script':'scripts/build_figures.py','asset_sha256':sha(BASE/f'figures/{name}.svg'),
        'source_caption_and_visual_checked':True,'checked_date':'2026-10-01',
        'assumptions':'Conceptual research/evidence relationships only; not data or proof that all routes have been experimentally realized.'})
by_path={r['asset_path']:r for r in records}
errors=[];used=[];chapter_counts=Counter();chapter_refs={}
for p in sorted((BASE/'chapters').glob('*.md')):
    ast=json.loads(subprocess.check_output(['pandoc',str(p),'--from=markdown+tex_math_dollars','-t','json']))
    for target in images(ast):
        asset=(p.parent/target).resolve().relative_to(BASE).as_posix()
        if asset not in by_path:
            errors.append(f'Unrecorded image: {asset}');continue
        r=dict(by_path[asset]);r['review_figure_number']=len(used)+1
        r['usage_chapter']=p.relative_to(BASE).as_posix()
        used.append(r);chapter_counts[p.name]+=1
        if r['kind']=='paper_figure_excerpt':chapter_refs.setdefault(p.name,set()).add(r['ref'])
        img=BASE/asset
        if not img.exists():errors.append(f'Missing image: {asset}');continue
        if sha(img)!=r['asset_sha256']:errors.append(f'Changed asset: {asset}')
        if not r.get('source_caption_and_visual_checked'):errors.append(f'Visual review pending: {asset}')
        if r['kind']=='paper_figure_excerpt':
            if sha(ROOT/r['source_pdf'])!=r['source_pdf_sha256']:errors.append(f'Changed source PDF: {r["ref"]}')
            with Image.open(img) as im:
                im.verify()
            with Image.open(img) as im:
                if list(im.size)!=[r['pixel_width'],r['pixel_height']]:errors.append(f'Pixel dimensions changed: {asset}')
                if min(im.size)<180:errors.append(f'Figure too small: {asset}')
missing=set(by_path)-{r['asset_path'] for r in used}
if missing:errors.append('Unused recorded images: '+', '.join(sorted(missing)))
paper=[r for r in used if r['kind']=='paper_figure_excerpt']
summary={'total_figures_in_chapters':len(used),'paper_figure_excerpts':len(paper),
    'unique_paper_sources':len({r['ref'] for r in paper}),
    'original_teaching_illustrations':len(used)-len(paper),
    'images_by_chapter':dict(chapter_counts),
    'paper_sources_by_chapter':{p:len(v) for p,v in chapter_refs.items()},
    'scope':'Selected key figures with local source/caption/crop/visual checks; not exhaustive figure review of all corpus papers.'}
(BASE/'data/figure-manifest.json').write_text(json.dumps({'summary':summary,'figures':used},ensure_ascii=False,indent=2)+'\n')
(BASE/'data/figure-validation.json').write_text(json.dumps({'status':'passed' if not errors else 'failed',
    'checked_date':'2026-10-01','summary':summary,'errors':errors,
    'scope':'Image usage, provenance hashes, pixel decoding, dimensions and recorded visual checks; not independent experimental or numerical reproduction.'},ensure_ascii=False,indent=2)+'\n')

def clean(x):return str(x).replace('|','\\|').replace('\n',' ')

lines=['# 图像导航、出处与复核方法','',
    f'正文共{len(used)}幅图，其中{len(paper)}幅论文原图摘录来自{summary["unique_paper_sources"]}篇论文，另有{len(used)-len(paper)}幅作者绘制的教学图。图在对应内容首次详细讨论处出现；本表仅作出处导航，不替代逐图讲解。合订图序按分章顺序生成，论文原图号单独保留。','',
    '## 论文原图怎么读','',
    '先读原始图号与版本，再辨认装置图、直接信号、反演物理量、模拟或理论曲线。检查所有子图的轴、单位、色标、归一化、误差与对照组，最后判断图能支持哪一步结论。正文逐图给出这一解读；来源侧录保留原PDF路径、页码、裁框、DPI与SHA-256。','',
    '原图仅从本地PDF渲染指定区域，不重画曲线、不重着色、不更改标签；裁框保留所选图的坐标和图例。原文图注与邻近段落用于解释，但图像视觉检查不自动成为对作者数据/代码的独立复现。摘录用于本综述的来源明确的分析讲解；论文图的权利仍属于相应作者或权利人。','',
    '## 教学图怎样与论文结果区分','',
    '教学图明确注明解析模型或自拟示例，公式、假设与重建脚本记录在`data/teaching-figures.json`。没有把教学曲线充当新实验、论文仿真数据或数字化原始曲线。PNG方便屏幕阅读，合订PDF优先使用其矢量版本。','',
    '| 合订图序 | 位置 | 主题与作用 | 来源 / 原图号 | 原PDF页 | 图像 |',
    '| ---: | --- | --- | --- | ---: | --- |']
for r in used:
    chapter=Path(r['usage_chapter']).name
    source=f'[{r["ref"]}](reference-catalog.md#{r["ref"].lower()}) · {r["original_figure"]}' if r['kind']=='paper_figure_excerpt' else '作者教学示意'
    page=r.get('source_page_1_based','—')
    lines.append(f'| {r["review_figure_number"]} | [{chapter[:2]}章](../{r["usage_chapter"]}) | {clean(r["title"])} | {clean(source)} | {page} | [查看原尺寸](../{r["asset_path"]}) |')
lines+=['','## 文件与重建','',
    '`data/figure-manifest.json`汇总当前图像，`data/figure-assets/`记录每幅论文摘图，`data/figure-validation.json`记录检查。`scripts/extract_paper_figures.py`提供可追溯的区域渲染；教学图用`scripts/build_teaching_figures.py`重建。新增或替换图后重新执行`scripts/build_figure_index.py`与`scripts/build_book.py`。','']
(BASE/'appendices/figure-guide.md').write_text('\n'.join(lines))
print(json.dumps({'summary':summary,'errors':errors},ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
