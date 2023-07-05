#usando o for
arq = open('Arquivo.txt','r')
for linha in arq:
    print(linha,end='')
arq.close()
