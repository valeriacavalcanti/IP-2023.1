'''
4. Escreva um programa que, a partir da digitação do
infinitivo de um verbo regular, faça a conjugação dele no
presente do indicativo para as pessoas do singular e plural.
Veja o exemplo abaixo.
Entrada:
    CANTAR
Saída:
    Eu canto
    Tu cantas
    Ele canta
    Nós cantamos
    Vós cantais
    Eles cantam
'''
verbo = input('Entre com um verbo regular no infinitivo: ').lower()
tam = len(verbo)
rad = ''
for i in range(tam-2):
    rad += verbo[i]
vt = verbo[tam-2]
if vt == 'a':
    print(f'Eu {rad}o')
    print(f'Tu {rad}as')
    print(f'Ele {rad}a')
    print(f'Nós {rad}amos')
    print(f'Vós {rad}ais')
    print(f'Eles {rad}am')
elif vt == 'e':
    print(f'Eu {rad}o')
    print(f'Tu {rad}es')
    print(f'Ele {rad}e')
    print(f'Nós {rad}emos')
    print(f'Vós {rad}eis')
    print(f'Eles {rad}em')
else:
    print(f'Eu {rad}o')
    print(f'Tu {rad}es')
    print(f'Ele {rad}e')
    print(f'Nós {rad}imos')
    print(f'Vós {rad}is')
    print(f'Eles {rad}em')

    
    
    








