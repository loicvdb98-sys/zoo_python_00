from models import Elephant, Girafe, Soigneur, Enclos

# ------------------------------
# OUTILS DE LECTURE UTILISATEUR
# ------------------------------

def lire_int(message, min_val=None, max_val=None):
    """Lecture sécurisée d'un entier."""
    while True:
        valeur = input(message).strip()
        if not valeur.isdigit():
            print("❌ Erreur : veuillez entrer un nombre valide.")
            continue

        valeur = int(valeur)

        if min_val is not None and valeur < min_val:
            print(f"❌ Erreur : la valeur doit être ≥ {min_val}.")
            continue

        if max_val is not None and valeur > max_val:
            print(f"❌ Erreur : la valeur doit être ≤ {max_val}.")
            continue

        return valeur


def lire_texte(message):
    """Lecture sécurisée d'un texte non vide."""
    while True:
        texte = input(message).strip()
        if texte == "":
            print("❌ Erreur : ce champ ne peut pas être vide.")
        else:
            return texte


# ------------------------------
# MENU
# ------------------------------

def afficher_menu():
    print("\n" + "=" * 50)
    print("           MENU DE GESTION DU ZOO")
    print("=" * 50)
    print("1. Ajouter un éléphant")
    print("2. Ajouter une girafe")
    print("3. Voir les animaux de l'enclos")
    print("4. Nourrir un animal")
    print("5. Entretenir un animal")
    print("6. Observer un animal")
    print("7. Comportement au hasard")
    print("8. Trier les animaux par nom")
    print("9. Ramasser un objet")
    print("10. Voir probabilité de décès")
    print("0. Quitter")
    print("=" * 50)


def choisir_animal(animaux):
    """Sélectionne un animal dans la liste."""
    if not animaux:
        print("❌ Aucun animal disponible.")
        return None

    print("\n--- Sélection d'un animal ---")
    for i, animal in enumerate(animaux):
        print(f"{i+1}. {animal.nom} ({animal.__class__.__name__})")

    while True:
        choix = input("Choisissez un animal : ").strip()
        if not choix.isdigit():
            print("❌ Erreur : veuillez entrer un numéro.")
            continue

        choix = int(choix)
        if not (1 <= choix <= len(animaux)):
            print("❌ Erreur : numéro invalide.")
            continue

        return animaux[choix - 1]


# ------------------------------
# PROGRAMME PRINCIPAL
# ------------------------------

def main():
    print("=== Gestion du Zoo : Version PRO++ ===\n")

    # Création du soigneur
    print("Création du soigneur :")
    nom_soigneur = lire_texte("Nom du soigneur : ")
    date_naissance = lire_texte("Date de naissance (YYYY-MM-DD) : ")
    experience = lire_int("Années d'expérience : ", 0)

    soigneur = Soigneur(nom_soigneur, date_naissance, experience)
    print(f"\nSoigneur créé ! Âge : {soigneur.age} ans\n")

    # Création de l'enclos
    print("Création de l'enclos :")
    nom_enclos = lire_texte("Nom de l'enclos : ")
    capacite = lire_int("Capacité maximale : ", 1)
    taille = lire_int("Taille de l'enclos (m²) : ", 1)

    enclos = Enclos(nom_enclos, capacite, taille)
    animaux = []

    # Boucle principale
    while True:
        afficher_menu()
        choix = input("Votre choix : ").strip()

        # ------------------------------
        # AJOUT D'UN ÉLÉPHANT
        # ------------------------------
        if choix == "1":
            print("\n--- Ajout d'un éléphant ---")
            nom = lire_texte("Nom : ")
            appetit = lire_int("Appétit (0-100) : ", 0, 100)
            satisfaction = lire_int("Satisfaction (0-100) : ", 0, 100)
            longueur_defense = lire_int("Longueur des défenses (cm) : ", 0)

            ele = Elephant(nom, appetit, satisfaction, soigneur.nom, longueur_defense)
            enclos.ajouter_animal(ele)
            animaux.append(ele)

        # ------------------------------
        # AJOUT D'UNE GIRAFE
        # ------------------------------
        elif choix == "2":
            print("\n--- Ajout d'une girafe ---")
            nom = lire_texte("Nom : ")
            appetit = lire_int("Appétit (0-100) : ", 0, 100)
            satisfaction = lire_int("Satisfaction (0-100) : ", 0, 100)
            longueur_cou = lire_int("Longueur du cou (cm) : ", 1)

            gi = Girafe(nom, appetit, satisfaction, soigneur.nom, longueur_cou)
            enclos.ajouter_animal(gi)
            animaux.append(gi)

        # ------------------------------
        # AFFICHER ANIMAUX
        # ------------------------------
        elif choix == "3":
            enclos.afficher_animaux()

        # ------------------------------
        # NOURRIR
        # ------------------------------
        elif choix == "4":
            animal = choisir_animal(animaux)
            if animal:
                soigneur.nourrir(animal)

        # ------------------------------
        # ENTRETENIR
        # ------------------------------
        elif choix == "5":
            animal = choisir_animal(animaux)
            if animal:
                soigneur.entretenir(animal)

        # ------------------------------
        # OBSERVER
        # ------------------------------
        elif choix == "6":
            animal = choisir_animal(animaux)
            if animal:
                animal.observer_environnement()

        # ------------------------------
        # COMPORTEMENT HASARD
        # ------------------------------
        elif choix == "7":
            animal = choisir_animal(animaux)
            if animal:
                animal.comportement_hasard()

        # ------------------------------
        # TRIER PAR NOM
        # ------------------------------
        elif choix == "8":
            if not animaux:
                print("❌ Aucun animal à trier.")
            else:
                enclos.trier_animaux_par_nom()
                print("✅ Animaux triés par nom.")
                enclos.afficher_animaux()

        # ------------------------------
        # RAMASSER OBJET
        # ------------------------------
        elif choix == "9":
            animal = choisir_animal(animaux)
            if animal:
                animal.ramasser_objet()

        # ------------------------------
        # PROBABILITÉ DE DÉCÈS
        # ------------------------------
        elif choix == "10":
            animal = choisir_animal(animaux)
            if animal:
                print(f"⚠ Probabilité de décès : {animal.probabilite_deces()}%")

        # ------------------------------
        # QUITTER
        # ------------------------------
        elif choix == "0":
            print("Fermeture du programme...")
            break

        else:
            print("❌ Choix invalide, réessayez.")


if __name__ == "__main__":
    main()
