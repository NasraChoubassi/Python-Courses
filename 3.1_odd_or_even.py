"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A number N
# 2. Process: Check if each number from 1 to N is odd or even
# 3. Out: For each number, print whether it is odd or even
# 4. What happens on 0, on a negative number, on a very large number: 
# If it's 0 or negative, it shows a message because it's excluded from 1 to N
#- 5000: the program accepts it and prints the 5000 lines. It is possible, but it takes 
# time and it is too long to read.
#between 1 and N: the program works normally


# Your code below

N = int(input("Please enter a number N: "))
while N <= 0:
    print("Please enter a number greater than 0.")
    N = int(input("Please enter a number N: "))

for i in range(1, N + 1):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")


#CHECK IT YOURSELF
# When N=6, the output should be:
# 1 is odd
# 2 is even
# 3 is odd
# 4 is even
# 5 is odd
# 6 is even

#When N=0 or negative, the program should prompt the user to enter a number greater than 0.
#When N=5000, the program will print 5000 lines indicating whether each number from 1 to 5000 is odd or even.