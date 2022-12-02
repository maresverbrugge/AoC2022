# star 1
SCORES = {
	'A X': 4,
	'A Y': 8,
	'A Z': 3,
	'B X': 1,
	'B Y': 5,
	'B Z': 9,
	'C X': 7,
	'C Y': 2,
	'C Z': 6,
}
infile = open('input.txt')
content = infile.read()
content_split = content.splitlines()
total = 0
for line in content_split:
    total += (SCORES[line])
print("star 1:", total)

# star 2
OPTIONS = {
	'A X': 'Z',
	'A Y': 'X',
	'A Z': 'Y',
	'B X': 'X',
	'B Y': 'Y',
	'B Z': 'Z',
	'C X': 'Y',
	'C Y': 'Z',
	'C Z': 'X',
}
infile = open('input.txt')
content = infile.read()
content_split = content.splitlines()
total = 0
for line in content_split:
    option = OPTIONS[line]
    points = line[0] + ' ' + option
    total += (SCORES[points])
print("star 2:", total)
