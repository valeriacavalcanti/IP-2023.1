rato = coelho = sapo = total = 0

qt_exp = int(input())
for i in range(qt_exp):
    qtd, tipo = input().split()
    qtd = int(qtd)
    #total = total + qtd

    if (tipo == 'C'):
        coelho = coelho + qtd
    elif (tipo == 'R'):
        rato = rato + qtd
    else:
        sapo = sapo + qtd

total = rato + sapo + coelho
p_coelho = coelho / total * 100
p_rato = rato / total * 100
p_sapo = sapo / total * 100

print('Total: {} cobaias'.format(total))
print('Total de coelhos:', coelho)
print('Total de ratos:', rato)
print('Total de sapos:', sapo)
print('Percentual de coelhos: {:.2f} %'.format(p_coelho))
print('Percentual de ratos: {:.2f} %'.format(p_rato))
print('Percentual de sapos: {:.2f} %'.format(p_sapo))
