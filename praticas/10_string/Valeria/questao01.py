meses = 'janeiro fevereiro marco abril maio junho julho agosto setembro outubro novembro dezembro'.split()

dia, mes, ano = input("Data: ").split('/')
mes = int(mes)

print(f'{dia} de {meses[mes - 1]} de {ano}')