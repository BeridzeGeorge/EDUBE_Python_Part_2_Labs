"""
Your task is to write a program which:
asks the user for two separate texts;
checks whether, the entered texts are anagrams and prints the result.
Note:
-assume that two empty strings are not anagrams;
-treat upper- and lower-case letters as equal;
-spaces are not taken into account during the check - treat them as non-existent

--> Test data
- Sample input:
Listen
Silent
- Sample output:Anagrams
- Sample input:
modern
norman
- Sample output: Not anagrams
"""

word_1 = input("Enter first word: ")
word_2 = input("Enter second word: ")
lst_1 = []
lst_2 = []
# Convert all characters to upper case and add corresponding ASCII number into the list
for char in word_1.upper():
    if char != chr(32): # exclude whitespace
        lst_1.append(ord(char))
for char in word_2.upper():
    if char != chr(32): # exclude whitespac
        lst_2.append(ord(char))

anagrams = True
sorted_lst_1 = sorted(lst_1)
sorted_lst_2 = sorted(lst_2)
if not word_1 and not word_2:
    # checking lists for emptiness
    print("Emtpy strings ar not anagrams")
elif len(lst_1) != len(lst_2):
    # compare lists length
    print("Not anagrams")
    anagrams = False
else:
    for i in range(len(lst_1)):
        if sorted_lst_1[i] != sorted_lst_2[i]:
            # compare lists elements identity
            print("Not anagrams")
            anagrams = False
            break
if anagrams:
    print("Anagrams")
