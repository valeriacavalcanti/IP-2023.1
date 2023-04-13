q_in = q_out = 0
qtd = int(input())

for i in range(qtd):
    num = int(input())
    if (num >= 10) and (num <= 20):
        q_in = q_in + 1
    else:
        q_out = q_out + 1

print(q_in, 'in')
print(q_out, 'out')

