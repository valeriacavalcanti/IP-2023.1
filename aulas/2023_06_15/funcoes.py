def somar(numero1, numero2):
    numero1 = 10
    numero2 = 20
    resultado = numero1 + numero2
    return resultado

def minha_islower(simbolo):
    if (simbolo >= 'a') and (simbolo <= 'z'):
        return True
    else:
        return False

# converter um símbolo para maiúsculo
def para_maiusculo(simbolo):
    codigo = ord(simbolo)
    codigo -= 32
    caractere = chr(codigo)
    return caractere

def minha_upper(frase):
    nova = ''
    for s in frase:
        if (minha_islower(s) == True):
            s = para_maiusculo(s)
        nova += s
    return nova

def e_vogal(simbolo):
    if (simbolo in 'AEIOUaeiou'):
        return True
    else:
        return False

def quantidade_vogais(frase):
    qtd = 0
    for s in frase:
        if (e_vogal(s) == True):
            qtd += 1
    return qtd

def quantidade_vogais_distintas(frase):
    memoria = []
    for s in frase.upper():
        if (e_vogal(s) == True) and (s not in memoria):
            memoria.append(s)
    return len(memoria)
