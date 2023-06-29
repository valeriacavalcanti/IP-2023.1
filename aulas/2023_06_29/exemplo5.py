import random
import time

arq = open('nomes.txt', 'r')
arqs = open('sortudos.txt', 'w')
sortudos = []

nomes = arq.read().splitlines()
arq.close()

while (len(sortudos) < 6):
    sortudo = random.randint(0, len(nomes) - 1)
    if (sortudo not in sortudos):
        sortudos.append(sortudo)

for s in sortudos:
    arqs.write(nomes[s])
    arqs.write('\n')
    print("-" ,nomes[s])
    time.sleep(2)

arqs.close()
