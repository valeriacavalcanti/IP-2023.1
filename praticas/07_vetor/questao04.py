sorteio = [6,7,13,14,26]

for i in range(2):
    print("Aposta:", i + 1)
    # ler uma aposta
    distintos = []
    qtd = 0
    acertos = 0
    for j in range(8):
        num = int(input("Valor: "))
        if (num not in distintos):
            distintos.append(num)
        if (num >= 1) and (num <= 80):
            qtd += 1
        if (num in sorteio):
            acertos += 1

    # verificar se a aposta é válida
    if ((len(distintos) == 8) and (qtd == 8)):
        print(acertos)
    else:
        print("Aposta inválida")
        
