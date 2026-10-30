"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a dictionary describing an investment fund, with 5 fields
# 2. Process: the program reads one field, changes one, removes one,
# and handles a field that does not exist
# 3. Out: the fund's information, field by field
# 4. My object, my five fields, and why those:
# I described an investment fund, like one a client could buy at a bank.
# the name: to know which fund we are talking about
# the currency: to know in which money the fund is valued
# the annual_fee: to know how much it costs the client each year
# the risk_level: to check if the fund matches what the client accepts
# the minimum_investment: to know if the client has enough money to buy it
 

# Your code below

name= input("Enter the fund's name: ")
currency= input("Enter the fund's currency: ")
annual_fee= float(input("Enter the fund's annual fee: "))
risk_level= input("Enter the fund's risk level: ")
minimum_investment= float(input("Enter the fund's minimum investment: "))

print("The fund's name is: ", name)
print("The fund's currency is: ", currency)
print("The fund's annual fee is: ", annual_fee)
print("The fund's risk level is: ", risk_level)
print("The fund's minimum investment is: ", minimum_investment)

# Create a dictionary for the fund
fund = {
    "name": name,
    "currency": currency,
    "annual_fee": annual_fee,
    "risk_level": risk_level,
    "minimum_investment": minimum_investment
}

#Read one field
print("The fund's name is: ", fund["name"])

#Change one field
fund["annual_fee"] = float(input("Enter the new annual fee: "))

#Remove one field
removed_field = fund.pop("risk_level")
print("The field risk_level was removed, its value was: ", removed_field)
print("The remaining fields are: ", fund)

# Display all fields and their values
for field, value in fund.items():
    print(f"The fund's {field} is: {value}")

# Ask for a field that does not exist
asked_field = input("Which field do you want to know about? ")
if asked_field in fund:
    print(f"The {asked_field} is: {fund[asked_field]}")
else:
    print(f"The {asked_field} does not exist in the fund's information.")


#CHECK IT YOURSELF
# If you ask for a field that does not exist, the program will tell you that it
# does not exist in the fund's information, instead of crashing or giving an error.






