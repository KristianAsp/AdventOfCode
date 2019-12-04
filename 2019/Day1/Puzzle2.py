#!/usr/bin/python3
import math

def sumFuelOfModules():
    totalFuel = 0
    with open("input1.txt", "r") as input:
        for mass in input:
            moduleFuel = getFuelForModule(mass)
            tempFuel = moduleFuel
            totalFuel = totalFuel + moduleFuel

            while getFuelForModule(tempFuel) > 0:
                newFuel = getFuelForModule(tempFuel)
                totalFuel = totalFuel + newFuel
                tempFuel = newFuel

    return totalFuel


def getFuelForModule(mass):
    fuel = math.floor(int(mass) / 3) - 2
    return fuel if fuel > 0 else 0


print("Sum: {}".format(sumFuelOfModules()))