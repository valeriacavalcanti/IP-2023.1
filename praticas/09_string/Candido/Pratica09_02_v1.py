'''
2. Faça um programa que leia uma frase e a exiba com a
inicial de cada palavra em maiúsculo.
'''
frase = input('Frase: ')
print(frase[0].upper(),end='')
for i in range(1,len(frase)):
    if frase[i-1]==' ':
        print(frase[i].upper(),end='')
    else:
        print(frase[i],end='')
        
