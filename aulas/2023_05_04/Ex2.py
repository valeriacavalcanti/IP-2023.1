notas = []

for i in range(5):
    notas.append(int(input()))

for i in range(10, 101, 10):
    print(i, notas.count(i))
