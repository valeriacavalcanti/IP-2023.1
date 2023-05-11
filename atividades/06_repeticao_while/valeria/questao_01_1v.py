num = int(input("Número: "))
maior = num

while (num != 0):
    if (num > maior):
        maior = num
    num = int(input("Número: "))

if (maior != 0):
    print(maior)
else:
    print("erro")
