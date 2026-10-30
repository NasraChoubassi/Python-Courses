"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the answer of a client who must confirm a loan request (yes or no)
# 2. Process: the program asks again while the answer is not "yes" or "no",
# with a maximum of 3 attempts
# 3. Out: a summary with the number of attempts, the wrong answers and the decision
# 4. My stop condition, my attempt limit, my summary:
#stop condition: the client answers "yes" or "no"
# - "Yes"/ "yes"/ " yes " count as the same answer, because I remove the
#   spaces with strip() and put everything in small letters with lower()
# - limit: 3 attempts. After 3 wrong answers, the request is cancelled,
#   because a bank cannot wait for ever for a confirmation
# - summary: number of attempts, the wrong answers, and the final decision


# Your code below
# Settings and counters
max_attempts = 3
attempts = 0
wrong_answers = []
decision = "no answer"
 
# Ask until the client says yes or no, or until the limit is reached
while attempts < max_attempts:
    answer = input("Do you confirm your loan request? (yes/no): ")
    attempts = attempts + 1
    clean_answer = answer.strip().lower()
 
    if clean_answer == "yes":
        decision = "confirmed"
        break
    elif clean_answer == "no":
        decision = "cancelled by the client"
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        wrong_answers.append(answer)
 
# If the limit was reached without a valid answer
if decision == "no answer":
    decision = "cancelled, too many invalid answers"
 
# Summary of what happened during the loop
print("----- Summary -----")
print("Number of attempts:", attempts)
print("Wrong answers:", wrong_answers)
print("Decision:", decision)
 
# CHECK IT YOURSELF
# When the expected answer was not given, the proram the summary showed the number of 
# attempts, the wrong answers, and the decision. The program stopped after 3 attempts. 
# With capitals and extra spaces (for example "  YES  "), the program still accepted it
# as a valid answer.