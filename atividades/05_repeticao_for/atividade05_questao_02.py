num = int(input("Número: "))

# Os números inteiros entre 1 e esse número lido, inclusive.
for i in range(1, num + 1):
    print(i, end=" ")

print() # pular a linha

# Os divisores desse número.
soma = 0
qtde = 0
for i in range(1, num + 1):
    if (num % i == 0):
        print(i, end=" ")
        qtde = qtde + 1
        soma = soma + i

print() # pular a linha

# Se este é um número primo.
if (qtde == 2):
    print("Primo")
else:
    print("Não é primo")

# Se este é um número perfeito ou não.
if (soma - num == num):
    print("Perfeito")
else:
    print("Não é perfeito")

# Fatorial desse número.
fat = 1
for i in range(num, 0, -1):
    fat = fat * i

print("Fatorial =", fat)
