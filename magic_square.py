import numpy as np

def create_magic_square(n):
    """Create a magic square with n*n elements"""

    def get_sums(s):
        """Calculate all magic sums in the square"""
        return [sum(s[x*n:(x+1)*n]) for x in range(n)] + \
               [sum(s[y::n]) for y in range(n)] +\
               [sum(s[::n+1]), sum(s[n-1:n*n-1:n-1])]

    def fill_magic(square, position):
        """Recursively find the next element"""
        sums = get_sums(square)
        elems = filter(lambda e: all(msum - e >= s for s in sums), nums)
        if (position + 1) % n == 0:
            x = position // n
            elems = filter(lambda e: e == msum - sum(square[x*n:(x+1)*n]), elems)
        for elem in elems:
            print(square, elem, nums, sums)
            square[position] = elem
            nums.remove(elem)
            if position < n * n - 1:
                fill_magic(square, position + 1)
            if all(msum == s for s in get_sums(square)):
                return square
            nums.append(elem)
            square[position] = 0
        return square

    nums = list(range(1, n * n + 1))  # Available elements
    msum = sum(nums) // n            # Magic Sum
    print(f'Magic square, Size = {n}, Magic Sum = {msum}')
    result = fill_magic([0 for _ in range(1, n * n + 1)], 0)
    #if sum(result):
    print(*np.array(result).reshape(n, n), sep='\n', end='\n\n')
    #else:
    #print('No such square was found.')


#size = int(input() or 4)
create_magic_square(3)
#create_magic_square(4)