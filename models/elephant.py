import random
from .animal import Animal

class Elephant(Animal):
    """Classe représentant un éléphant."""

    def __init__(self, nom, appetit=100, satisfaction=50, soigneur=None, longueur_defense=50):
        super().__init__(nom, appetit, satisfaction, soigneur)
        self.longueur_defense = longueur_defense

    @property
    def longueur_defense(self):
        return self._longueur_defense

    @longueur_defense.setter
    def longueur_defense(self, value):
        if value < 0:
            raise ValueError("La longueur de défense doit être positive.")
        self._longueur_defense = value

    # --- Implémentations obligatoires ---

    def observer_environnement(self):
        print(f"{self.nom} observe avec sa mémoire d’éléphant.")

    def ramasser_objet(self):
        print(f"{self.nom} ramasse un objet avec sa trompe.")

    def probabilite_deces(self):
        """Plus l'appétit est bas, plus le risque augmente."""
        return max(0, 100 - self.appetit)

    # --- Comportements spécifiques ---

    def prendre_bain_de_boue(self):
        print(f"{self.nom} prend un bain de boue.")
        self._satisfaction = min(100, self._satisfaction + 15)

    def aspirer_eau(self):
        print(f"{self.nom} aspire de l'eau avec sa trompe.")

    def comportement_hasard(self):
        actions = [
            self.prendre_bain_de_boue,
            self.aspirer_eau,
            lambda: self.manger(10),
        ]
        random.choice(actions)()

    def __len__(self):
        return int(self.longueur_defense)
