number_tuple = (i ** 2 for i in range(1_000_000))


def gen_lazzy():
    for i in range(1_000_000):
        yield i ** 2

print(number_tuple)