dictionnaire_mots = {
  "vie": "existence",
  "belle": "jolie",
  "sorcier":"magique"}

phrase = input("Entrez votre phrase : ")

nouveaux_mots = []

for mot in phrase.split():
  if mot in dictionnaire_mots:
    nouveaux_mots.append(dictionnaire_mots[mot])
  else:
    signification_mot = input(f"Quel est le synonyme de '{mot}' ? ")
    dictionnaire_mots[mot] = signification_mot
    nouveaux_mots.append(signification_mot)

    


print(" ".join(nouveaux_mots))