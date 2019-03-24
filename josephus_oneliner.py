""" Josephus Problem -- ONELINER """
# Parameter of the function is the list of the soldiers.
j = lambda s: s[0] if len(s) == 1 else j(s[2:] + s[0:1])

# Testing for various cases
for s in range(2, 21):
    print(f"{s} soldiers started. Soldier #{j(list(range(1, s+1)))} survived.")
