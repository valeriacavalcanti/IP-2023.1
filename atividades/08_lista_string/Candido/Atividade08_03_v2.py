'''
3. Escreva um programa que leia uma frase e a exiba invertida.
'''
frase = input('Frase: ')
tam = len(frase)
for i in range(tam):
    print(frase[tam-i-1],end='')
