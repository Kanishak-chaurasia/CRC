"""
WAP to print the current pattern:
1 2 3 4 
  7 6 5
    9 8
      10
"""
n = 4
x = 1

for i in range(1, n +1):
    for j in range(1, n + 1):
        if j >= i:
            print(x, end=' ')
            x+=1
        else:
            print(' ', end=' ')
    print()