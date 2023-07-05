'''
1. Escreva um programa que copie um arquivo texto
(cujo nome será lido pelo teclado) para um novo
arquivo chamado COPIA.TXT, porém substituindo
todos os brancos contidos no arquivo pelo ponto.
'''
nomearq = input('Arquivo: ')
arq = open(nomearq,'r')
cop = open('COPIA.TXT','w')
texto = arq.read()
novotexto = texto.replace(' ','.')
cop.write(novotexto)
arq.close()
cop.close()
print('Arquivo COPIA.TXT gerado com sucesso')
