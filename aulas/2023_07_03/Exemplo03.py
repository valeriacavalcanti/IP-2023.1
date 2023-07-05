#usando o readlines()
arq = open('Arquivo.txt','r')
lista = arq.readlines()
for linha in lista:
    print(linha,end='')
arq.close()
