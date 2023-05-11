'''
3. Escreva um programa para ler o valor da renda mensal
de um contribuinte, calcule e exiba qual é alíquota
aplicada e o respectivo valor do imposto que deve ser pago.
'''
renda = float(input('Renda mensal: R$'))
if renda <= 1903.98:
    aliq = 0
    deducao = 0.00
elif renda <= 2826.65:
    aliq = 7.5
    deducao = 142.80
elif renda <= 3751.05:
    aliq = 15
    deducao = 354.80
elif renda <= 4664.68:
    aliq = 22.5
    deducao = 636.13
else:
    aliq = 27.5
    deducao = 869.36
imposto = renda * aliq/100 - deducao
print(f'Renda mensal de R$ {renda:.2f}, incide alíquota de {aliq}% e o imposto a ser pago é de R$ {imposto:.2f}')

