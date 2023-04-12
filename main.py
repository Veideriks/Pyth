#2

x = 123
sum = (x//10%10)+(x//100%10)+(x%10)
print ("Сумма: ", sum)

#4

s=24
y=s/6
kat = y*4
pet = y
ser = y
print ("Катя: ", kat, "Петя: ", pet, "Сережа: ", ser)

#6

bilet = 385916
happyn = (bilet//10000%10)+(bilet//100000%10)+(bilet//1000%10)
happyk = (bilet//10%10)+(bilet//100%10)+(bilet%10)
if happyn == happyk:
    print ("Счастливый билетик")
else:
    print ("Не счастливый билетик")

#8

n=3
m=2
k=1

if k == m*n:
    print("Это и есть вся шоколадка")
elif k > m*n:
    print("Это больше чем размер шоколадки")
elif k == n or k == m or k!=2 and k%2!=1:
    print("Можно отломить")
else:
    print("Нельзя отломить")