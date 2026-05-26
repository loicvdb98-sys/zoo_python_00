from models import Elephant, Girafe, Soigneur, Enclos

print("=== TESTS SIMPLES PRO+ ===")

s = Soigneur("Marc", "1985-04-12", 10)
print(s)

e = Elephant("Dumbo", 80, 60, s.nom, longueur_defense=120)
g = Girafe("Melman", 70, 50, s.nom, longueur_cou=250)

print("\n--- Polymorphisme observer_environnement() ---")
for animal in [e, g]:
    animal.observer_environnement()

print("\n--- Comportement_hasard() ---")
for animal in [e, g]:
    animal.comportement_hasard()

print("\n--- Enclos ---")
en = Enclos("Savane", 5, 500)
en.ajouter_animal(e)
en.ajouter_animal(g)
en.afficher_animaux()
print("Nombre d'animaux dans l'enclos :", len(en))

print("\n--- Comparaisons & tri ---")
print("e == g ?", e == g)
animaux = [g, e]
animaux.sort()
print("Tri par nom :")
for a in animaux:
    print("-", a.nom)

print("\n--- len() sur les animaux ---")
print("len(e) (défenses) :", len(e))
print("len(g) (cou)      :", len(g))

print("\n--- Enclos itérable ---")
for a in en:
    print("Dans enclos :", a.nom)
print("e dans enclos ?", e in en)
