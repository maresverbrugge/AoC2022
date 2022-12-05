# star 1 PSEUDO:
# open file
# fill stacks with containers SORRY HARD CODED
# read moves from file
# push n containers from stack_src to stack_dest:
# - (push to stack_dest, with insert(a))
# - (delete container from stack_dest, with del())
# when all moves are executed:
# read top container of each stack add to str
# print str

import re

# star 1
with open('input.txt') as infile:
    containers, moves = infile.read().split('\n\n')
# print("moves =")
# print(moves + '\n')

print("containers =")
print(containers + '\n')
containers = containers.replace('[','').replace(']','').replace(' ', '').split('\n')
amount_containers = containers[-1]
print("amount_containers =", amount_containers[-1] + '\n')

# PRACTICE STACK:
# stack_1 = ['N', 'Z']
# stack_2 = ['D', 'C', 'M']
# stack_3 = ['P']
# stacks = [stack_1, stack_2, stack_3]

stack_1 = ['W', 'T', 'H', 'P', 'J', 'C', 'F']
stack_2 = ['H', 'B', 'J', 'Z', 'F', 'V', 'R', 'G']
stack_3 = ['R', 'T', 'P', 'H']
stack_4 = ['T', 'H', 'P', 'N', 'S', 'Z']
stack_5 = ['D', 'C', 'J', 'H', 'Z', 'F', 'V', 'N']
stack_6 = ['Z', 'D', 'W', 'F', 'G', 'M', 'P']
stack_7 = ['P', 'D', 'J', 'S', 'W', 'Z', 'V', 'M']
stack_8 = ['S', 'D', 'N']
stack_9 = ['M', 'F', 'S', 'Z', 'D']

stacks = [stack_1, stack_2, stack_3, stack_4, stack_5, stack_6, stack_7, stack_8, stack_9]
# print(stacks)

moves = moves.replace('move ','').replace('from','').replace('to', '').split('\n')
# print("moves =")
# print(moves)
for line in moves:
    amount, src, dst = line.split()
    # print('\n' + "amount =", amount)
    # print("src =", src)
    # print("dst =", dst)
    for move in range(int(amount)):
        stacks[int(dst)-1].insert(0,stacks[int(src)-1][0])
        del stacks[int(src)-1][0]
        # print(stacks)

result = ''
i = 0
while (i < int(amount_containers[-1])):
    # print(i, stacks[i][0])
    result += stacks[i][0]
    # print("result =", result)
    i += 1
print("star 1 =", result)


# star 2
with open('input.txt') as infile:
    containers, moves = infile.read().split('\n\n')

print("containers =")
print(containers + '\n')
containers = containers.replace('[','').replace(']','').replace(' ', '').split('\n')
amount_containers = containers[-1]
print("amount_containers =", amount_containers[-1] + '\n')

# PRACTICE STACK:
# stack_1 = ['N', 'Z']
# stack_2 = ['D', 'C', 'M']
# stack_3 = ['P']
# stacks = [stack_1, stack_2, stack_3]

stack_1 = ['W', 'T', 'H', 'P', 'J', 'C', 'F']
stack_2 = ['H', 'B', 'J', 'Z', 'F', 'V', 'R', 'G']
stack_3 = ['R', 'T', 'P', 'H']
stack_4 = ['T', 'H', 'P', 'N', 'S', 'Z']
stack_5 = ['D', 'C', 'J', 'H', 'Z', 'F', 'V', 'N']
stack_6 = ['Z', 'D', 'W', 'F', 'G', 'M', 'P']
stack_7 = ['P', 'D', 'J', 'S', 'W', 'Z', 'V', 'M']
stack_8 = ['S', 'D', 'N']
stack_9 = ['M', 'F', 'S', 'Z', 'D']
stacks = [stack_1, stack_2, stack_3, stack_4, stack_5, stack_6, stack_7, stack_8, stack_9]

# print(stacks)

moves = moves.replace('move ','').replace('from','').replace('to', '').split('\n')
# print("moves =")
# print(moves)
# print(stacks)
for line in moves:
    amount, src, dst = line.split()
    # print('\n' + "amount =", amount)
    # print("src =", src)
    # print("dst =", dst)
    amount = int(amount)
    src = int(src)
    dst = int(dst)
    stacks[dst-1][0:0] = stacks[src-1][0:amount]
    del stacks[src-1][0:amount]
    # print(stacks)

result = ''
i = 0
while (i < int(amount_containers[-1])):
    result += stacks[i][0]
    i += 1
print("star 2 =", result)