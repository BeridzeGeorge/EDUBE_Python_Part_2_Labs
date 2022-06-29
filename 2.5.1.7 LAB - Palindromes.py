"""
-->  our task is to write a program which:
-asks the user for some text;
-checks whether the entered text is a palindrome, and prints result.
--> Note:
-assume that an empty string isn't a palindrome;
-treat upper- and lower-case letters as equal;
-spaces are not taken into account during the check - treat them as non-existent;
--> Test data:
-Sample input:Ten animals I slam in a net
-Sample output:It's a palindrome
-Sample input:Eleven animals I slam in a net
-Sample output: It's not a palindrome
"""

user_text = input("Enter text & I'll check if it is palindrome or not: ")
while True:
    # Check that inputted data should contain some text.
    if user_text.isspace() or not user_text:
        user_text = input("You should enter some text: ")
    else:
        break
user_text_without_spaces = ""
for char in user_text:
    # Remove all whitespace from the text.
    if char != chr(32):
        user_text_without_spaces += char
lst = []
for i in user_text_without_spaces.upper():
    # Convert all characters to upper case and add corresponding ASCII number into the list
    lst.append(ord(i))

inversed_lst = lst[-1::-1] #Creating inverted list.
palindrome = True
for i in range(len(user_text_without_spaces) // 2):
    if lst[i] != inversed_lst[i]:
        # compare 2 lists' elements if they are the same.
        print("It's not a palindrome")
        pali = False
        break
if palindrome:
    print("It's a palindrome")
