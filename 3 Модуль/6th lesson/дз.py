class Year:
    def __init__(self, days):
        self.__days = days

    @property
    def days(self):
        return self.__days

    @days.setter
    def days(self, days):
        if days == 365 or days == 366:
            self.__days = days
        else:
            raise Exception('Некоректное значение')

year = Year(365)

year.days = 366

print(year.days)