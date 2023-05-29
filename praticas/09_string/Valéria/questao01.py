frase = input("Frase: ")
sem_espaco = ''

for s in frase:
    if (s != ' '):
        # solução Antony
        print(s, end='')
        # solução Helio
        sem_espaco += s

print()

# solução Helio
print(sem_espaco)
