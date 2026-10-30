"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a list of 8 monthly returns of an investment fund (in %)
# 2. Process: the program displays the list, picks one return, sorts the
# returns and computes the average monthly return
# 3. Out: the whole list, one return, the sorted list and the average return
# 4. What my list is about, and what I computed from it: My list is the return of a fund
# each month (8 months). I computed the average monthly return, because it shows if the fund
#makes money on average, even if some months are negative. An investor can use it to 
# compare this fund with another one.

# Your code below
returns = [2.1, -1.5, 3.4, 0.8, -2.3, 1.9, 4.0, -0.6]

print("All monthly returns (%) are :", returns)
print("Return of the third month is:", returns[2])

sorted_returns = sorted(returns)
print("Sorted returns:", sorted_returns)

average_return = sum(returns) / len(returns)
print("Average monthly return (%):", round(average_return, 2))

#CHECK IT YOURSELF
# By hand, with the first three returns: (2.1 + (-1.5) + 3.4) / 3 = 1.33
# The program agrees, it gives for these three: 1.33
