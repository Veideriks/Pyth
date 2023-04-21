import random

# 16 and 18 полагаю, можно решить как-то более изящно, но пришла именно такая странная идея)

numbers = []
n = int(input("Введите количество элементов: "))
if n <= 0:
    print("Введите число больше нуля")
else:
    for i in range (n):
        numbers.append(random.randint(1,10))
    print (numbers)
    s = int(input("Введите число для поиска совпадений: "))
    count = 0
    for i in range (n):
        if numbers[i] == s:
            count+=1
    print (count)
    x = int(input("Введите число для поиска ближайшего: "))
    sosed = 0
    dist = []
    for i in range(n):
        dist.append(abs(numbers[i]-x))
    print(dist)
    minim = dist[i]
    for i in range(n):
        if dist[i]<=minim:
            minim = dist[i]
            sosed = i
print (numbers[sosed])

# 20

slovo = list((input("Введите слово: ").upper()))
elements = ["A", "E", "I", "O", "U", "L", "N", "S", "T", "R",
             "А", "В", "Е", "И", "Н", "О", "Р", "С", "Т"]
elements_2 = ["D", "G", "Д", "К", "Л", "М", "П", "У"]
elements_3 = ["B", "C", "M", "P", "Б", "Г", "Ё", "Ь", "Я"]
elements_4 = ["F", "H", "V", "W", "Y", "Й", "Ы"]
elements_5 = ["K", "Ж", "З", "Х", "Ц", "Ч"]
elements_8 = ["J", "X", "Ш", "Э", "Ю"]
elements_10 = ["Q", "Z", "Ф", "Щ", "Ъ"]
print (slovo)

score = 0

for i in range (len(slovo)):
    for j in range (len(elements)):
        if slovo[i] == elements[j]:
            score = score + 1
for i in range (len(slovo)):
    for j in range (len(elements_2)):
        if slovo[i] == elements_2[j]:
            score = score + 2
for i in range(len(slovo)):
    for j in range (len(elements_3)):
        if slovo[i] == elements_3[j]:
            score = score + 3
for i in range(len(slovo)):
    for j in range (len(elements_4)):
        if slovo[i] == elements_4[j]:
            score = score + 4
for i in range(len(slovo)):
    for j in range (len(elements_5)):
        if slovo[i] == elements_5[j]:
            score = score + 5
for i in range(len(slovo)):
    for j in range (len(elements_8)):
        if slovo[i] == elements_8[j]:
            score = score + 8
for i in range(len(slovo)):
    for j in range (len(elements_10)):
        if slovo[i] == elements_10[j]:
            score = score + 10

print (score)


# хотел изначально список и чтобы в счет сразу значение цифры шло, но как то не задалось
# elements = {("A", "E", "I", "O", "U", "L", "N", "S", "T", "R",
#             "А", "В", "Е", "И", "Н", "О", "Р", "С", "Т"):"1",
#             ("D", "G", "Д", "К", "Л", "М", "П", "У"):"2",
#             ("B", "C", "M", "P", "Б", "Г", "Ё", "Ь", "Я"):"3",
#             ("F", "H", "V", "W", "Y", "Й", "Ы"):"4",
#             ("K", "Ж", "З", "Х", "Ц", "Ч"):"5",
#             ("J", "X", "Ш", "Э", "Ю"):"8",
#             ("Q", "Z", "Ф", "Щ", "Ъ"):"10"}
# потом еще словил ряд ошибок походу и закипел, поэтому то к чему пришел явно не оптимально,
# почему то даже после иф елсе корректно не работал, но т к закипел просто разбил на новые циклы
