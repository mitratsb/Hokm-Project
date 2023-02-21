from gamedata import mechanics as mc
from gamedata import classes as cs

clubs = cs.Cards("Club")
hearts = cs.Cards("Heart")
spades = cs.Cards("Spade")
diamonds = cs.Cards("Diamond")

deck = mc.deck_builder(clubs, diamonds, hearts, spades)

p1 = cs.Player("Ashkan", True)
p2 = cs.Player("Tina", False)
p3 = cs.Player("Payam", False)
p4 = cs.Player("Faraz", False)

player_list = [p1, p2, p3, p4]
team_a,team_b = mc.pair_up(player_list)

print(team_a,team_b)