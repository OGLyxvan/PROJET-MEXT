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
    resultat = {
    "url": url,
    "longueur_suspecte": False,
    "mot_suspect": False,
    "http": False,
    "extension_suspecte": False,
    "marque_suspecte": False,
    "score": 0
}
    suspects = False
    for j in mots_suspects:
        if j in url:
            resultat["mot_suspect"] = True
            resultat["score"] += 1
            break
    if len(url) > 30:
        resultat["longueur_suspecte"] = True
        resultat["score"] += 1
    if url.startswith("http://"):
        resultat["http"] = True
        resultat["score"] += 1
    if url.endswith(nom_de_domaine):
        resultat["extension_suspecte"] = True
        resultat["score"] += 1
    for k in marques:
        if k in url:
            resultat["marque_suspecte"] = True
            resultat["score"] += 1
            break
    if resultat["score"] >= 3:
        count_suspect += 1
        print(f"{url} -> 🚨 PHISHING DÉTECTÉ")
    elif resultat["score"] >= 1:
        print(f"{url} -> ⚠️ SUSPECTE")
    else:
        print(f"{url} -> ✅ URL NORMALE")
print(f"--- Résultat ---\n {count_suspect} URL(s) suspecte(s) trouvée(s) sur {count_total}\n")