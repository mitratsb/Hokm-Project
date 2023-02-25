from random import shuffle,choice,randint

x={"♥️":[2,3,4,5,6,7,8,9,10,11,12,13,14],
           "♠️":[2,3,4,5,6,7,8,9,10,11,12,13,14],
           "♦️":[2,3,4,5,6,7,8,9,10,11,12,13,14],
           "♣️":[2,3,4,5,6,7,8,9,10,11,12,13,14]}
all_cards = []
for key,value in x.items():
    for v in value:
        all_cards.append([key,v])

#-----------------------------------------------------------------------------------------

class Card:
    db=all_cards
    
    def __init__(self,suit,value,is_hokm):
        self.suit=suit
        self.value=int(value)
        self.is_hokm=False
        
    def __repr__(self):
        return f'{self.suit} , {self.value}'
        
    def compare(self,other_card):
        pass

#-----------------------------------------------------------------------------------------

class Player:
    def __init__(self,name,is_me,is_hakem):
        self.name=name
        self.is_me=is_me
        self.is_hakem=is_hakem
        self.hand=[]
        # self.wins=None
        
    def __str__(self) -> str:
        return self.name

me = Player("mitra",True,False)
npc1 = Player("mahtab",False,False)
npc2 = Player("farhad",False,False)
npc3 = Player("hamed",False,False)
players_list=[me , npc1 , npc2, npc3]

#-----------------------------------------------------------------------------------------

class Game:
    Hakem=None
    Hokm=None

    active_suit=None
    side=None
    
    @classmethod
    def level_0(cls):
        #تعیین حاکم
        print('---------Hakem---------')
        sample_db=Card.db.copy()
        i=0
        while True:
            if i==4:
                i=0
            random_card = choice(sample_db)
            sample_db.remove(random_card)
            if random_card[1]==14:
                player = players_list[i]
                player.is_hakem = True
                Game.Hakem = player
                break
            else:
                i+=1                
        print(f'Hakem : {player}')
        
        
    @classmethod        
    def level_1(cls):
        #پخش کارت. به هر نفر 5 تا
        print(f"\n---------Primary Card Distribution---------")
        i=players_list.index(Game.Hakem)
        while True :
            if i==4:
                i=0
            player=players_list[i]
            random_card= Card.db[randint(0,len(Card.db)-1)]
            player.hand.append(random_card)
            Card.db.remove(random_card)
            i+=1
            if len(player.hand)==5 and player.is_me:
                print(f'Your hand : {player.hand}')
                
            if len(player.hand)==5: #not seen
                print(f'{player} : {player.hand}')
                
            if len(Card.db)==32 :
                break
        
        
    @classmethod
    def level_2(cls):
        #تعیین حکم
        print(f"\n---------Hokm---------")
        print(f'Hakem hand : {Game.Hakem.hand}') #not seen
        if Game.Hakem.is_me:
            Game.Hokm = input("Please pick a suit as Hokm. (♥️/♠️/♦️/♣️) : ")
        else:
            Hakem_values=[]
            for card in Game.Hakem.hand:
                suit=card[0]
                value=card[1]
                Hakem_values.append(value)
                if len(Hakem_values)==5:
                    value=max(Hakem_values)
                    # Hokm_card = Card(suit,value,True)
                    Game.Hokm=suit         
        # print(Hokm_card)        
        print(f'Hokm : {Game.Hokm}')
    
    
    @classmethod
    def level_3(cls):
        #پخش بقیه کارت ها. به هر نفر 8 تا
        print(f"\n---------Full Card Distribution---------")
        i=players_list.index(Game.Hakem)
        while True :
            if i==4:
                i=0
            player=players_list[i]
            random_card= Card.db[randint(0,len(Card.db)-1)]
            player.hand.append(random_card)
            Card.db.remove(random_card)
            i+=1
            if len(player.hand)==13 and player.is_me:
                print(f'Your hand : {player.hand}')
                
            if len(player.hand)==13: #not seen
                print(f'{player} : {player.hand}')
                
            if len(Card.db)==0 :
                break
        
    
    @classmethod
    def level_4(cls):
        #شروع راند 1
        print(f"\n---------Round 1---------")
        hakem_hand=Game.hakem.hand
        if Game.hakem==mitra :
            # hakem_card_index = int(input(f"Please input a card index(1-13).\n{hakem_hand} : "))
            # hakem_card= hakem_hand[hakem_card_index - 1]
            Game.active_suit , value = input(f"Please input a suit and value.\n{hakem_hand} : ").split()
            active_card=[Game.active_suit,int(value)]
            # hakem_hand.remove(active_card)
            for card in hakem_hand:
                if active_card == card:
                    hakem_hand.remove(card)
                    break
        else:
            random_card = hakem_hand[randint(0,len(hakem_hand)-1)]
            hakem_hand.remove(random_card)
            Game.active_suit=random_card[0]
            active_card=random_card
        
        print(active_card)    
        print(Game.active_suit)
        
        
        for i,player in enumerate(player_list):
            if player==Game.hakem :
                turn= player_list.index(player)
        #         if i==3:
        #             i==-1
        #         next_player=player_list[i+1]
        #         break
        # print(next_player)
        # random_card = 

        while turn < len(player_list):
            pass   
            


#فراخوانی ها

Game.level_0()
Game.level_1()
Game.level_2()
Game.level_3()
# Game.level_4()
# Game.level_5()
# Game.level_6()