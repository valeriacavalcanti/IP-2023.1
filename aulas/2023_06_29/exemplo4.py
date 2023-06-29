import random
import time

arq = open('nomes.txt', 'r')
arqs = open('sortudos.txt', 'w')

#nomes = arq.read().split('\n')
nomes = arq.read().splitlines()
arq.close()

#for nome in nomes:
#    print(nome)

for i in range(4):
    sortudo = random.randint(0, len(nomes) - 1)
    #print(sortudo)
    arqs.write(nomes[sortudo])
    arqs.write('\n')
    print("-" ,nomes[sortudo])
    time.sleep(2)

arqs.close()
