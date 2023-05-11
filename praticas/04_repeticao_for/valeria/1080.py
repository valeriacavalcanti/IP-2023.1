maior = int(input())
posicao = 1

for i in range(2, 101):
    num = int(input())
    if (num > maior):
        maior = num
        posicao = i

print(maior)
print(posicao)
