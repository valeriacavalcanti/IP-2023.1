qtd = soma = 0

while (True):
    idade = int(input('Idade: '))
    if (idade < 0):
        break
    soma = soma + idade
    qtd = qtd + 1

if (qtd > 0):
    media = soma / qtd
    print(media)
else:
    print('erro')
