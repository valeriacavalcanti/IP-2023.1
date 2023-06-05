a = input("String a: ")
b = input("String b: ")

if (len(a) < len(b)):
    for i in range(len(a)):
        print(a[i], end='')
        print(b[i], end='')
    print(b[i + 1:])
else:
    for i in range(len(b)):
        print(a[i], end='')
        print(b[i], end='')
    print(a[i + 1:])