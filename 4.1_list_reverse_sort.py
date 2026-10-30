"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:the list of the 8 monthly fund returns from exercise 4.0
# 2. Process: the program shows the returns in four different orders,
#    without changing the original list
# 3. Out: the program shows the returns in four different orders, and at the end it shows the original list
# 4. My four orders, and which ones modify the original:
# I chose to show the returns in ascending order, descending order, backwards, smallest to biggest movement (lowest to highest absolute value or variation) 
# None of them modifies the original, because sorted() and [::-1] make a new list. 
# If I used returns.sort() or returns.reverse(), the original list would be changed.


# Your code below
returns = [2.1, -1.5, 3.4, 0.8, -2.3, 1.9, 4.0, -0.6]

print("All monthly returns (%) are :", returns)

print("Worst to best returns:", sorted(returns))
print("Best to worst returns:", sorted(returns, reverse=True))
print("Returns in reverse order:", returns[::-1])
print("Returns sorted by absolute value:", sorted(returns, key=abs))

print("The original list is still intact:", returns)

#CHECK IT YOURSELF
# Original in 4.0: [2.1, -1.5, 3.4, 0.8, -2.3, 1.9, 4.0, -0.6]
# Last line now:   [2.1, -1.5, 3.4, 0.8, -2.3, 1.9, 4.0, -0.6]
# Same items in the same order 