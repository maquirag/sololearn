"""Nine Men Morris representation
Challenge by Oma Falk"""
import numpy as np
from random import choice

NONE, FREE, WHITE, BLACK = 0, 1, 2, 3
TILES = {WHITE: "W",
         BLACK: "B",
         FREE:  "o",
         NONE:  " "}


class Morris:

    def __init__(self, rand_moves=0, setup=None):
        # dimensions: outer-inner, top-bottom, left-right
        self.morris = np.ones((3, 3, 3), dtype=np.int)
        self.morris[:, 1, 1] = NONE
        self.next_move = WHITE
        if setup:
            for b in setup[BLACK]:
                self.morris[b] = BLACK
            for w in setup[WHITE]:
                self.morris[w] = WHITE
        while rand_moves > 0:
            empties = [idx for idx in np.ndindex(
                self.morris.shape[:]) if self.morris[idx] == FREE]
            self.morris[choice(empties)] = self.next_move
            self.next_move = BLACK + WHITE - self.next_move
            rand_moves -= 1
        print(self)
        self.count_mills(WHITE)
        self.count_mills(BLACK)

    def count_mills(self, player):
        """TODO: Double mills!"""
        mills = 0
        slices = [idx for idx in np.ndindex(self.morris.shape[:2])]
        for x, y in slices:
            mills += all(player == piece for piece in self.morris[x, y, :])
            mills += all(player == piece for piece in self.morris[x, :, y])
            mills += all(player == piece for piece in self.morris[:, x, y])
        print(f'{TILES[player]} mills: {mills}')

    def stringify(self):
        return np.vectorize(TILES.get)

    def __repr__(self):
        board = [""]
        board.append("{}--------{}--------{}".format(*
                                                     self.stringify()(self.morris[0, 0, :])))
        board.append("|        |        |")
        board.append("|  {}-----{}-----{}  |".format(*
                                                     self.stringify()(self.morris[1, 0, :])))
        board.append("|  |     |     |  |")
        board.append("|  |  {}--{}--{}  |  |".format(*
                                                     self.stringify()(self.morris[2, 0, :])))
        board.append("|  |  |     |  |  |")
        board.append("{}--{}--{}     {}--{}--{}".format(*self.stringify()
                                                        (self.morris[:, 1, 0]), *self.stringify()(self.morris[::-1, 1, 2])))
        board.append("|  |  |     |  |  |")
        board.append("|  |  {}--{}--{}  |  |".format(*
                                                     self.stringify()(self.morris[2, 2, :])))
        board.append("|  |     |     |  |")
        board.append("|  {}-----{}-----{}  |".format(*
                                                     self.stringify()(self.morris[1, 2, :])))
        board.append("|        |        |")
        board.append("{}--------{}--------{}".format(*
                                                     self.stringify()(self.morris[0, 2, :])))
        return "\n".join(board)


wiki = {BLACK: [(1, 1, 0), (1, 2, 0), (2, 1, 0), (1, 0, 2), (1, 1, 2), (1, 2, 2)],
        WHITE: [(2, 0, 2), (2, 1, 2), (2, 2, 2), (1, 2, 1), (0, 2, 1)]}
Morris(setup=wiki)
Morris(rand_moves=16)
