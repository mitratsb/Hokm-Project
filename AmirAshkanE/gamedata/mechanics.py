from random import randint,shuffle



def deck_builder(suit1,suit2,suit3,suit4):
    _deck = []
    _suit_list = [suit1,suit2,suit3,suit4]
    for suit in _suit_list:
        for s in suit.card_list:
            _deck.append(s)
    return _deck


# def shuffle_deck(deck):
#     shuffle(deck)
#     return deck


def shuffle_players(player_list):
    shuffle(player_list)
    return player_list


def pair_up (player_list:list):
    _team1 =[]
    _team2 = []
    shuffle_players(player_list)

    _team1 = [player_list[0],player_list[2]]
    _team2 = [player_list[1],player_list[3]]
    
    return _team1,_team2


def choose_hakem(deck,player_list):
    _hakem = None
    _deck = deck[:]
    shuffle(_deck)
    
    i=0
    while i in range(0,4) and _hakem == None:
        for card in _deck:
            
            if i > 3 and _hakem == None :
                i = 0
                _deck.remove(card)
            elif card[1] == 14:
                _hakem = player_list[i]
                player_list[i].is_hakem = True
                break
            else:
                i += 1
                _deck.remove(card)
    
    return _hakem

def give_hand(deck,player_list):
    shuffle(deck)
    
    n = 5
    
    for player in player_list:
        for card in deck:
            i=0
            while i < n :
                player.hand.append(card)
                deck.remove(card)
                i+=1
                
            