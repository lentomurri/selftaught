
import random
import keyboard


class Card():
    seeds = ["Spades", "Hearts", "Diamonds", "Clubs"]
    nums = [None, "Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
    def __init__(self, s, n):
        self.index_seed = s
        self.seed = self.seeds[s]
        self.index_number = n
        self.number = self.nums[n]
    
    def compare(self, other):
        if self.index_number > other.index_number:
            return "Player 1 wins"
        if self.index_number < other.index_number:
            return "Player 2 wins"
        else:
            if self.index_seed > other.index_seed:
                return "Player 1 wins"
            if self.index_seed < other.index_seed:
                return "Player 2 wins"
            else:
                return "It's a draw!"

# function to create card
def create_card():
    seed = random.randrange(3)
    number = random.randrange(1, 12)
    return Card(seed, number)

def play_game():
    win = False
    tracker1 = 0
    tracker2 = 0
    while win == False:
        message = "Press q to quit or any other key to play: "
        if tracker1 == 5:
            print("Player 1 wins the game!!")
            win = True
        if tracker2 == 5:
            print("You lost!!")
            win = True
        response = input(message)
        if response == "q":
            break
        else:
            card1 = create_card()
            card2 = create_card()
            result = card1.compare(card2)
            print("Player1 drew " + str(card1.number) + " of " + str(card1.seed) + ", Player2 drew " + str(card2.number) + " of " +  str(card2.seed))
            if result == "Player 1 wins":
                print(result)
                tracker1 += 1
            if result == "Player 2 wins":
                print(result)
                tracker2 += 1

play_game()