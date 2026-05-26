import random
from .animal import Animal

class Girafe(Animal):
    """Classe représentant une girafe."""

    def __init__(self, nom, appetit=100, satisfaction=50, soigneur=None, longueur_cou=200):
        super().__init__(nom, appetit, satisfaction, soigneur)
        self.longueur_cou = longueur_cou

    # --- Propriété spécifique ---

    @property
    def longueur_cou(self):
        return self._longueur_cou

    @longueur_cou.setter
    def longueur_cou(self, value):
        if value <= 0:
            raise ValueError("La longueur du cou doit être positive.")
        self._longueur_cou = value

    # --- Comportements spécifiques ---

    def manger_feuilles(self):
        print(f"{self.nom} mange des feuilles en hauteur.")
        self._appetit = min(100, self._appetit + 10)

    def boire_eau(self):
        print(f"{self.nom} écarte ses pattes pour boire de l'eau.")

    # --- Polymorphisme : redéfinition ---

    def observer_environnement(self):
        print(f"{self.nom} observe l’environnement depuis les hauteurs.")

    # --- Comportement aléatoire ---

    def comportement_hasard(self):
        actions = [
            self.manger_feuilles,
            self.boire_eau,
            lambda: self.manger(10),
        ]
        action = random.choice(actions)
        action()

    # --- Méthodes spéciales ---

    def __len__(self):
        """Longueur de la girafe = longueur du cou."""
        return int(self.longueur_cou)

    def __str__(self):
        return f"Girafe {self.nom} (Cou: {self.longueur_cou} cm)"

    def __repr__(self):
        return f"Girafe(nom={self.nom}, cou={self.longueur_cou})"
