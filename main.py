#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
def chose_dificulty() :
  if input("Choose dificulty: \"easy\" or \"hard\"\n").lower() == "easy" :
    nr_of_guess = 10
  else: 
    nr_of_guess = 5
  return nr_of_guess


def guess_game() :
  nr_of_guess = chose_dificulty()
  while nr_of_guess :
    guess = int(input("Make a guess: "))
    if guess == RANDOM_NUMBER :
      print("Your guess is correct. You Win")
      exit()
    elif RANDOM_NUMBER > guess :
      print("Too Low")
    else :
      print("Too High")
    nr_of_guess -= 1
    print(f"You have {nr_of_guess} guesses left")


import random
print("Welcome to the number guessing game")
print("I am thinking of a number between 1 and 100")
RANDOM_NUMBER = random.randint(1,100)
guess_game()
print("You ran out of guesses. You Lose")
  


