'''
4. Escreva um programa que crie um arquivo texto
resultante da concatenação de dois outros arquivos.
'''
nomearq1 = input('1º Arquivo: ')
nomearq2 = input('2º Arquivo: ')
nomearq3 = input('Novo Arquivo: ')
arq1 = open(nomearq1,'r')
arq2 = open(nomearq2,'r')
arq3 = open(nomearq3,'x')
texto1 = arq1.read()
texto2 = arq2.read()
texto3 = texto1 + texto2
arq3.write(texto3)
arq1.close()
arq2.close()
arq3.close()

print('Arquivo gerado com sucesso')
