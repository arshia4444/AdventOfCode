with open('input.txt') as f:
    file = map(lambda x: x.strip('\n'), f.readlines())

rock, point_rock = ('A', 'X'), 1
paper, point_paper = ('B', 'Y'), 2
scissors, point_scissors = ('C', 'Z'), 3

game = list(file)
part1 = 0
part2 = 0

for i in game:
    opponent, me = i.split()

    # """ PART 1 """
    part1 += {rock[1]: point_rock, paper[1]: point_paper, scissors[1]: point_scissors}[me]
    part1 += {
        (rock[0], rock[1]): 3,
        (paper[0], rock[1]): 0,
        (scissors[0], rock[1]): 6,
        # ----
        (rock[0], paper[1]): 6,
        (paper[0], paper[1]): 3,
        (scissors[0], paper[1]): 0,
        # ----
        (rock[0], scissors[1]): 0,
        (paper[0], scissors[1]): 6,
        (scissors[0], scissors[1]): 3,
    }[(opponent, me)]

    # """ PART 2 """
    part2 += {rock[1]: 0, paper[1]: 3, scissors[1]: 6}[me]
    part2 += {
        (rock[0], rock[1]): 3,
        (paper[0], rock[1]): 1,
        (scissors[0], rock[1]): 2,
        # ----
        (rock[0], paper[1]): 1,
        (paper[0], paper[1]): 2,
        (scissors[0], paper[1]): 3,
        # ----
        (rock[0], scissors[1]): 2,
        (paper[0], scissors[1]): 3,
        (scissors[0], scissors[1]): 1,
    }[(opponent, me)]

print(f"PART1: {part1}")
print(f"PART2: {part2}")