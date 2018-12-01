# Written by Kristian Aspevik
# 01/12/2018

frequency = 0

with open("Puzzle2Input.txt", "r") as file_input:
    input_lines = file_input.readlines()
    seen_frequencies = {0}  # Initial frequency of 0
    found = False

    while not found:
        for line in input_lines:
            if "+" in line:
                frequency += int(line.replace("+", ""))
            elif "-" in line:
                frequency -= int(line.replace("-", ""))

            if frequency in seen_frequencies:
                found = True
                break
            seen_frequencies.add(frequency)
    print(frequency)
