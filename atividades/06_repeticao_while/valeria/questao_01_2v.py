num = int(input("Número: "))

if (num != 0):
    maior = num

    while (num != 0):
        if (num > maior):
            maior = num
        num = int(input("Número: "))

    print(maior)
else:
    print("erro")
