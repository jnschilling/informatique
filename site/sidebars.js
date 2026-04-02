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
        {
          type: "category",
          label: "TP2 : Podcast Écologie",
          items: [
            "activites/tp2-ecologie",
            "activites/tp2-cm1",
            "activites/tp2-cm2",
            "activites/tp2-pollution-nature",
            "activites/tp2-pollution-air",
            "activites/tp2-animaux",
            "activites/tp2-gaspillage",
            "activites/tp2-ecologie-ecole",
          ],
        },
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
