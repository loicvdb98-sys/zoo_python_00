from datetime import date, datetime

class Soigneur:
    """Classe représentant un soigneur du zoo."""

    def __init__(self, nom, date_naissance, experience=0, nb_animaux_responsable=0):
        self.nom = nom
        self._date_naissance = datetime.strptime(date_naissance, "%Y-%m-%d").date()
        self._experience = experience
        self._nb_animaux_responsable = nb_animaux_responsable

    # --- Propriétés ---

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        if not value.strip():
            raise ValueError("Le nom du soigneur ne peut pas être vide.")
        self._nom = value

    @property
    def date_naissance(self):
        return self._date_naissance

    @property
    def experience(self):
        return self._experience

    @property
    def nb_animaux_responsable(self):
        return self._nb_animaux_responsable

    @property
    def age(self):
        today = date.today()
        return today.year - self._date_naissance.year - (
            (today.month, today.day) < (self._date_naissance.month, self._date_naissance.day)
        )

    # --- Méthodes ---

    def nourrir(self, animal):
        if animal.soigneur != self._nom:
            print(f"{self._nom} n'est pas responsable de {animal.nom}.")
            return
        animal.manger(20)
        print(f"{animal.nom} a été nourri par {self._nom}.")

    def entretenir(self, animal):
        if animal.soigneur != self._nom:
            print(f"{self._nom} ne peut pas entretenir {animal.nom}.")
            return
        animal._satisfaction = min(100, animal._satisfaction + 10)
        print(f"{animal.nom} a été entretenu par {self._nom}.")

    def __str__(self):
        return f"Soigneur {self.nom} ({self.age} ans, {self.experience} ans d'expérience)"

    def __repr__(self):
        return f"Soigneur(nom={self.nom}, age={self.age}, experience={self.experience})"
