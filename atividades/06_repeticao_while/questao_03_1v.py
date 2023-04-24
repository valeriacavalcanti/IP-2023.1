num = int(input("Número: "))
if (num % 2 == 0):
    print("par")
else:
    print("ímpar")

resposta = input("Deseja continuar (s ou n): ")
while (resposta == 's'):
    num = int(input("Número: "))
    if (num % 2 == 0):
        print("par")
    else:
        print("ímpar")
    resposta = input("Deseja continuar (s ou n): ")
