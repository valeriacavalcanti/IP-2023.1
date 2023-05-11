qtd = 0

while (True):
    nota = int(input("Nota: "))
    if (nota >= 0) and (nota <= 100):
        break
    qtd = qtd + 1

print(nota)
print(qtd)
