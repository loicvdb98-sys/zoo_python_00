class Elephant:
    """Classe représentant un éléphant dans le zoo."""

    def __init__(self, nom, appetit=100, satisfaction=50, soigneur=None):
        self.nom = nom
        self._appetit = appetit
        self._satisfaction = satisfaction
        self._en_vie = True
        self.soigneur = soigneur

    # --- Propriétés ---

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        if not value.strip():
            raise ValueError("Le nom de l'éléphant ne peut pas être vide.")
        self._nom = value

    @nom.deleter
    def nom(self):
        print("Suppression du nom de l'éléphant.")
        del self._nom

    @property
    def appetit(self):
        return self._appetit  # lecture seule

    @property
    def satisfaction(self):
        return self._satisfaction  # lecture seule

    @property
    def en_vie(self):
        return self._en_vie  # lecture seule

    @property
    def soigneur(self):
        return self._soigneur

    @soigneur.setter
    def soigneur(self, value):
        if value is None or value == "":
            raise ValueError("Un éléphant doit avoir un soigneur.")
        self._soigneur = value

    # --- Méthodes ---

    def manger(self, quantite):
        if quantite < 0:
            raise ValueError("La quantité de nourriture doit être positive.")

        if not self._en_vie:
            print(f"{self._nom} ne peut plus manger, il est mort.")
            return

        self._appetit = min(100, self._appetit + quantite)
        self._satisfaction = min(100, self._satisfaction + quantite // 2)

        if self._appetit <= 0:
            self._en_vie = False

    def afficher_etat(self):
        print(f"\n--- État de {self._nom} ---")
        print(f"Appétit : {self._appetit}/100")
        print(f"Satisfaction : {self._satisfaction}/100")
        print(f"Soigneur : {self._soigneur}")
        print(f"En vie : {'Oui' if self._en_vie else 'Non'}")
