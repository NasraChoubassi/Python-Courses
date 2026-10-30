"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A sentence typed by the user
# 2. Process: The program will take the sentence and apply four different transformations to it.
# 3. Out: Four new versions of the same sentence tranformed in different ways
# 4. My four transformations, and when each is useful: 
#upper(): to write a client's name in capitals on an official bank document
#lower(): to compare two emails without caring about capital letters
#strip(): to remove spaces a client typed by mistake in a form
#title(): to display a name or an address nicely, like "John Smith" or "123 Main Street"


# Your code below
sentence = input("Enter a sentence: ")
print("Original sentence:", sentence)
print("Uppercase:", sentence.upper(), ". This transformation shows the sentence in capital letters.")
print("Lowercase:", sentence.lower(), ". This transformation shows the sentence in lowercase.")
print("Stripped:", sentence.strip(), ". This transformation removes spaces from the beginning and end of the sentence.")
print("Title case:", sentence.title(), ". This transformation puts a capital letter at the start of each word.")

#CHECK IT YOURSELF
# I ran the program with the sentence "  Hello World ". The results were:
# Uppercase: "  HELLO WORLD  ". This is what I expected.
# Lowercase: "  hello world  ". This is what I expected.
# Stripped: "Hello World". This is what I expected.
# Title case: "  Hello World  ". This is what I expected.