qtd = 0

num = int(input("Número: "))
while (num > 0):
    qtd = qtd + 1
    # exibir os divisores
    for i in range(1, num + 1):
        if (num % i == 0):
            print(i)
    num = int(input("Número: "))

print("Quantidade:", qtd)
