"""Arithmetic check of the printed Eq.(25); does not recalculate CEFT cross sections/rates.

Source: Nazari et al., 10.1038/s41598-026-78629-5, Article in Press,
PDF pages 7-8 (Eq.25 and Table1), downloaded 2026-11-03.
Run from any directory: python /absolute/path/to/this/file.py
"""
import json
import math
from pathlib import Path


def printed_eq25(t9):
    return (
        15.700 * t9 ** (-2 / 3) * math.exp(-7.416 * t9 ** (-1 / 3))
        * (1 - 0.682 * t9 ** (1 / 3) + 7.942 * t9 ** (2 / 3)
           - 11.226 * t9 + 12.203 * t9 ** (4 / 3) - 1.817 * t9 ** (5 / 3))
        + 43.317 * t9 ** (-3 / 2) * math.exp(-7.828 / t9)
    )


if __name__ == '__main__':
    table_samples = [(0.002, 2.544e-23), (0.1, 1.278e-5), (1.0, 4.392e-2), (10.0, 7.279)]
    results = {
        'scope': 'four printed Table1 points; no CEFT integral, fit, or author code rerun',
        'units': 'cm^3 s^-1 mol^-1',
        'equation_source': 'Nazari et al., Article in Press, PDF p7 Eq25',
        'reference_source': 'same PDF p8 Table1',
        'paper_claimed_fit_max_relative_deviation_percent': 1.29,
        'rows': [
            {'T9': t9, 'printed_eq25': printed_eq25(t9), 'table1': value,
             'relative_difference_percent': 100 * (printed_eq25(t9) / value - 1)}
            for t9, value in table_samples
        ],
        'interpretation': 'Printed equation and table disagree at these samples; unresolved coefficient/typesetting/normalization issue. No corrected formula inferred.'
    }
    output = Path(__file__).with_name('printed-rate-fit-check.json')
    output.write_text(json.dumps(results, indent=2) + '\n')
    print(json.dumps(results, indent=2))
