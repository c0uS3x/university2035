class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __add__(self, other):
        if isinstance(other, Item):
            return self.price + other.price
        elif isinstance(other, int):
            return self.price + other

    def __sub__(self, other):
        if isinstance(other, Item):
            return self.price - other.price
        elif isinstance(other, int):
            return self.price - other

    def __mul__(self, other):
        if isinstance(other, Item):
            return self.price * other.price
        elif isinstance(other, int):
            return self.price * other

    def __truediv__(self, other):
        if isinstance(other, Item):
            return self.price / other.price
        elif isinstance(other, int):
            return self.price / other

item1 = Item('Процессор', 15000)
item2 = Item('Видюха', 1999)

print(item2.price / item1.price)