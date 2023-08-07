import random, os

def roll_dice(global_scores, count):
    
    """Recieves the list of global scores and the number of the current player.
       Allow the player to roll dice until a winner is set, dice is 0 or 
       the player doesn't want to roll again. 

    Args:
        global_scores (list): Current list of global scores for all players
        count (_type_): Player counter

    Returns:
        global_scores: Updated list of global scores for all players
    """

    global_score = global_scores[count]
    threshold = 10
    
    while True:
        
        while True:
            roll_dice = input("Roll dice? (y/n): ")
            roll_dice = roll_dice.capitalize()
            
            if roll_dice != "Y" and roll_dice !="N":
                 print("Invalid option, try again.")
            
            else:
                 break
        
        if roll_dice == "Y":
            
            dice = random.randrange(1,6)
            print(f"Dice was: {dice}")
            
            if dice > 1:
                
                global_score += dice
                print(f"Your global score is: {global_score}\n")
                
                if global_score >= threshold:
                    global_score = 1111 #winner code
                    break
                
                else:
                    continue
        
        elif roll_dice == "N":
                break
            
            
        if dice == 1:
            print("Your global score is 0")
            global_score = 99
            break
        
    return global_score


        