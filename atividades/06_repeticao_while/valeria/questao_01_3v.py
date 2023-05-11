num = int(input("Número: "))
if (num != 0):
    maior = num
    while (True):
        num = int(input("Número: "))
        if (num == 0):
            break
        if (num > maior):
            maior = num
    print(maior)
else:
    print("erro")
