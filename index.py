dictionnaire_mots = {
  "vie": "existance",
  "belle": "jolie"}

phrase = input("Entrez votre phrase : ")

nouveaux_mots = []

for mot in phrase.split():
  if mot in dictionnaire_mots:
    nouveaux_mots.append(dictionnaire_mots[mot])
  else:
    nouveaux_mots.append(mot)

print(" ".join(nouveaux_mots))