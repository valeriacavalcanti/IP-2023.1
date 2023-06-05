simbolos = []
contadores = []
frase = input("Frase: ").upper()

for simbolo in frase:
    if (simbolo in simbolos):
        contadores[simbolos.index(simbolo)] += 1
    else:
        simbolos.append(simbolo)
        contadores.append(1)

for i in range(len(simbolos)):
    print(f"{simbolos[i]}-{contadores[i]}")