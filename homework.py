



def print_parity(x):
  if x % 2 == 0:
    print(x, "is even")
  else:
      print(x, "is odd")
    
def get_destination():

    destination_name = input("Where should we go? > ")

    if destination_name == "":

      print("Okay. I know where we can go.")

      destination_name = "home"

    print("Let's leave for " + destination_name +".")

    return destination_name


    
