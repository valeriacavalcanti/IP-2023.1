lista = "eu tu ele nós vós eles".split()
ar = "o as a amos ais am".split()
er = "o es e emos eis em".split()
ir = "o es e imos is em".split()

verbo = input("Verbo: ")

# radical = verbo[:len(verbo) - 2]
# sufixo = verbo[len(verbo) - 2:]

# radical = ''
# for i in range(len(verbo) - 2):
#     radical += verbo[i]

# sufixo = ''
# for i in range(len(verbo) - 2, len(verbo)):
#     sufixo += verbo[i]

radical = verbo[:-2]
sufixo = verbo[-2:]

# if (sufixo == 'ar'):
#     print(f"eu {radical}o")
#     print(f"tu {radical}as")
#     print(f"ele {radical}a")
#     print(f"nós {radical}amos")
#     print(f"vós {radical}ais")
#     print(f"eles {radical}am")
# elif (sufixo == 'er'):
#     print(f"eu {radical}o")
#     print(f"tu {radical}es")
#     print(f"ele {radical}e")
#     print(f"nós {radical}emos")
#     print(f"vós {radical}eis")
#     print(f"eles {radical}em")
# else:
#     print(f"eu {radical}o")
#     print(f"tu {radical}es")
#     print(f"ele {radical}e")
#     print(f"nós {radical}imos")
#     print(f"vós {radical}is")
#     print(f"eles {radical}em")

for i in range(6):
    if (sufixo == 'ar'):
        print(f"{lista[i]} {radical}{ar[i]}")
    elif (sufixo == 'er'):
        print(f"{lista[i]} {radical}{er[i]}")
    else:
        print(f"{lista[i]} {radical}{ir[i]}")