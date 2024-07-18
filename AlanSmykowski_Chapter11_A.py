#Program to deal a Poker hand of five cards, with an interactive draw phase

import random


#Deck class final
class Deck:

    def __init__(self, size):

        #Initializing lists
        self.cardList = [i for i in range(size)]
        self.cardsInPlayList = []
        self.discardsList = []

        #Shuffling cards
        random.shuffle(self.cardList)

    #Deal a card
    def deal(self):

        #Check if deck needs reshuffling
        if len(self.cardList) < 1:

            random.shuffle(self.discardsList)

            self.cardList = self.discardsList
            self.discardsList = []

            print('Reshuffling...!!!')

        #Dealing a new card
        newCard = self.cardList.pop()

        self.cardsInPlayList.append(newCard)

        return newCard

    #Start a new hand
    def newHand(self):
        self.discardsList += self.cardsInPlayList
        self.cardsInPlayList.clear()


#Print a hand of cards
def printHand(hand):

    #Card ranks and suits
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['clubs', 'diamonds', 'hearts', 'spades']

    for card in hand:

        rank = card % 13
        suit = card // 13

        print(ranks[rank], 'of', suits[suit])


#Main
def main():

    #Create a deck of 52 cards
    myDeck = Deck(52)

    #Deal initial hand
    hand = [myDeck.deal() for _ in range(5)]

    print("\nYour initial hand:")
    printHand(hand)

    #Prompt user for replacement
    replaceIndices = input("\nEnter the numbers of cards to replace (1-5), separated by commas: ")
    replaceIndices = [int(i) - 1 for i in replaceIndices.split(',') if i.strip().isdigit()]

    #Replace cards
    for index in replaceIndices:
        hand[index] = myDeck.deal()

    #Print final hand
    print("\nYour final hand:")
    printHand(hand)

    #Start a new hand
    myDeck.newHand()


#Main call
if __name__ == "__main__":
    main()
