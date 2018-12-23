"""Sorting Algorithms Implementation and Comparison
Sololearn cannot handle much more than 2500 items
due to time limit, but feel free to test offline with more!"""

from random import shuffle
from time import time

def measure_sort(run_sort):
    """Decorator for performance measurement"""
    def measure_sort_wrapper(unsorted_list, sort_name):
        global steps
        steps = 0
        timer = time()
        sorted_list = run_sort(unsorted_list)  # call sorting function
        timer = time() - timer
        result = '{0} result:\n    {1} items sorted in {2} steps and {3:.6f} seconds'
        print(result.format(sort_name, len(unsorted_list), steps, timer))
        # Uncomment the following two print lines to verify the result of the sorting!
        #print('\nStart :\n{}\n'.format(unsorted_list))
        #print('Sorted:\n{}\n'.format(sorted_list))
        return sorted_list
    return measure_sort_wrapper

@measure_sort
def bubble_sort(unsorted_list):
    """Optimized Bubble Sort: repeatedly steps through the list,
    compares adjacent pairs and swaps them if they are in the wrong order.
    """
    global steps
    elems = unsorted_list[:]  # create a new list
    end = len(elems)  # we keep iterating until this point, start with the full list.
    switched = end    # just a nonzero starting value
    while switched:   # if no switch was made then the list is already sorted.
        switched = 0  # reset position of last switch.
        for i in range(1, end):  # number of cycles is 1 less than unsorted length
            if elems[i - 1] > elems[i]:
                steps += 1
                elems[i - 1], elems[i] = elems[i], elems[i - 1]
                switched = i  # mark the last position of the switch
        end = switched  # next cycle only goes until the last switch, the rest is sorted
    return elems

@measure_sort
def insertion_sort(unsorted_list):
    """Insertion Sort: takes one element at a time and inserts it in its correct position in the list,
    starting from the beginning"""
    global steps
    elems = unsorted_list[:]  # creating a new list
    for pointer in range(1, len(elems)):  # first element remains in place, starting with second
        newposition = 0
        for sortedelem in range(pointer):  # find the correct position in the part of the list sorted so far
            if elems[pointer] > elems[sortedelem]:
                newposition = sortedelem + 1
        steps += 1
        # We are doing pop() and insert() inside a for loop. Usually this is a bad idea.
        # But here we delete the current index and insert it in an earlier position.
        # So the rest of the loop is not affected and will still work.
        elems.insert(newposition, elems.pop(pointer))
    return elems

@measure_sort
def selection_sort(unsorted_list):
    """Selection Sort with swap. Find the smallest element in the whole list and swap it with the first item.
    Then cycle through the remaining list and repeat."""
    global steps
    elems = unsorted_list[:]  # creating a new list
    for current in range(len(elems) - 1):  # cycle all positions in the list except the last
        minimum = current  # start with first index of unsorted part
        for cycle in range(current + 1, len(elems)):  # determine the index of the smallest element
            if elems[cycle] < elems[minimum]:
                minimum = cycle
        steps += 1
        elems[current], elems[minimum] = elems[minimum], elems[current]  # do the actual swap
    return elems

@measure_sort
def merge_sort(unsorted_list):
    """Splits the list in 2 parts, then keeps splitting until each part has only 1 item.
    Merge together the sub-lists in correct order until the whole list is rebuilt.
    """
    def merge_sort_start(elements):
        """Split the elements in two, until the parts have only 1 elements. Then they are sorted.
        In the end, combine the separated parts, so that sorted list partition is returned.
        """
        global steps
        splitpoint = len(elements) // 2
        left = elements[:splitpoint]
        right = elements[splitpoint:]
        # if the parts have more than 1 item, split them further by recursive call
        if len(left) > 1:
            left = merge_sort_start(left)
        if len(right) > 1:
            right = merge_sort_start(right)
        steps += 1
        # unite the two already sorted parts
        merged = []
        while len(left) + len(right) > 0:  # cycle as long as any side has at least 1 element
            if len(left) > 0 and len(right) > 0:
                # both sites are sorted, therefore it is enough to look at the first element
                # if both sides have an element left, then pick the smaller one
                merged.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
            else:
                # otherwise ju
                merged.append(left.pop(0) if len(left) > 0 else right.pop(0))
            steps += 1
        return merged

    global steps
    elems = unsorted_list[:]  # creating a new list
    elems = merge_sort_start(elems)
    return elems

@measure_sort
def radix_sort(unsorted_list):
    """Places the elements into buckets based on their digits.
    MSD = Most Significant Digit: starting the sort with the leftmost digits.
    Recursively sort the numbers in each bucket into further buckets based on next digit.
    """
    def radix_sort_start(elements, digit):
        """Recursively organize the numbers in buckets labeled by the next digit"""
        global steps
        buckets = [[] for i in range(10)]
        for number in elements:
            steps += 1
            # put the number in the current digit's correct bucket
            buckets[int(str(number // 10**(digit-1))[-1])].append(number)
        if digit > 1:
            for bucket in range(10):
                if buckets[bucket]:  # start recursive sort if bucket is not empty
                    buckets[bucket] = radix_sort_start(buckets[bucket], digit-1)
        # return the flattened contents of the buckets in the right order
        flattened_list = []
        for bucket in buckets:
            for number in bucket:
                flattened_list.append(number)
        return flattened_list

    global steps
    maxdigit = len(str(max(unsorted_list)))  # MSD = determined from the largest number in the list
    elems = unsorted_list[:]  # creating a new list
    elems = radix_sort_start(elems, maxdigit)
    return elems

@measure_sort
def quick_sort(unsorted_list):
    """Splits the list in Low and High parts.
    Pivoting: Chooses a pivot value and compare each element with the pivot.
    Partitioning: If an element is in the wrong place (Low or High) compared to the pivot, it is switched.
    Then all elements in High are larger than the pivot, and all elements in Low are smaller.
    Recursively repeats the same for each partition, until 1 value remains in each partition.
    """
    def quick_sort_start(elems, low, high):
        """Determines the splitpoint by partitioning the list, then calls the sort on both parts."""
        splitpoint = quick_sort_partition(elems, low, high)
        # The splitpoint is already in the correct position.
        if low < splitpoint - 1:
            quick_sort_start(elems, low, splitpoint - 1)  # run low recursion only with more than 1 sortable element
        if splitpoint + 1 < high:
            quick_sort_start(elems, splitpoint + 1, high)  # run high recursion only with more than 1 sortable element

    def quick_sort_partition(elems, low, high):
        """Hoare Partition Scheme: transverse the list with 2 parallel indices (left, right)"""
        # KLUDGE: this is not tested and may not work properly with lists that have some repeating values!
        global steps
        pivotvalue = elems[low]  # arbitrary selection of the first element as pivot, this can be improved
        left = low + 1  # ignore the pivot when we start iterating
        right = high
        while left <= right:
            # Find leftmost element greater than or equal to pivot.
            while elems[left] < pivotvalue and left < right:
                left += 1
            # Find rightmost element greater than or equal to pivot.
            while elems[right] > pivotvalue:
                right -= 1
            if left < right:
                # switch the high and low values that are out of place, then keep going
                elems[left], elems[right] = elems[right], elems[left]
                steps += 1
            if left >= high:  # the pivot is the highest value in the list, break out of cycle
                break
        # End of partitioning, switch the converged item with the pivot item.
        # The right landed on correct index of pivot.
        elems[low], elems[right] = elems[right], elems[low]
        steps += 1
        return right  # the index of the item that is now in correct position

    global steps
    elems = unsorted_list[:]  # creating a new list
    quick_sort_start(elems, 0, len(elems) - 1)  # start nested function with the full list first
    return elems

def distribution_sort(unsorted_list):
    """Not yet implemented"""
    return None

def heap_sort(unsorted_list):
    """Not yet implemented"""
    return None

steps = 0  # must be declared as global, so it can be incremented within functions and used in decorator
# Change the Range value to test with different number of elements!
unsorted = [i + 1 for i in range(2500)]  # unique values
shuffle(unsorted)
print('Sorting randomized unique values up to {}...\n'.format(len(unsorted)))
bubble_sort(unsorted, 'Optimized Bubble Sort')
insertion_sort(unsorted, 'Insertion Sort')
selection_sort(unsorted, 'Selection Sort')
merge_sort(unsorted, 'Merge Sort')
radix_sort(unsorted, 'Radix Sort')
quick_sort(unsorted, 'Quick Sort (Hoare)')
