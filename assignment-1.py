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
n = 4
x = 1
for r in range(1, n+1):
    for c in range(1, r+1):
        print(x, end=' ')
        x += 1
    print()
print()
