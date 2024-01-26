import sys
import random as rn

class Game:
    def __init__(self):
        self.deck = []
        for i in [2,3,4,5,6,7,8,9,10,11,12,13,14]:
            for j in [0,1,2,3]:
                self.deck.append(Card(j,i))
        rn.shuffle(self.deck)

    def play(self):
        pass

    def drawCard(self):
        return self.deck.pop(rn.randint(0,len(self.deck)-1))

class Player:
    def __init__(self, balance: float, name: str):
        self.balance = balance
        self.name = name
        self.hand = Hand()

class Card:
    rankStringConversions = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
    suitStringConversions = ["Hearts", "Clubs", "Diamonds", "Spades"]
    suitEmojiConversions = ["♥", "♣", "♦", "♠"]

    def __init__(self, suit: int, rank: int):
        self.suit = suit
        self.rank = rank

    def __str__(self) -> str:
        return f"{Card.rankStringConversions[self.rank - 2]} of {Card.suitStringConversions[self.suit]}"
    
    def getRank(self) -> str:
        return Card.rankStringConversions[self.rank - 2]
    
    def getSuit(self) -> str:
        return Card.suitEmojiConversions[self.suit]

class Hand:
    def __init__(self):
        self.hand = []

    def toList(self):
        return self.hand

    def add(self, card: Card) -> None:
        self.hand.append(card)

    def remove(self, index: int) -> None:
        self.hand.pop(index)

    def print(self, startIndex) -> None:
        handCount = len(self.hand)
        output = "----" * handCount + "\n"
        for i, e in enumerate(self.hand):
            if i < startIndex:
                output += "|??|"
                continue
            rank = e.getRank()
            if len(rank) > 2:
                rank = rank[0]
            output += f"|{rank + ' ' if len(rank) < 2 else rank}|"
        output += "\n"
        for i, e in enumerate(self.hand):
            if i < startIndex:
                output += "|??|"
                continue
            suit = e.getSuit()
            output += f"|{suit} |"
        output += "\n"
        output += "----" * handCount + "\n"
        print(output, end="", flush=True)

def intInput(prompt: str, min: int, max: int) -> int:
    """
    Prompts the user with {prompt} and then returns the first valid value they enter
    (will loop until the user enters a valid value)
    :param prompt: the prompt string
    :param min: the minimum value (inclusive)
    :param max: the maximum value (inclusive)
    :returns: the value entered by the user (int)
    """
    while True:
        print(prompt, end = "")
        try:
            num = int(input())        
            if num >= min and num <= max:
                return num
        except:
            continue


