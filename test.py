import pandas as pd

class PhoneNumbers:

    def __init__(self, name: str, numbers: int):
        self.name = name
        self.numbers = numbers

    def __iter__(self):
        for attr_name in self.__dict__:
            yield getattr(self, attr_name)

if __name__ == '__main__':

    site_1 = PhoneNumbers(name='Иван', numbers='9999999')
    site_2 = PhoneNumbers(name='Игорь', numbers='7777777')

    df = pd.DataFrame([site_1, site_2])
    df.columns = site_1.__dict__
    print(df)