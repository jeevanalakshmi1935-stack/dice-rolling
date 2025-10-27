import random
def roll_dice():
    dice = random.randint(1,6)
    print(f"You rolled a {dice}")
while True:
    roll_dice()
    choice = input("Roll again the dice? yes/no: ")
    if(choice == "yes"):
        print("Roll the dice")
    else:
        print("Thanks for playing")
        break
