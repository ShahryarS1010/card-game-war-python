import player
import card
import random


def War(player1, player2):

    while True:
        print(player1.name + "'s card is: " + player1.hand[0].name)

        print(player2.name + "'s card is: " + player2.hand[0].name)

        # Whoever has a higher value card wins those cards and those cards are placed in the bottom (end of list) of your hand.
        if player1.hand[0].value > player2.hand[0].value:
            print(player1.name + " wins the cards.")
            player1.hand.append(player1.hand[0])
            player1.hand.append(player2.hand[0])
            player1.hand.pop(0)
            player2.hand.pop(0)

        elif player1.hand[0].value < player2.hand[0].value:
            print(player2.name + " wins the cards.")
            player2.hand.append(player2.hand[0])
            player2.hand.append(player1.hand[0])
            player2.hand.pop(0)
            player1.hand.pop(0)

        elif player1.hand[0].value == player2.hand[0].value:
            print("There is a war. Each player will place 3 cards and then deal another one.")
            war_value = 0



            while len(player1.hand) > war_value + 4 and len(player2.hand) > war_value + 4:
                    war_value += 4

                    print(player1.name + "'s card is: " + player1.hand[war_value].name)
                    print(player2.name + "'s card is: " + player2.hand[war_value].name)

                    if player1.hand[war_value].value > player2.hand[war_value].value:
                        print(player1.name + " wins the cards.")
                        temp_cards = []
                        for i in range(0,war_value+1):
                            temp_cards.append(player1.hand[i])
                            temp_cards.append(player2.hand[i])

                        player1.hand.extend(temp_cards)
                        player1.hand = player1.hand[war_value+1:]
                        player2.hand = player2.hand[war_value+1:]
                        break

                    elif player1.hand[war_value].value < player2.hand[war_value].value:
                        print(player2.name + " wins the cards.")
                        temp_cards = []
                        for i in range(0, war_value+1):
                            temp_cards.append(player2.hand[war_value])
                            temp_cards.append(player1.hand[war_value])

                        player2.hand.extend(temp_cards)
                        player2.hand = player2.hand[war_value+1:]
                        player1.hand = player1.hand[war_value+1:]
                        break


                    elif player1.hand[war_value].value == player2.hand[war_value].value:
                        print("Same Cards, Another War.")
                        war_value += 4

        print(player1.name + " has " + str(len(player1.hand)) + " cards.")
        print(player2.name + " has " + str(len(player2.hand)) + " cards.")

        # When the opponent has no cards then you win the game.
        if len(player1.hand) == 0:
            return str(player2.name + " wins the game.")

        if len(player2.hand) == 0:
            return str(player1.name + " wins the game.")


        result = input("Continue or Quit? (Q to Quit, anything else to Continue): ")

        if result == "Q":
            return "Game has been Quit."



def CreateDeck():
    deck = []
    same_suit = (CreateCards("2", 2))
    for i in same_suit:
        deck.append(i)

    same_suit = (CreateCards("3", 3))
    for i in same_suit:
        deck.append(i)

    same_suit = (CreateCards("4", 4))
    for i in same_suit:
        deck.append(i)

    same_suit = (CreateCards("5", 5))
    for i in same_suit:
        deck.append(i)

    same_suit = (CreateCards("6", 6))
    for i in same_suit:
        deck.append(i)

    same_suit = (CreateCards("7", 7))
    for i in same_suit:
        deck.append(i)

    same_suit = (CreateCards("8", 8))
    for i in same_suit:
        deck.append(i)

    same_suit = (CreateCards("9", 9))
    for i in same_suit:
        deck.append(i)

    same_suit = (CreateCards("10", 10))
    for i in same_suit:
        deck.append(i)

    same_suit = (CreateCards("Jack", 11))
    for i in same_suit:
        deck.append(i)

    same_suit = (CreateCards("Queen", 12))
    for i in same_suit:
        deck.append(i)

    same_suit = (CreateCards("King", 13))
    for i in same_suit:
        deck.append(i)

    same_suit = (CreateCards("Ace", 14))
    for i in same_suit:
        deck.append(i)

    return deck

def CreateCards(face, value):
    cards = []
    number = face
    face = number + " of Clubs"
    card1 = card.Card(face, value)
    face = number + " of Diamonds"
    card2 = card.Card(face, value)
    face = number + " of Hearts"
    card3 = card.Card(face, value)
    face = number + " of Spades"
    card4 = card.Card(face, value)
    cards.append(card1)
    cards.append(card2)
    cards.append(card3)
    cards.append(card4)
    return cards




print("Welcome to War")

# Create the Deck of 52 cards.
deck = CreateDeck()

# Shuffle the Deck and give 26 cards to both players.
shuffled_deck = random.sample(deck, len(deck))

player1_cards = shuffled_deck[:26]

player2_cards = shuffled_deck[26:]


# Get the names of the players.
name1 = input("Please enter the name of Player 1: ")

player1 = player.Player(name1, player1_cards)

name2 = input("Please enter the name of Player 2: ")

player2 = player.Player(name2, player2_cards)


# Begin the Game.
result = War(player1, player2)

# Print the Result.
print(result)

print("Thanks for Playing.")

