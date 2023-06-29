def fatorial(num):
    resultado = 1
    for i in range(2, num + 1):
        resultado *= i
    return resultado

# MAIN
print(fatorial(2)) # 2
print(fatorial(3)) # 6
r = fatorial(2) + fatorial(3)
print(r) # 8