frase = input("Frase: ")
frase = frase.replace(" ", "")
frase = frase.upper()
if (frase == frase[::-1]):
    print("SIM")
else:
    print("NÃO")