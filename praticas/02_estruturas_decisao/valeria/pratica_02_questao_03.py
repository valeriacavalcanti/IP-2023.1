renda = float(input("Renda: "))

if (renda <= 1903.98):
    deducao = 0
    aliquota = 0
elif (renda <= 2826.65):
    deducao = 142.80
    aliquota = 7.5
elif (renda <= 3751.05):
    deducao = 354.80
    aliquota = 15
elif (renda <= 4664.68):
    deducao = 636.13
    aliquota = 22.5
else:
    deducao = 869.36
    aliquota = 27.5

pagar = (renda * aliquota / 100) - deducao

print("Alíquota: ", aliquota, "%")
print("Valor pago: R$ {:.2f}".format(pagar))
