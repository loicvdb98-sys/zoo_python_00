import random
from .animal import Animal

class Girafe(Animal):
    """Classe représentant une girafe."""

    def __init__(self, nom, appetit=100, satisfaction=50, soigneur=None, longueur_cou=200):
        super().__init__(nom, appetit, satisfaction, soigneur)
        self.longueur_cou = longueur_cou

    @property
    def longueur_cou(self):
        return self._longueur_cou

    @longueur_cou.setter
    def longueur_cou(self, value):
        if value <= 0:
            raise ValueError("La longueur du cou doit être positive.")
        self._longueur_cou = value

    # --- Implémentations obligatoires ---

    def observer_environnement(self):
        print(f"{self.nom} observe depuis les hauteurs.")

    def ramasser_objet(self):
        print(f"{self.nom} attrape un objet avec sa longue langue.")

    def probabilite_deces(self):
        return max(0, 100 - self.satisfaction)

    # --- Comportements spécifiques ---

    def manger_feuilles(self):
        print(f"{self.nom} mange des feuilles en hauteur.")
        self._appetit = min(100, self._appetit + 10)

    def boire_eau(self):
        print(f"{self.nom} écarte ses pattes pour boire.")

    def comportement_hasard(self):
        actions = [
            self.manger_feuilles,
            self.boire_eau,
            lambda: self.manger(10),
        ]
        random.choice(actions)()

    def __len__(self):
        return int(self.longueur_cou)
