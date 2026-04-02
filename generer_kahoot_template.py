"""
Génère un template ODT par équipe pour préparer les questions Kahoot.
Les élèves remplissent le document, l'enseignant crée le Kahoot.

Usage:
    poetry run python generer_kahoot_template.py
"""

from odf.opendocument import OpenDocumentText
from odf.style import Style, TextProperties, ParagraphProperties, TableColumnProperties, TableCellProperties
from odf.text import P, H, List, ListItem, ListLevelStyleBullet, ListStyle
from odf.table import Table, TableColumn, TableRow, TableCell


# --- Données des équipes ---

EQUIPES = [
    {
        "classe": "CM1",
        "nom": "Équipe 1",
        "theme": "Pollution de la nature",
        "question": "Comment la nature est-elle polluée autour de nous ?",
        "eleves": ["Cylia", "Maïly", "Annaëlle", "Alma"],
        "nb_questions": 4,
    },
    {
        "classe": "CM1",
        "nom": "Équipe 2",
        "theme": "Pollution de l'air",
        "question": "D'où vient la pollution de l'air ?",
        "eleves": ["Robin", "Martin", "Raphaël"],
        "nb_questions": 3,
    },
    {
        "classe": "CM1",
        "nom": "Équipe 3",
        "theme": "Faire plus attention aux animaux",
        "question": "Comment mieux protéger les animaux au quotidien ?",
        "eleves": ["Timeo", "Isobel", "Emilie", "Izia"],
        "nb_questions": 4,
    },
    {
        "classe": "CM2",
        "nom": "Équipe 1",
        "theme": "Comment ne pas gaspiller ?",
        "question": "On gaspille quoi exactement ? Comment changer nos habitudes ?",
        "eleves": ["Kiara", "Olivia", "Faustine", "Maëli"],
        "nb_questions": 4,
    },
    {
        "classe": "CM2",
        "nom": "Équipe 2",
        "theme": "Comment comprendre mieux l'écologie à l'école",
        "question": "Est-ce qu'on apprend assez sur l'écologie à l'école ?",
        "eleves": ["Ryan", "Oscar", "Gwenolé", "Léon", "Costa"],
        "nb_questions": 5,
    },
]


def creer_styles(doc):
    """Crée les styles du document."""
    # Titre principal
    s = Style(name="Titre", family="paragraph")
    s.addElement(TextProperties(fontsize="22pt", fontweight="bold", color="#2e7d32"))
    s.addElement(ParagraphProperties(marginbottom="0.5cm", textalign="center"))
    doc.styles.addElement(s)

    # Sous-titre
    s = Style(name="SousTitre", family="paragraph")
    s.addElement(TextProperties(fontsize="14pt", fontstyle="italic", color="#555555"))
    s.addElement(ParagraphProperties(marginbottom="0.8cm", textalign="center"))
    doc.styles.addElement(s)

    # Section
    s = Style(name="Section", family="paragraph")
    s.addElement(TextProperties(fontsize="16pt", fontweight="bold", color="#1565c0"))
    s.addElement(ParagraphProperties(margintop="0.8cm", marginbottom="0.3cm"))
    doc.styles.addElement(s)

    # Texte normal
    s = Style(name="Normal", family="paragraph")
    s.addElement(TextProperties(fontsize="12pt"))
    s.addElement(ParagraphProperties(marginbottom="0.3cm"))
    doc.styles.addElement(s)

    # Consigne
    s = Style(name="Consigne", family="paragraph")
    s.addElement(TextProperties(fontsize="11pt", fontstyle="italic", color="#666666"))
    s.addElement(ParagraphProperties(marginbottom="0.3cm"))
    doc.styles.addElement(s)

    # En-tête tableau
    s = Style(name="EnTete", family="table-cell")
    s.addElement(TableCellProperties(backgroundcolor="#2e7d32", padding="0.2cm", border="0.05pt solid #000000"))
    doc.automaticstyles.addElement(s)

    s = Style(name="EnTeteTexte", family="paragraph")
    s.addElement(TextProperties(fontsize="11pt", fontweight="bold", color="#ffffff"))
    s.addElement(ParagraphProperties(textalign="center"))
    doc.automaticstyles.addElement(s)

    # Cellule normale
    s = Style(name="Cellule", family="table-cell")
    s.addElement(TableCellProperties(padding="0.2cm", border="0.05pt solid #cccccc"))
    doc.automaticstyles.addElement(s)

    # Cellule bonne réponse
    s = Style(name="CelluleBonne", family="table-cell")
    s.addElement(TableCellProperties(padding="0.2cm", border="0.05pt solid #cccccc", backgroundcolor="#e8f5e9"))
    doc.automaticstyles.addElement(s)

    # Cellule numéro
    s = Style(name="CelluleNum", family="table-cell")
    s.addElement(TableCellProperties(padding="0.2cm", border="0.05pt solid #cccccc", backgroundcolor="#f5f5f5"))
    doc.automaticstyles.addElement(s)

    # Colonnes
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


def ajouter_entete(table, colonnes):
    """Ajoute la ligne d'en-tête au tableau."""
    row = TableRow()
    for texte in colonnes:
        cell = TableCell(stylename="EnTete")
        cell.addElement(P(stylename="EnTeteTexte", text=texte))
        row.addElement(cell)
    table.addElement(row)


def ajouter_ligne_vide(table, num, nb_cols):
    """Ajoute une ligne vide numérotée."""
    row = TableRow()
    # Numéro
    cell = TableCell(stylename="CelluleNum")
    cell.addElement(P(text=str(num)))
    row.addElement(cell)
    # Colonnes vides
    for i in range(nb_cols - 1):
        if i == nb_cols - 2:  # Dernière colonne = bonne réponse
            cell = TableCell(stylename="CelluleBonne")
        else:
            cell = TableCell(stylename="Cellule")
        cell.addElement(P(text=""))
        row.addElement(cell)
    table.addElement(row)


def generer_template(equipe):
    """Génère le template ODT pour une équipe."""
    doc = OpenDocumentText()
    creer_styles(doc)

    # Titre
    doc.text.addElement(P(stylename="Titre", text=f"Kahoot Écologie — {equipe['theme']}"))

    # Sous-titre
    doc.text.addElement(P(
        stylename="SousTitre",
        text=f"{equipe['classe']} · {equipe['nom']} · {', '.join(equipe['eleves'])}"
    ))

    # Question du thème
    doc.text.addElement(P(stylename="Normal", text=f"Notre question : {equipe['question']}"))

    # Consignes
    doc.text.addElement(P(stylename="Section", text="Comment écrire une bonne question ?"))
    consignes = [
        "La question doit être claire : on comprend tout de suite ce qu'on demande.",
        "Il y a UNE SEULE bonne réponse — les fausses doivent être crédibles !",
        "Utilise un chiffre ou un fait surprenant trouvé pendant ta recherche.",
        "Les autres élèves doivent pouvoir répondre sans avoir fait ta recherche.",
        f"Chaque membre de l'équipe écrit au moins 1 question = {equipe['nb_questions']} questions minimum.",
    ]
    for c in consignes:
        doc.text.addElement(P(stylename="Consigne", text=f"• {c}"))

    # Exemple
    doc.text.addElement(P(stylename="Section", text="Exemple"))
    exemple = Table(name="Exemple")
    exemple.addElement(TableColumn(stylename="ColNum"))
    exemple.addElement(TableColumn(stylename="ColQuestion"))
    for _ in range(4):
        exemple.addElement(TableColumn(stylename="ColReponse"))
    exemple.addElement(TableColumn(stylename="ColBonne"))

    ajouter_entete(exemple, ["#", "Question", "Réponse A", "Réponse B", "Réponse C", "Réponse D", "Bonne"])

    row = TableRow()
    exemples = [
        ("Ex", "Combien de temps met un sac plastique à se décomposer ?",
         "10 ans", "50 ans", "400 ans", "1000 ans", "C")
    ]
    for num, q, a, b, c, d, bonne in exemples:
        for i, val in enumerate([num, q, a, b, c, d, bonne]):
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

    doc.text.addElement(P(stylename="Normal", text=""))

    # Tableau principal
    doc.text.addElement(P(stylename="Section", text=f"Nos {equipe['nb_questions']} questions"))

    table = Table(name="Questions")
    table.addElement(TableColumn(stylename="ColNum"))
    table.addElement(TableColumn(stylename="ColQuestion"))
    for _ in range(4):
        table.addElement(TableColumn(stylename="ColReponse"))
    table.addElement(TableColumn(stylename="ColBonne"))

    ajouter_entete(table, ["#", "Question", "Réponse A", "Réponse B", "Réponse C", "Réponse D", "Bonne"])

    for i in range(1, equipe["nb_questions"] + 1):
        ajouter_ligne_vide(table, i, 7)

    doc.text.addElement(table)

    # Sources
    doc.text.addElement(P(stylename="Normal", text=""))
    doc.text.addElement(P(stylename="Section", text="Nos sources"))
    doc.text.addElement(P(stylename="Consigne", text="D'où viennent vos informations ? Notez les sites web utilisés."))
    for i in range(1, 4):
        doc.text.addElement(P(stylename="Normal", text=f"{i}. "))

    # Sauvegarder
    classe = equipe["classe"].lower()
    num = equipe["nom"].split()[-1]
    filename = f"projet_TP2/kahoot_{classe}_equipe{num}.odt"
    doc.save(filename)
    print(f"  Créé : {filename}")


if __name__ == "__main__":
    print("Génération des templates Kahoot ODT...")
    print()
    for equipe in EQUIPES:
        generer_template(equipe)
    print()
    print(f"  {len(EQUIPES)} fichiers créés dans projet_TP2/")
    print("  Les élèves ouvrent leur fichier dans LibreOffice Writer et remplissent le tableau !")
