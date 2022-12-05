score = 0

# A = Rock
# B = Paper
# C = Scissors

scenarios = [['A', 'Z'], ['B', 'Z'], ['C', 'Z'], ['A', 'Y'], ['B', 'Y'], ['C', 'Y'], ['A', 'X'], ['B', 'X'], ['C', 'X']]
point = [8, 9, 7, 4, 5, 6, 3, 1, 2]

def calcPoints(list):
    for scenario in scenarios:
        if list == scenario:
            i = scenarios.index(list)
            return point[i]

with open('list.txt') as file:
    for line in file:
        match = line.strip().split()
        result = calcPoints(match)
        print(result)
        score += result
    print(score)