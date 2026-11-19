import clsx from "clsx";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import { useLocation } from "@docusaurus/router";
import { useAlternatePageUtils } from "@docusaurus/theme-common/internal";
import styles from "./styles.module.css";

/**
 * L'interrupteur Enfant / Adulte.
 * Chaque vue est une locale du site : passer de l'une à l'autre, c'est ouvrir la même page
 * dans l'autre vue. Ce sont de simples liens : rien n'est mémorisé dans le navigateur.
 */
export default function ViewSwitch({ mobile }) {
  const {
    i18n: { currentLocale, locales, localeConfigs },
  } = useDocusaurusContext();
  const { createUrl } = useAlternatePageUtils();
  const { search, hash } = useLocation();

  return (
    <div
      className={clsx(styles.viewSwitch, mobile && styles.viewSwitchMobile)}
      role="group"
      aria-label="Choisir la vue du site"
    >
      {locales.map((locale) => {
        const active = locale === currentLocale;
        return (
          <a
            key={locale}
            className={clsx(styles.option, active && styles.optionActive)}
            href={`${createUrl({ locale, fullyQualified: false })}${search}${hash}`}
            aria-current={active ? "true" : undefined}
          >
            {localeConfigs[locale].label}
          </a>
        );
      })}
    </div>
  );
}
