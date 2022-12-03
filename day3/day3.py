# star 1
# infile = open('input.txt')
# content = infile.read()
# content_split = content.splitlines()
# total = 0
# for line in content_split:
#     length = len(line)
#     half = int(length / 2)
#     sack_a = line[:half]
#     sack_b = line[half:length]
#     print("sack_a = ", sack_a)
#     print("sack_b = ", sack_b)
#     com_str = ''.join(set(sack_a).intersection(sack_b))
#     # com_str = set(sack_a) & set(sack_b)
#     print(com_str)
#     if com_str.islower():
#         priority = ord(com_str) - ord('a') + 1
#     if com_str.isupper():
#         priority = ord(com_str) - ord('A') + 27
#     print(priority)
#     total += priority

# print("star 1:", total)

# star 2
infile = open('input.txt')
content = infile.read()
content_split = content.splitlines()
total = 0
group = []
for i, line in enumerate(content_split):
    if i % 3 == 0:
        group.clear()
    group.append(line)
    print(group)
    if i % 3 == 2:
        com_str = ''.join(set(group[0]).intersection(group[1]).intersection(group[2]))
        print(com_str)
        if com_str.islower():
            priority = ord(com_str) - ord('a') + 1
        if com_str.isupper():
            priority = ord(com_str) - ord('A') + 27
        print(priority)
        total += priority
print("star 2:", total)