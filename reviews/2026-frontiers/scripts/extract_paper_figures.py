#!/usr/bin/env python
"""Render selected original PDF figure regions without changing plotted data.

This is figure extraction, not whole-paper text conversion. Coordinates are PDF
points measured from the top-left of the selected source page, numbered from 1.
Each asset receives a provenance sidecar; visual review must be recorded by the
editor after inspecting the rendered crop and its surrounding source caption.
"""
import hashlib
import json
import re
from pathlib import Path

import pymupdf as fitz

BASE = Path(__file__).resolve().parents[1]
ROOT = BASE.parents[1]
CORPUS = {r['ref']: r for r in json.loads((BASE/'data/corpus.json').read_text())['articles']}


def extract_figure(ref, figure, page, box, chapter, *, title, caption_summary,
                   evidence_type, role, dpi=250):
    """Write a faithful PNG crop and editable source/selection metadata."""
    row = CORPUS[ref]
    source = ROOT/row['pdf_path']
    if source.read_bytes()[:5] != b'%PDF-':
        raise ValueError(f'{ref}: invalid PDF header')
    doc = fitz.open(source)
    src_page = doc[page-1]
    clip = fitz.Rect(box) if box is not None else src_page.rect
    if clip.is_empty or not src_page.rect.contains(clip):
        raise ValueError(f'{ref}: crop outside source page')
    slug = re.sub(r'[^a-z0-9-]+', '-', figure.lower()).strip('-')
    asset_id = f'ch{chapter}-{ref.lower()}-{slug}'
    output = BASE/f'figures/papers/ch{chapter}/{ref.lower()}-{slug}.png'
    output.parent.mkdir(parents=True, exist_ok=True)
    pix = src_page.get_pixmap(dpi=dpi, clip=clip, alpha=False)
    pix.save(output)
    record = {
        'asset_id': asset_id, 'kind': 'paper_figure_excerpt', 'chapter': chapter,
        'ref': ref, 'source_title': row['title'], 'source_url': row['source_url'],
        'source_pdf': row['pdf_path'], 'source_pdf_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
        'original_figure': figure, 'source_page_1_based': page,
        'crop_box_pdf_points': list(clip), 'dpi': dpi,
        'asset_path': output.relative_to(BASE).as_posix(),
        'pixel_width': pix.width, 'pixel_height': pix.height,
        'asset_sha256': hashlib.sha256(output.read_bytes()).hexdigest(),
        'title': title, 'source_caption_summary': caption_summary,
        'evidence_type': evidence_type, 'purpose_in_review': role,
        'processing': 'PDF region rendered to PNG; no data recoloring, relabeling or curve modification.',
        'source_caption_and_visual_checked': False,
        'checked_date': None,
    }
    dest = BASE/f'data/figure-assets/{asset_id}.json'
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n')
    doc.close()
    return record


def mark_visual_checked(asset_id, *, notes, date='2026-10-01'):
    """Call only after inspecting the original page and the final cropped image."""
    dest = BASE/f'data/figure-assets/{asset_id}.json'
    record = json.loads(dest.read_text())
    record.update(source_caption_and_visual_checked=True, checked_date=date,
                  visual_check_notes=notes)
    dest.write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n')
