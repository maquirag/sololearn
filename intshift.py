""" Shift Digit left/right without type conversion.
Left Shift: 12345 => 23451
Right Shift: 12345 => 51234
Enter test number or leave the input empty.
"""
def d(n):
    """The number of digits shifted oppositely.
    Same as round(math.log10(n))"""
    digit = 0
    while n >= 10:
        n //= 10
        digit += 1
    return digit

lshift = lambda n: n % (10**d(n)) * 10 +  n // (10**d(n))
rshift = lambda n: (n % 10) * 10**d(n) + n // 10
n = int(input() or 12345)
print(f'{n}: left {lshift(n)}, right {rshift(n)}')
