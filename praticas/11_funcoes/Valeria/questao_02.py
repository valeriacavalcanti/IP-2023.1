def print_e(st, n):
    for i in range(len(st) - 1):
        print(st[i], end=" "*n)
    print(st[-1])

# MAIN
print_e("IFPB ifpb", 0)
print_e("IFPB ifpb", 1)
print_e("IFPB ifpb", 2)
print_e("IFPB ifpb", 3)