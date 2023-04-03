# versão 1.0

#dia = int(input("Dia: "))
#mes = int(input("Mês: "))
#ano = int(input("Ano: "))

dia, mes, ano = input("Data (dd/mm/aaa): ").split("/")
dia, mes, ano = int(dia), int(mes), int(ano)


if (mes < 3):
    idade = 2023 - ano
else:
    if (mes > 3):
        idade = 2023 - ano - 1
    else:
        if (dia <= 30):
            idade = 2023 - ano
        else:
            idade = 2023 - ano - 1

print('Idade =', idade)
        
