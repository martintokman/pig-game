from roll_dice import roll_dice

number_of_players = int(input("Enter number of players: "))

global_scores = [0 for i in range(number_of_players)]

for count, value in enumerate(global_scores):
    print(f"Player #{count}, is your turn to play.")
    global_score = roll_dice()
    global_scores[count] = global_score

print(global_scores)
    

        