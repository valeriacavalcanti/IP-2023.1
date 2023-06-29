'''
03. Escreva uma função chamada soma que receba um
    vetor e retorne a soma dos seus elementos
    (obs: não use a função sum)
'''
def soma(v):
    s = 0
    for elem in v:
        s += elem
    return s

num = int(input('Digite o tamanho do vetor: '))
vetor = [None]*num
print('Digite os elementos do vetor:')
for i in range(num):
    vetor[i] = int(input())
print('Soma =',soma(vetor))
print('Soma =',sum(vetor))
