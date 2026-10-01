#!/usr/bin/env python
"""Original analytic teaching illustrations, never presented as paper results."""
import hashlib
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Rectangle
import numpy as np

BASE = Path(__file__).resolve().parents[1]
OUT = BASE/'figures/teaching'
OUT.mkdir(parents=True, exist_ok=True)
FONT = '/System/Library/Fonts/STHeiti Medium.ttc'
font_manager.fontManager.addfont(FONT)
plt.rcParams.update({'font.family':font_manager.FontProperties(fname=FONT).get_name(),
    'font.size':13, 'axes.labelsize':13, 'axes.titlesize':14, 'xtick.labelsize':11,
    'ytick.labelsize':11, 'legend.fontsize':11, 'axes.spines.top':False,
    'axes.spines.right':False, 'svg.fonttype':'none', 'mathtext.fontset':'stix',
    'axes.unicode_minus':False, 'savefig.facecolor':'white'})
BLUE='#176c91';PURPLE='#7757a6';ORANGE='#b56819';GRAY='#65717d'
records=[]


def save(fig,name,chapter,title,formula,assumptions):
    fig.text(.5,.01,'教学示意 / 解析模型 · 非论文数据、非独立实验或物理仿真结果',
             ha='center',fontsize=10,color=GRAY)
    fig.tight_layout(rect=(0,.055,1,1))
    fig.savefig(OUT/f'{name}.png',dpi=300)
    fig.savefig(OUT/f'{name}.pdf')
    svg=OUT/f'{name}.svg';fig.savefig(svg)
    svg.write_text('\n'.join(x.rstrip() for x in svg.read_text().splitlines())+'\n')
    plt.close(fig)
    record={'asset_id':f'teaching-{name}','kind':'original_teaching_illustration',
        'chapter':chapter,'title':title,'asset_path':f'figures/teaching/{name}.png',
        'vector_pdf':f'figures/teaching/{name}.pdf','vector_svg':f'figures/teaching/{name}.svg',
        'formula':formula,'assumptions':assumptions,
        'script':'scripts/build_teaching_figures.py',
        'asset_sha256':hashlib.sha256((OUT/f'{name}.png').read_bytes()).hexdigest(),
        'source_caption_and_visual_checked':False,'checked_date':None}
    records.append(record)


# Electron displacement in a finite slab and the oscillator phase relation.
fig,ax=plt.subplots(1,2,figsize=(10.2,4.2))
ax[0].set(xlim=(-.4,5.5),ylim=(0,3.5));ax[0].axis('off')
ax[0].add_patch(Rectangle((.1,1.8),4,.6,facecolor=BLUE,alpha=.15,edgecolor=BLUE))
ax[0].add_patch(Rectangle((.7,.7),4,.6,facecolor=PURPLE,alpha=.15,edgecolor=PURPLE))
for z in np.linspace(.25,3.95,10):ax[0].text(z,2.1,'+',ha='center',va='center',color=BLUE)
for z in np.linspace(.85,4.55,10):ax[0].text(z,1,'−',ha='center',va='center',color=PURPLE)
ax[0].text(.1,2.65,'离子层：短时间内固定',color=BLUE)
ax[0].text(.7,.3,'电子层：整体位移 x',color=PURPLE)
ax[0].annotate('',xy=(.7,1.55),xytext=(.1,1.55),arrowprops={'arrowstyle':'<->','color':GRAY})
ax[0].text(.4,1.6,'x',ha='center',fontsize=11)
ax[0].annotate('恢复力 −eE',xy=(1.5,1.48),xytext=(3.1,1.48),color=PURPLE,
               arrowprops={'arrowstyle':'->','color':PURPLE})
ax[0].text(.15,3.05,'(a) 有限平板的界面电荷分离')
t=np.linspace(0,4*np.pi,600)
ax[1].plot(t/(2*np.pi),np.cos(t),color=BLUE,label=r'$x/A=\cos(\omega_{pe}t)$')
ax[1].plot(t/(2*np.pi),-np.sin(t),'--',color=PURPLE,label=r'$v/(A\omega_{pe})=-\sin(\omega_{pe}t)$')
ax[1].axhline(0,color=GRAY,lw=.8);ax[1].set(xlabel=r'时间 $t/T_{pe}$',ylabel='无量纲位移 / 速度',title='(b) 位移与速度相差四分之一周期')
ax[1].legend(loc='upper right');ax[1].grid(alpha=.15)
save(fig,'plasma-oscillator','00','界面恢复场与电子振荡',
     'x=A*cos(omega_pe*t), v=-A*omega_pe*sin(omega_pe*t)',
     'Finite cold electron/ion slabs, small displacement, fixed ions, no damping. Layer vertical offset only separates drawing labels.')

# Debye screening. The potential normalization is explicit, including 1/r.
s=np.linspace(.2,6,400);fig,ax=plt.subplots(figsize=(8.8,4.2))
ax.semilogy(s,1/s,'--',color=GRAY,label='无屏蔽：1 / (r/λD)')
ax.semilogy(s,np.exp(-s)/s,color=BLUE,label='Debye 屏蔽：exp(−r/λD) / (r/λD)')
ax.axvline(1,color=ORANGE,ls=':',label='r = λD')
ax.set(xlabel=r'归一化距离 $r/\lambda_D$',ylabel=r'$\phi\,/\,[q/(4\pi\epsilon_0\lambda_D)]$',
       title='一个 Debye 长度之后，指数屏蔽迅速增强',ylim=(2e-4,7))
ax.legend();ax.grid(alpha=.18)
save(fig,'debye-screening','00','点电荷的屏蔽势',
     'phi/(q/(4*pi*epsilon0*lambda_D)) = exp(-r/lambda_D)/(r/lambda_D)',
     'Static, weak potential, classical thermal equilibrium, infinite medium; not a dynamic sheath or warm-dense matter model.')

# Cold electromagnetic dispersion and group velocity.
k=np.linspace(0,3,400);fig,ax=plt.subplots(1,2,figsize=(10.2,4.2))
ax[0].plot(k,np.sqrt(1+k*k),color=BLUE,label='等离子体横电磁波')
ax[0].plot(k,k,'--',color=GRAY,label='真空：ω = ck')
ax[0].axhline(1,ls=':',color=ORANGE,label='截止频率 ωpe')
ax[0].set(xlabel=r'$ck/\omega_{pe}$',ylabel=r'$\omega/\omega_{pe}$',title='(a) 传播波有最低频率')
ax[0].legend();ax[0].grid(alpha=.15)
u=np.linspace(0,.995,400)
ax[1].plot(u,np.sqrt(1-u),color=PURPLE)
ax[1].set(xlabel=r'密度比 $n_e/n_c$',ylabel=r'群速度 $v_g/c$',title='(b) 接近临界密度时传播变慢',ylim=(0,1.05))
ax[1].grid(alpha=.15)
save(fig,'cold-dispersion','00','截止频率、临界密度与群速度',
     'omega^2=omega_pe^2+c^2*k^2; v_g/c=sqrt(1-ne/nc)',
     'Cold, collisionless, unmagnetized, linear transverse wave; no relativistic transparency or pulse self-focusing.')

# Compare density scales without confusing field gradient with final energy.
n=np.logspace(16,22,400);wp=5.64e4*np.sqrt(n);lam=2*np.pi*299792458/wp*1e6;E=96*np.sqrt(n/1e18)
fig,ax=plt.subplots(1,2,figsize=(10.2,4.2))
ax[0].loglog(n,lam,color=BLUE);ax[1].loglog(n,E,color=PURPLE)
for a in ax:
    a.axvline(1.74e21,ls=':',color=ORANGE,label='0.8 μm 激光的冷临界密度')
    a.set_xlabel(r'电子密度 $n_e$ ($\mathrm{cm}^{-3}$)');a.grid(alpha=.2)
ax[0].set(ylabel=r'等离子体波长 $\lambda_p$ (μm)',title='(a) 密度越高，电子响应尺度越短')
ax[1].set(ylabel=r'特征场 $E_0$ (GV/m)',title='(b) 场更强不等于终能量更高')
ax[0].scatter([1e18],[lam[np.argmin(abs(n-1e18))]],color=BLUE)
ax[0].text(1.4e18,35,'约 33.4 μm',fontsize=11)
ax[1].scatter([1e18],[96],color=PURPLE);ax[1].text(1.4e18,110,'96 GV/m',fontsize=11)
ax[0].legend(loc='lower left',fontsize=10)
save(fig,'density-scales','00','密度、波长与场强的量级关系',
     'lambda_p=2*pi*c/omega_pe, omega_pe=5.64e4*sqrt(n[cm^-3]); E0=96*sqrt(n/1e18) GV/m',
     'Cold-electron characteristic scales, not obtainable accelerating gradients at every density. Dense matter may need additional physics.')

# Head-on ultra-relativistic electron/laser estimate, deliberately labeled.
I=np.logspace(17,22,300);K=np.logspace(-2,1,240)
aa=.855*.8*np.sqrt(I/1e18);gg=1+K/.000510999
chi=2*gg[:,None]*aa[None,:]*(1.239841984/.8)/510999
fig,ax=plt.subplots(figsize=(8.8,4.6))
cs=ax.contour(I,K,chi,levels=[.001,.01,.1,1],colors=[GRAY,BLUE,PURPLE,ORANGE],linewidths=1.7)
ax.clabel(cs,fmt={.001:'χ = 0.001',.01:'χ = 0.01',.1:'χ = 0.1',1:'χ = 1'},fontsize=11)
ax.axvline(1e18/(.855*.8)**2,color='black',ls='--',label=r'$a_0 = 1$（线偏振峰值强度）')
ax.set(xscale='log',yscale='log',xlabel=r'激光强度 $I$ ($\mathrm{W\,cm}^{-2}$)',
       ylabel='入射电子动能 K (GeV)',title=r'迎头碰撞：相同 $a_0$，不同电子能量可有不同 $\chi_e$')
ax.text(.78*1e18/(.855*.8)**2,.012,r'$a_0=1$',rotation=90,va='bottom',fontsize=11)
ax.grid(alpha=.18)
save(fig,'a0-chi-map','00','经典非线性参数与量子参数的区别',
     'a0=0.855*lambda[um]*sqrt(I/1e18); chi_e≈2*gamma*a0*hbar*omega0/(me*c^2)',
     '0.8 um plane wave, peak linear polarization, ultrarelativistic head-on collision; no focusing, overlap or energy-loss evolution. Contours are analytic estimates, not measured thresholds.')

# Equal geometric emittance, different overlap with a fixed acceptance.
theta=np.linspace(0,2*np.pi,600);rng=np.random.default_rng(20261001)
rad=np.sqrt(rng.uniform(size=4000));ang=rng.uniform(0,2*np.pi,4000)
fig,ax=plt.subplots(1,2,figsize=(10.2,4.3))
for a,(sx,sp),title in zip(ax,[(1,.5),(.25,2)],['(a) 较大束斑、较小发散','(b) 较小束斑、较大发散']):
    xx=sx*rad*np.cos(ang);xp=sp*rad*np.sin(ang)
    good=(abs(xx)<=.6)&(abs(xp)<=.8)
    a.scatter(xx[::5],xp[::5],s=2,color=BLUE,alpha=.28,rasterized=True)
    a.plot(sx*np.cos(theta),sp*np.sin(theta),color=BLUE)
    a.add_patch(Rectangle((-.6,-.8),1.2,1.6,edgecolor=ORANGE,facecolor=ORANGE,alpha=.18,lw=1.7))
    a.set(xlim=(-1.3,1.3),ylim=(-2.3,2.3),xlabel='位置 x (mm)',ylabel="斜率 x′ (mrad)",title=title)
    a.text(-1.18,1.95,f'落在接受区内约 {100*good.mean():.0f}%',fontsize=11)
    a.grid(alpha=.12)
save(fig,'phase-space-acceptance','10','同相空间面积不保证相同有效电荷',
     'Uniform filled ellipses: semi-axes (1 mm,0.5 mrad) and (0.25 mm,2 mrad); acceptance |x|≤0.6 mm, |xprime|≤0.8 mrad.',
     'Synthetic uniform geometric phase-space distribution, fixed energy, no dispersion or space charge. Percentages illustrate geometric overlap only.')

# Two different spectra with equal zeroth and first moments.
en=np.linspace(0,10,2000);integ=getattr(np,'trapezoid',np.trapz)
f1=np.exp(-(en-5)**2/(2*1.6**2));f2=np.exp(-(en-2.3)**2/(2*.45**2))+np.exp(-(en-7.7)**2/(2*.45**2))
f1/=integ(f1,en);f2/=integ(f2,en)
fig,ax=plt.subplots(1,2,figsize=(10.2,4.3))
ax[0].plot(en,f1,color=BLUE,label='宽单峰谱');ax[0].plot(en,f2,'--',color=PURPLE,label='窄双峰谱')
ax[0].set(xlabel='能量 E (MeV)',ylabel=r'归一化谱 $f(E)$ ($\mathrm{MeV}^{-1}$)',title='(a) 两个明显不同的物理分布')
ax[0].legend();ax[0].grid(alpha=.15)
pos=np.array([0,1]);vals1=[integ(f1,en),integ(en*f1,en)/5];vals2=[integ(f2,en),integ(en*f2,en)/5]
ax[1].bar(pos-.15,vals1,width=.3,color=BLUE,label='宽单峰谱');ax[1].bar(pos+.15,vals2,width=.3,color=PURPLE,hatch='//',label='窄双峰谱')
ax[1].set(xticks=pos,xticklabels=['粒子总数通道','能量加权通道 / 5 MeV'],ylabel='归一化理想读数',ylim=(0,1.28),title='(b) 少量投影不能唯一反演谱形')
ax[1].legend(fontsize=10)
save(fig,'inverse-ambiguity','10','响应模型中的非唯一性',
     'Integral f(E)dE=1 and Integral E*f(E)dE=5 MeV for both symmetric normalized spectra.',
     'Constructed spectra and idealized moment channels; not any actual detector response or fitted paper spectrum. Extra spectral channels may distinguish them.')

# A scalar recurrence explains why one-step error is insufficient.
fig,ax=plt.subplots(figsize=(8.8,4.1));steps=np.arange(1,61)
for L,co,ls in [(.8,BLUE,'-'),(1.,GRAY,'--'),(1.08,PURPLE,'-.')]:
    err=0.;seq=[]
    for _ in steps:err=L*err+1e-4;seq.append(err)
    ax.semilogy(steps,seq,color=co,ls=ls,label=f'L = {L:g}')
ax.set(xlabel='推进步数 n',ylabel=r'累积误差 $e_n$（无量纲）',title='每步同样的小误差，长期结果可以完全不同')
ax.legend(title='放大因子');ax.grid(alpha=.18)
save(fig,'rollout-error','10','局部误差与滚动误差',
     'e_(n+1)=L*e_n+delta, delta=1e-4, e_0=0, L=0.8/1/1.08.',
     'Exact scalar teaching recurrence with same-sign fixed local error; real nonlinear Jacobians are multidimensional and time dependent.')

(BASE/'data/teaching-figures.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print(f'Built {len(records)} analytic teaching figures in PNG/PDF/SVG.')
