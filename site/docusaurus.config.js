// @ts-check
import { themes as prismThemes } from "prism-react-renderer";

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: "Informatique Saint-Anne",
  tagline: "On apprend, on crée, on s'amuse avec l'informatique ! 🎉",
  favicon: "img/favicon.ico",

  future: {
    v4: true,
  },

  // TODO: set production URL when deployed
  url: "https://informatique.example.com",
  baseUrl: "/",

  onBrokenLinks: "throw",

  i18n: {
    defaultLocale: "fr",
    locales: ["fr"],
    localeConfigs: {
      fr: {
        label: "Français",
        direction: "ltr",
        htmlLang: "fr-FR",
        calendar: "gregory",
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
      colorMode: {
        respectPrefersColorScheme: true,
      },
      navbar: {
        title: "🖥️ Info Saint-Anne",
        items: [
          {
            type: "docSidebar",
            sidebarId: "programmeSidebar",
            position: "left",
            label: "📅 Programme",
          },
          {
            type: "docSidebar",
            sidebarId: "activitesSidebar",
            position: "left",
            label: "🚀 Activités",
          },
          {
            type: "docSidebar",
            sidebarId: "ressourcesSidebar",
            position: "left",
            label: "📚 Ressources",
          },
          { to: "/blog", label: "✏️ Blog", position: "left" },
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
                to: "/docs/activites/tp1-scratch-noel",
              },
            ],
          },
          {
            title: "📚 Apprendre",
            items: [
              {
                label: "Programme officiel Cycle 3",
                to: "/docs/ressources/programme-officiel",
              },
              {
                label: "Nos outils",
                to: "/docs/ressources/outils",
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
        copyright: `© ${new Date().getFullYear()} École Saint-Anne — CM1-CM2 🎓 Construit avec Docusaurus`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
        additionalLanguages: ["python", "bash", "json"],
      },
    }),
};

export default config;
