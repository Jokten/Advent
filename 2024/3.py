import re, aoc
d = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))", aoc.get_data(2024,3))
p1, p2, e = 0, 0, 1
for i in d:
    if i[2]: e = 1
    elif i[3]: e = 0
    else:
        p1 += int(i[0]) * int(i[1])
        p2 += int(i[0]) * int(i[1]) * e
print(p1, p2)
