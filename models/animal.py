from abc import ABC, abstractmethod
from functools import total_ordering

@total_ordering
class Animal(ABC):
    """Classe abstraite représentant un animal générique."""

    def __init__(self, nom, appetit=100, satisfaction=50, soigneur=None):
        self.nom = nom
        self._appetit = appetit
        self._satisfaction = satisfaction
        self.soigneur = soigneur
        self._en_vie = True

    # --- Propriétés communes ---

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        if not value.strip():
            raise ValueError("Le nom ne peut pas être vide.")
        self._nom = value

    @property
    def appetit(self):
        return self._appetit

    @property
    def satisfaction(self):
        return self._satisfaction

    @property
    def en_vie(self):
        return self._en_vie

    @property
    def soigneur(self):
        return self._soigneur

    @soigneur.setter
    def soigneur(self, value):
        if not value:
            raise ValueError("L'animal doit avoir un soigneur.")
        self._soigneur = value

    # --- Méthodes communes ---

    def manger(self, quantite):
        if quantite < 0:
            raise ValueError("La quantité doit être positive.")
        self._appetit = min(100, self._appetit + quantite)
        self._satisfaction = min(100, self._satisfaction + quantite // 2)

    # --- Méthodes abstraites obligatoires ---

    @abstractmethod
    def observer_environnement(self):
        pass

    @abstractmethod
    def ramasser_objet(self):
        """Chaque animal ramasse un objet différemment."""
        pass

    @abstractmethod
    def probabilite_deces(self):
        """Retourne un pourcentage de risque de décès."""
        pass

    # --- Méthodes spéciales (repr, eq, lt, getitem) ---

    def __str__(self):
        return f"{self.nom} (Appétit: {self.appetit}, Satisfaction: {self.satisfaction})"

    def __repr__(self):
        return f"Animal(nom={self.nom}, appetit={self.appetit}, satisfaction={self.satisfaction}, soigneur={self.soigneur})"

    def __eq__(self, other):
        if not isinstance(other, Animal):
            return NotImplemented
        return (self.nom, self.appetit, self.satisfaction) == (
            other.nom,
            other.appetit,
            other.satisfaction,
        )

    def __lt__(self, other):
        if not isinstance(other, Animal):
            return NotImplemented
        if self.nom != other.nom:
            return self.nom < other.nom
        return self.satisfaction > other.satisfaction

    def __getitem__(self, key):
        mapping = {
            "nom": self.nom,
            "appetit": self.appetit,
            "satisfaction": self.satisfaction,
            "soigneur": self.soigneur,
        }
        if key not in mapping:
            raise KeyError(f"Clé '{key}' inconnue pour Animal")
        return mapping[key]
