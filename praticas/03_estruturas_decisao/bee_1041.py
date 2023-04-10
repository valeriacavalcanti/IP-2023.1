x, y = input().split()
x, y = float(x), float(y)

if (x == 0) or (y == 0):
    if (x != 0):
        print("Eixo X")
    elif(y != 0):
        print("Eixo Y")
    else:
        print("Origem")
else:
    if (x > 0):
        if (y > 0):
            print("Q1")
        else:
            print("Q4")
    else:
        if (x > 0):
            print("Q2")
        else:
            print("Q3")
