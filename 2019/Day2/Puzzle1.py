#!/usr/bin/python3

def doCalculations(myList):
    x = 0
    while myList[x] != 99:
        if myList[x] == 1:
            myList[myList[x+3]] = myList[myList[x+1]] + myList[myList[x+2]]
        elif input[x] == 2:
            myList[myList[x+3]] = myList[myList[x+1]] * myList[myList[x+2]]
        else:
            break
        x = x + 4
    return input


with open("input.txt", "r") as file:
    # Get values from input file and map them to integers
    input = list(map(int, file.read().split(',')))

print("Result: {}".format(doCalculations(input)[0]))