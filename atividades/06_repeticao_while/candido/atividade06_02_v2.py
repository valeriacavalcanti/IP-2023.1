'''
02. No sistema Suap uma nota é considerada válida quando
está no intervalo [0,100]. Escreva um programa para ler
01 (uma) nota válida no Suap. Ao final exibir:
a. Nota válida;
b. Quantidade de valores inválidos que foram informados.
'''
cont = 0
while True:
    nota = int(input())
    if nota >= 0 and nota <= 100:
        break
    cont = cont + 1
print('Nota válida')
print('Quantidade de valores inválidos:',cont)
    
    
