import clsx from "clsx";
import Link from "@docusaurus/Link";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import Layout from "@theme/Layout";
import Heading from "@theme/Heading";
import styles from "./index.module.css";

function HomepageHeader() {
  const { siteConfig } = useDocusaurusContext();
  return (
    <header className={clsx("hero", styles.heroBanner)}>
      <div className="container">
        <span className={styles.heroEmoji}>🖥️🎨🎵</span>
        <Heading as="h1" className={styles.heroTitle}>
          {siteConfig.title}
        </Heading>
        <p className={styles.heroSubtitle}>{siteConfig.tagline}</p>
        <div className={styles.buttons}>
          <Link
            className={clsx("button button--secondary button--lg", styles.heroButton)}
            to="/docs/programme/progression"
          >
            🗺️ Découvrir le programme
          </Link>
          <Link
            className={clsx("button button--secondary button--lg", styles.heroButton)}
            to="/docs/activites/tp1-scratch-noel"
          >
            🚀 Voir les projets
          </Link>
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
  return (
    <Layout
      title="Accueil"
      description="Programme informatique Cycle 3 — École Saint-Anne"
    >
      <HomepageHeader />
      <main>
        <section className={styles.features}>
          <div className="container">
            <div className="row margin-bottom--lg">
              <FeatureCard
                emoji="📅"
                title="Notre année"
                description="De septembre à juin, on apprend à programmer, créer des documents et enregistrer des podcasts !"
                link="/docs/programme/progression"
                linkText="Voir le calendrier"
              />
              <FeatureCard
                emoji="🎄"
                title="Cartes de Noël"
                description="On crée des cartes animées avec Scratch : neige qui tombe, musique et personnages qui dansent !"
                link="/docs/activites/tp1-scratch-noel"
                linkText="Découvrir le projet"
              />
              <FeatureCard
                emoji="🎙️🌍"
                title="Podcast Écologie"
                description="En équipe, on crée un podcast sur un thème écologique : gaspillage, pollution, animaux, écologie à l'école !"
                link="/docs/activites/tp2-ecologie"
                linkText="Découvrir les équipes"
              />
            </div>
            <div className="row margin-bottom--lg">
              <FeatureCard
                emoji="🎙️"
                title="Podcast Aventure"
                description="Toute la classe invente une histoire et l'enregistre en podcast avec des voix, des bruitages et de la musique !"
                link="/docs/activites/tp3-podcast-aventure"
                linkText="Explorer le projet"
              />
              <FeatureCard
                emoji="🗺️"
                title="Chasse au Trésor"
                description="Résous des calculs pour naviguer sur l'océan et trouver le coffre au trésor ! Un exercice dans un tableur."
                link="/docs/activites/chasse-au-tresor"
                linkText="Partir à l'aventure"
              />
              <FeatureCard
                emoji="✖️"
                title="Labyrinthe des Multiplications"
                description="Un labyrinthe de calculs où tu révises tes tables en t'amusant. Chaque exécution donne un nouveau défi !"
                link="/docs/activites/labyrinthe-multiplications"
                linkText="Entrer dans le labyrinthe"
              />
            </div>
          </div>
        </section>
      </main>
    </Layout>
  );
}
