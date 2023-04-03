nota1 = int(input("Nota 1: "))
nota2 = int(input("Nota 2: "))
nota3 = int(input("Nota 3: "))

# nota1, nota2, nota3 = input('Notas: ').split()
# nota1, nota2, nota3 = int(nota1), int(nota2), int(nota3)

ma = (nota1 + nota2 + nota3) / 3
mp = ((nota1 * 4) + (nota2 * 6) + (nota3 * 8)) / 18

if (ma > mp):
    print("Aritmética")
elif (ma < mp):
    print("Ponderada")
else:
    print("tanto faz")
