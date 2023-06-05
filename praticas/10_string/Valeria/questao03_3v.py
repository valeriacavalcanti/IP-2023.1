a = input("String a: ")
b = input("String b: ")
i = 0

while True:
    if (i < len(a)):
        print(a[i], end='')
    if (i < len(b)):
        print(b[i], end='')
    i += 1
    if ((i > len(a)) and (i > len(b))):
        break