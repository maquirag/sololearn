# Beaver Challenge by Oma Falk
# Cheat solution with SimpleAI Library
# https://simpleai.readthedocs.io/en/latest/
# This doesn't always give perfect result...

from simpleai.search import SearchProblem, astar
from itertools import product

codes = "ABCDEFGHI"
names = "Alex Bob Chop Dan Ed Fred Greg Hugo Ivan".split(" ")
weights = [2, 3, 5, 8, 9, 9, 12, 12, 22]
beavers = {code: (name, weight) for code, name, weight in zip(codes, names, weights)}

start = "|"
"""Starting state shows the two empty elevators.
Left of the pipe is elevator 1
Right of the pipe is elevator 2
We add the beaver codes left and right of pipe.
Keeping the state in string, makes it hashable.
"""
weight_cap = 30

class ElevatedBeavers(SearchProblem):
    def actions(self, state):
        """Define the list of possible actions.
        Add one beaver who is not in the elevators,
        to either left of right side.
        We cannot exceed each elevator capacity.
        (1, "B") means add Bob to right elevator."""
        all_options = product([0, 1], set(codes)-set(state))
        left, right = state.split("|")
        max_left_weight = weight_cap - sum(beavers[code][1] for code in left)
        max_right_weight = weight_cap - sum(beavers[code][1] for code in right)
        return [(side, code) for side, code in all_options if [max_left_weight, max_right_weight][side] >= beavers[code][1]]

    def result(self, state, action):
        """Define the new state after the action."""
        left, right = state.split("|")
        if action[0]:
            return left + "|" + ''.join(sorted(right+action[1]))
        else:
            return ''.join(sorted(left+action[1])) + "|" + right

    def is_goal(self, state):
        """We are done when the elevators are full"""
        left, right = state.split("|")
        left_weight = sum(beavers[code][1] for code in left)
        right_weight = sum(beavers[code][1] for code in right)
        return left_weight == weight_cap and right_weight == weight_cap

    def cost(self, state, action, state2):
        """The cost of an action when changing state.
        The saving of each beaver deserves the same reward.
        So the best choice is to pick the skinny ones fist.
        The cost is the weight of each beaver."""
        return beavers[action[1]][1]

    def heuristic(self, state):
        """The estimation of the remaining cost.
        This is used by informed search algorithms.
        We calculate the weight of the remaining beavers"""
        load_weight = sum(beavers[code][1] for code in state if code != "|")
        return 2 * weight_cap - load_weight

problem = ElevatedBeavers(initial_state=start)
result = astar(problem)

print(f"{result.state=}\n")

print(f"Beaver Lineup - {len(beavers)} beavers")
for name, weight in beavers.values():
    print(f"    {name:8}{weight:2} kg")
left, right = result.state.split("|")
left_weight = sum(beavers[code][1] for code in left)
right_weight = sum(beavers[code][1] for code in right)
print(f"Elevator 1 - {len(left)} beavers, total weight {left_weight} kg")
for name, weight in [guy for code, guy in beavers.items() if code in left]:
    print(f"    {name:8}{weight:2} kg")
print(f"Elevator 2 - {len(right)} beavers, total weight {right_weight} kg")
for name, weight in [guy for code, guy in beavers.items() if code in right]:
    print(f"    {name:8}{weight:2} kg")
