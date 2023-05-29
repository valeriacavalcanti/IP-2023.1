frase = input("Frase: ")
lista = frase.split()

for i in range(len(lista)):
    for j in range(len(lista[i])):
        if (j == 0):
            print(lista[i][j].upper(), end='')
        else:
            print(lista[i][j], end='')
    print(' ', end='')
