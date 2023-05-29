frase = input("Frase: ")
lista = frase.split()

for i in range(len(lista)):
    print(f"{lista[i][0].upper()}{lista[i][1:]}", end=' ')