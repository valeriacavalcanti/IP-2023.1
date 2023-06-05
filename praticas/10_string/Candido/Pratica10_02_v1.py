'''
2. Escreva um programa que leia o nome de uma
pessoa e exiba-o no formato bibliográfico (veja o
exemplo abaixo).
Obs: suponha que o nome lido não possua nenhuma
preposição, artigo, etc.
Exemplo:
Entrada: FLAVIO RIBEIRO COUTINHO
Saída: COUTINHO, F. R.
'''
nome = input().upper()
lista = nome.split()
print(f'{lista[-1]}, ',end='')
for i in range(len(lista)-1):
    print(f'{lista[i][0]}. ',end='')
