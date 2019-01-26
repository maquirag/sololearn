"""
Drawing a circle with radius N on char
"""
#import sys
#from codecs import getwriter
#sys.stdout = getwriter('utf_16')(sys.stdout.buffer, 'strict')
T = '\N{WHITE LARGE SQUARE}'

try:
    r = int(input('Enter radius: '))
    assert 4 < r < 50
except (ValueError, AssertionError):
    r = 10

for x in range(-r, r + 1):
    for y in range(-r, r + 1):
        d = (x**2 + y**2)**0.5
        print('*' if d >= r else ' ', sep='', end='' if y < r else '\n')
