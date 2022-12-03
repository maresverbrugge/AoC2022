# star 1
infile = open('input_day1.txt')
content = infile.read()
content_split = content.splitlines()
elfs = []
total = 0
for content in content_split:
    print(content)
    if (content is ''):
        elfs.append(total)
        total = 0
    else:
        total += int(content)
# print("elfs =", elfs)
print("highest =", max(elfs))

# star 2
infile = open('input_day1.txt')
content = infile.read()
content_split = content.splitlines()
elfs = []
total = 0
for content in content_split:
    if (content is ''):
        elfs.append(total)
        total = 0
    else:
        total += int(content)
elfs.sort()
# print("sorted elfs =", elfs)
last_3 = elfs[-3:]
print("last 3 =", last_3)
print("sum of last 3 =", sum(last_3))
