# versão 2.0

#dia = int(input("Dia: "))
#mes = int(input("Mês: "))
#ano = int(input("Ano: "))

dia, mes, ano = input("Data (dd/mm/aaa): ").split("/")
dia, mes, ano = int(dia), int(mes), int(ano)

idade = 2023 - ano

if (mes > 3) or ((mes == 3) and (dia > 30)):
    idade = idade - 1

print('Idade =', idade)
        
