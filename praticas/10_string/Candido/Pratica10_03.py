'''
3. Escreva um programa que leia 2 strings (A e B)
e imprima os caracteres de A e B intercalados.
Por exemplo, se A = 'laranja' e B = 'uva',
então será impresso 'luavraanja'.
'''
a = input()
b = input()
na = len(a)
nb = len(b)
if na > nb:
    m = na
else:
    m = nb
for i in range(m):
    if i < na:
        print(a[i],end='')
    if i < nb:
        print(b[i],end='')



