class Enclos:
    """Classe représentant un enclos dans le zoo."""

    def __init__(self, nom, capacite_max, taille):
        self.nom = nom
        self.capacite_max = capacite_max
        self._taille = taille
        self._liste_animaux = []

    # --- Propriétés ---

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        if not value.strip():
            raise ValueError("Le nom de l'enclos ne peut pas être vide.")
        self._nom = value

    @property
    def capacite_max(self):
        return self._capacite_max

    @capacite_max.setter
    def capacite_max(self, value):
        if value <= 0:
            raise ValueError("La capacité doit être positive.")
        self._capacite_max = value

    @property
    def taille(self):
        return self._taille

    @property
    def liste_animaux(self):
        return list(self._liste_animaux)

    # --- Méthodes ---

    def ajouter_animal(self, animal):
        if len(self._liste_animaux) >= self._capacite_max:
            raise ValueError("Enclos plein.")
        self._liste_animaux.append(animal)
        print(f"{animal.nom} ajouté dans l'enclos {self._nom}.")

    def afficher_animaux(self):
        print(f"\n--- Animaux dans l'enclos {self._nom} ---")
        if not self._liste_animaux:
            print("Aucun animal pour le moment.")
            return
        for animal in self._liste_animaux:
            print(f"- {animal} ({animal.__class__.__name__})")

    # --- Data model ---

    def __len__(self):
        return len(self._liste_animaux)

    def __iter__(self):
        return iter(self._liste_animaux)

    def __contains__(self, animal):
        return animal in self._liste_animaux

    def __repr__(self):
        return f"Enclos(nom={self.nom}, capacite={self.capacite_max}, nb_animaux={len(self)})"

    # --- Outils "pro" ---

    def trier_animaux_par_nom(self):
        self._liste_animaux.sort(key=lambda a: a.nom)

    def trier_animaux_par_satisfaction(self, reverse=True):
        self._liste_animaux.sort(key=lambda a: a.satisfaction, reverse=reverse)
