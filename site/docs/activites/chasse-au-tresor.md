---
sidebar_position: 4
title: "Chasse au Trésor des Nombres"
---

# Chasse au Trésor des Nombres

Générateur Python d'une feuille de calcul interactive où les élèves résolvent des opérations arithmétiques pour naviguer dans une grille « océan » et trouver le trésor.

## Principe

Les élèves partent d'une case de départ et résolvent des additions/soustractions. Le résultat de chaque opération leur indique où aller ensuite (ligne, colonne). À la fin, une formule `SOMME` calcule le score total.

## Utilisation

```bash
python generer_chasse.py
```

Génère le fichier `chasse_au_tresor.xlsx` à la racine du projet.

## Parcours des étapes

1. **Départ A2** : `5 + 3 = ?` → descends à la ligne 8
2. **Île aux crabes A8** : `4 - 1 = ?` → saute à la colonne 3
3. **Caverne sombre C8** : `7 + 2 = ?` → avance 9 cases à droite
4. **Presque là I8** : `10 - 6 = ?` → monte à la ligne 4
5. **Trésor I4** : `=SOMME(B2;B8;D8;J8)` → score total = 24

## Dépendance

```bash
pip install openpyxl
```

:::tip
Les formules Excel utilisent le séparateur `;` (format français/LibreOffice Calc) et non `,`.
:::
