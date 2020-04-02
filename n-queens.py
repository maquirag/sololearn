"""
N-Queens Problem
Placing N chess-queens on an NxN chessboard
so that no two queens attack each other.

Algorithm is based on the idea from:
https://www.geeksforgeeks.org/n-queen-problem-using-branch-and-bound/
"""

import time
from random import randint
# import sys
# from codecs import getwriter
# sys.stdout = getwriter('utf_16')(sys.stdout.buffer, 'strict')


def queen_solver(N):
    """Place a queen in one column at a time, starting from left.
    If all queens are down, mark solution.
    """
    # Initializing the Board
    solution = []
    Q = '\N{WHITE CHESS QUEEN}'
    T = '\N{WHITE LARGE SQUARE}' + '\N{BLACK LARGE SQUARE}'
    board, taken_rows, taken_slash, taken_backs = {}, set(), set(), set()
    # Rows and Columns are indexed from 0 to N-1
    # taken_rows  taken_slash  taken_backs
    #     0           0 1 2 3      3 2 1 0
    #     1           1 2 3 4      4 3 2 1
    #     2           2 3 4 5      5 4 3 2
    #     3           3 4 5 6      6 5 4 3
    # Taken column is tracked by the calling parameter of the recursion.
    # Board dictionary format: {row: col}  e.g. {0: 2, 1: 0, 2: 3, 3: 1}

    def queen_column(col):
        """Try to place a queen in column `col`"""
        # If all columns are taken, adding the valid solution stringified
        if col == N:
            solution.append('\n' + '\n'.join(
                ''.join(Q if board[r] == c else T[(r+c) % 2]
                        for c in range(N)) for r in range(N))
            )
            return
        # Try placing a queen in each row
        for row in range(N):
            # If the position is not taken:  put down a queen, mark taken spots and recurse
            if row not in taken_rows and \
                    (row + col) not in taken_slash and \
                    (row - col + N - 1) not in taken_backs:
                board[row] = col
                taken_rows.add(row)
                taken_slash.add(row + col)
                taken_backs.add(row - col + N - 1)
                # Jump to next column
                queen_column(col + 1)
                # When backtracking, remove the queen and the marks
                board.pop(row)
                taken_rows.remove(row)
                taken_slash.remove(row + col)
                taken_backs.remove(row - col + N - 1)
        return

    queen_column(0)  # Start putting down queens at column 0
    # If solutions were found at the end of recursion, they are collected and returned
    return solution


t = time.time()  # Performance Measurement
# Change the range to get specific N solutions
for N in range(1, 13):
    solutions = queen_solver(N)
    print(f'\n{len(solutions)} solutions found for N = {N}')
    # Uncomment the following line to print one random solution for each N
    if solutions:
        print(
            f'One random solution:{solutions[randint(0, len(solutions) - 1)]}')
    # Uncomment the following line to print all solutions for the range of Ns
    # print(*solutions, sep='\n', end='\n')
print(f'\nTime taken: {time.time() - t:.3f} seconds')

"""
Number of solutions found (offline):
1 solutions found for N = 1
0 solutions found for N = 2
0 solutions found for N = 3
2 solutions found for N = 4
10 solutions found for N = 5
4 solutions found for N = 6
40 solutions found for N = 7
92 solutions found for N = 8
352 solutions found for N = 9 -- time < 0.05s
724 solutions found for N = 10 -- time 0.2s
2680 solutions found for N = 11 -- time 0.8s
14200 solutions found for N = 12 -- time 3.9s
73712 solutions found for N = 13 -- time 21.7s
365596 solutions found for N = 14 -- time 129.5s
"""
