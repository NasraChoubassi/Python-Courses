"""Exercise 1.0 — Hello World

WHAT THE PROGRAM MUST DO
    Display a message of your choice, five times, with each line numbered.

ANSWER THESE FIRST, in comments at the top of your file, before any code
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What message did you choose, and why that one?

WHAT THE AI CANNOT KNOW
    The message is yours. Choose something you would actually want a program to say,
    not "Hello, World!". Your comment has to justify it.

CHECK IT YOURSELF
    Count the lines your program produced. Five, not four and not six.
    Then change the number to 3 and run it again. If you had to rewrite more than one
    character, your program is not built the way it should be.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a message (my name) and the number of times to print it (5)
# 2. Process: the program prints the same message 5 times, with each line numbered
# 3. Out: five lines of the same message, each with a number in front of it
# 4. My message, and why: I chose to print my name 5 times, it's the simplest message I could think of
#  and it is a good way to test that the program works.


# Your code below
message = "Nasra"
repeat = 5

for i in range(1, repeat + 1):
    print(str(i) + ". " + message)

#CHECK IT YOURSELF
# I ran the program and counted the lines. There were five lines, as expected.
# Then I changed the number to 3 by modifying the `repeat` variable and ran it again. 
# There were three lines, as expected.