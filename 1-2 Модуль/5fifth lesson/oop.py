class User:
    def __init__(self, name, phone, img):
        self.name = name
        self.phone = phone
        self.img = img

    def print_hello(self):
        print('Привет! Меня зовут', self.name)


user1 = User('Masha', '999', './img/123.jpg')
user2 = User('Lena', '888', './img/222.jpg')
user3 = User('Vanya', '779', './img/1113.jpg')

user1.print_hello()
user3.print_hello()