prenom = input("Quel est votre prénom ? ")
age = input("Quel est votre âge ? ")
annee = input("En quelle année sommes nous ? ")
age = int(age)
annee = int(annee)
c = annee - age
c = str(c)
print(prenom + ", vous êtes donc nés en " + c + ".")
