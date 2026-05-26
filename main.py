from models import Elephant, Girafe, Soigneur, Enclos

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
    print("2. Ajouter une girafe")
    print("3. Voir les animaux de l'enclos")
    print("4. Nourrir un animal")
    print("5. Entretenir un animal")
    print("6. Observer un animal")
    print("7. Comportement au hasard")
    print("0. Quitter")
    print("=" * 45)

def choisir_animal(animaux):
    if not animaux:
        print("❌ Aucun animal disponible.")
        return None
    print("\n--- Sélection d'un animal ---")
    for i, animal in enumerate(animaux):
        print(f"{i+1}. {animal.nom} ({animal.__class__.__name__})")
    while True:
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
    print("=== Gestion du Zoo : Multi-Animaux ===\n")

    print("Création du soigneur :")
    nom_soigneur = lire_texte("Nom du soigneur : ")
    date_naissance = lire_texte("Date de naissance (YYYY-MM-DD) : ")
    experience = lire_int("Années d'expérience : ", 0)

    soigneur = Soigneur(nom_soigneur, date_naissance, experience)
    print(f"Soigneur créé ! Âge : {soigneur.age} ans\n")

    print("Création de l'enclos :")
    nom_enclos = lire_texte("Nom de l'enclos : ")
    capacite = lire_int("Capacité maximale : ", 1)
    taille = lire_int("Taille de l'enclos (m²) : ", 1)

    enclos = Enclos(nom_enclos, capacite, taille)
    animaux = []

    while True:
        afficher_menu()
        choix = input("Votre choix : ").strip()

        if choix == "1":
            print("\n--- Ajout d'un éléphant ---")
            nom = lire_texte("Nom : ")
            appetit = lire_int("Appétit (0-100) : ", 0, 100)
            satisfaction = lire_int("Satisfaction (0-100) : ", 0, 100)
            longueur_defense = lire_int("Longueur des défenses (cm) : ", 0)
            ele = Elephant(nom, appetit, satisfaction, soigneur.nom, longueur_defense)
            enclos.ajouter_animal(ele)
            animaux.append(ele)

        elif choix == "2":
            print("\n--- Ajout d'une girafe ---")
            nom = lire_texte("Nom : ")
            appetit = lire_int("Appétit (0-100) : ", 0, 100)
            satisfaction = lire_int("Satisfaction (0-100) : ", 0, 100)
            longueur_cou = lire_int("Longueur du cou (cm) : ", 1)
            gi = Girafe(nom, appetit, satisfaction, soigneur.nom, longueur_cou)
            enclos.ajouter_animal(gi)
            animaux.append(gi)

        elif choix == "3":
            enclos.afficher_animaux()

        elif choix == "4":
            animal = choisir_animal(animaux)
            if animal:
                soigneur.nourrir(animal)

        elif choix == "5":
            animal = choisir_animal(animaux)
            if animal:
                soigneur.entretenir(animal)

        elif choix == "6":
            animal = choisir_animal(animaux)
            if animal:
                animal.observer_environnement()

        elif choix == "7":
            animal = choisir_animal(animaux)
            if animal and hasattr(animal, "comportement_hasard"):
                animal.comportement_hasard()
            else:
                print("Cet animal n'a pas de comportement aléatoire défini.")

        elif choix == "0":
            print("Fermeture du programme...")
            break

        else:
            print("❌ Choix invalide, réessayez.")

if __name__ == "__main__":
    main()
