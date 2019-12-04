"""
--- Day 3: Crossed Wires ---

The wires twist and turn, but the two wires occasionally cross paths.
To fix the circuit, you need to find the intersection point closest to
the central port. Because the wires are on a grid, use the Manhattan
distance for this measurement. While the wires do technically cross right
at the central port where they both start, this point does not count, nor
does a wire count as crossing with itself.

Here are a few more examples:

    R75,D30,R83,U83,L12,D49,R71,U7,L72
    U62,R66,U55,R34,D71,R55,D58,R83 = distance 159
    R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
    U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = distance 135
    
What is the Manhattan distance from the central port to the closest intersection?

--- Part Two ---

It turns out that this circuit is very timing-sensitive; you actually need to
minimize the signal delay.

To do this, calculate the number of steps each wire takes to reach each intersection;
choose the intersection where the sum of both wires' steps is lowest.
If a wire visits a position on the grid multiple times, use the steps value from the
first time it visits that position when calculating the total value of a specific intersection.

The number of steps a wire takes is the total number of grid squares the wire has
entered to get to that location, including the intersection being considered.

Here are the best steps for the extra examples from above:

    R75,D30,R83,U83,L12,D49,R71,U7,L72
    U62,R66,U55,R34,D71,R55,D58,R83 = 610 steps
    R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
    U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = 410 steps

What is the fewest combined steps the wires must take to reach an intersection?
"""

def get_init():
  a = open("directions.txt", "r").read().split('\n')
  coords = []
  for x in a:
      coords.append(x.split(','))
  return coords[:2]

def part_one():
    wires = get_init()
    dirmap = {
        'R':  [1,0],
        'L':  [-1,0],
        'U':  [0,1],
        'D':  [0,-1]
        }
    grid = {}
    cur = [0,0]
    
    for move in wires[0]:
        ldir = dirmap[move[0]]
        for step in range(int(move[1:])):
            cur[0] += ldir[0]
            cur[1] += ldir[1]
            if tuple(cur) not in grid:
                grid[tuple(cur)] = "X"
                    
    cur = [0,0]
    intersect = []
    
    for move in wires[1]:
        ldir = dirmap[move[0]]
        for step in range(int(move[1:])):
            cur[0] += ldir[0]
            cur[1] += ldir[1]
            if tuple(cur) in grid:
                intersect.append(abs(cur[0])+abs(cur[1]))
                
    return(min(intersect))

def part_two():
    wires = get_init()
    dirmap = {
        'R':  [1,0],
        'L':  [-1,0],
        'U':  [0,1],
        'D':  [0,-1]
        }
    grid = {}
    steps = 0
    cur = [0,0]
    
    for move in wires[0]:
        ldir = dirmap[move[0]]
        for step in range(int(move[1:])):
            steps += 1
            cur[0] += ldir[0]
            cur[1] += ldir[1]
            if tuple(cur) not in grid:
                grid[tuple(cur)] = steps
                    
    steps = 0
    cur = [0,0]
    intersect = []
    
    for move in wires[1]:
        ldir = dirmap[move[0]]
        for step in range(int(move[1:])):
            steps += 1
            cur[0] += ldir[0]
            cur[1] += ldir[1]
            if tuple(cur) in grid:
                intersect.append(steps+grid[tuple(cur)])
                
    return(min(intersect))
    

if __name__ == '__main__':
  
    print("Part One:", part_one())
    print("Part Two:", part_two())
