from roll_dice import roll_dice
import sys, os

os.system("clear")

while True:
    
    try:
        number_of_players = int(input("Enter number of players (2 or more): "))

        global_scores = [0 for i in range(number_of_players)]
        
        if number_of_players > 1:
            
            while True:
                
                for count, value in enumerate(global_scores):
                    
                    print(f"\n\nPlayer #{count+1}, is your turn to play.")
                    global_score = roll_dice(global_scores, count)
                    
                    if global_score == 99:
                        global_scores[count] = 0
                    
                    else:
                        
                        if global_score == 1111: #si hay un ganador salgo del bucle for
                            break

                        else:        
                            global_scores[count] = global_score
  
                
                if global_score == 1111: #si hay un ganador salgo del bucle while
                    break
                
                
                print("\n\nRound finished. Overall scores are the following.")

                for count, value in enumerate(global_scores):
                    print(f"Player #{count+1} has {value}.")

                while True:
                    
                    _continue = input("\nA new round will start, press (y) to continue, (q) to end game: ")
                    
                    if _continue.capitalize() != "Y" and _continue.capitalize() != "Q":
                        print("Invalid option, try again.")
                        continue
                    
                    elif _continue.capitalize() == "Q":
                        print("Thank you for playing. Goodbye :)")
                        sys.exit()
                    
                    else:
                        break
                
                os.system("clear")

            
            if global_score == 1111: #si hay un ganador termina el juego
                    
                    print(f"Player #{count+1} wins!!!\n")
                    
                    while True:
                        
                        play_again = input("Play again? (y/n): ")
                        play_again = play_again.capitalize()
                        
                        if play_again != "Y" and play_again != "N":
                            print("Option not allowed, try again.")
                            continue
                        
                        else:
                            break
                    
                    if play_again == "Y":
                        os.system("clear")
                        continue
                    
                    elif play_again == "N":
                        sys.exit()
            

        else:
            print("The minimum number of players is two, try again.\n")
    
    
    except ValueError:
        print("Only numbers allowed, try again\n")
        continue

    






        