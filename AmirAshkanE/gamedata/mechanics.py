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

def give_hand(deck:list,player,n):
    shuffle(deck)
    i=0
    for card in deck:
        player.hand.append(card)
        deck.remove(card)
        i+=1
        if i==n:
            break
            
def choose_hokm(player):
    if player.is_player:
        print(player.hand)
        suit = input("Choose Hokm suit: ")
        for card in player.hand:
            if suit.capitalize() == card[0]:
                print(f"Hokm is: {card[0]}")
                break
        return suit.capitalize()
    else:
        i = randint(0, len(player.hand)-1)
        card = player.hand[i]
        print(f"Hokm is: {card[0]}")
        return card[0]

def check_suit_availability(player,active_suit):
    suits_in_hand=[]
    for card in player.hand:
        if card[0] == active_suit:
            suits_in_hand.append(card[0])
    return active_suit in suits_in_hand        

def find_available_cards(player,active_suit):
    _hand = []
    for card in player.hand:
        if card[0] == active_suit:
            _hand.append(card)
    return _hand
    
def play_cards(player,table,active_suit,play_history):
    
    if player.is_player:
        has_chosen = False
        while not has_chosen:
            print(player.hand)
            c,v = input("Choose a card from your hand(seperate suit and value by space): ").split()
            drawn_card = [c.capitalize(),int(v)]
            if drawn_card not in player.hand:
                print("You must choose a card from you hand!!")
            else:
                if active_suit == "":
                    for card in player.hand:
                        if drawn_card == card:
                            table.append(drawn_card)
                            player.hand.remove(drawn_card)
                            active_suit = c.capitalize()
                            play_history.append({player.name : drawn_card})
                            has_chosen = True
                            break
                else:
                    if check_suit_availability(player, active_suit) and c.capitalize() != active_suit:
                        print(f"{active_suit} is available in your hand, choose again appropriately")
                    else:
                        table.append(drawn_card)
                        player.hand.remove(drawn_card)
                        play_history.append({player.name : drawn_card})
                        has_chosen = True
                        
                            
    else:
        if active_suit == "" or not check_suit_availability(player, active_suit):
            drawn_card = player.hand[randint(0, len(player.hand)-1)]
            player.hand.remove(drawn_card)
            table.append(drawn_card)
            play_history.append({player.name : drawn_card})
            active_suit = drawn_card[0]
        else:
            drawn_card = find_available_cards(player, active_suit)[randint(0, len(find_available_cards(player, active_suit))-1)]
            player.hand.remove(drawn_card)
            table.append(drawn_card)
            play_history.append({player.name : drawn_card})
