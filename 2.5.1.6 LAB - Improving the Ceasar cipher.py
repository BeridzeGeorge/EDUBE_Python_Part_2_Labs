# Improving the Caesar cipher
"""
our task is to write a program which:
--> asks the user for one line of text to encrypt;
--> asks the user for a shift value (an integer number from the range 1..25 - note:
you should force the user to enter a valid shift value
(don't give up and don't let bad data fool you!)
--> prints out the encoded text.

Test data:
-> Sample input:
abcxyzABCxyz 123
2
-> Sample output:
cdezabCDEzab 123
"""

cipher = input('Enter your cryptogram: ')
while True:
    try:
        shift = int(input('choose shift from 1 to 25: '))
        if 1 < shift < 26:
            break
    except ValueError:
        print("Enter only numbers!")
text = ''
for char in cipher:
    if not char.isalpha():  # check if character is non-alphabetical to remain untouched
        text += char
        continue
    code = ord(char) + shift  # letter shift
    if 65 <= ord(char) <= 90:  # check letter if it is capital
        if code > 90:  # if shifted letter is out of upper-case letters range, substract 26 to return in range (cycle)
            code -= 26
    elif 97 <= ord(char) <= 122:  # check letter if it is lower-case
        if code > 122:  # if shifted letter is out of lower-case letters range, substract 26 to return in range (cycle)
            code -= 26
    text += chr(code)
print(text)

