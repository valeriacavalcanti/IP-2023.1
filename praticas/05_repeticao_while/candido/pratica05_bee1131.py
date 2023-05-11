cp = 0
ci = 0
cg = 0
ce = 0
while True:
    pi,pg = input().split()
    pi,pg = int(pi),int(pg)
    cp = cp + 1
    if pi > pg:
        ci = ci + 1
    elif pg > pi:
        cg = cg + 1
    else:
        ce = ce + 1
    cod = int(input('Novo grenal (1-sim,2-não)'))
    if cod == 2:
        break
print(cp,'grenais')
print('Inter',ci)
print('Grêmio',cg)
print('Empates',ce)
if ci > cg:
    print('Inter venceu mais')
elif cg > ci:
    print('Grêmio venceu mais')
else:
    print('Nao houve vencedor')


    



