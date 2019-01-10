# Generate Triplets of Left/Right values (Left = 1, Right = 2)
# Basic idea: the possible combinations are 2 * 2 * 2 = 8
# And each position in the triplet can have only one of two values.
# So the result can be mapped from the binary representation of number 0-7 on 3 digits.
left_right = [format(i, '03b') for i in range(8)]
print(*left_right)
triplets = [(int(n[0]) + 1, int(n[1]) + 1, int(n[2]) + 1) for n in left_right]
print(*triplets)
