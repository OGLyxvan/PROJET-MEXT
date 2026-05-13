resultat = {
    "url" : "http://paypal-secure.tk",
    "longueur_suspecte" : True,
    "mot_suspect" : True,
    "http" : True,
    "extension_suspecte" : True,
    "score" : 3
}
for cle, valeur in resultat.items():
    print(f"{cle} : {valeur}")