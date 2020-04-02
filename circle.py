"""
BLACK HOLE
Enter the radius of the hole!
MIN = 1
MAX = 10 for Portrait, 18 for Landscape
"""
#import sys
#from codecs import getwriter
#sys.stdout = getwriter('utf_16')(sys.stdout.buffer, 'strict')
W = '\N{WHITE LARGE SQUARE}'
B = '\N{BLACK LARGE SQUARE}'

try:
    r = int(input())
    assert 0 < r < 19
except (ValueError, AssertionError):
    r = 10

for x in range(-r, r + 1):
    for y in range(-r, r + 1):
        d = (x**2 + y**2)**0.5
        print(W if d >= r else B, sep='', end='' if y < r else '\n')

print('')

for x in range(-r, r + 1):
    for y in range(-r, r + 1):
        d = (x**2 + y**2)**0.5
        print(B if abs(d - r) < 0.5 else W, sep='', end='' if y < r else '\n')
