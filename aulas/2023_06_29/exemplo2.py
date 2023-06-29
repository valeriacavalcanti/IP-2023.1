arq = open('eita.txt', 'r')

for i in range(10):
    nome = "eita{}.txt".format(i)
    arq = open(nome, 'w')
    arq.close()
