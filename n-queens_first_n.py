"""
N-Queens Problem
Simplified version: find first solution for a specific N

Enter Board Size (N) in input box!
SoloLearn can handle up to N = 21
"""
# import sys
# from codecs import getwriter
# sys.stdout = getwriter('utf_16')(sys.stdout.buffer, 'strict')
Q, T = u'\u2655', u'\u2b1c' + u'\u2b1b'

def queen_solver(N):
    solution, board = [], {}
    taken_rows, taken_slash, taken_backs = set(), set(), set()

    def queen_column(col):
        if col == N:
            solution.append('\n'.join(''.join(Q if board[r] == c else T[(r+c) % 2]
                for c in range(N)) for r in range(N)))
            return
        for row in range(N):
            if row not in taken_rows and \
                    (row + col) not in taken_slash and \
                    (row - col + N - 1) not in taken_backs:
                board[row] = col
                taken_rows.add(row)
                taken_slash.add(row + col)
                taken_backs.add(row - col + N - 1)
                queen_column(col + 1)
                if solution:
                    return
                board.pop(row)
                taken_rows.remove(row)
                taken_slash.remove(row + col)
                taken_backs.remove(row - col + N - 1)
        return

    queen_column(0)
    return solution

try:
    N = int(input('Enter the Board Size (N > 0): '))
    if N < 1:
        raise ValueError
except ValueError:
    N = 8
first = queen_solver(N)
if first:
    print(f'\nFirst solution found for N = {N}:\n{first[0]}')
else:
    print('\nThere are no solutions for this board size.')