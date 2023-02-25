
class Cards:
    def __init__(self,suit):
        __values = [2,3,4,5,6,7,8,9,10,11,12,13,14]
        
        self.suit = suit
        self.card_list = [] 
        self.is_hokm = False

        for v in __values:
            self.card_list.append([suit,v])


class Player:
    def __init__(self,name,is_player):
        self.name = name
        self.hand = []
        self.is_player = is_player
        self.is_hakem = False

    def __repr__(self):
        return self.name
    

# class Score:
#     def __init__(self):
#         self.team_score = 0
#         self.match_score = 0


class Teams:
    def __init__(self,name,members:list):
        self.name = name
        self.members = members
        self.team_score = 0
        self.match_score = 0
    
