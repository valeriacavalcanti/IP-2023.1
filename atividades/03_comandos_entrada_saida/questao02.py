descricao = input("Descrição: ")
valor = float(input("Valor: "))

desconto = valor * 0.2
valor_final = valor - desconto

print("Descrição: ", descricao)
#print("Valor com desconto: ", valor_final)
print("Desconto = {:.2f}".format(desconto))
print("Valor com desconto: {:.2f}".format(valor_final))

