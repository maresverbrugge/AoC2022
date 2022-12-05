# import re
# import copy
# star 1
with open('input.txt') as infile:
    containers, moves = infile.read().split('\n\n')
print(moves)
print(containers + '\n')
containers = containers.replace('[','').replace(']','').replace(' ', '').split('\n')
amount_containers = containers[-1]
print(amount_containers[-1])

containers = containers[0:-1]
print(containers)
fullest = 1
for container in containers:
    longest = len(container)
    if (longest > fullest):
        fullest = longest
print(fullest)

i = 0
stack = {}
print(containers[0][0])
print(containers[1][0])
print(containers[2][2])
while (i < int(amount_containers[-1])):
    j = 0
    stack[i] = []
    # print("stack", i + 1, stack[i])
    i += 1
    # print(containers[i][j])
    # stack[i].append(containers[1][0])
    # print("stack", i + 1, stack[i])

i = 0
while (i > amount_containers):
    j = amount_containers
    while (j < fullest - 1):
        stack[i].append(containers[j + 1][0])
        j += 1
    print("stack", i + 1, stack[i])
    i -= 1