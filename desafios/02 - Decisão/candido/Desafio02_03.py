inicio = int(input('Início: '))
final = int(input('Final: '))
if inicio < final:
    duracao = final - inicio
else:
    duracao = 24 - inicio + final
print(f'O JOGO DUROU {duracao} HORA(S)')
