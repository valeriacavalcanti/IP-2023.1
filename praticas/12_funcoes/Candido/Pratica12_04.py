'''
4. Escreva um programa que calcule e imprima o valor do cosseno de X
   através de 20 termos da série abaixo:
   < FIGURA >
   Observações:
   • O valor de X será lido.
   • Escreva uma função para o cálculo do fatorial e outra para o
     cálculo da potência.
   • Compare o resultado do seu programa com o resultado da função:
     math.cos(numero) - retorna o cosseno do número em radiano
     (da biblioteca math).
'''
#Função para calcular o fatorial
def fat(n):
    f = 1
    for i in range(1,n+1):
        f *= i
    return f

#Função para calcular a potência
def pot(b,e):
    return b ** e

#Programa principal
import math
x = float(input('Entre com o valor de x: '))
n = 0
s = 0
for i in range(1,21):
    t = pot(x,n) / fat(n)
    if i % 2 == 1:
        s += t
    else:
        s -= t
    n += 2
print('Meu resultado:',s)
print('Função cos(x):',math.cos(x))
