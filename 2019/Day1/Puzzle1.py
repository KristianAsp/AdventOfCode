#!/usr/bin/python3
import math
def sumMassOfModules():
    sum = 0
    with open("input1.txt", "r") as input:
        for line in input:
            sum = sum + math.floor(int(line) / 3) - 2

    return sum
print("Sum: {}".format(sumMassOfModules()))