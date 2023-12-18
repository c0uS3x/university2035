def temp(*args, **kwargs):
    print(args)
    print(kwargs)

temp(0,2,1,2,2,x=1,y=2,z=4)

import time

class Timer:
    def __init__(self):
        self.timer_start = None

    def __enter__(self):
        print("марш")
        self.timer_start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        if exc_type is TypeError:
            return True
        print("финиш")
        timer_stop = time.time()
        print(f'{timer_stop - self.timer_start}')

with Timer() as f:
    my_list = [i**2 for i in range(2000)]
    print(my_list[-1])
    my_list - 1


my_list = [1, 2 , 3, 4, 5]
my_iter = iter(my_list)

a = [print(i) for i in my_list]

class Range:
    def __init__(self, start, limit):
        self.start = start
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.limit == 0:
            raise StopIteration
        else:
            self.limit -= 1
            self.start += 1
            return self.limit

my_range = Range(start=0, limit=0)
my_iter = iter(my_range)
for i in my_range:
    print(i)
