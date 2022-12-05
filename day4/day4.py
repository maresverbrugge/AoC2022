# star 1
infile = open('input.txt')
lines = infile.read().splitlines()
total = 0
for line in lines:
    new_lines = line.replace(",", "-").split("-")
    print(new_lines)
    start_a, end_a, start_b, end_b = [int(x) for x in new_lines]
    print(start_a)
    print(end_a)
    print(start_b)
    print(end_b)
    if (start_a >= start_b and end_a <= end_b) or (start_b >= start_a and end_b <= end_a):
        total += 1
    print("   ")
print("star 1:", total)

# star 2
infile = open('input.txt')
lines = infile.read().splitlines()
total = 0
for line in lines:
    new_lines = line.replace(",", "-").split("-")
    start_a, end_a, start_b, end_b = [int(x) for x in new_lines]
    if (end_a <= end_b and end_a >= start_b) or (end_b <= end_a and end_b >= start_a):
        total += 1
print("star 2:", total)