frase = input("Frase: ")
frase = frase.replace(" ", "")
frase = frase.upper()

palindromo = True
for i in range(len(frase) // 2):
    if (frase[i] != frase[-1 - i]):
        palindromo = False
        break

if (palindromo == True):
    print("Sim")
else:
    print("Não")