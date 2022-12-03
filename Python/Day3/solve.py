with open("input.txt") as f:
    file = list(map(lambda x: x.strip(), f.readlines()))

alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
priority = 0

#""" PART 1 """

for i in file:
    first_part = set(i[:len(i) // 2])
    second_part = set(i[len(i) // 2:])
    type_of_item = first_part & second_part
    priority += alphabets.index(type_of_item.pop()) + 1

print(f"PART 1:{priority}")

#""" PART 2 """

priority = 0
groups = list(filter(None, [file[i:i+3] for i in range(0, len(file), 3)]))

for i in range(len(groups)):
    type_of_item = set(groups[i][0]) & set(groups[i][1]) & set(groups[i][2])
    priority += alphabets.index(type_of_item.pop()) + 1

print(f"PART 2:{priority}")

