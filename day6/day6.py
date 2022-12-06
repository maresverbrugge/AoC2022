# star 1

# Set items are unordered, unchangeable, and DO NOT ALLOW DUPLICATE VALUES!
def get_start(string, marker_len):
    length = len(string)
    i = 0
    while (i < length):
        # print(string[i : i + marker_len])
        # print("i = ", i, "diff_chars = ", diff_chars)
        diff_chars = set(string[i : i + marker_len])
        len_diff_chars = len(diff_chars)
        if (len_diff_chars == marker_len):
            break
        i += 1
    character = marker_len + i
    return (character)

# infile = open('input_practice.txt')
infile = open('input.txt')
string = infile.read()
marker_star1 = 4
marker_star2 = 14

print("star 1:", get_start(string, marker_star1))
print("star 2:", get_start(string, marker_star2))
