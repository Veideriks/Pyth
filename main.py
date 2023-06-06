import pandas as pd

df = pd.read_excel(r"C:\Users\Veider\Desktop\Python\Sem\Справочник.xlsx")
def dobavlenie():
    df.loc[len(df.index)] = [input("Введите Имя/фамилию: "),
    input("Введите номер: ")]
    return
def poisk():
    print ("По какому параметру ищем контакт?")
    print ("Имя/Фамилия, Номер телефона")
    otvet = input()
    if otvet == ("Имя" or "Фамилия"):
        print("Введите Имя/Фамилию: ")
        name = input()
        print(df[df["Имя/Фамилия"] == name])
        index = df[df["Имя/Фамилия"] == name].index[0]
        return index
    if otvet == "Номер телефона":
        print("Введите номер телефона: ")
        numbers = int(input())
        print(df[df["Номер телефона"] == numbers])
        index = df[df["Имя/Фамилия"] == numbers].index[0]
        return index
    else:
        print("Такого контакта нет")
        poisk()
def ydalenie ():
    index = poisk()
    df.drop(index = df.index[index], inplace = True)
def izmenenie ():
    index = poisk()
    print("Вы хотите изменить Имя/Фамилию или Номер телефона?")
    otvet = input()
    if otvet == ("Имя" or "Фамилия"):
        print("Введите новое значение: ")
        name = input()
        df.at[index, "Имя/Фамилия"] = name
        print(df[df["Имя/Фамилия"] == name])
        return
    if otvet == "Номер телефона":
        print("Введите новое значение: ")
        numbers = int(input())
        df.at[index, "Номер телефона"] = numbers
        print(df[df["Номер телефона"] == numbers])
        return

def spravochnik():
    print("Что необходимо сделать?")
    print("Показать весь справочник")
    print("Найти контакт")
    print("Добавить контакт")
    print("Удалить контакт")
    print("Изменить контакт")
    print("Сохранить и выйти")
    otvet = input()
    if otvet == "Показать весь справочник":
        print(df)
        spravochnik()
    if otvet == "Найти контакт":
        poisk()
        spravochnik()
    if otvet == "Добавить контакт":
        dobavlenie()
        spravochnik()
    if otvet == "Удалить контакт":
        ydalenie()
        print("Контакт удален")
        spravochnik()
    if otvet == "Изменить контакт":
        izmenenie()
        print("Контакт изменен")
        spravochnik()
    if otvet == "Сохранить и выйти":
        df.to_excel(r"C:\Users\Veider\Desktop\Python\Sem\Справочник.xlsx", engine='xlsxwriter', index=False)
        return

# spravochnik()

name = "Игорь"
x = (df[df["Имя/Фамилия"] == name].empty)
if ((df[df["Имя/Фамилия"] == name].empty)!= True):
    print(df[df["Имя/Фамилия"] == name])
else:
    print("нет такого")
#
# df[df["Имя/Фамилия"] == "Иван"]

# print (x)
# print (type(x))