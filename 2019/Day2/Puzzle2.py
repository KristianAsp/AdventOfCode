#!/usr/bin/python3

def getInputValues():
    with open("input.txt", "r") as file:
        # Get values from input file and map them to integers
        original_input = list(map(int, file.read().split(',')))

    wanted_output = 19690720
    for n in range(100):
        for k in range(100):

            input = original_input.copy()
            # Input in the context of this questions is defined as
            # the two values in position 1 & 2 of the array
            input[1] = n
            input[2] = k
            x = 0
            while input[x] != 99:
                if input[x] == 1:
                    input[input[x+3]] = input[input[x+1]] + input[input[x+2]]
                elif input[x] == 2:
                    input[input[x+3]] = input[input[x+1]] * input[input[x+2]]
                else:
                    break
                x = x + 4

            if input[0] == wanted_output:
                return(n, k)

n, k = getInputValues()
print("n: {} \t k: {}".format(n,k))