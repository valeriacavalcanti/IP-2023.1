import random

# alocar matriz original (3x5)
original = []
for i in range(3):
    original.append([None] * 5)

# alocar matriz transposta (5x3)
transposta = []
for i in range(5):
    transposta.append([None] * 3)

# gerar os valores da matriz original
for i in range(3):
    for j in range(5):
        original[i][j] = random.randint(1,9)

# copiar os valores da original para a transposta
for i in range(5):
    for j in range(3):
        transposta[i][j] = original[j][i]

# exibir matriz original
for i in range(3):
    for j in range(5):
        print(original[i][j], end=' ')
    print()

# exibir matriz transposta
for i in range(5):
    for j in range(3):
        print(transposta[i][j], end=' ')
    print()