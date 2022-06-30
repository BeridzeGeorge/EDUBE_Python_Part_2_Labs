"""
Your task is to write a program which:
asks the user her/his birthday (in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY - actually, the order of the digits doesn't matter)
outputs the Digit of Life for the date.

--> Test data
- Sample input:19991229
- Sample output:    6
- Sample input:20000101
- Sample output:    4
"""

while True:
    # demand user to enter data corectly
    user_bday = input("Enter your birthday in the formats: YYYYMMDD, or YYYYDDMM, or MMDDYYYY :  ")
    if len(user_bday) == 8 and int(user_bday):
        break
    else:
        print("Strictly follow the rule")

# Function with recursion to sum up digits until their length is 1.
def dol_recursion (bday):
    dol = 0
    for i in bday:
        dol += int(i)
    if len(str(dol)) == 1 :
        return dol
    if len(str(dol)) > 1:
        return dol_recursion(str(dol))

print(dol_recursion(user_bday))
