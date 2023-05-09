maior = qtde = 0
altura = float(input('Altura: '))
largura = float(input('Largura: '))
profundidade = float(input('Profundidade: '))

while (altura == largura) and (altura == profundidade) and (altura > 0):
    qtde = qtde + 1
    if (altura > maior):
        maior = altura
    altura = float(input('Altura: '))
    largura = float(input('Largura: '))
    profundidade = float(input('Profundidade: '))

print("Quantidade:", qtde)
if (qtde > 0):
    print("Maior aresta:", maior)
else:
    print("Nenhum cubo informado.")
