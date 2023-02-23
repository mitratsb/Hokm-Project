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


score_a = cs.Score()
score_b = cs.Score()
game_score = cs.Score()

player_list = [p1, p2, p3, p4]
team_a_members,team_b_members = mc.pair_up(player_list)

team_a = cs.Teams("A", team_a_members , score_a)
team_b = cs.Teams("B", team_b_members , score_b)

##########################
#     Choosing Hakem     #
##########################

hakem = mc.choose_hakem(main_deck, player_list)

##########################
#     Handing out cards  #
#      Choosing Hokm     #
##########################

print(player_list)
print(team_a.members,team_b.members)
print(hakem)