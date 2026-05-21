from models import Elephant, Soigneur, Enclos

print("=== TESTS ===")

s = Soigneur("Marc", "1985-04-12", 10)
print("Âge du soigneur :", s.age)

e = Elephant("Dumbo", 80, 60, "Marc")
print("Appétit :", e.appetit)
print("Bonheur :", e.satisfaction)

en = Enclos("Savane", 2, 500)
en.ajouter_animal(e)
print("Animaux :", [a.nom for a in en.liste_animaux])
