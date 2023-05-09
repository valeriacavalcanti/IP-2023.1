total = 0
qt = 0

for i in range(100):
    salario = float(input("Salário: "))
    if (salario < 1903.98):
        qt += 1
        imposto = 0
    elif (salario <= 2826.65):
        imposto = (salario * 0.075) - 142.80
    elif (salario <= 3751.05):
        imposto = (salario * 0.15) - 354.80
    elif (salario <= 4664.68):
        imposto = (salario * 0.225) - 636.13
    else:
        imposto = (salario * 0.275) - 869.36
    total += imposto

print("Isentos: {}%".format(qt))
print("Total: R$ {:.2f}".format(total))

# 1000  -> 0.00
# 2000  -> 7.20
# 3000  -> 95.20
# 4000  -> 263.87

# total -> 366,27
