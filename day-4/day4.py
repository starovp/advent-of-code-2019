"""
--- Day 4: Secure Container ---

You arrive at the Venus fuel depot only to discover it's protected by a password.
The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

    It is a six-digit number.
    The value is within the range given in your puzzle input.
    Two adjacent digits are the same (like 22 in 122345).
    Going from left to right, the digits never decrease; they only ever increase
    or stay the same (like 111123 or 135679).

Other than the range rule, the following are true:

    111111 meets these criteria (double 11, never decreases).
    223450 does not meet these criteria (decreasing pair of digits 50).
    123789 does not meet these criteria (no double).

How many different passwords within the range given in your puzzle input
meet these criteria?

--- Part Two ---

An Elf just remembered one more important detail:
the two adjacent matching digits are not part of a larger group of matching digits.

Given this additional criterion, but still ignoring the range rule,
the following are now true:

    112233 meets these criteria because the digits never decrease and all repeated digits
    are exactly two digits long.
    
    123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
    111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).

How many different passwords within the range given in your puzzle input meet all of the criteria?

"""

def any_two(s):
    for i in range(5):
        if int(s[i]) == int(s[i+1]):
            return True
    return False

def exactly_two(s):
    for i in range(6):
        ct = 0
        for j in range(6):
            if s[i] == s[j]:
                ct += 1
        if ct == 2:
            return True
    return False
            
def does_decrease(s):
    if list(s) == sorted(s):
        return True
    return False

def check_valid(s):
    if any_two(s) and does_decrease(s):
        return True

def part_one(n1, n2):
    uct = 0
    for i in range(n1,n2+1):
        i = str(i)
        if check_valid(i):
            uct += 1
    return uct

def part_two(n1, n2):
    uct = 0
    for i in range(n1,n2+1):
        i = str(i)
        if check_valid(i) and exactly_two(i):
            uct += 1
    return uct
    
if __name__ == '__main__':
    
    num1 = 165432
    num2 = 707912

    print("Range:",num1,"-",num2)
    print("Part One:",part_one(num1, num2))
    print("Part Two:",part_two(num1, num2))
