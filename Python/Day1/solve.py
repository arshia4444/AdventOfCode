with open("input.txt") as f:
    file = list(map(lambda x: x.strip('\n'), f.readlines()))

sum_of_calories = []
temp = []

# """ PART 1 """
for i in file:
    if i.isnumeric():
        temp.append(int(i))
    else:
        sum_of_calories.append(sum(temp))
        temp = []

max_calorie = max(sum_of_calories)

print(f"PART1: {max_calorie}")

# """ PART 2 """
sum_top3_calories = sum(sorted(sum_of_calories)[-3:])

print(f"PART2: {sum_top3_calories}")