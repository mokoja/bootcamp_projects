import random

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
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print (game_images[user_choice])
computer_choice = random.choice(game_images)
print (f' Computer chose: \n {computer_choice}')
if game_images[user_choice] == rock:
    if computer_choice == rock:
        print ("It's a draw.")
    elif computer_choice == paper:
        print ("Paper wraps rock. You lost!")
    else:
        print ('Rock beats scissors. You won!')
if game_images[user_choice] == paper:
    if computer_choice == rock:
        print ("Paper wraps rock. You won!")
    elif computer_choice == paper:
        print (" It's a draw")
    else:
        print ('Scissors cut paper. You lost!')
if game_images[user_choice] == scissors:
    if computer_choice == rock:
        print ("IRock beats scissors. You lost!")
    elif computer_choice == paper:
        print ("Scissors cut paper. You won!")
    else:
        print ("It's a draw")
