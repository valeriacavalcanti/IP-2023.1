# Data atual: 27/04/2023

# A data deverá ser informada no formado dd/mm/aaaa
dia, mes, ano = input("Informe a data: ").split("/")
dia, mes, ano = int(dia), int(mes), int(ano)

if (ano < 2023):
    print('Vencido')
elif (ano == 2023) and (mes < 4):
    print('Vencido')
elif (ano == 2023) and (mes == 4) and (dia < 27):
    print('Vencido')
else:
    print('Não vencido')
