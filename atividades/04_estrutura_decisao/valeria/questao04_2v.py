# versão 2.0

n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
n3 = int(input("Terceiro valor: "))


if (n1 > n2) and (n1 > n3):
    maior = n1
    soma = n2 + n3
else:
    if (n2 > n3):
        maior = n2
        soma = n1 + n3
    else:
        maior = n3
        soma = n1 + n2

if (maior < soma):
    print("forma")
else:
    print("não forma")
