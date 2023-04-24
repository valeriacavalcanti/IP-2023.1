qtd = 0

nota = int(input("Nota: "))
while (nota < 0) or (nota > 100):
    qtd = qtd + 1
    nota = int(input("Nota: "))

print(nota)
print(qtd)
