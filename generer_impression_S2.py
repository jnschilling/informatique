"""
Génère un PDF unique pour l'impression couleur de la séance S2 du TP2.

Contenu :
- 1 Kahoot template par équipe (5 pages)
- 1 fiche nominative par élève (21 pages — chaque élève reçoit sa copie avec son nom)

Ordre dans le PDF (pour faciliter la distribution en classe) :
  CM1 Équipe 1 : Kahoot + 4 fiches (Cylia, Maïly, Annaëlle, Alma)
  CM1 Équipe 2 : Kahoot + 3 fiches (Robin, Martin, Raphaël)
  CM1 Équipe 3 : Kahoot + 4 fiches (Timéo, Isobel, Emilie, Izia)
  CM2 Équipe 1 : Kahoot + 5 fiches (Kiara, Olivia, Faustine, Maëli, Scott)
  CM2 Équipe 2 : Kahoot + 5 fiches (Ryan, Oscar, Gwenolé, Léon, Costa)

Usage:
    poetry run python generer_impression_S2.py
"""

import os
import shutil
import subprocess
import tempfile

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
from pypdf import PdfWriter

SOFFICE = "/Applications/LibreOffice.app/Contents/MacOS/soffice"

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
        "kahoot_questions": 4,
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
        "kahoot_questions": 3,
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
        "kahoot_questions": 4,
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
        "kahoot_questions": 4,
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
        "kahoot_questions": 5,
    },
]


# --- Styles ---


def creer_styles_communs(doc):
    """Styles communs (fiches + kahoot)."""
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

    s = Style(name="NomEleve", family="paragraph")
    s.addElement(TextProperties(fontsize="22pt", fontweight="bold", color="#ffffff"))
    s.addElement(
        ParagraphProperties(
            margintop="0.3cm",
            marginbottom="0.5cm",
            textalign="center",
            backgroundcolor="#1565c0",
            padding="0.4cm",
        )
    )
    doc.styles.addElement(s)


def creer_styles_table_fiche(doc):
    """Styles tableau pour la section rôles."""
    s = Style(name="EnTeteFiche", family="table-cell")
    s.addElement(
        TableCellProperties(
            backgroundcolor="#1565c0", padding="0.15cm", border="0.05pt solid #000000"
        )
    )
    doc.automaticstyles.addElement(s)

    s = Style(name="EnTeteTexteFiche", family="paragraph")
    s.addElement(TextProperties(fontsize="10pt", fontweight="bold", color="#ffffff"))
    s.addElement(ParagraphProperties(textalign="center"))
    doc.automaticstyles.addElement(s)

    s = Style(name="CelluleFiche", family="table-cell")
    s.addElement(TableCellProperties(padding="0.2cm", border="0.05pt solid #aaaaaa"))
    doc.automaticstyles.addElement(s)

    s = Style(name="CelluleEnteteFiche", family="table-cell")
    s.addElement(
        TableCellProperties(
            backgroundcolor="#e3f2fd", padding="0.15cm", border="0.05pt solid #aaaaaa"
        )
    )
    doc.automaticstyles.addElement(s)

    s = Style(name="ColRoleFiche", family="table-column")
    s.addElement(TableColumnProperties(columnwidth="4cm"))
    doc.automaticstyles.addElement(s)

    s = Style(name="ColEleveFiche", family="table-column")
    s.addElement(TableColumnProperties(columnwidth="3cm"))
    doc.automaticstyles.addElement(s)


def creer_styles_kahoot(doc):
    """Styles pour le tableau Kahoot."""
    # Title green for Kahoot
    s = Style(name="TitreVert", family="paragraph")
    s.addElement(TextProperties(fontsize="22pt", fontweight="bold", color="#2e7d32"))
    s.addElement(ParagraphProperties(marginbottom="0.5cm", textalign="center"))
    doc.styles.addElement(s)

    # Headers
    s = Style(name="EnTete", family="table-cell")
    s.addElement(
        TableCellProperties(
            backgroundcolor="#2e7d32",
            padding="0.2cm",
            border="0.05pt solid #000000",
        )
    )
    doc.automaticstyles.addElement(s)

    s = Style(name="EnTeteTexte", family="paragraph")
    s.addElement(TextProperties(fontsize="11pt", fontweight="bold", color="#ffffff"))
    s.addElement(ParagraphProperties(textalign="center"))
    doc.automaticstyles.addElement(s)

    s = Style(name="Cellule", family="table-cell")
    s.addElement(
        TableCellProperties(padding="0.2cm", border="0.05pt solid #cccccc")
    )
    doc.automaticstyles.addElement(s)

    s = Style(name="CelluleBonne", family="table-cell")
    s.addElement(
        TableCellProperties(
            padding="0.2cm",
            border="0.05pt solid #cccccc",
            backgroundcolor="#e8f5e9",
        )
    )
    doc.automaticstyles.addElement(s)

    s = Style(name="CelluleNum", family="table-cell")
    s.addElement(
        TableCellProperties(
            padding="0.2cm",
            border="0.05pt solid #cccccc",
            backgroundcolor="#f5f5f5",
        )
    )
    doc.automaticstyles.addElement(s)

    s = Style(name="ColNum", family="table-column")
    s.addElement(TableColumnProperties(columnwidth="1cm"))
    doc.automaticstyles.addElement(s)

    s = Style(name="ColQuestion", family="table-column")
    s.addElement(TableColumnProperties(columnwidth="5cm"))
    doc.automaticstyles.addElement(s)

    s = Style(name="ColReponse", family="table-column")
    s.addElement(TableColumnProperties(columnwidth="3cm"))
    doc.automaticstyles.addElement(s)

    s = Style(name="ColBonne", family="table-column")
    s.addElement(TableColumnProperties(columnwidth="2cm"))
    doc.automaticstyles.addElement(s)


# --- Helpers ---


def add(doc, txt, style):
    doc.text.addElement(P(stylename=style, text=txt))


def lignes_vides(doc, n):
    for _ in range(n):
        doc.text.addElement(P(stylename="Ligne", text=""))


# --- Fiche équipe nominative ---


def fiche_section_roles(doc, equipe):
    table = Table(name="Roles")
    table.addElement(TableColumn(stylename="ColRoleFiche"))
    table.addElement(TableColumn(stylename="ColEleveFiche"))

    row = TableRow()
    for txt in ["Rôle", "Élève"]:
        cell = TableCell(stylename="EnTeteFiche")
        cell.addElement(P(stylename="EnTeteTexteFiche", text=txt))
        row.addElement(cell)
    table.addElement(row)

    n = len(equipe["eleves"])
    if n == 5:
        roles = ["Chef de projet", "Scénariste", "Documentaliste", "Technicien son", "Visuel"]
    elif n == 4:
        roles = ["Chef de projet", "Scénariste", "Documentaliste", "Technicien son / Visuel"]
    else:
        roles = ["Chef de projet", "Scénariste-Documentaliste", "Technicien son / Visuel"]

    for role in roles:
        row = TableRow()
        cell = TableCell(stylename="CelluleEnteteFiche")
        cell.addElement(P(text=role))
        row.addElement(cell)
        cell = TableCell(stylename="CelluleFiche")
        cell.addElement(P(text=""))
        row.addElement(cell)
        table.addElement(row)

    doc.text.addElement(table)


def generer_fiche_nominative(equipe, eleve, output_dir):
    doc = OpenDocumentText()
    creer_styles_communs(doc)
    creer_styles_table_fiche(doc)

    # Bandeau nominatif en haut
    add(doc, eleve, "NomEleve")

    add(doc, "FICHE ÉQUIPE — Podcast Écologie", "Titre")
    add(
        doc,
        f"{equipe['classe']} · Équipe {equipe['num']} · {equipe['theme']}",
        "SousTitre",
    )
    add(doc, f"Membres : {', '.join(equipe['eleves'])}", "Normal")
    add(
        doc,
        f"⏰ Gardien du temps aujourd'hui : {equipe['gardien_du_temps_S2']}",
        "Italic",
    )

    add(doc, "🎯 Notre question centrale", "Section")
    add(doc, equipe["question"], "Normal")
    add(
        doc,
        "(Reformulez ensemble en 1 phrase claire si vous voulez modifier)",
        "Italic",
    )
    lignes_vides(doc, 1)

    add(doc, "👥 Nos rôles", "Section")
    fiche_section_roles(doc, equipe)

    add(doc, "🔍 3 infos clés à trouver (Documentaliste)", "Section")
    add(doc, "Cherchez sur Qwant Junior, 1jour1actu, Lumni :", "Italic")
    for i in range(1, 4):
        add(doc, f"{i}.", "Ligne")

    add(doc, "✨ Notre chiffre marquant pour le « Le saviez-vous ? »", "Section")
    lignes_vides(doc, 1)

    add(doc, "📚 Nos 3 sources (site web + auteur)", "Section")
    for i in range(1, 4):
        add(doc, f"{i}.", "Ligne")

    add(
        doc,
        f"✏️ Script v1 ({equipe['mots_script']}, durée {equipe['duree_cible']})",
        "Section",
    )
    add(
        doc,
        "Structure : (1) Bonjour... (2) Notre question (3) Ce qu'on a appris (4) Et toi... ?",
        "Italic",
    )
    lignes_vides(doc, 8)

    add(doc, "❓ Notre 1ère question Kahoot", "Section")
    add(doc, "Question :", "Ligne")
    add(doc, "Réponse A :", "Ligne")
    add(doc, "Réponse B :", "Ligne")
    add(doc, "Réponse C :", "Ligne")
    add(doc, "Réponse D :", "Ligne")
    add(doc, "✓ Bonne réponse : ☐ A   ☐ B   ☐ C   ☐ D", "Normal")

    add(doc, f"🏠 DEVOIRS À LA MAISON — {eleve}", "SectionDevoirs")
    add(doc, f"☐ 1. Écouter le podcast : {equipe['podcast_recommande']}", "Normal")
    add(doc, f"     {equipe['podcast_url']}", "Italic")
    add(
        doc,
        "☐ 2. Note 3 choses qui t'ont plu (la voix, un bruitage, une info...) :",
        "Normal",
    )
    lignes_vides(doc, 3)
    add(
        doc,
        "☐ 3. Cherche 1 nouvelle info sur notre thème (1 site, 1 fait, 1 chiffre)",
        "Normal",
    )
    lignes_vides(doc, 2)
    add(
        doc,
        "☐ 4. Si tu sais enregistrer du son sur portable/tablette → demande à tes parents si OK pour S4",
        "Normal",
    )
    add(doc, "", "Normal")

    add(doc, "📅 Prochaine séance : Jeudi 21 mai (S4)", "Section")
    add(
        doc,
        "On apporte : nos infos trouvées + script finalisé + accord parents si on enregistre",
        "Normal",
    )

    safe_eleve = eleve.replace("é", "e").replace("ï", "i").replace("ë", "e").replace("ô", "o").replace("è", "e").lower()
    filename = os.path.join(
        output_dir,
        f"fiche_{equipe['classe'].lower()}_e{equipe['num']}_{safe_eleve}.odt",
    )
    doc.save(filename)
    return filename


# --- Kahoot ---


def kahoot_entete(table, colonnes):
    row = TableRow()
    for txt in colonnes:
        cell = TableCell(stylename="EnTete")
        cell.addElement(P(stylename="EnTeteTexte", text=txt))
        row.addElement(cell)
    table.addElement(row)


def kahoot_ligne_vide(table, num, nb_cols):
    row = TableRow()
    cell = TableCell(stylename="CelluleNum")
    cell.addElement(P(text=str(num)))
    row.addElement(cell)
    for i in range(nb_cols - 1):
        if i == nb_cols - 2:
            cell = TableCell(stylename="CelluleBonne")
        else:
            cell = TableCell(stylename="Cellule")
        cell.addElement(P(text=""))
        row.addElement(cell)
    table.addElement(row)


def generer_kahoot(equipe, output_dir):
    doc = OpenDocumentText()
    creer_styles_communs(doc)
    creer_styles_kahoot(doc)

    add(doc, f"Kahoot Écologie — {equipe['theme']}", "TitreVert")
    add(
        doc,
        f"{equipe['classe']} · Équipe {equipe['num']} · {', '.join(equipe['eleves'])}",
        "SousTitre",
    )
    add(doc, f"Notre question : {equipe['question']}", "Normal")

    add(doc, "Comment écrire une bonne question ?", "Section")
    consignes = [
        "La question doit être claire : on comprend tout de suite ce qu'on demande.",
        "Il y a UNE SEULE bonne réponse — les fausses doivent être crédibles !",
        "Utilise un chiffre ou un fait surprenant trouvé pendant ta recherche.",
        "Les autres élèves doivent pouvoir répondre sans avoir fait ta recherche.",
        f"Chaque membre de l'équipe écrit au moins 1 question = {equipe['kahoot_questions']} questions minimum.",
    ]
    for c in consignes:
        add(doc, f"• {c}", "Italic")

    add(doc, "Exemple", "Section")
    exemple = Table(name="Exemple")
    exemple.addElement(TableColumn(stylename="ColNum"))
    exemple.addElement(TableColumn(stylename="ColQuestion"))
    for _ in range(4):
        exemple.addElement(TableColumn(stylename="ColReponse"))
    exemple.addElement(TableColumn(stylename="ColBonne"))

    kahoot_entete(
        exemple,
        ["#", "Question", "Réponse A", "Réponse B", "Réponse C", "Réponse D", "Bonne"],
    )

    row = TableRow()
    vals = [
        "Ex",
        "Combien de temps met un sac plastique à se décomposer ?",
        "10 ans",
        "50 ans",
        "400 ans",
        "1000 ans",
        "C",
    ]
    for i, val in enumerate(vals):
        if i == 0:
            cell = TableCell(stylename="CelluleNum")
        elif i == 6:
            cell = TableCell(stylename="CelluleBonne")
        else:
            cell = TableCell(stylename="Cellule")
        cell.addElement(P(text=val))
        row.addElement(cell)
    exemple.addElement(row)
    doc.text.addElement(exemple)

    add(doc, "", "Normal")

    add(doc, f"Nos {equipe['kahoot_questions']} questions", "Section")
    table = Table(name="Questions")
    table.addElement(TableColumn(stylename="ColNum"))
    table.addElement(TableColumn(stylename="ColQuestion"))
    for _ in range(4):
        table.addElement(TableColumn(stylename="ColReponse"))
    table.addElement(TableColumn(stylename="ColBonne"))

    kahoot_entete(
        table,
        ["#", "Question", "Réponse A", "Réponse B", "Réponse C", "Réponse D", "Bonne"],
    )

    for i in range(1, equipe["kahoot_questions"] + 1):
        kahoot_ligne_vide(table, i, 7)

    doc.text.addElement(table)

    add(doc, "", "Normal")
    add(doc, "Nos sources", "Section")
    add(doc, "D'où viennent vos informations ? Notez les sites web utilisés.", "Italic")
    for i in range(1, 4):
        add(doc, f"{i}. ", "Normal")

    filename = os.path.join(
        output_dir, f"kahoot_{equipe['classe'].lower()}_e{equipe['num']}.odt"
    )
    doc.save(filename)
    return filename


# --- Conversion ODT → PDF ---


def odt_to_pdf(odt_path, output_dir):
    """Convertit un ODT en PDF via LibreOffice headless."""
    result = subprocess.run(
        [SOFFICE, "--headless", "--convert-to", "pdf", "--outdir", output_dir, odt_path],
        capture_output=True,
        text=True,
        timeout=60,
    )
    if result.returncode != 0:
        print(f"  ⚠️ Erreur conversion {odt_path}: {result.stderr}")
        return None
    base = os.path.splitext(os.path.basename(odt_path))[0]
    return os.path.join(output_dir, f"{base}.pdf")


# --- Pipeline ---


def main():
    output_pdf = "projet_TP2/impression_S2.pdf"

    with tempfile.TemporaryDirectory() as tmp:
        odt_dir = os.path.join(tmp, "odt")
        pdf_dir = os.path.join(tmp, "pdf")
        os.makedirs(odt_dir)
        os.makedirs(pdf_dir)

        # Génération des ODTs dans l'ordre voulu (équipe par équipe : kahoot puis fiches élèves)
        odt_files = []
        for equipe in EQUIPES:
            print(f"\n--- {equipe['classe']} Équipe {equipe['num']} : {equipe['theme']} ---")

            # 1. Kahoot équipe
            f = generer_kahoot(equipe, odt_dir)
            odt_files.append(f)
            print(f"  📝 Kahoot     : {os.path.basename(f)}")

            # 2. Fiches nominatives (1 par élève)
            for eleve in equipe["eleves"]:
                f = generer_fiche_nominative(equipe, eleve, odt_dir)
                odt_files.append(f)
                print(f"  📄 Fiche      : {eleve}")

        # Conversion ODT → PDF
        print("\n--- Conversion ODT → PDF ---")
        pdf_files = []
        for odt in odt_files:
            pdf = odt_to_pdf(odt, pdf_dir)
            if pdf:
                pdf_files.append(pdf)

        # Fusion
        print(f"\n--- Fusion en {output_pdf} ---")
        writer = PdfWriter()
        for pdf in pdf_files:
            writer.append(pdf)
        with open(output_pdf, "wb") as f:
            writer.write(f)

        # Stats
        from pypdf import PdfReader
        nb_pages = len(PdfReader(output_pdf).pages)
        print(f"\n✅ PDF généré : {output_pdf}")
        print(f"   {len(pdf_files)} documents fusionnés")
        print(f"   {nb_pages} pages au total")
        print(f"\n🖨️  Prêt pour impression couleur !")


if __name__ == "__main__":
    main()
