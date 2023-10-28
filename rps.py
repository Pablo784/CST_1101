def rps(user_wins=True) :
  print("Let's play Rock, Paper, Scissors!")
  prompt = "Choose rock, paper or scissors by entering the word in lower case: "
  your_choice = input(prompt)
  if user_wins:
    if your_choice == "rock" :
      print("Scissors.  You win!")
    elif your_choice == "paper" :
      print("Rock.  You win!")
    elif your_choice == "scissors" :
      print("Paper.  You win!")
    else :
      print("Invalid choice")
      return "Invalid choice"
  else:
    if your_choice == "rock" :
      print("Paper.  You lose!")
    elif your_choice == "paper" :
      print("Scissors.  You lose!")
    elif your_choice == "scissors" :
      print("Rock.  You lose!")
    else :
      print("Invalid choice")
      return "Invalid choice"
  return your_choice
