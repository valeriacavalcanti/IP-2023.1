n = int(input('Nº de casos de teste: '))
for i in range(n):
    string = input('String: ').upper()
    desloc = int(input('Deslocamento: '))
    for caracter in string:
        cod = ord(caracter) - desloc
        if cod < ord('A'):
            dif = ord('A') - cod
            cod = ord('Z') - dif + 1  
        print(chr(cod),end='')
