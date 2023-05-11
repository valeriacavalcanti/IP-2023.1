hi, hf = input().split()
hi, hf = int(hi), int(hf)

if (hi == hf):
    duracao = 24
elif (hi > hf):
    duracao = 24 - hi + hf
else:
    duracao = hf - hi

print('O JOGO DUROU {} HORA(S)'.format(duracao))
