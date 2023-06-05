vogais = consoantes = 0

frase = input("Digite a frase: ")
frase = frase.upper()

for simbolo in frase:
    if (simbolo.isalpha()):
        if (simbolo in "AEIOU"):
            vogais += 1
        else:
            consoantes += 1

print(vogais, consoantes)