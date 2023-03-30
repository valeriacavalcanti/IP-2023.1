desc = input('Descrição: ')
qtde = int(input('Quantidade: '))
valor = float(input('Valor: '))

total = qtde * valor

print('Total = R$ {:.2f}'.format(total))

if (total <= 10):
    print('que bom!')
    print('pode comprar')
else:
    print('não pode comprar')
    print('que ruim')

# calcular o desconto e atualizar o total
if (total > 50):
    desconto = total * 0.2
    total = total - desconto

print('Total = R$ {:.2f}'.format(total))
