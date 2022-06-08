N = 4
for i in range(N):
    for j in range(2*N-1):
        if j >= N-i-1 and j <= N+i-1:
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()
        