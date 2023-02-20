from random import randint
from random import shuffle


def deck_builder(suit1,suit2,suit3,suit4):
    _deck = []
    _suit_list = [suit1,suit2,suit3,suit4]
    for suit in _suit_list:
        for s in suit.card_list:
            _deck.append(s)
    return _deck

def shuffle_deck(deck):
    shuffle(deck)
    return deck

def shuffle_players(player_list):
    shuffle(player_list)
    return player_list

def pair_up (player_list:list):
    _team1 =[]
    _team2 = []
    shuffle_players(player_list)
    for p in player_list:
        if len(_team1)<2:
            _team1.append(p)
        else:
            _team2.append(p)
    
    return _team1,_team2