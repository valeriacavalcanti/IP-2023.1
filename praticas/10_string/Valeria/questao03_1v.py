a = input("String a: ")
b = input("String b: ")

if (len(a) > len(b)):
    for i in range(len(a)):
        print(a[i],end='')
        if (i < len(b)):
            print(b[i], end='')
else:
    for i in range(len(b)):
        if (i < len(a)):
            print(a[i], end='')
        print(b[i],end='')

print()