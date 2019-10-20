# import csv

# movies = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
# with open("C:/Users/Lento/Desktop/SelfTaught/tstp/movies.csv", "w") as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=",")
#     for movie_list in movies:
#         spamwriter.writerow(movie_list)


#player one picks a secret word

def hangman():
    word = input("Choose a word for your competitor! ")
    #save drawing of hangman in a list to display
    drawing = ["-----¬",
               "     |",
               "     O",
               "    /|\\",
               "     |",
               "    / \\"]
    #set number of mistakes to 0.
    wrong = 0
    #set number of attempts left before game over. That's the length of drawing - wrong attempts
    #set word printed with underscore by multiplying word length * underscore and saving it in a var
    board = ['_'] * len(word)
    #set win condition
    win = False
    #put everything in a loop so the game keeps going until you lose or win
    while wrong < len(drawing):
        # check the condition for victory and break the loop 
        if "_" not in board:
            win = True
            print("You won! The word was " + str("".join(board)))
            break
        # ask for attempt from user and check if in word
        attempt = input("Enter a letter: ")
        # generate index and item at the same time. VERY USEFUL TO GET INDEX!!
        for index, item in enumerate(word):
        #this var will change when we find letters by substituiting index(char) with the _
            if item == attempt:
                board[index] = attempt
                print((" ".join(board)))
        if attempt not in word:
            wrong += 1
            attemptsLeft = len(drawing) - wrong
            print("Wrong letter! You still have " + str(attemptsLeft) + " attempts")
            if wrong == 6:
                print("\n".join(drawing))
                print("YOU KILLED THE MAN!! GAME OVER!")
                break
        print("\n".join(drawing[0:wrong]))



hangman()