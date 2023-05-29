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
pessoa = ['Eu','Tu','Ele','Nós','Vós','Eles']
final_a = ['o','as','a','amos','ais','am']
final_e = ['o','es','e','emos','eis','em']
final_i = ['o','es','e','imos','is','em']
verbo = input('Entre com um verbo regular no infinitivo: ').lower()
tam = len(verbo)
rad = ''
for i in range(tam-2):
    rad += verbo[i]
vt = verbo[tam-2]
if vt == 'a':
    for i in range(6):
        print(f'{pessoa[i]} {rad}{final_a[i]}')
elif vt == 'e':
    for i in range(6):
        print(f'{pessoa[i]} {rad}{final_e[i]}')
else:
    for i in range(6):
        print(f'{pessoa[i]} {rad}{final_i[i]}')

    
    
    








