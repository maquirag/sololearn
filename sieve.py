"""Sieve of Eratosthenes
Calculates prime numbers.
Enter the upper range of Primes.
"""
import time


def primes_reduction(nums: list):
    """ Returns the list of primes by list reduction. """
    prime = 0
    while prime < len(nums):
        for e in nums[prime+1:]:
            if e % nums[prime] == 0:
                nums.remove(e)
        prime += 1
    return nums


def primes_filter(nums: list):
    """ Returns the list of primes by list slicing. """
    p = 0
    while p < len(nums):
        nums = nums[:p + 1] + list(filter(lambda x: x % nums[p] != 0, nums[p + 1:]))
        p += 1
    return nums


def primes_recursion(nums: list):
    """ Returns the list of primes by recursion. MAX range: 998 """
    if len(nums) == 1:
        return nums
    else:
        return [nums[0]] + list(filter(lambda x: x % nums[0] != 0, primes_recursion(nums[1:])))


try:
    n = int(input('Calculate primes up to this number:'))
except ValueError:
    n = 997

r = [i for i in range(2, n + 1)]

t = time.time()
print(*primes_reduction(r), sep=', ')
t = time.time() - t
print('Execution time of primes_reduction({0}): {1:.8f} sec'.format(n, t))
print('List of primes up to {0}:'.format(n))
t = time.time()
print(*primes_filter(r), sep=', ')
t = time.time() - t
print('Execution time of primes_filter({0}): {1:.8f} sec'.format(n, t))
t = time.time()
print(*primes_recursion(r), sep=', ')
t = time.time() - t
print('Execution time of primes_recursion({0}): {1:.8f} sec'.format(n, t))