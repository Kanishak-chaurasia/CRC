n = 5 
s = 0
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=' ')
    for j in range(s):
        print(" ", end=' ')
    for j in range(i):
        print("*", end=' ')
    print()
    s+=2