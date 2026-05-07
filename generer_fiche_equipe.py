"""
Génère une fiche équipe ODT par équipe pour la séance S2 du TP2.

À remplir EN CLASSE avec l'équipe, puis photocopier en fin de séance
pour que chaque élève reparte avec sa copie pour le travail à la maison.

Usage:
    poetry run python generer_fiche_equipe.py
"""

from odf.opendocument import OpenDocumentText
from odf.style import (
    Style,
    TextProperties,
    ParagraphProperties,
    TableColumnProperties,
    TableCellProperties,
)
from odf.text import P
from odf.table import Table, TableColumn, TableRow, TableCell


# --- Données des équipes ---

EQUIPES = [
    {
        "classe": "CM1",
        "num": 1,
        "theme": "Pollution de la nature",
        "question": "Comment la nature est-elle polluée autour de nous ?",
        "eleves": ["Cylia", "Maïly", "Annaëlle", "Alma"],
        "podcast_recommande": "Radio Bambou (Reporterre) — reportage de terrain",
        "podcast_url": "https://reporterre.net/Radio-Bambou",
        "duree_cible": "2-3 min",
        "mots_script": "~100 mots",
        "gardien_du_temps_S2": "Maïly",
    },
    {
        "classe": "CM1",
        "num": 2,
        "theme": "Pollution de l'air",
        "question": "D'où vient la pollution de l'air ?",
        "eleves": ["Robin", "Martin", "Raphaël"],
        "podcast_recommande": "Allo, 1jour1actu ? — Q&R clair en 5 min",
        "podcast_url": "https://podcast.ausha.co/allo-1jour1actu",
        "duree_cible": "2-3 min",
        "mots_script": "~100 mots",
        "gardien_du_temps_S2": "Robin",
    },
    {
        "classe": "CM1",
        "num": 3,
        "theme": "Faire plus attention aux animaux",
        "question": "Comment mieux protéger les animaux au quotidien ?",
        "eleves": ["Timéo", "Isobel", "Emilie", "Izia"],
        "podcast_recommande": "Bestioles (France Inter / MNHN) — un animal par épisode",
        "podcast_url": "https://www.radiofrance.fr/franceinter/podcasts/bestioles",
        "duree_cible": "2-3 min",
        "mots_script": "~100 mots",
        "gardien_du_temps_S2": "Isobel",
    },
    {
        "classe": "CM2",
        "num": 1,
        "theme": "Comment ne pas gaspiller ?",
        "question": "On gaspille quoi exactement ? Comment changer nos habitudes ?",
        "eleves": ["Kiara", "Olivia", "Faustine", "Maëli", "Scott"],
        "podcast_recommande": "Allo 1jour1actu + Salut l'info ! — actu accessible",
        "podcast_url": "https://podcast.ausha.co/allo-1jour1actu",
        "duree_cible": "3-5 min",
        "mots_script": "~150 mots",
        "gardien_du_temps_S2": "Olivia",
    },
    {
        "classe": "CM2",
        "num": 2,
        "theme": "Comment comprendre mieux l'écologie à l'école",
        "question": "Est-ce qu'on apprend assez sur l'écologie à l'école ?",
        "eleves": ["Ryan", "Oscar", "Gwenolé", "Léon", "Costa"],
        "podcast_recommande": "Curieux de sciences (MNHN) — co-conçu avec une classe CM2 !",
        "podcast_url": "https://www.mnhn.fr/fr/curieux-de-sciences",
        "duree_cible": "3-5 min",
        "mots_script": "~150 mots",
        "gardien_du_temps_S2": "Oscar",
    },
]


def creer_styles(doc):
    """Crée les styles du document."""
    s = Style(name="Titre", family="paragraph")
    s.addElement(TextProperties(fontsize="20pt", fontweight="bold", color="#1565c0"))
    s.addElement(ParagraphProperties(marginbottom="0.3cm", textalign="center"))
    doc.styles.addElement(s)

    s = Style(name="SousTitre", family="paragraph")
    s.addElement(TextProperties(fontsize="13pt", fontstyle="italic", color="#555555"))
    s.addElement(ParagraphProperties(marginbottom="0.6cm", textalign="center"))
    doc.styles.addElement(s)

    s = Style(name="Section", family="paragraph")
    s.addElement(TextProperties(fontsize="14pt", fontweight="bold", color="#2e7d32"))
    s.addElement(ParagraphProperties(margintop="0.6cm", marginbottom="0.2cm"))
    doc.styles.addElement(s)

    s = Style(name="SectionDevoirs", family="paragraph")
    s.addElement(TextProperties(fontsize="14pt", fontweight="bold", color="#c62828"))
    s.addElement(ParagraphProperties(margintop="0.8cm", marginbottom="0.2cm"))
    doc.styles.addElement(s)

    s = Style(name="Normal", family="paragraph")
    s.addElement(TextProperties(fontsize="11pt"))
    s.addElement(ParagraphProperties(marginbottom="0.2cm"))
    doc.styles.addElement(s)

    s = Style(name="Italic", family="paragraph")
    s.addElement(TextProperties(fontsize="10pt", fontstyle="italic", color="#666666"))
    s.addElement(ParagraphProperties(marginbottom="0.2cm"))
    doc.styles.addElement(s)

    s = Style(name="Ligne", family="paragraph")
    s.addElement(TextProperties(fontsize="11pt"))
    s.addElement(
        ParagraphProperties(
            marginbottom="0.5cm",
            borderbottom="0.5pt solid #cccccc",
            paddingbottom="0.3cm",
        )
    )
    doc.styles.addElement(s)

    # Table styles
    s = Style(name="EnTete", family="table-cell")
    s.addElement(
        TableCellProperties(
            backgroundcolor="#1565c0",
            padding="0.15cm",
            border="0.05pt solid #000000",
        )
    )
    doc.automaticstyles.addElement(s)

    s = Style(name="EnTeteTexte", family="paragraph")
    s.addElement(TextProperties(fontsize="10pt", fontweight="bold", color="#ffffff"))
    s.addElement(ParagraphProperties(textalign="center"))
    doc.automaticstyles.addElement(s)

    s = Style(name="Cellule", family="table-cell")
    s.addElement(
        TableCellProperties(padding="0.2cm", border="0.05pt solid #aaaaaa")
    )
    doc.automaticstyles.addElement(s)

    s = Style(name="CelluleEntete", family="table-cell")
    s.addElement(
        TableCellProperties(
            backgroundcolor="#e3f2fd",
            padding="0.15cm",
            border="0.05pt solid #aaaaaa",
        )
    )
    doc.automaticstyles.addElement(s)

    s = Style(name="ColRole", family="table-column")
    s.addElement(TableColumnProperties(columnwidth="4cm"))
    doc.automaticstyles.addElement(s)

    s = Style(name="ColEleve", family="table-column")
    s.addElement(TableColumnProperties(columnwidth="3cm"))
    doc.automaticstyles.addElement(s)

    s = Style(name="ColLignes", family="table-column")
    s.addElement(TableColumnProperties(columnwidth="13cm"))
    doc.automaticstyles.addElement(s)


def add_text(doc, text, style):
    """Ajoute un paragraphe avec un style donné."""
    doc.text.addElement(P(stylename=style, text=text))


def add_lignes_vides(doc, nombre):
    """Ajoute des lignes vides à remplir à la main."""
    for _ in range(nombre):
        doc.text.addElement(P(stylename="Ligne", text=""))


def section_roles(doc, equipe):
    """Tableau des rôles à remplir."""
    table = Table(name="Roles")
    table.addElement(TableColumn(stylename="ColRole"))
    table.addElement(TableColumn(stylename="ColEleve"))

    # En-tête
    row = TableRow()
    for txt in ["Rôle", "Élève"]:
        cell = TableCell(stylename="EnTete")
        cell.addElement(P(stylename="EnTeteTexte", text=txt))
        row.addElement(cell)
    table.addElement(row)

    # Rôles
    if len(equipe["eleves"]) == 5:
        roles = [
            "Chef de projet",
            "Scénariste",
            "Documentaliste",
            "Technicien son",
            "Visuel",
        ]
    elif len(equipe["eleves"]) == 4:
        roles = [
            "Chef de projet",
            "Scénariste",
            "Documentaliste",
            "Technicien son / Visuel",
        ]
    else:  # 3
        roles = [
            "Chef de projet",
            "Scénariste-Documentaliste",
            "Technicien son / Visuel",
        ]

    for role in roles:
        row = TableRow()
        cell = TableCell(stylename="CelluleEntete")
        cell.addElement(P(text=role))
        row.addElement(cell)
        cell = TableCell(stylename="Cellule")
        cell.addElement(P(text=""))
        row.addElement(cell)
        table.addElement(row)

    doc.text.addElement(table)


def generer_fiche(equipe):
    """Génère la fiche ODT pour une équipe."""
    doc = OpenDocumentText()
    creer_styles(doc)

    # En-tête
    add_text(doc, f"FICHE ÉQUIPE — Podcast Écologie", "Titre")
    add_text(
        doc,
        f"{equipe['classe']} · Équipe {equipe['num']} · {equipe['theme']}",
        "SousTitre",
    )
    add_text(
        doc,
        f"Membres : {', '.join(equipe['eleves'])}",
        "Normal",
    )
    add_text(
        doc,
        f"⏰ Gardien du temps aujourd'hui : {equipe['gardien_du_temps_S2']}",
        "Italic",
    )

    # Notre question
    add_text(doc, "🎯 Notre question centrale", "Section")
    add_text(doc, equipe["question"], "Normal")
    add_text(
        doc,
        "(Reformulez ensemble en 1 phrase claire si vous voulez modifier)",
        "Italic",
    )
    add_lignes_vides(doc, 1)

    # Répartition des rôles
    add_text(doc, "👥 Nos rôles", "Section")
    section_roles(doc, equipe)

    # 3 infos clés à trouver
    add_text(doc, "🔍 3 infos clés à trouver (Documentaliste)", "Section")
    add_text(
        doc, "Cherchez sur Qwant Junior, 1jour1actu, Lumni :", "Italic"
    )
    for i in range(1, 4):
        add_text(doc, f"{i}.", "Ligne")

    # Le chiffre marquant
    add_text(doc, "✨ Notre chiffre marquant pour le « Le saviez-vous ? »", "Section")
    add_lignes_vides(doc, 1)

    # 3 sources
    add_text(doc, "📚 Nos 3 sources (site web + auteur)", "Section")
    for i in range(1, 4):
        add_text(doc, f"{i}.", "Ligne")

    # Script v1
    add_text(doc, f"✏️ Script v1 ({equipe['mots_script']}, durée {equipe['duree_cible']})", "Section")
    add_text(
        doc,
        "Structure : (1) Bonjour... (2) Notre question (3) Ce qu'on a appris (4) Et toi... ?",
        "Italic",
    )
    add_lignes_vides(doc, 8)

    # 1 question Kahoot
    add_text(doc, "❓ Notre 1ère question Kahoot", "Section")
    add_text(doc, "Question :", "Ligne")
    add_text(doc, "Réponse A :", "Ligne")
    add_text(doc, "Réponse B :", "Ligne")
    add_text(doc, "Réponse C :", "Ligne")
    add_text(doc, "Réponse D :", "Ligne")
    add_text(doc, "✓ Bonne réponse : ☐ A   ☐ B   ☐ C   ☐ D", "Normal")

    # Devoirs à la maison (en rouge !)
    add_text(doc, "🏠 DEVOIRS À LA MAISON — Pour chacun !", "SectionDevoirs")
    add_text(
        doc,
        f"☐ 1. Écouter le podcast : {equipe['podcast_recommande']}",
        "Normal",
    )
    add_text(doc, f"     {equipe['podcast_url']}", "Italic")
    add_text(
        doc,
        "☐ 2. Note 3 choses qui t'ont plu (la voix, un bruitage, une info...) :",
        "Normal",
    )
    add_lignes_vides(doc, 3)
    add_text(
        doc,
        "☐ 3. Cherche 1 nouvelle info sur notre thème (1 site, 1 fait, 1 chiffre)",
        "Normal",
    )
    add_lignes_vides(doc, 2)
    add_text(
        doc,
        "☐ 4. Si tu sais enregistrer du son sur portable/tablette → demande à tes parents si OK pour S4",
        "Normal",
    )
    add_text(doc, "", "Normal")

    # Pour la prochaine fois
    add_text(doc, "📅 Prochaine séance : Jeudi 21 mai (S4)", "Section")
    add_text(
        doc, "On apporte : nos infos trouvées + script finalisé + accord parents si on enregistre", "Normal"
    )

    # Sauvegarder
    classe = equipe["classe"].lower()
    filename = f"projet_TP2/fiche_equipe_{classe}_equipe{equipe['num']}.odt"
    doc.save(filename)
    print(f"  Créé : {filename}")


if __name__ == "__main__":
    print("Génération des fiches équipe ODT...")
    print()
    for equipe in EQUIPES:
        generer_fiche(equipe)
    print()
    print(f"  {len(EQUIPES)} fiches créées dans projet_TP2/")
    print("  → Remplir en classe avec chaque équipe, puis photocopier pour chaque élève !")
