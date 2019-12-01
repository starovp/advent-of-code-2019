'''

--- Day 1: The Tyranny of the Rocket Equation ---

What is the sum of the fuel requirements for all of
the modules on your spacecraft?

'''

import math

def get_fuel(mass):
    return math.floor(mass/3)-2

if __name__ == '__main__':
    sum = 0
    m = open("modules.txt", "r")
    for x in m:
        add_fuel = get_fuel(int(x))
        sum += add_fuel
        while get_fuel(add_fuel) > 0:
            add_fuel = get_fuel(add_fuel)
            sum += add_fuel
    print(sum)


