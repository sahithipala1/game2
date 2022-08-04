answer = input("what you like to play? (yes/no)")

if answer.lower().strip() == "yes":
    
    answer = input("you reach a crossroads, would you like to left or right?").lower
    if answer == "left":
        answer = input("You encounter a monster, would you like to run or attack?")
        
        if answer == "attack":
            print("this was not the greatest idea, you lost!")
        else:
            print("good choice")
    
    elif answer == "right":
        print("you walk aimlessly to the right and fall path of ice")
    
    else:
        print("Invalid choice, you lost")

else:
    print("That's too bad!")
