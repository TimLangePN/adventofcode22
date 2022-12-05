score = 0

# Rock = A X
# Paper = B Y
# Scissors = C Z

class Scenarios:
    win = [['A', 'Y'], ['B', 'Z'], ['C', 'X']]
    tie = [['A', 'X'], ['B', 'Y'], ['C', 'Z']]
    loss = [['A', 'Z'], ['C', 'Y'], ['B', 'X']]


def CalculatePoints(item):
    match item:
        case 'X': return 1
        case 'Y': return 2
        case 'Z': return 3


def CalculateOutcome(decisions):
    for scenario in Scenarios.win:
        if scenario == decisions: 
            return 6 + CalculatePoints(decisions[1])
    for scenario in Scenarios.tie:
        if scenario == decisions: 
            return 3 + CalculatePoints(decisions[1])
    for scenario in Scenarios.loss:
        if scenario == decisions: 
            return 0 + CalculatePoints(decisions[1])

# C vs Z = tie, scissor vs scissor = 3 + 3 = 6

with open('list.txt') as file:
    for line in file:
        match = line.strip().split()
        try:
            score += CalculateOutcome(match)
        except: 
            print(Exception)
        print(score)