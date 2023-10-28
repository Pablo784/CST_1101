# April 20th, 2021
# I just found out how the program is suppose to look like
# The professor provided the source code in the slides so i'll just change some things to my liking
# Pablo Vasquez
# Credit goes to Professor Slattery because he provided the code
# You can never learn something if you don't practice it. 

# Part 1 of program
need_basic_items = ['bread', 'cheese', 'milk', 'sausage',]
print("Let's start a shopping cart.")
print("Here are some suggested basic items:")
print("-----")
for item in need_basic_items:
    print("- " +item)

# Part 2 of program
response = input("Would you like the items above in your shopping cart? (yes/no)")
if response != "no":
    shopping_list = need_basic_items[:]
    print("Your shopping cart now includes: ")
    print("-----")
    for item in need_basic_items:
        print("- " +item)
        print("-----")

# Part 3 of program
while need_basic_items == True:
    need_basic_items = input("What item do you want to add? ")
shopping_list.append(need_basic_items)
print("Your shopping cart has the following items in it: ")
print("-----")
for item in need_basic_items:
    print("- " +item)
    print("-----")
    response = input("Add another item? (yes/no) ")
    if response == "n":
        add_more = False
