"""
Your task is to write a program which answers the following question: are the characters comprising the first
string hidden inside the second string?
For example:
if the second string is given as "vcxzxduybfdsobywuefgas", the answer is yes;
if the second string is "vcxzxdcybfdstbywuefsas", the answer is no
(as there are neither the letters "d", "o", or "g", in this order)
Hints:
-you should use the two-argument variants of the pos() functions inside your code;
-don't worry about case sensitivity.

--> Test data
 Sample input:
- donor
- Nabucodonosor
- Sample output:Yes
Sample input:
- donut
- Nabucodonosor
- Sample output: No
"""

first_string = input("Enter first text: ")
second_string = input("Enter second text: ")

for i in first_string:
    if i in second_string:
        # chek if current element of the first_string is in the second_string
        continue
    else:
        first_string = ""
        print("no")
        break
if first_string:
    print("Yes")


