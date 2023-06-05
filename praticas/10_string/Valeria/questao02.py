partes = input("Nome: ").upper().split()

print(partes[-1], end=', ')

i = -1
for i in range(len(partes) - 2):
    print(partes[i][0], end='. ')

print(partes[i+1][0], end='.')