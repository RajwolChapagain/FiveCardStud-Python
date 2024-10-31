from functools import cmp_to_key
from card import Card
from deck import Deck
from hand import Hand
from hand_identifier import HandIdentifier
from hand_sorter import HandSorter

cards1 = [Card("AS"), Card("2C"), Card("3S"), Card("4H"), Card("5D")] 
cards2 = [Card("9H"), Card("JC"), Card("QH"), Card("KD"), Card("AH")] 

hand1 = Hand()
hand2 = Hand()

for a, b in zip(cards1, cards2):
    hand1.add_card(a)
    hand2.add_card(b)

hands = [hand1, hand2]

strength = HandSorter.compare_straight(hand1, hand2)

if strength == -1:
    print("Hand 1 is stronger")
elif strength == 1:
    print("Hand 2 is stronger")
