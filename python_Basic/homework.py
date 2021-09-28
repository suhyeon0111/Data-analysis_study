import random


def make_random_number():
    res = []
    for i in range(3):
        num = random.randint(0,9)
        while num in res:
            num = random.randint(0,9)
        res.append(num)
    
    x0 = res.pop()
    x1 = res.pop()
    x2 = res.pop()

    return [x0,x1,x2]


for i in range(0,10):
    print(make_random_number())