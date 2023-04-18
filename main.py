import random

# 10

n = int(input("Введите число монет: "))
i=0
orel = 0
rewka = 0
while (i<n):
    brosok = random.randint (0,2)
    if (brosok==1):
        orel+=1
    else:
        rewka+=1
    i+=1
print (orel)
print (rewka)
if (orel==0 or rewka==0):
    print("Ничего не нужно переворачивать")
elif (orel>rewka):
    print("Необходимо перевернуть монет:", orel)
else:
    print("Необходимо перевернуть монет:", rewka)

# 12

x = random.randint (0,1001)
y = random.randint (0,1001)
s = x + y
p = x*y
n1, n2, n3 = 1, 1, 1

i = 0
print (x)
print (y)

while i<i+1:
    n1 = n3
    n1 = p//n1
    n2 = s-n1
    if ((n1 == x and n2 == y) or (n1 == y and n2 == x)):
        print("Заданы числа:", n1, "и", n2)
        break
    n3+=1
    i+=1

# 14

number = int(input("Введите число: "))
i = 1
step = 2
while (step <= number):
    step *=2
    if (step>number):
        break
    print ("Степень", i, step)
    i+=1