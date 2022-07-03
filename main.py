#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo

EASY_TURNS = 10
HARD_TURNS = 5

def check_answer(guess, answer, turns):
  """checks asnwer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high")
    return turns - 1
  elif guess < answer:
    print("Too low")
    return turns - 1
  else:
    print(f"You got it right. The number is {answer}.")
  
def set_difficulty():  
  difficulty = input("Chosse a difficulty. Type 'easy' or 'hard': ").lower()
  if difficulty == "easy":
    return EASY_TURNS
  else:
    return HARD_TURNS
 
def game():
  print(logo)
  print("Welcome to the Number Guessing Game coded by future exceptional programmer Allen Chi!")
  answer = random.randint(1, 100)

  turns = set_difficulty()
  #Repeat the guessing functionality if the get it wrong.
  guess = 0
  #To avoid undefined name guess.
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("I am thinking of a number between 1 and 100. Guess what it is: "))
    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You have run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")

game()