def get_name():
    print("What is your name?")
    playername = input()
    if playername == "":
        print("Okay. I will assign you a name.")
        playername = "The Nameless One"
    print("Your name is " + playername + ".")

    return playername


def start_adventure():
    print("You enter the room, and you see a red door to your left and a blue door to your right.")
    print("Do you pick the red door or blue door?")
    
    doorpicked = input()
    if doorpicked == "red":
        print("You picked the red door.")
    else:
        if doorpicked == "blue":
            print("You picked the blue door.")
        else:
            print("Sorry, the correct answer is either 'red' or 'blue'. Game Over. Goodbye!")



name = get_name()
print(name + "walk into the room, please.")

start_adventure()




# Pablo Vasquez
#  pablo.vasquez@mail.citytech.cuny.edu


 
 
