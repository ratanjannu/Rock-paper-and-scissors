rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
import random
user = int(input("What do you choose? Type 0 for Rock,1 for Paper or 2 for Scissors\n"))
if user >=3:
  print("dum dum")
else:
  print(game_images[user])
random_int = random.randint(0,2)
print("The computer choose:")
print(game_images[random_int])
if user == 0 and random_int == 0 :
  print("Its a draw")
elif user == 1 and random_int == 0:
  print("You win")
elif user ==1 and random_int == 1:
  print("Its a draw")
elif user == 2 and random_int == 1:
  print("You win")
elif user == 2 and random_int == 0:
  print("You loose")
elif user == 2 and random_int == 2:
  print("Its a draw")
elif user == 1 and random_int == 2:
  print("You loose")
elif user == 0 and random_int == 1:
  print("You loose")
elif user == 0 and random_int == 2:
  print("You win")
else:
  print("You choose an invalid number")

