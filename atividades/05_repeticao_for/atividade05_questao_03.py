n, x, y = input("Informe n, x e y: ").split()
n, x, y = int(n), int(x), int(y)

#n = int(input("Informe N: "))
#x = int(input("Informe X: "))
#y = int(input("Informe Y: "))

for i in range(x + 1, y):
    if (i % n == 0):
        print(i)
