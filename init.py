# patterns
n = 5
for i in range(1, n+1):
    for j in range(1, n+1):
        print("*", end=" ")
    print()
# *
# **
# ***
# ****
# *****
for i in range(5):
    for j in range(i+1):
        print("*", end=" ")
    print()

#          *
#        * *
#      * * *
#    * * * *
#  * * * * *

for i in range(5):
    for j in range(5-i):
        print("*", end=" ")
    print()
x= 5
for r in range(x):
    for c in range(x+1):
        if c>=n-r+1 and c<=n:
            print("*", end=" ")
        if c>=1 and c<=n-r:
            print(" ", end=" ")
    print()

# 
# * * * * *
#   * * * *
#     * * *
#       * *
#         *

y = 5
for i in range(1, y+1):
    for j in range(1, y+1):
        if j>=i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()    


#        *
#      * * *
#    * * * * *
#  * * * * * * *
r = 10 
#  c>=1 and c <n-r  for symbol *
# c>=n-r+1 and c<=n for symbol space
for  i in range(1, r+1):
    for j in range(1,2*n):
        if j>=i and j<=2*n-i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


