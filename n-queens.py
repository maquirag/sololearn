"""
N-Queens Problem
Placing N chess-queens on an NxN chessboard
so that no two queens attack each other.

Algorithm is based on the idea from:
https://www.geeksforgeeks.org/n-queen-problem-using-branch-and-bound/
"""

import time

def queen_solver(N):
    """Place a queen in one column at a time, starting from left.
    If all queens are down, mark solution.
    """
    # Initializing the Board
    solution = []
    board = [[0 for j in range(N)] for i in range(N)]
    taken_rows = [0 for i in range(N)]
    taken_slash = [0 for i in range(2 * N + 1)]  # Slash shaped diagonals
    taken_backs = [0 for i in range(2 * N + 1)]  # Backslash shaped diagonals
    # taken_slash    taken_backs
    #    0 1 2 3        3 2 1 0
    #    1 2 3 4        4 3 2 1
    #    2 3 4 5        5 4 3 2
    #    3 4 5 6        6 5 4 3

    def queen_column(col):
        """Try to place a queen in column `col`"""
        # If all columns are taken, then this is a valid solution
        if col >= N:
            # Solution stringified, because the board is mutable and will change
            solution.append('\n'.join(' '.join(str(c) for c in r) for r in board))
            return True
        # Try placing a queen in each row
        for row in range(N):
            # If the position is not taken, then put down a queen, mark taken spots and recurse
            if not (taken_rows[row] or taken_slash[row + col] or taken_backs[row - col + N - 1]):
                board[row][col] = 1
                taken_rows[row] = 1
                taken_slash[row + col] = 1
                taken_backs[row - col + N - 1] = 1
                # Jump to next column
                queen_column(col + 1)
                # Remove the queen and the marks for further iterations
                board[row][col] = 0
                taken_rows[row] = 0
                taken_slash[row + col] = 0
                taken_backs[row - col + N - 1] = 0
        return

    queen_column(0)
    return solution

t = time.time()
# Change the range to get specific N solutions
for N in range(1, 12):
    solutions = queen_solver(N)
    print(f'{len(solutions)} solutions found for N = {N}\n')
    # Uncomment the following print to see detailed solutions!
    print(*solutions, sep='\n\n', end='\n\n')
print(f'Time taken: {time.time() - t:.3f} seconds')

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
352 solutions found for N = 9
724 solutions found for N = 10
2680 solutions found for N = 11
14200 solutions found for N = 12
73712 solutions found for N = 13
365596 solutions found for N = 14
"""