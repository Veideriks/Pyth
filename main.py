import random

# 22

numbers = []
numbers_2 = []
n = int(input("Введите количество элементов: "))
m = int(input("Введите количество элементов: "))

for i in range (n):
    numbers.append(random.randint(1,10))
print (numbers)
for i in range (m):
    numbers_2.append(random.randint(1,10))
print (numbers_2)

x = sorted(set(numbers).intersection(set(numbers_2)))

print (x)

# 24

jag = []
n = int(input("Введите количество элементов: "))
for i in range (n):
    jag.append(random.randint(1,5))
print(jag)

maxim = 0
for i in range (n):
    if i == 0:
        if jag[i]+jag[-1]+jag[i+1]>maxim:
            maxim = jag[i]+jag[-1]+jag[i+1]
    if i == n-1:
        if jag[i]+jag[1]+jag[i-1]>maxim:
            maxim = jag[i]+jag[1]+jag[i-1]
    else:
        if jag[i]+jag[i+1]+jag[i-1]>=maxim:
            maxim = jag[i]+jag[i-1]+jag[i+1]
print (maxim)
