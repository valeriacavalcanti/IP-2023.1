frase = input("Frase: ")

for i in range(len(frase)):
    print(frase[i] * (i + 1))

for i in range(len(frase) - 2, -1, -1):
    print(frase[i] * (i + 1))