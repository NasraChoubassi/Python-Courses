"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the list of 8 monthly returns of a fund from exercise 4.0 (in %)
# 2. Process: for each month, the program checks if the return is positive or
# negative and compares it with the average return
# 3. Out: one line per month with the month number, the return, if it is a
# gain or a loss, and if it is above or below the average
# 4. What I compute for each item, and why it is worth showing:
# I decided to show if each month is a gain or a loss, and if it is above or
# below the average. The reader sees quickly the good and the bad months of the fund.


# Your code below
returns = [2.1, -1.5, 3.4, 0.8, -2.3, 1.9, 4.0, -0.6]
average = sum(returns) / len(returns)
for position, value in enumerate(returns, start=1):
    if value >= 0:
        result = "gain"
    else:
        result = "loss"

    if value > average:
        comparison = "above"
    else:
        comparison = "below"

    print(f"Month {position}: {value}% -> {result}, {comparison} the average")

    #CHECK IT YOURSELF
#Month 1: 2.1% -> gain, above the average
#Month 2: -1.5% -> loss, below the average
#Month 3: 3.4% -> gain, above the average
#Month 4: 0.8% -> gain, below the average
#Month 5: -2.3% -> loss, below the average
#Month 6: 1.9% -> gain, above the average
#Month 7: 4.0% -> gain, above the average
#Month 8: -0.6% -> loss, below the average

#-> There are 8 lines printed, which matches the number of items in the list.

