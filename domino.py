"""Project Domino (OOP)
This program will pick a random tile from a full Domino Set
and make a connected sequence consuming all the tiles.
"""
# TODO: full code review and refactor (simplify)
class Domino:
    def __init__(self):
        self.onhand_set = [(x, y) for x in range(7) for y in range(7) if x >= y]
        random.shuffle(self.onhand_set)
        self.play_tile(self.onhand_set[0])

    def play_tile(self, tile, last = None):
        self.onhand_set.pop(i)
        if last is None:
            self.played_set = [tile] if random.choice([0, 1]) else [(tile[1], tile[0])]
        else:
            self.played_set.extend([tile] if tile[0] == last else [(tile[1], tile[0])])

    def play(self):
        while self.onhand_set:
            last_pip = self.played_set[-1][1]
            if (last_pip, last_pip) in self.onhand_set:
                i = self.onhand_set.index(tile)
                self.play_tile(i)
                continue
            eligible = [tile for tile in self.onhand_set if last_pip in tile]
            self.play_tile(random.choice(eligible), last_pip)
        return

    def printable(self, tile):
        return f"{self.pips[tile[0]]}{self.pips[tile[1]]}"

    def print_sequence(self):
        print(self.played_set)

print("Shuffling Domino Set.")
domino = Domino()
print(f"The starting tile is: {domino.printable(domino.played_set[0])}")
print("Playing the whole set.")
domino.play()
print("Result:")
domino.print_sequence()