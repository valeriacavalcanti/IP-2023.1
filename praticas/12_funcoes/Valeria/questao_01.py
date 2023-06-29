#import questao_01_funcoes as f
from questao_01_funcoes import *

n = int(input("Quantidade: "))
valores = criar_vetor(n)
media = calcular_media(valores)
abaixo = verificar_abaixo(valores, media)

print(valores)
print(media)
print(abaixo)
