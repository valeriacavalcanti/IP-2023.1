'''
3. Escreva um programa que abra um arquivo texto
e o exiba na tela com todas as suas linhas
numeradas sequencialmente.
'''
nomearq = input('Arquivo: ')
arq = open(nomearq,'r')
cont = 0
for linha in arq:
    cont += 1
    print(cont,linha,end='')
arq.close()
    
