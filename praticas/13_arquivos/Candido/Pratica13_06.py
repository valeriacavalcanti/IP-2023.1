'''
6. Escreva um programa que leia o arquivo gerado
na questão 5 e copie os nomes distribuindo para
dois novos arquivos: homens.txt e mulheres.txt
(sendo um nome por linha).
'''
arq = open('CADASTRO.TXT','r')
hom = open('HOMENS.TXT','w')
mul = open('MULHERES.TXT','w')

for linha in arq:
    lista = linha.split(',')
    nome = lista[0]
    sexo = lista[1]
    if sexo == 'M':
        hom.write(nome+'\n')
    else:
        mul.write(nome+'\n')
arq.close()
hom.close()
mul.close()
print('Arquivos gerados com sucesso')

        
