def hangman():
#player one picks a secret word     
    word = input("Choose a word for your competitor! ").lower()
    #save hangmanDrawing of hangman in a list to display
    hangmanDrawing = ["-----¬",
               "     |",
               "     O",
               "    /|\\",
               "     |",
               "    / \\"]
    # make a drawing for winning
    winningDrawing = [
                      "   * *   * * ",
                      "  *    *    *",
                      "   *  YOU  *",
                      "    * WIN *",
                      "     *   * ",
                      "       *"]
    #set number of mistakes to 0.
    wrong = 0
    #set number of attempts left before game over. That's the length of hangmanDrawing - wrong attempts
    #set word printed with underscore by multiplying word length * underscore and saving it in a var
    board = ['_'] * len(word)
    #set win condition
    win = False
    #put everything in a loop so the game keeps going until you lose or win
    while wrong < len(hangmanDrawing):
        # check the condition for victory and break the loop 
        if "_" not in board:
            win = True
            print("You won! The word was " + str("".join(board)))
            print("\n".join(winningDrawing))
            break
        # ask for attempt from user and check if in word
        attempt = input("Enter a letter: ").lower()
        # generate index and item at the same time. VERY USEFUL TO GET INDEX!!
        for index, item in enumerate(word):
        #this var will change when we find letters by substituiting index(char) with the _
            if item == attempt:
                board[index] = attempt
                # joins all the items in board and show them nicely to the user
                print((" ".join(board)))
        if attempt not in word:
            wrong += 1
            attemptsLeft = len(hangmanDrawing) - wrong
            print("Wrong letter! You still have " + str(attemptsLeft) + " attempts")
            # game over - lose condition
            if wrong == 6:
                print("\n".join(hangmanDrawing))
                print("YOU KILLED THE MAN!! GAME OVER!")
                break
        print("\n".join(hangmanDrawing[0:wrong]))



hangman()