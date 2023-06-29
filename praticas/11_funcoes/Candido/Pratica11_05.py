'''
05. Escreva um programa que leia as 3 notas de um
aluno, determine e exiba a sua média e seu conceito.
O programa deve conter as seguintes funções:
• Uma função que recebe como parâmetros as 3 notas
do aluno e retorne a sua média(aritmética).
• Uma função que receba como parâmetro a média do
aluno e retorne o seu conceito, de acordo com a
tabela abaixo:
   MÉDIA   CONCEITO
    8,0       A
5,0 e < 8,0   B
  < 5,0       C
'''
def media(a,b,c):
    return (a+b+c)/3

def conceito(m):
    if m >= 8.0:
        return 'A'
    elif m >= 5.0:
        return 'B'
    else:
        return 'C'

n1 = int(input('1ª Nota: '))
n2 = int(input('2ª Nota: '))
n3 = int(input('3ª Nota: '))
med = media(n1,n2,n3)
conc = conceito(med)
print('Média =',med)
print('Conceito =',conc)






    
