from models import Elephant, Soigneur, Enclos

def lire_int(message, min_val=None, max_val=None):
    while True:
        valeur = input(message)
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
    while True:
        texte = input(message).strip()
        if texte == "":
            print("❌ Erreur : ce champ ne peut pas être vide.")
        else:
            return texte


def afficher_menu():
    print("\n" + "=" * 45)
    print("        MENU DE GESTION DU ZOO")
    print("=" * 45)
    print("1. Ajouter un éléphant")
    print("2. Voir les animaux de l'enclos")
    print("3. Nourrir un animal")
    print("4. Entretenir un animal")
    print("5. Afficher l'état d'un animal")
    print("0. Quitter")
    print("=" * 45)


def choisir_animal(animaux):
    if not animaux:
        print("❌ Aucun animal disponible.")
        return None

    while True:
        print("\n--- Sélection d'un animal ---")
        for i, animal in enumerate(animaux):
            print(f"{i+1}. {animal.nom}")

        choix = input("Choisissez un animal : ")

        if not choix.isdigit():
            print("❌ Erreur : veuillez entrer un numéro.")
            continue

        choix = int(choix)

        if not (1 <= choix <= len(animaux)):
            print("❌ Erreur : numéro invalide.")
            continue

        return animaux[choix - 1]


def main():
    print("=== Gestion du Zoo : Mode Multi-Animaux ===\n")

    # --- Création du soigneur ---
    print("Création du soigneur :")
    nom_soigneur = lire_texte("Nom du soigneur : ")
    date_naissance = lire_texte("Date de naissance (YYYY-MM-DD) : ")
    experience = lire_int("Années d'expérience : ", 0)

    try:
        soigneur = Soigneur(nom_soigneur, date_naissance, experience)
    except Exception as e:
        print("❌ Erreur lors de la création du soigneur :", e)
        return

    print(f"Soigneur créé ! Âge : {soigneur.age} ans\n")

    # --- Création de l'enclos ---
    print("Création de l'enclos :")
    nom_enclos = lire_texte("Nom de l'enclos : ")
    capacite = lire_int("Capacité maximale : ", 1)
    taille = lire_int("Taille de l'enclos (m²) : ", 1)

    try:
        enclos = Enclos(nom_enclos, capacite, taille)
    except Exception as e:
        print("❌ Erreur lors de la création de l'enclos :", e)
        return

    animaux = []

    # --- Boucle principale ---
    while True:
        afficher_menu()
        choix = input("Votre choix : ").strip()

        # Ajouter un éléphant
        if choix == "1":
            while True:
                print("\n--- Ajout d'un éléphant ---")
                nom = lire_texte("Nom : ")
                appetit = lire_int("Appétit (0-100) : ", 0, 100)
                satisfaction = lire_int("Satisfaction (0-100) : ", 0, 100)

                try:
                    ele = Elephant(nom, appetit, satisfaction, soigneur.nom)
                    enclos.ajouter_animal(ele)
                    animaux.append(ele)
                    print(f"✔ Éléphant {nom} ajouté avec succès !")
                    break
                except Exception as e:
                    print("❌ Erreur :", e)
                    print("🔁 Réessayons...")

        # Voir les animaux
        elif choix == "2":
            enclos.afficher_animaux()

        # Nourrir un animal
        elif choix == "3":
            animal = choisir_animal(animaux)
            if animal:
                try:
                    soigneur.nourrir(animal)
                except Exception as e:
                    print("❌ Erreur :", e)

        # Entretenir un animal
        elif choix == "4":
            animal = choisir_animal(animaux)
            if animal:
                try:
                    soigneur.entretenir(animal)
                except Exception as e:
                    print("❌ Erreur :", e)

        # Afficher état d’un animal
        elif choix == "5":
            animal = choisir_animal(animaux)
            if animal:
                animal.afficher_etat()

        # Quitter
        elif choix == "0":
            print("Fermeture du programme...")
            break

        else:
            print("❌ Choix invalide, réessayez.")


if __name__ == "__main__":
    main()
