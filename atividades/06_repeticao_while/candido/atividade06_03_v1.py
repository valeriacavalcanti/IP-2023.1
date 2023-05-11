'''
03. Escreva um programa para ler um número inteiro e
informar se é par ou ímpar. Ao final, o programa deverá
perguntar se o usuário deseja continuar (ou seja, digitar
outro valor) ou sair. Se o usuário desejar continuar, o
programa deverá repetir tudo novamente, caso contrário
deverá encerrar.
'''
resp = 'S'
while resp == 'S':
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        print('par')
    else:
        print('ímpar')
    resp = input('Deseja continuar (S/N)?').upper()
print('Fim do programa')
    
        
