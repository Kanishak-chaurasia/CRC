import math
# x = int(input("enter the number for factor"))
# for i in range(1,x+1):
#     if x%i==0:
#         print(i , end=' ')

# y = int(input("enter the number for factor"))
# for i in range(1,y+1):
#     if y % i/2 == 0:
#         print(i,end=' ')

z = int(input("enter the number for factor"))
for i in range(1,z+1):
    if z % math.sqrt(i) == 0:
        print(i,end=' ')