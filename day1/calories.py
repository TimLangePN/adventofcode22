calories = []
top_three_calories = []
with open('list.txt') as file:
    temp_calories = []
    for line in file:
            if line == '\n':
                calories.append(sum(temp_calories))
                temp_calories = []
                continue
            temp_calories.append(int(line))
    i = 0
    while i != 3:
        top_three_calories.append(max(calories))
        calories.remove(max(calories))
        i += 1
    print(sum(top_three_calories))