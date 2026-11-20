// @ts-check
import { themes as prismThemes } from "prism-react-renderer";

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: "Informatique Sainte-Anne",
  tagline: "On apprend, on crée, on s'amuse avec l'informatique ! 🎉",
  favicon: "img/favicon.ico",

  future: {
    v4: true,
  },

  url: "https://ecole-sainte-anne.locki.io",
  baseUrl: "/",

  onBrokenLinks: "throw",

  // GitHub Pages ajoute le slash final : sans lui, 37/38 URLs du sitemap redirigent.
  trailingSlash: true,

  // Pas de référencement pour l'instant (site de classe, travaux d'élèves à venir).
  // Lever ce verrou = décision opérateur + passage Proþreynir (données d'élèves).
  noIndex: true,

  i18n: {
    // Deux vues d'un même site, portées par l'i18n : « fr » = la vue Enfant (à la racine),
    // « fr-adulte » = la vue Adulte (sous /adulte/). Une page sans version adulte
    // affiche la version enfant dans les deux vues.
    defaultLocale: "fr",
    locales: ["fr", "fr-adulte"],
    localeConfigs: {
      fr: {
        label: "🧒 Enfant",
        direction: "ltr",
        htmlLang: "fr-FR",
        calendar: "gregory",
      },
      "fr-adulte": {
        label: "🎓 Adulte",
        direction: "ltr",
        htmlLang: "fr-FR",
        calendar: "gregory",
        baseUrl: "/adulte/",
      },
    },
  },

  presets: [
    [
      "classic",
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: "./sidebars.js",
        },
        blog: {
          showReadingTime: true,
          blogSidebarCount: "ALL",
          feedOptions: {
            type: ["rss", "atom"],
            xslt: true,
          },
          onInlineTags: "warn",
          onInlineAuthors: "warn",
          onUntruncatedBlogPosts: "warn",
        },
        theme: {
          customCss: "./src/css/custom.css",
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // the share card (WhatsApp, Signal, X...): a 1200 px copy of the banner, under 300 KB so WhatsApp keeps it
      image: "img/og-ecole-sainte-anne.jpg",
      colorMode: {
        respectPrefersColorScheme: true,
      },
      navbar: {
        title: "🖥️ Info Sainte-Anne",
        items: [
          {
            type: "docSidebar",
            sidebarId: "programmeSidebar",
            position: "left",
            label: "📅 Notre année",
          },
          {
            type: "docSidebar",
            sidebarId: "activitesSidebar",
            position: "left",
            label: "🚀 Nos projets",
          },
          {
            type: "docSidebar",
            sidebarId: "ressourcesSidebar",
            position: "left",
            label: "📚 Boîte à outils",
          },
          { to: "/blog", label: "✏️ Blog", position: "left" },
          { type: "custom-viewSwitch", position: "right" },
        ],
      },
      footer: {
        style: "dark",
        links: [
          {
            title: "🗺️ Explorer",
            items: [
              {
                label: "📅 Notre année",
                to: "/docs/programme/progression",
              },
              {
                label: "🚀 Les projets",
                to: "/docs/activites/tp1-machine-temps",
              },
            ],
          },
          {
            title: "📚 Apprendre",
            items: [
              {
                label: "Pourquoi l'informatique à l'école ?",
                to: "/docs/ressources/programme-officiel",
              },
              {
                label: "Nos outils",
                to: "/docs/ressources/outils",
              },
              {
                label: "🏠 Notre site est une maison",
                to: "/docs/ressources/notre-site-maison",
              },
              {
                label: "Mentions légales (pour les adultes)",
                to: "/vie-privee",
              },
            ],
          },
          {
            title: "✏️ Écrire",
            items: [
              {
                label: "Blog de la classe",
                to: "/blog",
              },
            ],
          },
        ],
        copyright: `© ${new Date().getFullYear()} École Sainte-Anne — CM1-CM2 🎓 Construit avec Docusaurus`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
        additionalLanguages: ["python", "bash", "json"],
      },
    }),
};

export default config;
