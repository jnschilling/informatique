import ComponentTypes from "@theme-original/NavbarItem/ComponentTypes";
import ViewSwitch from "@site/src/components/ViewSwitch";

// Ajoute l'interrupteur Enfant / Adulte aux éléments que la barre du haut sait afficher.
export default {
  ...ComponentTypes,
  "custom-viewSwitch": ViewSwitch,
};
