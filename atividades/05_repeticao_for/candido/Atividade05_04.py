'''
04. Escreva um programa, em Python, para ler as notas de
40 (quarenta) alunos. Com base na tabela, a seguir,
informe a porcentagem de alunos aprovados e reprovados.
    Nota      Situação
 70 até 100   Aprovado
 40 até 69    Final
  0 até 39    Reprovado 
'''
qtd = 4
contA = 0
contR = 0
print(f'Digite a nota dos {qtd} alunos:')
for i in range(qtd):
    nota = int(input('Nota: '))
    if nota >= 70:
        contA = contA + 1
    if nota < 40:
        contR = contR + 1
percA = contA / qtd * 100
percR = contR / qtd * 100
print(f'Porcentagem de Aprovados = {percA:.1f}%')
print(f'Porcentagem de Reprovados = {percR:.1f}%')





        
