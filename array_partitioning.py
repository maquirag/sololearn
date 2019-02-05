"""Array Partitioning Challenge
Divide the given array of numbers into two subarrays
such that the absolute difference between their sums
is the smallest possible.

Possible input: enter numbers separated by spaces, e.g.
12 34 67 12 3
...or leave blank for 3 default tests
"""
def array_part(array):
    """This is a Backtracking algorithm
    that tries to find the ideal composition of the first
    part of array by repeated recursion."""

    def backtrack_part(left, right, ideal):
        """ The recursive call attempts to move the next element
        to the left part from the elements of the right part.
        If we reach the ideal then we have the solution.
        """
        # We only consider elements so we don't exceed the ideal amount
        eligibles = [n for n in right if sum(left) + n <= ideal]
        for n in eligibles:
            left.append(n)
            right.remove(n)
            # if the sum is correct now, then we return the result of the fixed half
            if ideal in (sum(left), sum(right)):
                return left
            # otherwise go deeper in the recursion
            left = backtrack_part(left, right, ideal)
            # processing the return from recursion
            if ideal in (sum(left), sum(right)):
                return left
            # if the result is not right, move the last element from left to right
            right.append(left.pop(len(left)-1))
        return left

    # First we assume that the ideal sum is half of the whole array sum
    idealsum = sum(array) // 2
    part1 = []
    part2 = array[:]
    while not part1 and idealsum > 0:
        part1 = backtrack_part(part1[:], array[:], idealsum)
        # Decrement the ideal sum for the next cycle
        idealsum -= 1
    # As soon as we have a result (left) we calculate the remaining elements
    for e in part1:
        part2.remove(e)
    return [sorted(part1), sorted(part2)]


userarray = input("Enter a list of numbers, separated by spaces.\n")
testarray = [list(map(int, userarray.split()))] if userarray else []
testarray += [[1,2,9,2], [4,15,20,2,7,5], [20,15,13,12,10]]
for a in testarray:
    subarrays = array_part(a)
    print(f'\nThe full array is: {a}')
    print(f'The first part sums up to {sum(subarrays[0])}, elements: {subarrays[0]}')
    print(f'The other part sums up to {sum(subarrays[1])}, elements: {subarrays[1]}')
    print(f'The difference is {abs(sum(subarrays[0])-sum(subarrays[1]))}')