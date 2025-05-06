import random 
score = 0
player_name = input("Please enter your name: ") 

while True:    
    words = ["python", "computer", "programming",
            "condition", "else", "break", "input",
            "print", "while", "for"] 
    pick = random.choice(words)

    random_word = random.sample(pick, len(pick)) 
    jumbled = "".join(random_word)
    print("Jumbled word is :", jumbled)
    answer = input("what is in your mind? ")
    
    if answer == pick:
        score+- 1
        print("Your score is", score)
    
    if score== 10:
        print("Congratulations",player_name,"you win!")
        print ("Your score is", score)
        break
    
    else:
        print("Better luck next time... correct word is :", pick)    
        cont = input("press 'y' to continue and 'n' to quit : ") 
        if cont == "n":
            print(player_name, "Your score is :", score)
            print("Thanks for playing...")
            break 