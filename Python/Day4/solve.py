with open("input.txt") as f:
    file = list(map(lambda x: x.strip(), f.readlines()))

pairs = [i.split(',') for i in file]
count = 0
overlaps = 0

for i in pairs:
    sorted_pair = sorted(map(lambda x: x.split('-'), i))
    p_left1, p_right1 = int(sorted_pair[0][0]), int(sorted_pair[1][0])
    p_left2, p_right2 = int(sorted_pair[0][1]), int(sorted_pair[1][1])

    # """ PART 1 """
    if p_left1 <= p_right1 and p_left2 >= p_right2 or p_right1 <= p_left1 and p_left2 <= p_right2:
        count += 1

    # """ PART 2 """
    if not p_left2 < p_right1 or p_right2 < p_left1:
        overlaps += 1

print(f"PART 1: {count}")
print(f"PART 2:{overlaps}")
