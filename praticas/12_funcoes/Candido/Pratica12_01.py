'''
1. Escreva um programa que leia N números inteiros (máximo 20) e armazene em
   um vetor X. Calcule a média dos elementos do vetor e informe quantos elementos
   estão abaixo da média do conjunto.
   O programa deverá conter as seguintes funções:
   • Uma função que faça a leitura dos elementos de um vetor de inteiros.
     Essa função deve receber como parâmetro o número de elementos do vetor e deve
     retornar o vetor preenchido.
   • Uma função que calcule a média dos elementos de um vetor. Essa função deve
     receber como parâmetro um vetor e retornar a média dos elementos dele.
   • Uma função que receba um vetor e um número, e retorne quantos elementos do
     vetor estão abaixo desse número.
'''
#Função para ler um vetor
def ler_vetor(qtd):
    vetor = []
    for i in range(qtd):
        elem = int(input())
        vetor.append(elem)
    return vetor

#Função para calcular a média de um vetor
def media_vetor(vetor):
    if len(vetor) > 0:
        return sum(vetor) / len(vetor)
    else:
        return None

#Função para contar os elementos abaixo da média
def cont_vetor(vetor,num):
    cont = 0
    for elem in vetor:
        if elem < num:
            cont += 1
    return cont

#Programa principal
n = 5  
print(f'Digite os {n} elementos do vetor:')
x = ler_vetor(n)
m = media_vetor(x)
c = cont_vetor(x,m)
print(f'A média do elementos do vetor é: {m:.1f}')
print(f'Existe(m) {c} elemento(s) abaixo da média')


