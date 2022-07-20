"""
-As you probably know, Sudoku is a number-placing puzzle played on a 9x9 board. The player has to
fill the board in a very specific way:
-each row of the board must contain all digits from 0 to 9 (the order doesn't matter)
-each column of the board must contain all digits from 0 to 9 (again, the order doesn't matter)
-each of the nine 3x3 "tiles" (we will name them "sub-squares") of the table must contain all digits from 0 to 9.

--> Your task is to write a program which:
-reads 9 rows of the Sudoku, each containing 9 digits (check carefully if the data entered are valid)
-outputs Yes if the Sudoku is valid, and No otherwise.

Test data:
-- Sample input:
295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672
- Sample output: Yes
-- Sample input:
195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671

- Sample output: No
"""
from pprint import pprint
"""sudoko = '''195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671'''.split()


converted_sudoko = [[letter for letter in element] for element in sudoko]
for lst in converted_sudoko:
    for digit in lst:
        if lst.count(digit) > 1:
            print("Nooooooooo")
            break

for column in range(9):
    for row in range(8):
        if converted_sudoko[column][row] == converted_sudoko[column][row+1]:
            print("NNNNNNNNNNooooo")
            break

sqr_1 = []
"""
# A function that checks whether a list passed as an argument contains
# nine digits from '1' to '9'.
def checkset(digs):
    return sorted(list(digs)) == [chr(x + ord('0')) for x in range(1, 10)]


# A list of rows representing the sudoku.
rows = [ ]
for r in range(9):

ok = True

# Check if all rows are good.
for r in range(9):


# Check if all columns are good.
if ok:
    for c in range(9):


# Check if all sub-squares (3x3) are good.
if ok:
    for r in range(0, 9, 3):


# Print the final verdict.
if ok:
    print("Yes")
else:
    print("No")


