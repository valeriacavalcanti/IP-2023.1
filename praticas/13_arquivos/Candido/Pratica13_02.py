'''
2. Escreva um programa que leia do teclado o nome
de um arquivo texto e uma string, abra o arquivo
e inclua no final dele a string lida.
'''
nomearq = input('Arquivo: ')
arq = open(nomearq,'a')
texto = input('Texto: ')
arq.write(texto + '\n')
arq.close()
print('Texto adicionado com sucesso')



