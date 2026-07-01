#!/usr/bin/env python
"""Build browseable paper and category indexes from processed_articles.json."""

from __future__ import annotations

import json
import os
import re
from collections import defaultdict
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STATE_PATH = ROOT / "state" / "processed_articles.json"
PAPERS_DIR = ROOT / "papers"
CATEGORIES_DIR = ROOT / "categories"


CATEGORIES = [
    {
        "slug": "laser-plasma-acceleration",
        "title": "激光等离子体与束流加速",
        "description": "LWFA、PWFA、wakefield、电子束品质、注入、去相位、波导与高梯度加速。",
        "keywords": [
            "lwfa",
            "wakefield",
            "plasma wake",
            "laser wakefield",
            "plasma-wakefield",
            "accelerator",
            "acceleration",
            "electron beam",
            "dephasing",
            "waveguide",
            "beam-driven",
        ],
    },
    {
        "slug": "laser-accelerated-beam-applications",
        "title": "激光加速电子/离子束应用",
        "description": "转换靶韧致辐射、伽马源、光核反应、中子/同位素产生、辐照、诊疗、材料与核诊断应用。",
        "keywords": [
            "bremsstrahlung",
            "converter",
            "gamma",
            "photonuclear",
            "photoneutron",
            "neutron",
            "isotope",
            "proton",
            "stopping power",
            "energy deposition",
            "ion acceleration",
            "ion beam",
            "radiotherapy",
            "irradiation",
            "nuclear reaction",
            "nuclear diagnostic",
            "target normal sheath",
            "tnsa",
        ],
    },
    {
        "slug": "strong-field-qed-radiation",
        "title": "强场 QED 与辐射反作用",
        "description": "强场量子效应、辐射反作用、非线性 Compton、pair production 与极端场实验。",
        "keywords": [
            "qed",
            "radiation reaction",
            "strong field",
            "strong-field",
            "pair production",
            "compton",
            "nonlinear",
            "quantum",
            "gamma ray",
            "positron",
        ],
    },
    {
        "slug": "hedp-icf-laboratory-astrophysics",
        "title": "高能量密度物理、ICF 与实验室天体",
        "description": "HEDP、惯性约束聚变、冲击、辐射输运、等离子体不稳定性与实验室天体物理。",
        "keywords": [
            "high-energy-density",
            "high energy density",
            "hedp",
            "icf",
            "inertial confinement",
            "shock",
            "hohlraum",
            "implosion",
            "fusion",
            "laboratory astrophysics",
            "magnetized plasma",
            "rayleigh",
            "srs",
            "sbs",
        ],
    },
    {
        "slug": "pic-and-plasma-simulation",
        "title": "PIC、动理学与数值模拟",
        "description": "PIC 算法、动理学求解、能量守恒格式、谱方法、数值稳定性与多物理耦合。",
        "keywords": [
            "pic",
            "particle-in-cell",
            "particle in cell",
            "kinetic",
            "simulation",
            "numerical",
            "spectral",
            "solver",
            "vlasov",
            "fokker",
            "finite difference",
            "monte carlo",
        ],
    },
    {
        "slug": "ai-ml-plasma-physics",
        "title": "机器学习与等离子体物理",
        "description": "代理模型、Bayesian optimization、神经算子、数据驱动诊断与物理约束机器学习。",
        "keywords": [
            "machine learning",
            "deep learning",
            "neural",
            "bayesian",
            "bayesian optimization",
            "surrogate",
            "operator",
            "fno",
            "data-driven",
            "data informed",
            "reduced",
            "dimensionality",
            "artificial intelligence",
        ],
    },
    {
        "slug": "magnetic-fusion-and-alpha-particles",
        "title": "磁约束聚变与 alpha 粒子",
        "description": "stellarator、tokamak、runaway electron、alpha-particle confinement 与聚变装置优化。",
        "keywords": [
            "stellarator",
            "tokamak",
            "alpha-particle",
            "alpha particle",
            "neutral beam",
            "fusion reaction",
            "runaway electron",
            "magnetic confinement",
            "confinement",
            "gyrokinetic",
        ],
    },
    {
        "slug": "experimental-platforms-diagnostics",
        "title": "实验平台、靶设计与诊断",
        "description": "高功率激光平台、靶设计、光学元件、诊断、重复频率、束线与实验工程问题。",
        "keywords": [
            "diagnostic",
            "target",
            "microlens",
            "laser facility",
            "beamline",
            "pulse train",
            "optics",
            "plasma mirror",
            "experiment",
            "experimental",
            "shot",
            "repetition",
        ],
    },
]


FALLBACK_CATEGORY = {
    "slug": "general-plasma-and-methods",
    "title": "综合等离子体与交叉方法",
    "description": "未被关键词强匹配到单一主题、但仍属于本仓库关注范围的论文。",
    "keywords": [],
}


def slugify(text: str, fallback: str) -> str:
    text = text.lower()
    text = re.sub(r"10\.48550/arxiv\.", "arxiv-", text)
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text[:96] or fallback


def read_note_text(item: dict) -> str:
    note_path = item.get("note_path")
    if not note_path:
        return ""
    path = ROOT / note_path
    if not path.exists():
        return ""
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def item_corpus(item: dict) -> str:
    pieces = [
        item.get("title") or "",
        item.get("normalized_title") or "",
        item.get("journal") or "",
        item.get("doi") or "",
        item.get("source_url") or "",
    ]
    note_text = read_note_text(item)
    for line in note_text.splitlines():
        if "主题关键词" in line or "与当前研究方向" in line or "相关性评分" in line:
            pieces.append(line)
    return "\n".join(pieces).lower()


def classify(item: dict) -> list[str]:
    corpus = item_corpus(item)
    matched = []
    for category in CATEGORIES:
        if any(keyword in corpus for keyword in category["keywords"]):
            matched.append(category["slug"])
    return matched or [FALLBACK_CATEGORY["slug"]]


def rel(path: str | None, from_dir: Path) -> str | None:
    if not path:
        return None
    target = ROOT / path
    return Path(os.path.relpath(target, start=from_dir))


def doi_url(doi: str | None) -> str | None:
    if not doi:
        return None
    if doi.startswith("http://") or doi.startswith("https://"):
        return doi
    return f"https://doi.org/{doi}"


def md_link(label: str, url: str | None) -> str:
    if not url:
        return label
    return f"[{label}]({url})"


def load_items() -> list[dict]:
    items = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    for index, item in enumerate(items, start=1):
        base = item.get("doi") or item.get("title") or f"paper-{index}"
        item["_paper_slug"] = slugify(base, f"paper-{index}")
        item["_categories"] = classify(item)
    seen = {}
    for item in items:
        slug = item["_paper_slug"]
        if slug in seen:
            seen[slug] += 1
            item["_paper_slug"] = f"{slug}-{seen[slug]}"
        else:
            seen[slug] = 1
    return items


def all_categories() -> list[dict]:
    return CATEGORIES + [FALLBACK_CATEGORY]


def write_paper_pages(items: list[dict], category_by_slug: dict[str, dict]) -> None:
    PAPERS_DIR.mkdir(exist_ok=True)
    for item in items:
        paper_dir = PAPERS_DIR / item["_paper_slug"]
        paper_dir.mkdir(parents=True, exist_ok=True)
        note = rel(item.get("note_path"), paper_dir)
        pdf = rel(item.get("pdf_path"), paper_dir)
        categories = ", ".join(
            f"[{category_by_slug[slug]['title']}](../../categories/{slug}.md)"
            for slug in item["_categories"]
        )
        source = item.get("source_url")
        doi = doi_url(item.get("doi"))
        lines = [
            f"# {item.get('title') or 'Untitled paper'}",
            "",
            "## 基本信息",
            "",
            f"- 分类：{categories}",
            f"- 期刊/平台：{item.get('journal') or '未记录'}",
            f"- 发表日期：{item.get('publication_date') or '未记录'}",
            f"- 入库日期：{item.get('processed_date') or '未记录'}",
            f"- DOI：{md_link(item.get('doi') or '未记录', doi)}",
            f"- 来源：{md_link(source or '未记录', source)}",
            f"- 中文笔记：{md_link('打开笔记', str(note)) if note else '未生成'}",
            f"- 本地 PDF：{md_link('本地路径', str(pdf)) if pdf else '未补回或未跟踪'}",
            "",
            "## 索引说明",
            "",
            "本页由 `scripts/build_indexes.py` 根据 `state/processed_articles.json` 自动生成；正文解读以中文笔记为准。",
            "",
        ]
        (paper_dir / "README.md").write_text("\n".join(lines), encoding="utf-8")


def write_category_pages(items: list[dict], category_by_slug: dict[str, dict]) -> None:
    CATEGORIES_DIR.mkdir(exist_ok=True)
    grouped = defaultdict(list)
    for item in items:
        for slug in item["_categories"]:
            grouped[slug].append(item)

    overview_lines = [
        "# 分类索引",
        "",
        "这些索引由 `scripts/build_indexes.py` 根据已入库论文自动生成；一篇论文可以出现在多个分类中。",
        "",
        "| 分类 | 篇数 | 说明 |",
        "| --- | ---: | --- |",
    ]
    for category in all_categories():
        slug = category["slug"]
        overview_lines.append(
            f"| [{category['title']}](./{slug}.md) | {len(grouped[slug])} | {category['description']} |"
        )
    overview_lines.append("")
    (CATEGORIES_DIR / "README.md").write_text("\n".join(overview_lines), encoding="utf-8")

    for category in all_categories():
        slug = category["slug"]
        rows = sorted(
            grouped[slug],
            key=lambda x: (x.get("processed_date") or "", x.get("publication_date") or ""),
            reverse=True,
        )
        lines = [
            f"# {category['title']}",
            "",
            category["description"],
            "",
            f"- 当前收录：{len(rows)} 篇",
            f"- 索引更新时间：{date.today().isoformat()}",
            "",
            "| 入库日期 | 论文 | 期刊/平台 | 笔记 |",
            "| --- | --- | --- | --- |",
        ]
        for item in rows:
            paper_link = f"../papers/{item['_paper_slug']}/README.md"
            note = item.get("note_path")
            note_link = f"../{note}" if note else None
            lines.append(
                "| {date} | {paper} | {journal} | {note} |".format(
                    date=item.get("processed_date") or "",
                    paper=md_link(item.get("title") or "Untitled", paper_link),
                    journal=item.get("journal") or "",
                    note=md_link("笔记", note_link) if note_link else "未生成",
                )
            )
        lines.append("")
        (CATEGORIES_DIR / f"{slug}.md").write_text("\n".join(lines), encoding="utf-8")


def write_papers_index(items: list[dict]) -> None:
    PAPERS_DIR.mkdir(exist_ok=True)
    rows = sorted(
        items,
        key=lambda x: (x.get("processed_date") or "", x.get("publication_date") or ""),
        reverse=True,
    )
    lines = [
        "# 论文总索引",
        "",
        f"- 当前入库论文：{len(items)} 篇",
        f"- 索引更新时间：{date.today().isoformat()}",
        "",
        "| 入库日期 | 论文 | 期刊/平台 | DOI |",
        "| --- | --- | --- | --- |",
    ]
    for item in rows:
        doi = item.get("doi")
        lines.append(
            "| {date} | {paper} | {journal} | {doi} |".format(
                date=item.get("processed_date") or "",
                paper=md_link(item.get("title") or "Untitled", f"./{item['_paper_slug']}/README.md"),
                journal=item.get("journal") or "",
                doi=md_link(doi or "", doi_url(doi)) if doi else "",
            )
        )
    lines.append("")
    (PAPERS_DIR / "README.md").write_text("\n".join(lines), encoding="utf-8")


def write_daily_index() -> None:
    daily_dir = ROOT / "daily"
    days = sorted([p for p in daily_dir.iterdir() if p.is_dir()], reverse=True)
    lines = [
        "# 每日论文索引",
        "",
        "每日目录保存当日新增论文、下载报告、中文笔记和运行结果。",
        "",
        "| 日期 | 当日索引 | 运行结果 |",
        "| --- | --- | --- |",
    ]
    for day in days:
        index = day / "index.md"
        run_results = day / "run_results.json"
        lines.append(
            f"| {day.name} | {md_link('index.md', f'./{day.name}/index.md') if index.exists() else ''} | "
            f"{md_link('run_results.json', f'./{day.name}/run_results.json') if run_results.exists() else ''} |"
        )
    lines.append("")
    (daily_dir / "README.md").write_text("\n".join(lines), encoding="utf-8")


def write_root_index(items: list[dict], category_by_slug: dict[str, dict]) -> None:
    grouped = defaultdict(list)
    for item in items:
        for slug in item["_categories"]:
            grouped[slug].append(item)
    latest = sorted(
        items,
        key=lambda x: (x.get("processed_date") or "", x.get("publication_date") or ""),
        reverse=True,
    )[:12]
    lines = [
        "# everyday_paper 索引",
        "",
        "激光等离子体、强场 QED、高能量密度物理、PIC、机器学习等方向的每日论文索引。",
        "",
        "## 索引文件",
        "",
        "- [分类索引](./categories/README.md)",
        "- [论文总索引](./papers/README.md)",
        "- [每日索引](./daily/README.md)",
        "- [年度回填](./yearly/index.md)",
        "- [项目 README](./README.md)",
        "- [开发记录 TODO](./TODO.md)",
        "",
        "## 分类概览",
        "",
        "| 分类 | 篇数 | 说明 |",
        "| --- | ---: | --- |",
    ]
    for category in all_categories():
        slug = category["slug"]
        lines.append(
            f"| [{category['title']}](./categories/{slug}.md) | {len(grouped[slug])} | {category['description']} |"
        )
    lines.extend(["", "## 最新入库", "", "| 入库日期 | 论文 | 分类 |", "| --- | --- | --- |"])
    for item in latest:
        cats = "、".join(category_by_slug[slug]["title"] for slug in item["_categories"])
        lines.append(
            f"| {item.get('processed_date') or ''} | "
            f"{md_link(item.get('title') or 'Untitled', f'./papers/{item['_paper_slug']}/README.md')} | {cats} |"
        )
    lines.append("")
    lines.append(f"_自动生成时间：{date.today().isoformat()}_")
    lines.append("")
    (ROOT / "INDEX.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    items = load_items()
    category_by_slug = {category["slug"]: category for category in all_categories()}
    write_paper_pages(items, category_by_slug)
    write_category_pages(items, category_by_slug)
    write_papers_index(items)
    write_daily_index()
    write_root_index(items, category_by_slug)
    print(f"Indexed {len(items)} papers across {len(all_categories())} categories.")


if __name__ == "__main__":
    main()
