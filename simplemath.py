"""Greatest Common Factor and  Least Common Multiple"""


from random import randint
from functools import reduce


def find_gcf(nums):
    """ Greatest Common Factor of two numbers """
    n = list(set(nums))
    factor, gcf = 2, 1
    while factor <= min(n):
        # only when ALL of the numbers are divisible by factor
        while reduce(lambda x, y: x * y, list(map(lambda z: z % factor == 0, n))):
            gcf *= factor
            for k, v in enumerate(n):
                n[k] = v // factor
        factor += 1
    return gcf


def find_lcm(nums):
    """ Least Common Multiple of several numbers """
    n = list(set(nums))
    factor, lcm = 2, 1
    while factor <= max(n):
        # only when ANY of the numbers are divisible by factor
        while reduce(lambda x, y: x + y, list(map(lambda z: z % factor == 0, n))):
            lcm *= factor
            for k, v in enumerate(n):
                if v % factor == 0:
                    n[k] = v // factor
        factor += 1
    return lcm


numbers = [randint(1, 30) for i in range(randint(2, 5))]
print('The Chosen Numbers are: ', end='')
print(*numbers, sep=', ')
print('Their Greatest Common Factor is: {}'.format(find_gcf(numbers)))
print('Their Least Common Multiple is: {}'.format(find_lcm(numbers)))
