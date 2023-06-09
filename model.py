import pandas as pd

df = pd.read_excel(r"C:\Users\Veider\Desktop\Python\Sem\Справочник.xlsx")

def pokaz ():
    print(df)
    # global df = pd.read_excel(r"C:\Users\Veider\Desktop\Python\Sem\Справочник.xlsx")
    # - пробовал тут так через глобал, но ломается все

def poisk():
    print ("По какому параметру ищем контакт?")
    print ("Имя/Фамилия, Номер телефона")
    otvet = input()
    if otvet == ("Имя" or "Фамилия"):
        print("Введите Имя/Фамилию: ")
        name = input()
        if ((df[df["Имя/Фамилия"] == name].empty) != True):
            print(df[df["Имя/Фамилия"] == name]).index[0]
            index = df[df["Имя/Фамилия"] == name].index[0]
            return index
        else:
            print("нет такого")
    if otvet == "Номер телефона":
        print("Введите номер телефона: ")
        numbers = int(input())
        if ((df[df["Номер телефона"] == numbers].empty) != True):
            print(df[df["Номер телефона"] == numbers])
            index = df[df["Номер телефона"] == numbers].index[0]
            return index
        else:
            print("нет такого")
    else:
        print("Такого контакта нет")
        poisk()

def dobavlenie():
    df.loc[len(df.index)] = [input("Введите Имя/фамилию: "),
    input("Введите номер: ")]

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

def save():
    df.to_excel(r"C:\Users\Veider\Desktop\Python\Sem\Справочник.xlsx", engine='xlsxwriter', index=False)