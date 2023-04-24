qtd = 0
num = 1

while (num > 0):
    num = int(input("Número: "))
    if (num <= 0):
        break
    qtd = qtd + 1
    # exibir os divisores
    for i in range(1, num + 1):
        if (num % i == 0):
            print(i)

print("Quantidade:", qtd)
