"""Exercise 2.0 — Asking the user

WHAT THE PROGRAM MUST DO
    Ask the user for two pieces of information, then display a sentence that uses both.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two pieces of information did you choose, and for what purpose?
       Imagine a real form in your future job. Not "name and age" unless you can
       say what you would do with them.

WHAT THE AI CANNOT KNOW
    Your two fields, and the sentence you want at the end. Decide both before you ask.

    One of your two values will almost certainly need to be a number. Find out what
    happens when you try to add 1 to something the user typed, and deal with it.

CHECK IT YOURSELF
    Run your program and answer with an empty line. Then with a space. Then with text
    where you expected a number. Write in a comment what happened each time.
    You are not asked to fix it yet, only to see it.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: for this example, the client's name and the amount they need to borrow
# 2. Process: the program will take the name and the amount and print a sentence with 
# these two pieces of information
# 3. Out: a sentence with the client's name and the amount they need to borrow
# 4. My two fields, and what I would do with them: In a bank loan application, I would 
# ask for the client's name and the amount they need to borrow. I show a confirmation 
# message so they can check their request before it is sent to an advisor.

# Your code below
name = input("Enter your name: ")
amount = input("Enter the amount you need to borrow: ")
print("Client's name is ", name)
print("Amount to borrow is ", amount)


print("Thank you " + name + ", your loan of $" + amount + " has been submitted.")

#CHECK IT YOURSELF
# Empty line: there is no error, the sentence is printed with an empty space where the 
# name and number should be.
# A space: no error also, it looks empty but there is an extra space in the sentence.
# Text instead of a number: no error, it prints "j" for example as the loan amount, because input()
#always gives text