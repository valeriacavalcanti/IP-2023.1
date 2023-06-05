'''
3. Escreva um programa que leia uma frase e
verifique se ela é um palíndromo ou não.
Palíndromo é uma palavra (ou frase) que tenha a
propriedade de poder ser lida tanto da direita
para a esquerda como da esquerda para a direita.
Para identificar um palíndromo, desconsidera-se os
acentos, pontuações e espaços em branco, além
disso também não é levada em conta a diferença
entre maiúsculas e minúsculas.
Exemplos:
- Ovo;
- Arara;
- Aérea;
- Roma me tem amor;
- Anotaram a data da maratona;
- Socorram-me, subi no onibus em Marrocos.
'''
frase = input('Frase: ').upper()
comp = ''
for caracter in frase:
    if caracter.isalpha():
        comp = comp + caracter
inv = ''
for caracter in comp:
    inv = caracter + inv
if comp == inv:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')
    








