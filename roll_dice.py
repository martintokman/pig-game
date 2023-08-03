import random, os




def roll_dice():
    global_score = 0
    
    while True:
        
        roll_dice = input("Roll dice? (y/n): ")
        roll_dice = roll_dice.capitalize()
        
        if roll_dice == "Y":
            
            dice = random.randrange(1,6)
            print(f"Dice was: {dice}")
            
            if dice > 1:
                global_score += dice
                print(f"Your global score is: {global_score}")
                continue
        
        elif roll_dice == "N":
                break
            
            
        if dice == 1:
                print("You loose all your score.")
                global_score = 99
                
                break
        
    return global_score


        