#import funcoes
#from funcoes import somar, minha_islower
from funcoes import *

# PROGRAMA PRINCIPAL
numero1 = int(input("Primeiro: "))
numero2 = int(input("Segundo: "))

print(somar(numero1, numero2))
print(somar(20, 30))

print(minha_islower('v'))
print(minha_islower('V'))
print(minha_islower('1'))

print(para_maiusculo('v'))
print(para_maiusculo('V'))
print(para_maiusculo('1'))

print(minha_upper('ifpb'))
print(minha_upper('ifpb ifpb'))
print(minha_upper('ifpb IFPB'))
print(minha_upper('ifpb 12344 @@@@'))

print(e_vogal('a'))
print(e_vogal('v'))
print(e_vogal('1'))
print(e_vogal(' '))
print(e_vogal('A'))

print(quantidade_vogais('valeria maria!'))
print(quantidade_vogais('VALERIA MARIA!'))
print(quantidade_vogais_distintas('valeria maria'))
print(quantidade_vogais_distintas('VALERIA MARIA'))
print(quantidade_vogais_distintas('valeria MARIA'))
