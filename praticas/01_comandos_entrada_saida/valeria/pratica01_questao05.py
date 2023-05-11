PESO1 = 6
PESO2 = 4

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = ((nota1 * PESO1) + (nota2 * PESO2)) / (PESO1 + PESO2)

print("Média = {:.2}".format(media))
