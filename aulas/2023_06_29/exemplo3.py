lista = ["10"] * 10

arq = open('eita.txt', 'w')

arq.writelines(lista)

print("teste")

arq.write('sério?')

arq.close()
