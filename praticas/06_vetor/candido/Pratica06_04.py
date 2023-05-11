'''
4. Escreva um programa para ler 6 números distintos, ou seja,
não podem repetir.
Imprima os números lidos.
'''
v = []
while len(v) < 6:
    n = int(input('Digite um número: '))
    if n not in v:
        v.append(n)
print(*v)
    

