from roll_dice import roll_dice
import sys

number_of_players = int(input("Enter number of players: "))

global_scores = [0 for i in range(number_of_players)]

for count, value in enumerate(global_scores):
    print(f"Player #{count+1}, is your turn to play.")
    global_score = roll_dice()
    if global_score == 99:
        global_scores[count] = 0
    else:
        if global_score == 1111:
            print(f"Player #{count+1} wins!!!")
            sys.exit()
        else:        
            global_scores[count] = global_score

print(global_scores)
    

        