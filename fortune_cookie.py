# This program behaves like a fortune cookie but in python.

def fortune_cookie(user_input=True):
    fortune_cookie = input("I am a fortune cookie. Type a number between 1 and 5 to receive a fortune")
    if fortune_cookie == "1":
        print("You are not the weakest link.")
    elif fortune_cookie == "2":
        print("Apply what you learn and that is the true meaning of learning.")
    elif fortune_cookie == "3":
        print("Express your creativity")
    elif fortune_cookie == "4":
        print("Be Yourself")
    elif fortune_cookie == "5":
        print("Negativy swings but positivity slides")
