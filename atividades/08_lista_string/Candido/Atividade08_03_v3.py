'''
3. Escreva um programa que leia uma frase e a exiba invertida.
'''
frase = input('Frase: ')
tam = len(frase)
inversa = ''
for i in range(tam-1,-1,-1):
    inversa += frase[i]
print(inversa)
