'''
3. Escreva um programa para ler 6 números. Após a leitura dos
números, verifique, para cada um deles, se é distinto, ou seja,
não possui repetição.
'''
import random
n = 6
v = []
for i in range(n):
    v.append(random.randint(1,10))
print(*v)
for e in v:
    if v.count(e) > 1:
        print(e,'REPETE')
    else:
        print(e,'NÃO REPETE')

