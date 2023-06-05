'''
4. Escreva um programa que leia uma frase e a
exiba na tela conforme o exemplo abaixo.
Exemplo:
Entrada:
ABCDE
Saída:
A
BB
CCC
DDDD
EEEEEE
DDDD
CCC
BB
A
'''
s = input()
n = len(s)
for i in range(n):
    print(s[i]*(i+1))
for i in range(n-2,-1,-1):
    print(s[i]*(i+1))
    
    





