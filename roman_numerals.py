"""
Roman Numerals Helper (OOP implementation)
https://www.codewars.com/kata/roman-numerals-helper
"""

class RomanNumerals:

    # a constant dictionary to map number values
    ROMANS = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
              10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
              100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
              }

    @classmethod
    def to_roman(cls, arabic: int) -> str:
        # As classmethod, this function can access the dict by referencing to cls (class object)
        roman = ''
        while arabic:
            next_chunk = max(filter(lambda x: x <= arabic, cls.ROMANS.keys()))
            roman += cls.ROMANS[next_chunk]
            arabic -= next_chunk
        return roman

    @staticmethod
    def from_roman(roman: str) -> int:
        # As static method, this function can access the dict by referencing the full class name
        arabic = 0
        while len(roman):
            next_chunk = max(filter(lambda x: roman.find(x[1]) == 0, RomanNumerals.ROMANS.items()))
            arabic += next_chunk[0]
            roman = roman[len(next_chunk[1]):]
        return arabic

print('Transformation from Arabic to Roman numbers:')
for i in [1, 75, 94, 111, 1856, 2019]:
    print('{} = {}'.format(i, RomanNumerals.to_roman(i)))
print('Transformation from Roman to Arabic numbers:')
for i in ['I', 'LXXV', 'XCIV', 'CXI', 'MDCCCLVI', 'MMXIX']:
    print('{} = {}'.format(i, RomanNumerals.from_roman(i)))
