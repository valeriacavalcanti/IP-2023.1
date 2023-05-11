'''
02. No sistema Suap uma nota é considerada válida quando
está no intervalo [0,100]. Escreva um programa para ler
01 (uma) nota válida no Suap. Ao final exibir:
a. Nota válida;
b. Quantidade de valores inválidos que foram informados.
'''
nota = int(input())
cont = 0
while nota < 0 or nota > 100:
    cont = cont + 1
    nota = int(input())
print('Nota válida')
print('Quantidade de valores inválidos:',cont)
    
    
