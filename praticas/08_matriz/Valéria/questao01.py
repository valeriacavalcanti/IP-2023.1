import random

# alocar as matrizes A, B e C

ma = []
mb = []
mc = []

for i in range(2):
    ma.append([None] * 3)
    mb.append([None] * 3)
    mc.append([None] * 3)

print("A:", ma)
print("B:", mb)
print("C:", mc)

# gerar valores aleatórios na matriz A
for i in range(2):
    for j in range(3):
        ma[i][j] = random.randint(1, 10)

# gerar valores aleatórios na matriz C
for i in range(2):
    for j in range(3):
        mb[i][j] = random.randint(1, 10)

# gerar a matriz C
for i in range(2):
    for j in range(3):
        mc[i][j] = ma[i][j] + mb[i][j]

print("A:", ma)
print("B:", mb)
print("C:", mc)

for i in range(2):
    for j in range(3):
        print(mc[i][j], end=' ')
    print()