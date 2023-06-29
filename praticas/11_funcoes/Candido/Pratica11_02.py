'''
02. Escreva uma função chamada print_e que receba
    como parâmetro uma string e um número inteiro
    “n” correspondente ao espaçamento que deseja
    imprimir a string. A função deverá exibir a
    string com “n” espaços em branco entre os
    símbolos.
'''
def print_e(s,n):
    for caracter in s:
        print(caracter,' '*n,sep='',end='')

palavra = input('Entre com a palavra: ')
espacos = int(input('Entre com o número de espaços em branco: '))
print_e(palavra,espacos)
