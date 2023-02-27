from random import randint,shuffle
from gamedata import classes as cs



def deck_builder(suit1,suit2,suit3,suit4):
    _deck = []
    _suit_list = [suit1,suit2,suit3,suit4]
    for suit in _suit_list:
        for s in suit.card_list:
            _deck.append(s)
    return _deck

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
    print(f"Hakem is {_hakem}")
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
            drawn_card = [card for card in player.hand if c.capitalize() == card[0] and int(v) == card[1]][0]
            if drawn_card not in player.hand:
                print("You must choose a card from you hand!!")
            else:
                if active_suit == "":
                    for card in player.hand:
                        if drawn_card == card:
                            table.append(card)
                            player.hand.remove(card)
                            active_suit = c.capitalize()
                            play_history.update({player.name : card})
                            has_chosen = True
                            break
                else:
                    if check_suit_availability(player, active_suit) and c.capitalize() != active_suit:
                        print(f"{active_suit} is available in your hand, choose again appropriately")
                    else:
                        table.append(drawn_card)
                        player.hand.remove(drawn_card)
                        play_history.update({player.name : drawn_card})
                        has_chosen = True
                        
                            
    else:
        if active_suit == "" or not check_suit_availability(player, active_suit):
            drawn_card = player.hand[randint(0, len(player.hand)-1)]
            player.hand.remove(drawn_card)
            table.append(drawn_card)
            play_history.update({player.name : drawn_card})
            active_suit = drawn_card[0]
        else:
            drawn_card = find_available_cards(player, active_suit)[randint(0, len(find_available_cards(player, active_suit))-1)]
            player.hand.remove(drawn_card)
            table.append(drawn_card)
            play_history.update({player.name : drawn_card})

def compare_cards(table,hokm,active_suit):
    for card in table:
        if card[0] == hokm:
            card[1] += 100
        elif card[0] != active_suit:
            card[1] = 0
    
    winner_card = table[0]
    for card in table:
        if winner_card[1] < card[1]:
            winner_card = card
    if winner_card[0] == hokm:
        winner_card[1] -= 100
    return winner_card

def find_winner(play_history,winner_player):
    winner = [k for k,v in play_history.items() if v == winner_player]
    return winner[0]

def find_winner_team(teams,winner_player):
    for team in teams:
        for member in team.members:
            if winner_player == str(member):
                return team

def set_winner_index(winner_player,player_list):
    for player in player_list:
        if winner_player == player.name:
            return player_list.index(player)

def give_point_winner(teams,winner_player):
    for team in teams:
        for member in team.members:
            if winner_player == str(member):
                team.team_score += 1

def tally_round_score(team_a,team_b,round_score,winner_team):
    if team_a.team_score == round_score and team_b.team_score == 0:
        team_a.match_score += 2
        team_a.team_score = 0
        team_b.team_score = 0
    elif team_b.team_score == round_score and team_a.team_score == 0:
        team_b.match_score += 2
        team_a.team_score = 0
        team_b.team_score = 0
    else:
        winner_team.match_score += 1
        team_a.team_score = 0
        team_b.team_score = 0

def begin_new_game(main_deck,winner_player,winner_team,player_list,turn_index,hakem,teams):
    clubs = cs.Cards("Club")
    hearts = cs.Cards("Heart")
    spades = cs.Cards("Spade")
    diamonds = cs.Cards("Diamond")
    
    for player in player_list:
        player.hand.clear()
    
    main_deck = deck_builder(clubs, diamonds, hearts, spades)
    shuffle(main_deck)
    
    hakem_index = player_list.index(hakem)

    for team in teams:
        if winner_team.members == team.members:
            for member in team.members:
                if winner_player == member.name:
                    hakem_index = player_list.index(hakem)
                    break
            
        else:
            player_list[hakem_index].is_hakem = False
            hakem_index = player_list.index(hakem) + 1
            if hakem_index > 3:
                hakem_index = 0
            hakem = player_list[hakem_index]    
            player_list[hakem_index].is_hakem = True
            break
            
            
    
    
    for player in player_list:
        if player.is_hakem:
            hakem_index = player_list.index(player)
            break
    
    turn_index = hakem_index
    
    while True:
        if turn_index > 3:
            turn_index = 0
        elif player_list[turn_index].hand != []:
            break
        else:    
            give_hand(main_deck, player_list[turn_index], 5)
            turn_index += 1

    hokm = choose_hokm(hakem)

    turn_index = hakem_index
    while main_deck != []:
        if turn_index > 3:
            turn_index = 0
        else:
            if len(player_list[turn_index].hand)<13:
                give_hand(main_deck, player_list[turn_index], 8)
            else:    
                turn_index += 1
    print(f"Hakem is : {hakem}")
    return hakem_index,hakem,hokm