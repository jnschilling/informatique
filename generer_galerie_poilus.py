"""Génère la page galerie des fiches Poilus à partir des PDF déposés.

Scanne site/static/travaux/poilus/*.pdf (déposés et relus par l'enseignant)
et écrit site/docs/activites/poilus-galerie.md. À relancer après chaque dépôt,
puis commit + push : le site se met à jour tout seul (GitHub Actions).

Convention de nommage des PDF : prenom_nom-du-poilu.pdf
"""

from pathlib import Path

RACINE = Path(__file__).parent
DEPOT = RACINE / "site" / "static" / "travaux" / "poilus"
PAGE = RACINE / "site" / "docs" / "activites" / "poilus-galerie.md"

ENTETE = """---
sidebar_position: 2
title: "Galerie : nos fiches Poilus"
---

# Galerie — nos fiches Poilus 🕊️

Les fiches rédigées par la classe à partir des archives « Mémoire des hommes »,
présentées le 10 novembre. Chaque fiche redonne un nom et une histoire à un
soldat de la Première Guerre mondiale.
"""

VIDE = """
:::info Bientôt !
Les premières fiches arrivent ici très prochainement. 📬
:::
"""


def libelle(pdf: Path) -> tuple[str, str]:
    """`lea_martin-jean.pdf` -> ('Lea', 'Martin Jean')."""
    tige = pdf.stem
    if "_" in tige:
        prenom, poilu = tige.split("_", 1)
    else:
        prenom, poilu = "", tige
    joli = lambda s: s.replace("-", " ").strip().title()  # noqa: E731
    return joli(prenom), joli(poilu)


def principale() -> None:
    pdfs = sorted(p for p in DEPOT.glob("*.pdf"))
    morceaux = [ENTETE]
    if not pdfs:
        morceaux.append(VIDE)
    else:
        morceaux.append(f"\n**{len(pdfs)} fiche(s) publiée(s)** — clique pour ouvrir le PDF.\n")
        morceaux.append("\n| Poilu | Fiche rédigée par | Lire |\n|---|---|---|\n")
        for pdf in pdfs:
            prenom, poilu = libelle(pdf)
            lien = f"/travaux/poilus/{pdf.name}"
            morceaux.append(f"| **{poilu}** | {prenom or '—'} | [📄 ouvrir]({lien}) |\n")
    morceaux.append(
        "\n---\n\n*Fiches publiées avec l'accord des familles — prénoms seuls. "
        "Source des archives : [Mémoire des hommes]"
        "(https://www.memoiredeshommes.sga.defense.gouv.fr).*\n"
    )
    PAGE.write_text("".join(morceaux), encoding="utf-8")
    print(f"Galerie générée : {PAGE} ({len(pdfs)} fiche(s))")


if __name__ == "__main__":
    principale()
