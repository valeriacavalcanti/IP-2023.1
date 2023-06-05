maior = 0
while True:
    string = input()
    if string == '0':
        break
    lista = string.split()
    n = len(lista)
    for i in range(n):
        pal = lista[i]
        tam = len(pal)
        if i < n-1:
            print(tam,end='-')
        else:
            print(tam)
        if tam >= maior:
            maior = tam
            biggest = pal
print('The biggest word:',biggest)
