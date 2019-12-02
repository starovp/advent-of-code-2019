"""
--- Day 2: 1202 Program Alarm ---

-- Part One --

An Intcode program is a list of integers separated by commas (like 1,0,0,3,99).
To run one, start by looking at the first integer (called position 0).
Here, you will find an opcode - either 1, 2, or 99. The opcode indicates what to do;
for example, 99 means that the program is finished and should immediately halt.
Encountering an unknown opcode means something went wrong.

Opcode 1 adds together numbers read from two positions and stores the result
in a third position. The three integers immediately after the opcode tell you
these three positions - the first two indicate the positions from which you should
read the input values, and the third indicates the position at which the output
should be stored.

For example, if your Intcode computer encounters 1,10,20,30, it should read the
values at positions 10 and 20, add those values, and then overwrite the value at
position 30 with their sum.

Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead
of adding them. Again, the three integers after the opcode indicate where the inputs
and outputs are, not their values.

(Opcode 99 halts the program.)

Once you're done processing an opcode, move to the next one by stepping forward 4 positions.

Once you have a working computer, the first step is to restore the gravity assist program
(your puzzle input) to the "1202 program alarm" state it had just before the last computer
caught fire. To do this, before running the program, replace position 1 with the value 12 and
replace position 2 with the value 2. What value is left at position 0 after the program halts?

-- Part Two --
"With terminology out of the way, we're ready to proceed. To complete the gravity assist,
you need to determine what pair of inputs produces the output 19690720."

The inputs should still be provided to the program by replacing the values at addresses 1 and 2,
just like before. In this program, the value placed in address 1 is called the noun, and the
value placed in address 2 is called the verb. Each of the two input values will be between 0 and 99,
inclusive.

Once the program has halted, its output is available at address 0, also just like before.
Each time you try a pair of inputs, make sure you first reset the computer's memory to the values
in the program (your puzzle input) - in other words, don't reuse memory from a previous attempt.

Find the input noun and verb that cause the program to produce the output 19690720.
What is 100 * noun + verb? (For example, if noun=12 and verb=2, the answer would be 1202.)

"""

def part_one():
  ins = open("intcode.txt", "r")
  ics = (ins.readline()).split(",")
  i = 0
  while i < (len(ics)):
    if ics[i] == "1":
        ics[int('%s'%(ics[i+3]))] = int(ics[int('%s'%(ics[i+1]))]) + int(ics[int('%s'%(ics[i+2]))])
        i += 4
    elif ics[i] == "2":
        ics[int('%s'%(ics[i+3]))] = int(ics[int('%s'%(ics[i+1]))]) * int(ics[int('%s'%(ics[i+2]))])
        i += 4
    elif ics[i] == "99":
        return ics[0]

def part_two():
  for k in range(0,100):
      for j in range(0, 100):
          ins = open("intcode.txt", "r")
          ics = (ins.readline()).split(",")
          ics[1] = '%s'%(k)
          ics[2] = '%s'%(j)
          i = 0
          while i < (len(ics)):
              if ics[i] == "1":
                  ics[int('%s'%(ics[i+3]))] = int(ics[int('%s'%(ics[i+1]))]) + int(ics[int('%s'%(ics[i+2]))])
                  i += 4
              elif ics[i] == "2":
                  ics[int('%s'%(ics[i+3]))] = int(ics[int('%s'%(ics[i+1]))]) * int(ics[int('%s'%(ics[i+2]))])
                  i += 4
              elif ics[i] == "99":
                  break
          if ics[0] == 19690720:
              return(100*k + j)
              
if __name__ == '__main__':
  print(part_one())
  print(part_two())
