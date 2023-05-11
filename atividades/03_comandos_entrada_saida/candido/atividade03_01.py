'''
01. Escreva um programa, em Python, para ler 02(dois)
números naturais (N∗). Calcular e exibir:
- Soma dos dois números;
- Subtração do primeiro número pelo segundo;
- Multiplicação dos dois números;
- Divisão real do primeiro número pelo segundo;
- Divisão inteira do primeiro número pelo segundo;
- Resto da divisão do primeiro número pelo segundo;
- Potência do primeiro número pelo segundo.
'''
print('Digite dois números naturais:')
num1 = int(input("Primeiro valor: "))
num2 = int(input("Segundo valor: "))

soma = num1 + num2
sub = num1 - num2
mult = num1 * num2
div_real = num1 / num2
div_int = num1 // num2
resto = num1 % num2
potencia = num1 ** num2

print(f'A soma dos dois valores: {soma}')
print('A subtração dos dois valores:', sub)
print('A multiplicação: ', mult)
print('A divisão real: ', div_real)
print('A divisão inteira: ',div_int)
print('O resto é: ', resto)
print('A potencia é: ', potencia)

