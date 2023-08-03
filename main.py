from roll_dice import roll_dice
import sys, os

os.system("clear")


number_of_players = int(input("Enter number of players: "))

global_scores = [0 for i in range(number_of_players)]

while True:
    for count, value in enumerate(global_scores):
        print(f"\n\nPlayer #{count+1}, is your turn to play.")
        global_score = roll_dice(global_scores, count)
        if global_score == 99:
            global_scores[count] = 0
        else:
            if global_score == 1111:
                print(f"Player #{count+1} wins!!!")
                sys.exit()
            else:        
                global_scores[count] = global_score

    
    os.system("clear")
    print("\n\nRound finished. Overall scores are the following.")

    for count, value in enumerate(global_scores):
        print(f"Player #{count+1} has {value}.")

    print("\nA new round will start")

    

        