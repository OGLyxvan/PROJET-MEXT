urls = [
    "http://paypal-secure.tk",
    "https://google.com",
    "http://apple-gagnant-prix-verify.tk",
    "https://github.com"
]
count_suspect = 0

for i in urls:
    if (len(i) > 30):
        print(f"{i} -> URL SUSPECTE")
        count_suspect = count_suspect + 1
    else:
        print(f"{i} -> URL NORMALE")
        
print(f"--- Résultat ---\n {count_suspect} URL(s) suspecte(s) trouvée(s) sur 4\n")    