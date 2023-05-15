uf = ['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT',
      'MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO',
      'RR','SC','SP','SE','TO']
votos = [0] * len(uf)

# ler os votos
while (True):
    sigla = input("Informe seu voto: ")
    if (sigla not in uf):
        break
    pos = uf.index(sigla)
    votos[pos] += 1

maior = votos[0]
for i in range(1,len(uf)):
    if(votos[i] > maior):
        maior = votos[i]

print('Maior votacao:', maior)

# exibir todos as pontuacoes
for i in range(len(uf)):
    if (votos[i] == maior):
        print(uf[i], votos[i])