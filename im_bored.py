def im_bored(user_input=True):
    im_bored = input("Are you bored? (yes/no)")
    if im_bored == "yes":
        print("Find something to do.")
    elif im_bored == "no":
        print("I don't know what to do then.")
    else:
        print("I don't understand, what exactly do you want.")
