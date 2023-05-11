# versão 1.0

n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
n3 = int(input("Terceiro valor: "))


if (n1 < n2 + n3) and (n2 < n1 + n3) and (n3 < n1 + n2):
    print("Forma")
else:
    print("Não forma")
