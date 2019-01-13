for i in range(ord('\u2580'),ord('\u259f')+1):
    print(('' if i % 32 else f'\n{i: >6}  ') + f'{chr(i) if chr(i).isprintable() else " ":2}', end=' ')

Q = '\N{WHITE CHESS QUEEN}'
T = '\N{WHITE LARGE SQUARE}' + '\N{BLACK LARGE SQUARE}'
print(Q, T)

solution = '\n' + '\n'.join(''.join(Q if r == c else T[(r+c) % 2] for c in range(8)) for r in range(8))
print(solution)