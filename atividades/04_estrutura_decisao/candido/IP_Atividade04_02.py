'''
2. Uma nota é considerada válida no sistema Suap se estiver
entre 0 (zero) e 100(cem), inclusive.
Escreva um programa para ler uma nota e informar se esta
nota é válida para o Suap.
'''
nota = int(input('Nota: '))
if nota >= 0 and nota <= 100:
    print('sim')
else:
    print('não')
