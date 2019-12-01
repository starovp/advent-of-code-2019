'''

--- Day 1: The Tyranny of the Rocket Equation ---

-- Part 1 --
The Elves quickly load you into a spacecraft and prepare to launch.

At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper. 
They haven't determined the amount of fuel required yet.

Fuel required to launch a given module is based on its mass. Specifically, 
to find the fuel required for a module, take its mass, divide by three, 
round down, and subtract 2. What is the sum of the fuel requirements for all 
of the modules on your spacecraft?

-- Part 2 --
During the second Go / No Go poll, the Elf in charge of the Rocket Equation 
Double-Checker stops the launch sequence. Apparently, you forgot to include 
additional fuel for the fuel you just added.

Fuel itself requires fuel just like a module - take its mass, divide by three, 
round down, and subtract 2. However, that fuel also requires fuel, and that 
fuel requires fuel, and so on. Any mass that would require negative fuel should 
instead be treated as if it requires zero fuel; the remaining mass, if any, is 
instead handled by wishing really hard, which has no mass and is outside the 
scope of this calculation.

So, for each module mass, calculate its fuel and add it to the total. Then, 
treat the fuel amount you just calculated as the input mass and repeat the 
process, continuing until a fuel requirement is zero or negative.

What is the sum of the fuel requirements for all of the modules on your 
spacecraft when also taking into account the mass of the added fuel? 

'''

def get_fuel(mass):
    return int(mass/3)-2

def fuel_sum():
    sum = [0,0]
    m = open("modules.txt", "r")
    for x in m:
        add_fuel = get_fuel(int(x))
        sum[0] += add_fuel
        while get_fuel(add_fuel) > 0:
            add_fuel = get_fuel(add_fuel)
            sum[1] += add_fuel
    return sum
    

if __name__ == '__main__':
    result = fuel_sum()
    print("Part 1:", fuel_sum()[0])
    print("Part 2:", fuel_sum()[0]+fuel_sum()[1])



