from gamedata import mechanics as mc
from gamedata import classes as cs

##########################
# On Awake Instantiation #
##########################

clubs = cs.Cards("Club")
hearts = cs.Cards("Heart")
spades = cs.Cards("Spade")
diamonds = cs.Cards("Diamond")

main_deck = mc.deck_builder(clubs, diamonds, hearts, spades)

p1 = cs.Player("Ashkan", True)
p2 = cs.Player("Tina", False)
p3 = cs.Player("Payam", False)
p4 = cs.Player("Faraz", False)


# score_a = cs.Score()
# score_b = cs.Score()
# game_score = cs.Score()

player_list = [p1, p2, p3, p4]
team_a_members,team_b_members = mc.pair_up(player_list)

team_a = cs.Teams("A", team_a_members)
team_b = cs.Teams("B", team_b_members)
Teams = [team_a,team_b]
##########################
#     Choosing Hakem     #
##########################

hakem = mc.choose_hakem(main_deck, player_list)

##########################
#     Handing out cards  #
#      Choosing Hokm     #
##########################

turn_index = 0

for player in player_list:
    if player.is_hakem:
        turn_index = player_list.index(player)
        break


while True:
    if turn_index > 3:
        turn_index = 0
    elif player_list[turn_index].hand != []:
        break
    else:    
        mc.give_hand(main_deck, player_list[turn_index], 5)
        turn_index += 1

mc.choose_hokm(hakem)


while main_deck != []:
    if turn_index > 3:
        turn_index = 0
    else:
        if len(player_list[turn_index].hand)<13:
            mc.give_hand(main_deck, player_list[turn_index], 8)
        else:    
            turn_index += 1

##########################
#       Begin Game       #
##########################

game_score = 7

while team_a.match_score < game_score or team_b.match_score < game_score :
    round_score = 7
    while team_a.team_score < round_score or team_b.team_score < round_score:
        table = []
        while len(table) < 4:
            
            # Play cards
            # Compare cards
            # Determine Winner and add score
            # clear table and continue to next round
            
            pass
    pass