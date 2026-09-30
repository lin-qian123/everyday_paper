#!/usr/bin/env python
"""Build the derived reading editions. Chapter Markdown remains authoritative."""
import json
import re
import subprocess
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
TMP = BASE / '.build'
TMP.mkdir(exist_ok=True)
rows = json.loads((BASE / 'data/corpus.json').read_text())['articles']
parts = [
    '# 关于本合订本', '',
    '本版截止2026-09-30，以仓库393条文献为范围，其中365条的仓库发表日期为2026年。全库目录覆盖与重点论文讲解分别记录；不是393篇全文精读，也不是全球穷尽检索。', '',
    '正文包括共同基础、九个主题和跨方向学习路线。每章引用使用统一R编号，末尾附全库精简书目。完整路径、逐条覆盖矩阵、阅读缺口与来源核查在 reviews/2026-frontiers/ 的Markdown及data目录。', '',
    '基础推导为教学整理；实验、反演、作者模拟与条件化理论保留各自边界。本版没有重跑相关物理代码、模型训练或绝对标定。部分早期笔记存在模板公式/参数/日期差异，新综述以重点原文核查为准。', '',
]
for p in sorted((BASE / 'chapters').glob('*.md')):
    t = p.read_text()
    t = re.sub(r'\(\.\./appendices/reference-catalog\.md#(r\d{3})\)', r'(#\1)', t)
    t = t.replace('(../figures/', '(figures/')
    # Move source links from chapters/ to the book's root directory.
    t = t.replace('../../../daily/', '../../daily/').replace('../../../yearly/', '../../yearly/')
    t = t.replace('(../chapters/', '(chapters/').replace('(../appendices/', '(appendices/')
    t = re.sub(r'\]\((\d{2}-[^)]+\.md)\)', r'](chapters/\1)', t)
    t = t.replace('\\[\n', '$$\n').replace('\n\\]', '\n$$')
    t = t.replace('\\(', '$').replace('\\)', '$')
    parts += ['', r'\newpage', '', t, '']
parts += [r'\newpage', '', '# 附录 · 全库精简书目', '',
          '以下元数据沿用此版仓库快照。预印本、正式文章、作者稿等状态按来源记录保留；不把可用路径当作逐篇精读证明。完整中文笔记与全文链接见分章版 reference-catalog.md。', '']
for r in rows:
    parts += [f'### {r["ref"]} · {r["title"]} {{#{r["ref"].lower()}}}', '',
              f'{r["publication_date"]}；{r.get("journal", "未记录")}。  \n'
              f' [原始来源]({r["source_url"]})。标识：{r.get("doi") or "无DOI记录"}。', '']
text = '\n'.join(parts)
book = TMP / 'book.md'
book.write_text(text)
header = TMP / 'header.tex'
header.write_text(r'''\usepackage{xeCJK}
\usepackage{newunicodechar}
\newunicodechar{β}{\ensuremath{\beta}}
\newunicodechar{γ}{\ensuremath{\gamma}}
\newunicodechar{δ}{\ensuremath{\delta}}
\newunicodechar{λ}{\ensuremath{\lambda}}
\newunicodechar{μ}{\ensuremath{\mu}}
\newunicodechar{σ}{\ensuremath{\sigma}}
\newunicodechar{χ}{\ensuremath{\chi}}
\newunicodechar{⁻}{\ensuremath{{}^{-}}}
\newunicodechar{₀}{\ensuremath{{}_0}}
\newunicodechar{₂}{\ensuremath{{}_2}}
\renewcommand{\textendash}{-}
\renewcommand{\textemdash}{-}
\renewcommand{\figurename}{图}
\setCJKmainfont[Path=/System/Library/Fonts/Supplemental/,FontIndex=6,BoldFont=Songti.ttc,BoldFeatures={FontIndex=1}]{Songti.ttc}
\setCJKsansfont[Path=/System/Library/Fonts/]{STHeiti Medium.ttc}
\setCJKmonofont[Path=/System/Library/Fonts/]{STHeiti Medium.ttc}
\usepackage{fvextra}
\DefineVerbatimEnvironment{Highlighting}{Verbatim}{breaklines,commandchars=\\\{\}}
\setlength{\emergencystretch}{3em}
\setcounter{secnumdepth}{0}
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small 2026 等离子体与强激光研究综述}
\fancyfoot[C]{\thepage}
\setlength{\headheight}{15pt}
''')
css = TMP / 'style.css'
css.write_text('''body{max-width:1000px;margin:auto;padding:2rem;color:#193441;font-family:system-ui,"Songti SC",serif;line-height:1.8}h1,h2,h3{line-height:1.4;color:#123e55}h1{margin-top:3rem;border-bottom:2px solid #c5dbe4;padding-bottom:.6rem}a{color:#056990}table{border-collapse:collapse;display:block;overflow-x:auto;font-size:.92rem}th,td{padding:.5rem .7rem;border:1px solid #b8cbd2}thead{background:#e8f1f5}img{max-width:100%;height:auto}blockquote{border-left:4px solid #8aafc0;margin-left:0;padding-left:1rem}code{background:#f2f3f3}#TOC{background:#f3f7f8;padding:1rem}''')
common = ['pandoc', str(book), '--from=markdown+tex_math_dollars+raw_html-smart', '--standalone', '--toc', '--toc-depth=2',
          '--metadata=title:2026 等离子体与强激光研究：分类综述', '--metadata=date:截至 2026-09-30', '--metadata=toc-title:目录',
          '--resource-path='+str(BASE)]
html = BASE / '综述合订本.html'
subprocess.run(common+['--mathjax=https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js', '--css='+str(css), '-o', str(html)],check=True,cwd=BASE)
# Inline the CSS to keep the HTML styling self contained.
h=html.read_text()
h=re.sub(r'<link rel="stylesheet" href="[^"]*style\.css"\s*/?>', '<style>'+css.read_text()+'</style>', h)
html.write_text(h)
pdf_text = text.replace('figures/research-map.svg', 'figures/research-map.pdf').replace('figures/evidence-chain.svg','figures/evidence-chain.pdf')
pdf_text = pdf_text.replace('–','-').replace('—','-').replace('‑','-')
pdf_text = re.sub(r'!\[图\d+[：:]\s*', '![', pdf_text)
pdf_text = re.sub(r'(?<=R\d{3})/(?=R\d{3})', '/ ', pdf_text)
for i in range(16):
    pdf_text=pdf_text.replace(chr(0x2460+i), f'({i+1})')
(TMP / 'book-pdf.md').write_text(pdf_text)
pdf_cmd=common.copy()
pdf_cmd[1]=str(TMP/'book-pdf.md')
pdf_cmd += ['--pdf-engine=xelatex', '--include-in-header='+str(header),
    '--variable=mainfont:lmroman10-regular.otf','--variable=monofont:lmmono10-regular.otf',
    '--variable=mainfontoptions:BoldFont=lmroman10-bold.otf,ItalicFont=lmroman10-italic.otf,BoldItalicFont=lmroman10-bolditalic.otf',
    '--variable=fontsize:10pt','--variable=geometry:margin=22mm', '--variable=colorlinks:true',
    '--variable=linkcolor:blue', '--variable=urlcolor:blue', '-o', str(BASE/'综述合订本.pdf')]
proc=subprocess.run(pdf_cmd,cwd=BASE,text=True,capture_output=True)
(BASE/'data/build-log.txt').write_text(proc.stdout+proc.stderr)
if proc.returncode:
    print(proc.stderr[-7000:])
    raise SystemExit(proc.returncode)
print('Built HTML and PDF. See data/build-log.txt for diagnostics.')
