'''
3. Escreva um programa que abra um arquivo texto
e o exiba na tela com todas as suas linhas
numeradas sequencialmente.
'''
nomearq = input('Arquivo: ')
arq = open(nomearq,'r')
lista = arq.readlines()
for i in range(len(lista)):
    print(i+1,lista[i],end='')
arq.close()
    
