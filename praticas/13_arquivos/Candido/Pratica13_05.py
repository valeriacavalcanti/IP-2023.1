'''
5. Escreva um programa que leia do teclado o nome,
o sexo e a idade de várias pessoas e armazene esses
dados em um arquivo texto chamado CADASTRO.TXT,
sendo uma pessoa por linha e os dados separados
por vírgula.
Obs: a leitura do nome vazio (string nula)
encerra os dados de entrada.
'''
arq = open('CADASTRO.TXT','w')
while True:
    nome = input('Nome: ')
    if nome == '':
        break
    sexo = input('Sexo(M/F): ').upper()
    idade = int(input('Idade: '))
    linha = nome+','+sexo+','+str(idade)+'\n'
    arq.write(linha)
arq.close()
print('Arquivo CADASTRO.TXT gerado com sucesso')
