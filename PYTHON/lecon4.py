urls = [
    "http://paypal-secure.tk",
    "https://google.com",
    "http://apple-gagnant-prix-verify.tk",
    "https://github.com"
]
count_suspect = 0
mots_suspects = ["secure", "verify", "login", "password", "account"]
nom_de_domaine = (".tk", ".xyz", ".ml")
marques = ["paypal", "apple", "amazon", "microsoft", "paypal-secure", "apple-login"]

for i in urls:
    suspects = False
    if (len(i) > 30):
        suspects = True
    for j in mots_suspects:
        if j in i:
            suspects = True
            break
    if suspects == True:
        count_suspect += 1
    if i.startswith("http://"):
        suspects = True
    if i.endswith(nom_de_domaine):
        suspects = True
    for k in marques:
        if k in i:
            suspects = True
            break
    if suspects:
        print(f"{i} -> SUSPECT")
    else:
        print(f"{i} -> NORMALE")
print(f"--- Résultat ---\n {count_suspect} URL(s) suspecte(s) trouvée(s) sur 4\n")