from common import *

class BlackJackPlayer(Player):
    def __init__(self, balance, name):
        super(BlackJackPlayer, self).__init__(balance, name)

    def printHand(self):
        self.hand.print(0)

    def calcHandTotal(self):
        total = 0
        aces = []
        handList = self.hand.toList()
        for i in handList:
            if i.rank < 11:
                total += i.rank
            elif i.rank < 14:
                total += 10
            else:
                aces.append(i)
        for i in aces:
            if total + 11 <= 21:
                total += 11
            else:
                total += 1
        return total

class BlackJackHuman(BlackJackPlayer):
    def __init__(self, balance):
        super(BlackJackHuman, self).__init__(balance, "Player")

class BlackJackDealer(BlackJackPlayer):
    def __init__(self):
        super(BlackJackDealer, self).__init__(-1, "Dealer")

    def printHand(self):
        self.hand.print(1)

    def calcHandTotal(self, startIndex):
        total = 0
        aces = []
        handList = self.hand.toList()
        for i in handList[startIndex:]:
            if i.rank < 11:
                total += i.rank
            elif i.rank < 14:
                total += 10
            else:
                aces.append(i)
        for i in aces:
            if total + 11 <= 21:
                total += 11
            else:
                total += 1
        return total

class BlackJack(Game):
    def __init__(self):
        super(BlackJack, self).__init__()

    def play(self):
        self.player = BlackJackHuman(100) # 100 credits -> this would be fetched from DB
        # Not currently doing anything with these, but would be ez to add wager amount here
        # and do smth with it in dealer and player win functions
        self.dealer = BlackJackDealer()

        # Initial Hands
        self.player.hand.add(self.drawCard())
        self.player.hand.add(self.drawCard())
        self.dealer.hand.add(self.drawCard())
        self.dealer.hand.add(self.drawCard())

        self.playerTotal = self.player.calcHandTotal()
        self.dealerTotal = self.dealer.calcHandTotal(0)

        if self.playerTotal == 21:
            self.playerWin()
            return

        self.displayCards()
        while self.stickOrTwist():
            self.player.hand.add(self.drawCard())
            self.playerTotal = self.player.calcHandTotal()
            self.displayCards()
            print(f"The player drew the {self.player.hand.toList()[-1]}.")
            if self.playerTotal == 21: # CASE : Player blackjack
                self.playerWin()
                return
            if self.playerTotal > 21: # CASE : Player bust
                self.dealerWin()
                return
        
        while self.dealerTotal < 17:
            self.dealer.hand.add(self.drawCard())
            self.dealerTotal = self.dealer.calcHandTotal(0)
            self.displayCards()
            print(f"The dealer drew the {self.dealer.hand.toList()[-1]}.")
            if self.dealerTotal > 21: # CASE : Dealer bust
                self.playerWin()
                return

        if self.playerTotal > self.dealerTotal:
            self.playerWin()
        else:
            self.dealerWin()
    
    def dealerWin(self):
        self.displayCards()
        print("The dealer won!")

    def playerWin(self):
        self.displayCards()
        print("The player won!")

    def displayCards(self):
        print("Dealer Cards:")
        self.dealer.printHand()
        print(f"{self.dealer.calcHandTotal(1)} + ?")
        print("Your Cards:")
        self.player.printHand()
        print(self.playerTotal)

    def stickOrTwist(self):
        return intInput("[Twist (1) / Stick(2)]:\n", 1, 2) == 1
