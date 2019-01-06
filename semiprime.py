"""
Semiprimes are integer numbers which can be factorized as the product of exactly 2 prime numbers.
"""


def is_semiprime(n: int) -> bool:
    prime, facts = 2, []
    while n > 1:
        while n % prime == 0:
            n //= prime
            facts.append(prime)
        prime += 1
    return True if len(facts) == 2 else False


start, end = 2, 1000
for i in range(start, end + 1):
    if is_semiprime(i):
        print(i, end=' ')
