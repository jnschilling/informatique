---
sidebar_position: 5
title: "Labyrinthe des Multiplications"
---

# Labyrinthe des Multiplications

Générateur Python d'une grille de multiplications aléatoires (tables de 1 à 10) avec auto-correction cachée dans les commentaires des cellules.

## Principe

Une grille 7x7 de problèmes de multiplication est générée aléatoirement. Les élèves écrivent leurs réponses dans la ligne dédiée. En survolant chaque cellule de problème, un commentaire révèle la réponse correcte.

## Utilisation

```bash
python labyrinthe_mult.py
```

Génère le fichier `labyrinthe_multiplications.xlsx` à la racine du projet.

## Structure de la feuille

- **Ligne 3** : En-têtes (multiplicateurs x1 à x7)
- **Lignes 4-10** : Grille de problèmes (multiplieur aléatoire × multiplicateur)
- **Ligne 11** : Ligne de réponses (les élèves écrivent ici)
- **Ligne 13** : Instructions

## Auto-correction

Chaque cellule de problème contient un commentaire Excel avec la réponse correcte (visible au survol). Les élèves peuvent aussi ajouter une colonne I avec des formules `=SI(B11={réf}; "✓"; "✗")` pour vérification automatique.

## Dépendance

```bash
pip install openpyxl
```

:::note
La grille est aléatoire : chaque exécution du script produit un exercice différent, permettant de générer des feuilles uniques par élève.
:::
