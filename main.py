# 30

# a1 = int(input())
# d = int(input())
# n = int(input())
# m = []
#
# for i in range (n):
#     m.append(a1 + i * d)
#
# print (m)

# 32

x = int(input())
m = [1,2,3,4,5,6,7,8,9]

for i in range (len(m)):
    if (m[i]==x):
        print ("Индекс заданного числа =" , i)
    elif (i==len(m)-1):
        print("Заданное число вне диапозона")

