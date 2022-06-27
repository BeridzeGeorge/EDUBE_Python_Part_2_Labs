#  2.4.1.6 LAB : A LED Display
""" write a program which is able to simulate the work of a seven-display device """

n0 = ["###","# #","# #","# #","###"]
n1 = ["  #","  #","  #","  #","  #"]
n2 = ["###","  #","###","#  ","###"]
n3 = ["###","  #","###","  #","###"]
n4 = ["# #","# #","###","  #","  #"]
n5 = ["###","#  ","###","  #","###"]
n6 = ["###","#  ","###","# #","###"]
n7 = ["###","  #","  #","  #","  #"]
n8 = ["###","# #","###","# #","###"]
n9 = ["###","# #","###","  #","###"]
numbers_list = [n0,n1,n2,n3,n4,n5,n6,n7,n8,n9]
user_input = input("Enter number: ")
new_list = []
for j in range(5):
    print("")
    for i in user_input:
        print(numbers_list[int(i)][j],end=' ')
