'''
02. Um professor realizou 03 (três) avaliações e ofereceu
a turma a possibilidade de calcular a média de duas formas,
podendo ser: aritmética ou ponderada (pesos: 4, 6 e 8).
Escreva um programa para ler as 03(três) notas de um aluno
e informar qual seria a melhor opção. Em caso de empate
informe: tanto faz.
'''
p1 = 4
p2 = 6
p3 = 8
n1 = float(input('1ª nota: '))
n2 = float(input('2ª nota: '))
n3 = float(input('3ª nota: '))
ma = (n1 + n2 + n3) / 3
mp = (n1 * p1 + n2 * p2 + n3 * p3) / (p1 + p2 + p3)
if ma > mp:
    print(f'Melhor: Média Aritmética = {ma:.1f}')
if ma < mp:
    print(f'Melhor: Média Ponderada = {mp:.1f}')
if ma == mp:
    print(f'Tanto faz: Média = {ma:.1f}')

    
    
