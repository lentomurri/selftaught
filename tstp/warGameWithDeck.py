import random

class Card():
    seeds = [None, "Spades", "Hearts", "Diamonds", "Clubs"]
    nums = [None, "Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
    def __init__(self, n, s):
        self.index_number = n
        self.index_seed = s
        self.seed = self.seeds[s]
    def compare(self, other):
        if self.index_number > other.index_number:
            return "Player 1 wins"
        if self.index_number < other.index_number:
            return "Player 2 wins"
        else:
            if self.index_seed > other.index_seed:
                return "Player 1 wins"
            else:
                return "Player 2 wins"
            

class Deck():
    def __init__(self):
        self.deck = []
        for i in range (1, 15):
            for j in range(1,5):
                card = Card(i, j)
                self.deck.append(card)
        random.shuffle(self.deck)

class Player():
  def __init__(self):
      self.wins = 0
      self.name = input("Choose player's name: ").capitalize()
      
def play_game():
    deck = Deck()
    deck = deck.deck
    player1 = Player()
    player2 = Player()
    while len(deck) > 2:
        message = "Press q to quit or any other key to play: "
        response = input(message)
        if response == "q":
            break
        else:
            random1 = random.randint(0, len(deck) - 1)
            random2 = random.randint(0, len(deck) - 1)
            card1 = deck[random1]
            card2 = deck[random2]
            result = card1.compare(card2)
            message = "{} has drawn {} of {}"
            print(message.format(player1.name, card1.index_number, card1.seed))
            print(message.format(player2.name, card2.index_number, card2.seed))
            for index, value in enumerate(deck):
                if deck[index] == card1 or deck[index] ==card2:
                    deck.pop(index)    
            if result == "Player 1 wins":
                print(result)
                player1.wins += 1
            if result == "Player 2 wins":
                print(result)
                player2.wins += 1
    result = player1.wins - player2.wins
    if result > 0:
        print("THE WAR HAS FINISHED! " + player1.name + " won!")
    elif result == 0:
        print("THE WAR HAS FINISHED! And it's a draw!")
    else:
        print("THE WAR HAS FINISHED! " + player2.name + " won!")

                    

play_game()