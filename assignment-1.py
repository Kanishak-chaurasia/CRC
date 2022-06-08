# N=4
# *
# * *
# * * *
# * * * *

# N = 4
# for i in range(N):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()

# print()
# M = 4
# for i in range(M):
#     for j in range(M-i):
#         print("*", end=' ')
#     print()

# print()

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# n = 4
# x = 1
# for r in range(1, n+1):
#     for c in range(1, r+1):
#         print(x, end=' ')
#         x += 1
#     print()
# print()

#          *
#        * *
#      * * *
#    * * * *
#  * * * * *

# N = 4
# for i in range(N):
#     for j in range(2*N-1):
#         if j >= N-i-1 and j <= N+i-1:
#             print("*", end=' ')
#         else:
#             print(" ", end=' ')
#     print()

# N = 5 
# for i in range(1,N+1):
#     for j in range(i):
#         print("*", end=' ')  
#     print()
# for k in range(N):
#     for l in range(N-k-1):
#         print("*", end=' ')
#     print()

# n= 5
# for i in range(n):
#     # p=1
#     for j in range(i,n):
#         print(" ", end=' ')
#     for j in range(i):
#         print("* ", end='')
#     for j in range(i+1):
#         print("*", end=' ')
#     print()

# X = 5
# for i in range(X,0,-1):
#     for k in range(X-i):
#         print(" ", end=' ')
#     for j in range(2*i-1):
#         print("* ", end='')
        
#     print()

# *                 * 
# * *             * *
# * * *         * * *
# * * * *     * * * *
# * * * * * * * * * *
# n = 5 
# s = 0
# for i in range(n, 0, -1):
#     for j in range(i):
#         print("*", end=' ')
    
#     for j in range(s):
#         print(" ", end=' ')
#     for j in range(i):
#         print("*", end=' ')
   
#     print()
#     s+=2
N= 4
for i in range(N):
    for j in range(i+1):
        print("*", end=" ")
    for j in range(N):
        if j < N-i-1:
            print("  ", end=' ')
        else:
            print("*", end=' ')
    print()
  
