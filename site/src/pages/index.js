import clsx from "clsx";
import Link from "@docusaurus/Link";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import Layout from "@theme/Layout";
import Heading from "@theme/Heading";
import styles from "./index.module.css";

// La vue Adulte est la locale « fr-adulte » ; la vue Enfant est la locale par défaut.
const ADULT_LOCALE = "fr-adulte";

const KID_HOME = {
  subtitle: (tagline) => `2026-2027 : une année tournée vers l'Histoire ! ${tagline}`,
  buttons: [
    { to: "/docs/programme/progression", label: "🗺️ Découvrir notre année" },
    { to: "/docs/activites/tp1-machine-temps", label: "🚀 Voir les projets" },
  ],
  cards: [
    {
      emoji: "📅",
      title: "Notre année",
      description: "De septembre à juin, on apprend à programmer, créer des documents et enregistrer des podcasts !",
      link: "/docs/programme/progression",
      linkText: "Voir le calendrier",
    },
    {
      emoji: "🕰️",
      title: "La Machine à Remonter le Temps",
      description: "Chaque élève programme une scène historique sur Scratch, et le Voyageur du Temps les traverse toutes : de la préhistoire à aujourd'hui !",
      link: "/docs/activites/tp1-machine-temps",
      linkText: "Monter dans la machine",
    },
    {
      emoji: "📜",
      title: "La Gazette du Temps",
      description: "Deviens journaliste d'une autre époque ! Chaque équipe publie la une d'un journal historique avec articles, images et graphiques.",
      link: "/docs/activites/tp2-gazette-temps",
      linkText: "Lire la gazette",
    },
    {
      emoji: "🎙️",
      title: "Podcast d'Histoire",
      description: "Toute la classe raconte un épisode historique réel en podcast, façon « Les Odyssées » : voix, bruitages et frissons garantis !",
      link: "/docs/activites/tp3-podcast-histoire",
      linkText: "Tendre l'oreille",
    },
    {
      emoji: "🗺️",
      title: "Chasse au Trésor",
      description: "Résous des calculs pour naviguer sur l'océan et trouver le coffre au trésor ! Un exercice dans un tableur.",
      link: "/docs/activites/chasse-au-tresor",
      linkText: "Partir à l'aventure",
    },
    {
      emoji: "🏠",
      title: "Notre site est une maison",
      description: "Une adresse, une porte, des fenêtres... Fais le tour de notre site comme on visite une maison, et deviens détective d'internet !",
      link: "/docs/ressources/notre-site-maison",
      linkText: "Visiter la maison",
    },
  ],
};

const ADULT_HOME = {
  subtitle: () =>
    "Cours d'informatique des CM1-CM2 — année 2026-2027. Progression, attendus, évaluation et références officielles.",
  buttons: [
    { to: "/docs/programme/progression", label: "Progression annuelle" },
    { to: "/vie-privee", label: "Mentions légales & vie privée" },
  ],
  cards: [
    {
      emoji: "📅",
      title: "Progression annuelle",
      description: "Le calendrier de l'année, les trois grands travaux pratiques et les attendus par niveau, CM1 et CM2.",
      link: "/docs/programme/progression",
      linkText: "Lire la progression",
    },
    {
      emoji: "📘",
      title: "Programme officiel",
      description: "Les extraits du cycle 3 et les deux programmes en vigueur cette année, avec leurs références.",
      link: "/docs/ressources/programme-officiel",
      linkText: "Voir les textes",
    },
    {
      emoji: "✅",
      title: "Évaluation",
      description: "L'évaluation continue, la grille par TP et les attendus de fin d'année pour chaque niveau.",
      link: "/docs/programme/evaluation",
      linkText: "Voir l'évaluation",
    },
    {
      emoji: "🚀",
      title: "Les projets de l'année",
      description: "Poilus, Robots & Parcours, Machine à Remonter le Temps, Gazette du Temps, Podcast d'Histoire.",
      link: "/docs/activites/poilus-memoire",
      linkText: "Voir les activités",
    },
    {
      emoji: "🧰",
      title: "Outils et logiciels",
      description: "Les logiciels utilisés en classe, l'infrastructure, et les ressources sur la vie privée en ligne.",
      link: "/docs/ressources/outils",
      linkText: "Voir les outils",
    },
    {
      emoji: "🛡️",
      title: "Vie privée",
      description: "Aucune collecte, aucun cookie, aucun traceur. Travaux d'élèves publiés avec accord parental écrit, prénom seul.",
      link: "/vie-privee",
      linkText: "Lire les mentions légales",
    },
  ],
};

function useHome() {
  const { i18n } = useDocusaurusContext();
  return i18n.currentLocale === ADULT_LOCALE ? ADULT_HOME : KID_HOME;
}

function HomepageHeader() {
  const { siteConfig } = useDocusaurusContext();
  const home = useHome();
  return (
    <header className={clsx("hero", styles.heroBanner)}>
      <div className="container">
        <span className={styles.heroEmoji}>🖥️🏛️🎙️</span>
        <Heading as="h1" className={styles.heroTitle}>
          {siteConfig.title}
        </Heading>
        <p className={styles.heroSubtitle}>{home.subtitle(siteConfig.tagline)}</p>
        <div className={styles.buttons}>
          {home.buttons.map((button) => (
            <Link
              key={button.to}
              className={clsx("button button--secondary button--lg", styles.heroButton)}
              to={button.to}
            >
              {button.label}
            </Link>
          ))}
        </div>
      </div>
    </header>
  );
}

function FeatureCard({ emoji, title, description, link, linkText }) {
  return (
    <div className={clsx("col col--4")}>
      <div className={styles.featureCard}>
        <span className={styles.featureEmoji}>{emoji}</span>
        <Heading as="h3" className={styles.featureTitle}>{title}</Heading>
        <p className={styles.featureDescription}>{description}</p>
        <Link className={styles.featureLink} to={link}>
          {linkText} →
        </Link>
      </div>
    </div>
  );
}

export default function Home() {
  const home = useHome();
  const rows = [home.cards.slice(0, 3), home.cards.slice(3, 6)];
  return (
    <Layout
      title="Accueil"
      description="Programme informatique Cycle 3 — École Sainte-Anne"
    >
      <HomepageHeader />
      <main>
        <section className={styles.features}>
          <div className="container">
            {rows.map((row, index) => (
              <div className="row margin-bottom--lg" key={index}>
                {row.map((card) => (
                  <FeatureCard key={card.link} {...card} />
                ))}
              </div>
            ))}
          </div>
        </section>
      </main>
    </Layout>
  );
}
