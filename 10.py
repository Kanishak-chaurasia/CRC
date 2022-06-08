N = 5 
for i in range(1,N+1):
    for j in range(i):
        print("*", end=' ')  
    print()
for k in range(N):
    for l in range(N-k-1):
        print("*", end=' ')
    print()