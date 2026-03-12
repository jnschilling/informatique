# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Educational resources for teaching computer science to CM1/CM2 students (cycle 3, ages 9-11) at École Saint-Anne, school year 2025-2026. The project contains:

- **Python scripts** generating interactive Excel worksheets for classroom use (openpyxl)
- **Curriculum documents** (programme.md) aligned with French national education standards (BOEN 2023)
- **Official program extracts** (extraits_cycle3.md) from the cycle 3 curriculum

## Commands

Python scripts use `openpyxl` and generate `.xlsx` files in the project root:

```bash
python generer_chasse.py        # Generates chasse_au_tresor.xlsx (number treasure hunt)
python labyrinthe_mult.py       # Generates labyrinthe_multiplications.xlsx (multiplication maze)
```

No virtual environment or requirements.txt exists. Install dependency with: `pip install openpyxl`

## Architecture

- `generer_chasse.py` — Generates a treasure hunt spreadsheet where students solve arithmetic problems to navigate a grid. Uses Excel formulas (`=5+3`, `=SOMME(...)`) so students see computed results.
- `labyrinthe_mult.py` — Generates a multiplication practice grid with randomized multipliers. Answers are hidden in cell comments (visible on hover). Includes a response row for self-correction.
- `programme.md` — Full yearly curriculum: 3 major projects (TP1: Scratch Christmas cards, TP2: environmental digital journal, TP3: collaborative podcast), weekly progression, evaluation grids.
- `docs/programmes_cycle-3_2023.pdf` — Official French cycle 3 program reference.

## Key Conventions

- Excel formulas use semicolons (`;`) as separators for LibreOffice Calc compatibility (French locale), not commas.
- Content is in French — all user-facing text, comments, and documentation must remain in French.
- Scripts are standalone (no shared modules) and output files directly to the project root.
