'''
04. Escreva um programa para ler 03 (três) valores.
Calcule e exiba se estes valores formam triângulo.
'''
print('Digite o 3 valores:')
a = int(input())
b = int(input())
c = int(input())

ma = abs(b-c)
mb = abs(a-c)
mc = abs(a-b)

if ma<a and a<b+c and mb<b and b<a+c and mc<c and c<a+b:
    print('Sim')
else:
    print('Não')
