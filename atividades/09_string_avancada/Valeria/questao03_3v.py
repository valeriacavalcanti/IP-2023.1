frase = input("Frase: ").replace(" ", "").upper()
if (frase == frase[::-1]):
    print("SIM")
else:
    print("NÃO")