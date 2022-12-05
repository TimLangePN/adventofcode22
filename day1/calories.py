calories = []

with open('list.txt') as file:
    temp_calories = []
    for line in file:
            if line == '\n':
                calories.append(sum(temp_calories))
                temp_calories = []
                continue
            temp_calories.append(int(line))
    print(max(calories))