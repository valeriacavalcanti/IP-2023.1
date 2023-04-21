soma = qtd = 0

idade = int(input('Idade: '))
while (idade >= 0):
    soma = soma + idade
    qtd = qtd + 1

    idade = int(input('Idade: '))

if (qtd > 0):
    media = soma / qtd
    print(media)
else:
    print('erro')
