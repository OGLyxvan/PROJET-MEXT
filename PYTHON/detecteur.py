count_suspect = 0
mots_suspects = ["secure", "verify", "login", "password", "account"]
nom_de_domaine = (".tk", ".xyz", ".ml")
marques = ["paypal", "apple", "amazon", "microsoft", "paypal-secure", "apple-login"]
count_total = 0

while True:
    url = input("Entre une URL (ou 'quit' pour quitter) : ")
    if url == 'quit':
        break
    count_total += 1
    suspects = False
    for j in mots_suspects:
        if j in url:
            suspects = True
            break
    if len(url) > 30:
        suspects = True
    if url.startswith("http://"):
        suspects = True
    if url.endswith(nom_de_domaine):
        suspects = True
    for k in marques:
        if k in url:
            suspects = True
            break
    if suspects == True:
        count_suspect += 1    
    if suspects:
        print(f"{url} -> 🚨 PHISHING DÉTECTÉ")
    else:
        print(f"{url} -> ✅ URL NORMALE")
print(f"--- Résultat ---\n {count_suspect} URL(s) suspecte(s) trouvée(s) sur {count_total}\n")