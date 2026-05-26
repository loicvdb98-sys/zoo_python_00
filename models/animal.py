from functools import total_ordering

@total_ordering
class Animal:
    """Classe parent représentant un animal générique."""

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

    def observer_environnement(self):
        print(f"{self.nom} observe calmement son environnement.")

    def afficher_etat(self):
        print(f"\n--- État de {self.nom} ---")
        print(f"Appétit : {self.appetit}/100")
        print(f"Satisfaction : {self.satisfaction}/100")
        print(f"Soigneur : {self.soigneur}")
        print(f"En vie : {'Oui' if self.en_vie else 'Non'}")

    # --- Méthodes spéciales (représentations) ---

    def __str__(self):
        return f"{self.nom} (Appétit: {self.appetit}, Satisfaction: {self.satisfaction})"

    def __repr__(self):
        return (
            f"Animal(nom={self.nom}, appetit={self.appetit}, "
            f"satisfaction={self.satisfaction}, soigneur={self.soigneur})"
        )

    # --- Comparaisons (Data Model) ---

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
        # Tri par nom, puis par satisfaction décroissante
        if self.nom != other.nom:
            return self.nom < other.nom
        return self.satisfaction > other.satisfaction

    # --- Accès façon dictionnaire ---

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
