# Written by Kristian Aspevik
# 01/12/2018

frequency = 0
with open("Puzzle1Input.txt", "r") as input:
    for line in input:
        if "+" in line:
            frequency += int(line.replace("+", ""))
        elif "-" in line:
            frequency -= int(line.replace("-", ""))

print(frequency)
