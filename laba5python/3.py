with open('3input.txt', 'r', encoding='utf-8') as infile:
    lines = infile.readlines()
children = []
for line in lines:
    parts = line.strip().split()
    surname = parts[0]
    name = parts[1]
    age = int(parts[2])
    children.append((surname, name, age))

youngest = min(children, key=lambda x: x[2])
oldest = max(children, key=lambda x: x[2])

with open('youngest.txt', 'w') as f_mladshiy:
    f_mladshiy.write(f"{youngest[0]} {youngest[1]} {youngest[2]}\n")

with open('oldest.txt', 'w') as f_starshiy:
    f_starshiy.write(f"{oldest[0]} {oldest[1]} {oldest[2]}\n")
