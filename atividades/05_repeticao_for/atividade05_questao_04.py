aprovado = reprovado = 0
total = 4

for i in range(total):
    nota = int(input("Nota: "))

    if (nota >= 70):
        aprovado = aprovado + 1
    else:
        if (nota < 40):
            reprovado = reprovado + 1

p_aprovado = (aprovado / total) * 100
p_reprovado = (reprovado / total) * 100

print("Aprovado = {}%".format(p_aprovado))
print("Reprovado = {}%".format(p_reprovado))
