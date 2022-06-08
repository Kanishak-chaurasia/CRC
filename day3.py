"""
WAP to print the current pattern:
1 2 3 4 
  7 6 5
    9 8
      10
"""
# n = 4
# x = 1
# y = 1
# for i in range(1, n +1):
#     for j in range(1, n + 1):
#         if x <= n:
#             print(x, end=' ')
#             x += 1
#         else:
#             y = x
#             t = x+i
#             print(t, end=' ')
#             t-=1
#     print()
# n = 4
# s,n1 = 1,0
# for r in range(1, n+1):
#     for c in range(1, r+1):
#         if c >= r and c <= n:
#             if(r == 1):
#                 print(s, end=' ')
#                 s += 1
#                 n1 += 1
#             else:
#                 print(s, end=' ')
#                 s -= 1
#         if c>= 1 and c <= r-1:
#             print(" ", end=' ')
#     s = n1 + n - r
#     n1 = s
#     print()

"""
*           *
* *       * *
* * *   * * *
* * * * * * *
"""
from re import I


a = 4
x = 1
for r in range(1, a+1):
    for c in range(1, 2*a+1):
        if c >= r+1 and c <= 2*a-r: 
            print(x, end=' ')  
            x+=1
        else:
            print(" ", end=' ')

    print()
