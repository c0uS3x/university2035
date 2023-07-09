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

    @age.deleter
    def age(self):
        del self.__age

Person.get_age = 50
del Person.age
print(Person.__dict__)