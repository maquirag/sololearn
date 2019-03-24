""" Josephus Problem
INSTRUCTION: Enter number of soldiers > 1
             or leave empty for default 10.
The problem is named after Flavius Josephus, a Jewish historian living in the 1st century.
According to Josephus' account of the siege of Yodfat, he and his 40 soldiers were trapped
in a cave by Roman soldiers. They chose suicide over capture, and settled on a serial method
of committing suicide by drawing lots. Josephus states that by luck or possibly by the hand of God,
he and another man remained until the end and surrendered to the Romans rather than killing themselves.
Source: Wikipedia
"""
def josephus(circle):
    if len(circle) == 1:
        return circle[0]
    print(f'Soldier #{circle[0]} kills Soldier #{circle[1]}.')
    return josephus(circle[2:] + circle[0:1])

try:
    soldiers = int(input())
    assert soldiers > 1
except (ValueError, AssertionError) as e:
    soldiers = 10
print(f'{soldiers} soldiers are standing in circle.')
print(f'Soldier #{josephus(list(range(1, soldiers + 1)))} remains the only survivor.')