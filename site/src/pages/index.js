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
        <span className={styles.heroEmoji}>🖥️🏛️🎙️</span>
        <Heading as="h1" className={styles.heroTitle}>
          {siteConfig.title}
        </Heading>
        <p className={styles.heroSubtitle}>
          2026-2027 : une année tournée vers l'Histoire ! {siteConfig.tagline}
        </p>
        <div className={styles.buttons}>
          <Link
            className={clsx("button button--secondary button--lg", styles.heroButton)}
            to="/docs/programme/progression"
          >
            🗺️ Découvrir le programme
          </Link>
          <Link
            className={clsx("button button--secondary button--lg", styles.heroButton)}
            to="/docs/activites/tp1-machine-temps"
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
      description="Programme informatique Cycle 3 — École Sainte-Anne"
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
                emoji="🕰️"
                title="La Machine à Remonter le Temps"
                description="Chaque élève programme une scène historique sur Scratch, et le Voyageur du Temps les traverse toutes : de la préhistoire à aujourd'hui !"
                link="/docs/activites/tp1-machine-temps"
                linkText="Monter dans la machine"
              />
              <FeatureCard
                emoji="📜"
                title="La Gazette du Temps"
                description="Deviens journaliste d'une autre époque ! Chaque équipe publie la une d'un journal historique avec articles, images et graphiques."
                link="/docs/activites/tp2-gazette-temps"
                linkText="Lire la gazette"
              />
            </div>
            <div className="row margin-bottom--lg">
              <FeatureCard
                emoji="🎙️"
                title="Podcast d'Histoire"
                description="Toute la classe raconte un épisode historique réel en podcast, façon « Les Odyssées » : voix, bruitages et frissons garantis !"
                link="/docs/activites/tp3-podcast-histoire"
                linkText="Tendre l'oreille"
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
