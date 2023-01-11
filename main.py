from random import choice

class Card:
  def __init__(self, num, col):
    self.num = num
    self.col = col

class Num:
  def __init__(self, name, num):
    self.num = num
    self.name = name

class Colour:
    def __init__(self, name,unicode):
        self.name = name
        self.unicode = unicode

class Player:
    def __init__(self, name,cards):
        self.name = name
        self.cards = cards

def takecards(incards,num):
    outcards = []
    for i in range(num):
        card = choice(cards)
        outcards.append(card)
        incards.remove(card)
    return outcards

# init cards
numbers = [Num("2",2),Num("3",3),Num("4",4),Num("5",5),Num("6",6),Num("7",7),Num("8",8),Num("9",9),Num("10",10),Num("J",11),Num("Q",12),Num("K",13),Num("A",14)]

cards = []
colours = [Colour("spade","\U00002660"),Colour("heart","\U00002665"),Colour("club","\U00002666"),Colour("dianmond","\U00002663")]
# print(colours[0].name)
for colour in colours:
    for number in numbers:
        cards.append(Card(number,colour))

for card in cards:
    print(card.num.name,card.col.unicode)

#define players and handcards
print("Sending starting hands: ")
players = [Player("Yifan",None),Player("Tingting",None)]

for player in players:
    player.cards = takecards(cards,2)

for player in players:
    print("\n",player.name,":",end=" ")
    for card in player.cards:
        print(card.num.name,card.col.unicode, end=" ")

print("\n\nSending flopcards: ")
flopcards = takecards(cards,3)

print("\nFlop cards are: ",end="")
for card in flopcards:
    print(card.num.name,card.col.unicode, end=" ")



print("\n\nSending Turn card:")
flopcards = takecards(cards,1)

print("\nTurn cards is: ",end="")
for card in flopcards:
    print(card.num.name,card.col.unicode, end=" ")



print("\n\nSending River card:")
flopcards = takecards(cards,1)

print("\nRiver cards is: ",end="")
for card in flopcards:
    print(card.num.name,card.col.unicode, end=" ")

