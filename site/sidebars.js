/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  programmeSidebar: [
    {
      type: "category",
      label: "Programme Annuel",
      items: [
        "programme/progression",
        "programme/competences-base",
        "programme/evaluation",
      ],
    },
  ],
  activitesSidebar: [
    {
      type: "category",
      label: "Travaux Pratiques",
      items: [
        "activites/tp1-scratch-noel",
        "activites/tp2-journal-environnement",
        "activites/tp3-podcast-aventure",
      ],
    },
    "activites/kahoot",
    {
      type: "category",
      label: "Outils Générateurs",
      items: [
        "activites/chasse-au-tresor",
        "activites/labyrinthe-multiplications",
      ],
    },
  ],
  ressourcesSidebar: [
    {
      type: "category",
      label: "Références",
      items: [
        "ressources/programme-officiel",
        "ressources/outils",
      ],
    },
  ],
};

export default sidebars;
