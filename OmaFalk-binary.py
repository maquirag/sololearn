""" Solution to Oma Falk's puzzle, fixed """

# Karen says: Today is Tuesday
# Lara says: no - tomorrow is Tuesday
# Ben says: both are wrong. yesterday was Tuesday
# Marc says: yesterday was Saturday
# Paul says: today is Thursday or Friday
#   @lion what if Paul had said "either Wednesday, Thursday or Friday"
# Julia says: today is Sunday
# Sarah says: today is not Sunday.
# Which day is today if ONE person is right?

from functools import reduce
from calendar import day_name

statement = {'Karen': 0b0100000,
             'Lara' : 0b1000000,
             'Ben'  : 0b0010000,
             'Marc' : 0b0000001,
             #'Paul': 0b0001100,
             'Paul' : 0b0011100,
             'Julia': 0b0000001,
             'Sarah': 0b1111110
             }

for day in range(7):
    days = list(map(lambda x: '{:07b}'.format(x)[day], statement.values()))
    if reduce(lambda a, b: int(a) + int(b), days) == 1:
        print('Today must be {} because exactly 1 person thinks so.'.format(day_name[day]))
        whoisright = [k for (k, v) in statement.items() if '{:07b}'.format(v)[day] == '1']
        print(*whoisright, 'was right!')

# Original concept: Bitwise XOR
# It doesn't work if Paul says "Wednesday or Thurdsay or Friday"
# realday = '{:07b}'.format(reduce(lambda x, y: x ^ y, statement.values()))
# print('Today is {}.'.format(day_name[realday.find('1')]))
