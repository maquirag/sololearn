# SUDOKU Validator with sets
from itertools import chain

def validate_sudoku(puzzle):
    nums = set(range(1, 10))
    rows = lambda x: set(puzzle[x])
    cols = lambda y: {puzzle[n][y] for n in range(9)}
    blks = lambda x, y: set(chain.from_iterable(list(zip(*puzzle[x:x + 3]))[y:y + 3]))
    return all(nums == rows(i) == cols(i) == blks(i//3*3, i%3*3) for i in range(9))

puzzles = [

    [[3, 5, 2, 9, 1, 8, 6, 7, 4],
    [8, 9, 7, 2, 4, 6, 5, 1, 3],
    [6, 4, 1, 7, 5, 3, 2, 8, 9],
    [7, 8, 3, 5, 6, 9, 4, 2, 1],
    [9, 2, 6, 1, 3, 4, 7, 5, 8],
    [4, 1, 5, 8, 2, 7, 9, 3, 6],
    [8, 6, 4, 3, 7, 5, 8, 9, 2],
    [2, 7, 8, 4, 9, 1, 3, 6, 5],
    [5, 3, 9, 6, 8, 2, 1, 4, 7]],

    [[3, 5, 2, 9, 1, 8, 6, 7, 4],
    [8, 9, 7, 2, 4, 6, 5, 1, 3],
    [6, 4, 1, 7, 5, 3, 2, 8, 9],
    [7, 8, 3, 5, 6, 9, 4, 2, 1],
    [9, 2, 6, 1, 3, 4, 7, 5, 8],
    [4, 1, 5, 8, 2, 7, 9, 3, 6],
    [1, 6, 4, 3, 7, 5, 8, 9, 2],
    [2, 7, 8, 4, 9, 1, 3, 6, 5],
    [5, 3, 9, 6, 8, 2, 1, 4, 7]]

    ]

for p in puzzles:
    print(*p, sep='\n')
    print('Result: ', validate_sudoku(p))
