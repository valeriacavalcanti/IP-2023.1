'''
04. Escreva um programa para ler 03 (três) valores.
Calcule e exiba se estes valores formam triângulo.
'''
print('Digite o 3 valores:')
a = int(input())
b = int(input())
c = int(input())

if a < b+c and b < a+c and c < a+b:
    print('Sim')
else:
    print('Não')
