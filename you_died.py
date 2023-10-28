# Pablo Vasquez April 13th , 2021
# you_died program
# In this program the user is given a reason on how they died
# At first I was having some trouble but then the professor put some source code up and it made the assingment more clearer
# I was able to figure out how to get a sound to play and you need the code on lines 7 and 11 but use the mp3 file that you want
# Now, thanks to the professor's help I was able to get a working python program!!!
import subprocess
def you_died(how="you wandered too long and fell down a shaft "):
    print(how+" You died Thank for playing. Goodbye.")
    subprocess.call (["afplay", "woosh.mp3"])
    exit(0)

