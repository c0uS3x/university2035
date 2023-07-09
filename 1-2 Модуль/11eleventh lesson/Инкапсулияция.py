class A:
    name = 'John'

    def public(self):
        print('hello! I`m public method')

    def _private(self):
        print('hello! I`m public method')
    def __UltraPrivate(self):
        print('hello! I`m public method')




a = A()
print(a.name)
a.public()
