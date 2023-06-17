import random

class Card:
  def __init__(self,suit,rank):
    self.rank = rank
    self.suit = suit
  
  def __str__(self):
      return f"{self.rank['rank']} of {self.suit}"


class Deck:
  def __init__(self):

    self.cards = []

    suits = [ "Hearts", "Diamonds", "Spades", "Clubs" ]
    ranks = [ {"rank":"A","value":"1"},{"rank":"2","value":"2"},{"rank":"3","value":"3"},{"rank":"4","value":"4"}, {"rank":"5","value":"5"},{"rank":"6","value":"6"}, {"rank":"7","value":"7"},{"rank":"8","value":"8"}, {"rank":"9","value":"9"},{"rank":"10","value":"10"}, {"rank":"Q","value":"10"},{"rank":"K","value":"10"}, {"rank":"J","value":"10"} ]



    for suit in suits:
      for rank in ranks:
        self.cards.append(Card(suit,rank))
  

  def display_cards(self):
        for card in self.cards:
            print(card)

  
  def shuffle(self):
    if(len(self.cards)>1):
      random.shuffle(self.cards)

  def deal(self,number):
    cards_dealt = []
    for x in range(number):
      if(len(self.cards)>0):
        card = self.cards.pop()
        cards_dealt.append(card)

    return cards_dealt

class Hand:
    def __init__(self, dealer=False):
        self.cards = []
        self.value = 0
        self.dealer = dealer

    def add_card(self, card_list):
        self.cards.extend(card_list)

    def calculate_value(self):
        self.value = 0
        has_ace = False
 
        for card in self.cards:
            card_value = int(card.rank["value"])
            self.value += card_value
            if card.rank["rank"] == "A":
                has_ace = True

        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        self.calculate_value()
        return self.value

    def display(self,show_all_cards = False):

        if self.dealer:
            print("Dealer's Hand: ")
            for index,card in enumerate(self.cards):
                if index == 0 and not show_all_cards:
                    print("Face Down Card!")
                else:
                    print(card)
        else:
            print("Player's Hand: ")
            for card in self.cards:
                print(card)
            print("value: ", self.get_value())
        print()


deck=Deck()
deck.shuffle()


player_hand = Hand()
player_hand.add_card(deck.deal(2))
player_hand.display()

dealer_hand = Hand(dealer = True)
dealer_hand.add_card(deck.deal(2))
dealer_hand.display()

