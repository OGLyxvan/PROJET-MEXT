url = "http://paypal-secure-login-verify-account-password-reset.tk"
length = len(url)

if length > 50:
    print("URL TRES SUSPECTE")
elif length > 30 and length < 50:
    print("URL SUSPECTE")
else :
    print("URL NORMALE")