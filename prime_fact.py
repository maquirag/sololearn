"""Prime factorization
Enter a number > 1 or leave empty for default test.
get_prime_factors function returns a dictionary.
Output is printed in exponential form.
"""


def get_prime_factors(num):
    """Returns prime factors of a number in a dictionary."""
    test, primes = 2, {}
    while test <= num:
        if num % test == 0:
            num /= test
            # Increase the value of the prime key or add key
            primes[test] = 1 + (primes[test] if test in primes else 0)
        else:
            test += 1
    return primes


# Operation can be done on a positive integer, greater than 1.
try:
    number = int(input('Enter a number: '))
    if number < 2:
        raise ValueError
except ValueError:
    # Default test value is assigned if the input is not suitable.
    number = 2 ** 3 * 3 ** 7 * 5 * 11 ** 2 * 67 * 389
factors = get_prime_factors(number)
exp_form = ' * '.join(str(k) + ('^' + str(factors[k]) if factors[k] > 1 else '') for k in factors)
print('Prime factorization\n{} = {}'.format(number, exp_form))
