while (True):
    num = int(input("Número: "))
    if (num % 2 == 0):
        print("par")
    else:
        print("ímpar")
        
    resposta = input("Deseja continuar (s ou n): ")
    if (resposta == 'n'):
        break
