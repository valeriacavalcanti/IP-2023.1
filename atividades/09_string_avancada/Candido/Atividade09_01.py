'''
1. Escreva um programa que leia uma frase e
imprima a quantidade de vogais e a quantidade
de consoantes contidas na frase.
'''
frase = input('Frase: ')
contv = 0
contc = 0
for caracter in frase:
    if caracter.isalpha():
        if caracter in 'AaEeIiOoUu':
            contv += 1
        else:
            contc += 1
print(f'A frase possui {contv} vogal(is)')
print(f'A frase possui {contc} consoante(s)')
