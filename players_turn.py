import random, os


global_score = 0
threshold = 20

os.system("clear")

while True:
    dice = random.randrange(1,7)
    

    if dice == 1:
        global_score = 0
        print(f"\nYour score for this round is: {dice} ")
        print("You loose all your score")
        break
    else:
        global_score += dice
        print(f"\nYour score for this round is: {dice} ")
        print(f"Your global score is {global_score}")

    if global_score >= threshold:
        print("You win!")
        break
    else:
        while True:
            roll_again = input("Roll again? (y/n): ")
            roll_again = roll_again.capitalize()
            if roll_again != "Y" and roll_again != "N":
                print(roll_again)
                print("Invalid option, try again.")
                continue
            else: 
                break
        if roll_again == "Y":
            continue
        else:
            print("Thank you for playing. Goodbye :)")
            break

        