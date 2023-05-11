'''
01. O e-mail de qualquer pessoa é formado por duas partes:
o login do usuário e o domínio do provedor.
Escreva um programa que leia o login de um usuário e o
domínio do seu provedor e mostre o seu e-mail completo:
Veja o exemplo abaixo.
Login: antonio.silva
Domínio: ifpb.edu.br
E-mail: antonio.silva@ifpb.edu.br
'''
login = input('Login: ')
dominio = input('Domínio: ')
email = f'{login}@{dominio}'
print(f'Email: {email}')
