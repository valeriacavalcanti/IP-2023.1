def soma(vetor):
    total = 0
    for elem in vetor:
        total += elem
    return total

# MAIN
print(soma([1,2,3,4])) # 10
print(soma([10,20,30,40])) # 100
print(soma([10])) # 10
print(soma([])) # 0