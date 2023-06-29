def media(n1, n2, n3):
    return (n1 + n2 + n3) / 3

def conceito(media):
    if (media >= 8):
        return "A"
    elif (media >= 5):
        return "B"
    else:
        return "C"

def conceito2(n1, n2, n3):
    m = media(n1, n2, n3)
    return conceito(m)

# MAIN
nota1 = int(input("Nota 1: "))
nota2 = int(input("Nota 2: "))
nota3 = int(input("Nota 3: "))
valor_media = media(nota1, nota2, nota3)
print(valor_media)
print(conceito(valor_media))
print(conceito(media(nota1, nota2, nota3)))
print(conceito2(nota1, nota2, nota3))