
# class Year:
#     def __init__(self, days):
#         self.__days = days
#
#     def get_days(self):
#         return self.__days
#
#     def set_days(self, days):
#         if days == 365 or days == 366:
#             self.__days = days
#         else:
#             raise Exception('Некоректное значение')
#
# year = Year(365)
#
# year.set_days(366)
#
# print(year.get_days())

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age > 0:
            self.__age = age
        else:
            raise Exception('Вы еще не родились')

