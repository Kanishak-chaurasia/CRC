X = 5
for i in range(X,0,-1):
    for k in range(X-i):
        print(" ", end=' ')
    for j in range(2*i-1):
        print("* ", end='')
        
    print()