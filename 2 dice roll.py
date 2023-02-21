import random

def roll_dice():
    return random.randint(1, 6)

def add(dice1,dice2):
    return dice1 + dice2

def main():
    print("Welcome to the Dice Rolling Simulator!")

    while True:
        user_input = input("Press enter to roll the dice, or type 'x' to exit: ").lower()

        if user_input.lower() == "x":
            print("Thank you for playing!")
            break
        else:
            dice1 = roll_dice()
            dice2 = roll_dice()
            print(f"\nYour first dice rolled a {dice1}!")
            print(f"Second dice rolled a {dice2}!")
            print(f"Total of {add(dice1,dice2)} moves\n")



main()