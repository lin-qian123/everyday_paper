#!/usr/bin/env python
"""Draw original explanatory SVGs and PDF equivalents; no paper data reproduced."""
from pathlib import Path
from xml.sax.saxutils import escape
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from matplotlib.font_manager import FontProperties

BASE = Path(__file__).resolve().parents[1]
FONT = FontProperties(fname='/System/Library/Fonts/STHeiti Medium.ttc')
plt.rcParams['svg.fonttype'] = 'none'

def draw(name, title, boxes, arrows, footer):
    fig, ax = plt.subplots(figsize=(12, 6.5))
    ax.set(xlim=(0, 12), ylim=(0, 6.5))
    ax.axis('off')
    fig.patch.set_facecolor('#fcfcfa')
    ax.text(.35, 6.12, title, fontproperties=FONT, fontsize=20, color='#153b50')
    for x, y, w, h, text, color in boxes:
        ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.08',
                     facecolor=color, edgecolor='#83939b', linewidth=.9))
        ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontproperties=FONT,
                fontsize=12,color='#18353f',linespacing=1.8)
    for start, end in arrows:
        ax.annotate('',xy=end,xytext=start,arrowprops={'arrowstyle':'->','color':'#536c76','lw':1.8})
    ax.text(.35,.22,footer,fontproperties=FONT,fontsize=10,color='#59676d')
    svg = BASE / f'figures/{name}.svg'
    fig.savefig(svg,bbox_inches='tight')
    svg.write_text('\n'.join(line.rstrip() for line in svg.read_text().splitlines())+'\n')
    fig.savefig(BASE / f'figures/{name}.pdf',bbox_inches='tight')
    plt.close(fig)

draw('research-map','从驱动到输出：九个主题如何相连',[
    (.4,3.8,2.1,1.25,'激光 / 粒子束\n磁场 / 加热系统','#dcecf2'),
    (3.2,3.8,2.2,1.25,'等离子体动力学\n波、加速、输运','#dcecf2'),
    (6.1,4.45,2.35,.65,'电子束 / 离子束','#edf1df'),
    (6.1,3.3,2.35,.65,'HED / 燃烧 / 约束','#edf1df'),
    (9.1,3.75,2.4,1.35,'光子 / 中子 / 同位素\n光源、成像与聚变','#f6e5d6'),
    (.5,1.4,3.2,1,'PIC / 动理学 / 多物理模型\n守恒、误差与尺度','#e8e5f3'),
    (4.4,1.4,3.2,1,'AI / 代理 / 反演 / 控制\n泛化、延迟与闭环','#e8e5f3'),
    (8.3,1.4,3.2,1,'靶 / 平台 / 实验诊断\n响应、标定与可观测量','#e8e5f3'),
], [((2.55,4.4),(3.1,4.4)),((5.5,4.6),(6,4.8)),((5.5,4.1),(6,3.6)),
    ((8.55,4.8),(9,4.55)),((8.55,3.6),(9,4.0)),
    ((2.1,2.5),(3.7,3.65)),((6,2.5),(6.9,3.15)),((9.9,2.5),(10.2,3.6))],
    '作者绘制的概念图；连接表示研究关系，不代表所有应用路线均已实验实现。')

draw('evidence-chain','从信号到结论：每个环节都有自己的证据边界',[
    (.5,4.35,2.2,.95,'真实物理过程\n粒子、场与材料','#dcecf2'),
    (3.4,4.35,2.3,.95,'仪器记录\n像素、计数、谱与时序','#edf1df'),
    (6.45,4.35,2.3,.95,'响应模型与反演\n标定、先验、本底','#f6e5d6'),
    (9.45,4.35,2.05,.95,'物理参数与结论\n误差与适用条件','#edf1df'),
    (.5,1.7,3.05,1.15,'作者模拟 / 条件化理论\n输入、维度、近似与收敛','#e8e5f3'),
    (4.55,1.7,3.05,1.15,'独立观测与交叉验证\n多诊断、留出数据','#e8e5f3'),
    (8.5,1.7,3.05,1.15,'本综述的综合判断\n趋势、缺口与研究建议','#e8e5f3'),
], [((2.8,4.8),(3.3,4.8)),((5.8,4.8),(6.35,4.8)),((8.85,4.8),(9.35,4.8)),
    ((2,2.95),(4.4,4.2)),((6.1,2.95),(7.5,4.2)),((10,4.2),(10,2.95))],
    '信号可直接记录，物理量常需反演；模拟预测、机制解释与本文建议分别标明。')
print('Built 2 original SVG figures and their PDF equivalents.')
