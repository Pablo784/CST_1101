print("Example of a void function for its side effects")
def print_void(argument):
    """This void function prints the value passed in as an argument"""
    print ("Your value is:", argument)

print_this = input("What content should we use as an argument to print_void()? > ")
print_void(print_this)
print()
wait = input("Hit Enter to continue > ")
print()


print("Example of local and global variable")
def change_value(argument):
    """This function changes the local value passed in to 17"""
    print ("Inside (local) argument is:", argument)
    argument = 17
    print ("Inside (local) argument is changed to:", argument)

number = 42
print ("Outside (global) number is:", number)
change_value(number)
print ("Outside (global) number is still:", number)
print()
wait = input("Hit Enter to continue > ")
print()


print("Example of using the global statement to access a global variable")
def change_number():
    """This function changes the value passed in to 19 (global)"""
    global number
    number = 19

number = 55
print ("Outside (global) number is:", number)
change_number()
print ("Outside (global) number is now:", number)
print()
wait = input("Hit Enter to continue > ")
print()



print("Example of returning a value(s)")
def square(root):
    """This function calculates the square of the argument value"""
    result = root * root
    return result



def square(root):
    """This function calculates the square of the argument value"""
    return root * root

for i in range(1,11):
    print(square(i))
print()
wait = input("Hit Enter to continue > ")
print()


print("Example of setting a default value for an argument")
def square(root = 1):
    """This function calculates the square of a the argument value"""
    return root * root

print(square())
print()
wait = input("Hit Enter to continue > ")
print()


print("Examples of using/not-using a default value for an argument")
def prompt_user(prompt, num_tries = 2):
    """This function prompts the user for 'yes' or 'no' a number of times"""
    answer = input(prompt)

    while (answer != "yes" and answer != "no" and num_tries > 1):
       num_tries = num_tries - 1
       print ("Try again")
       answer = input(prompt)

prompt_user("Enter yes or no: ")
prompt_user("Enter yes or no: ", 4)
print()
wait = input("Hit Enter to continue > ")
print()



print("Example of using keywords to assign values to arguments")
prompt_user(prompt="Hello ")
prompt_user(num_tries=1, prompt="Hi ")
print()
wait = input("Hit Enter to continue > ")
print()



