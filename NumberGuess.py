# Code for number guessing game:
from random import randint
from art import logo

Hard_level=5
Easy_level=10
def guess_number(guess,turns,answer):
  if answer>guess:
    print("Number is Too high")
    return turns-1
  elif answer<guess:
    print("Number is Too low")
    return turns-1

  else:
    print(f"Congratulation you guessed right numner that is -  {answer}")


def difficulties_level():
  level =input("choose your difficulty level easy or hard?: ").lower()
  if level=="easy":
    return Easy_level

  elif level=="hard":
    return Hard_level
 











def game():
 print(logo)

 print("Welcome to the guessing number game")
 print("I am thinking number between 1 to 100")
 answer=randint(1,100)
 turns=difficulties_level()
 guess=0
 while guess!=answer:
  print(f"you have remaining {turns} chances, use next turns to choose right number")
  guess=int(input("Guess the Number:  "))

  turns=guess_number(guess, turns, answer)

  if turns==0:
    print("you have exhausted all the chances better luck next time")

  elif guess !=0:
   print("Guess again.")

game()

    








