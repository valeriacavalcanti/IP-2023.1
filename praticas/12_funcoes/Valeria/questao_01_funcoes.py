def criar_vetor(n):
    vetor = [0] * n
    for i in range(n):
        vetor[i] = int(input('Valor:'))
    return vetor

def somar(vetor):
    total = 0
    for num in vetor:
        total += num
    return total

def calcular_media(vetor):
    return somar(vetor)/len(vetor)

def verificar_abaixo(vetor, valor):
    qtd = 0
    for num in vetor:
        if (num < valor):
            qtd += 1
    return qtd

