from random import randint,choice

#ساخت دیتابیس کارت ها
cards={"Heart":[2,3,4,5,6,7,8,9,10,11,12,13,14],
           "Spade":[2,3,4,5,6,7,8,9,10,11,12,13,14],
           "Diamond":[2,3,4,5,6,7,8,9,10,11,12,13,14],
           "Club":[2,3,4,5,6,7,8,9,10,11,12,13,14]}
cards_list = []
for key,value in cards.items():
    for v in value:
        cards_list.append([key,v])

class Player:
    our_side=False
    opp_side=False
    our_score=0
    opp_score=0
    # player_hand=[]
    
    def __init__(self,num,name):
        self.num=num
        self.name=name
        self.player_hand=[]
        
    def __str__(self) -> str:
        return self.name
    
    # def __repr__(self) -> str:
    #     return self.name
        
    def give_team_score(self):
        #اگر بازیکن اول یا سوم برد یه امتیاز بریز تو متغیر امتیاز
        #ایف باید شرطش جزئی تر بشه
        if self.num==1 or self.num==3 :
            our_side=True
        
        elif self.num==2 or self.num==4 :
            opp_side=True
            
        if our_side:
            our_score+=1
            
        if opp_side:
            opp_score+=1
            
mitra= Player(1,"mitra")
mahtab= Player(2,"mahtab")
farhad= Player(3,"farhad")
hamed= Player(4,"hamed")
player_list=[mitra , mahtab , farhad , hamed]


class Game:
    cards=cards_list
    hakem=None
    
    @classmethod
    def level_0(cls):
        #تعیین حاکم
        print("---------who is Hakem?---------")
        player=1
        while True:
            if player==5:
                player=1
            
            random_card_number= randint(2,15)
            
            if random_card_number==14:
                if player==1:
                    print('You are Hakem.')
                    Game.hakem= mitra
                    break
                elif player==2:
                    print("player2 is Hakem.")
                    Game.hakem= mahtab
                    break
                elif player==3:
                    print("player 3 (your partner) is Hakem.")
                    Game.hakem= farhad
                    break
                elif player==4:
                    print("player4 is Hakem.")
                    Game.hakem= hamed
                    break
            else:
                player+=1
            
    @classmethod        
    def level_1(cls):
        #پخش کارت به هر نفر 5 تا
        #mitra
        for player in player_list:
            
            i=0
            while i < 5:
                random_card = Game.cards[randint(0,len(Game.cards))]
                player.player_hand.append(random_card)
                Game.cards.remove(random_card)
                i+=1
            print(player.player_hand)
        # print(len(Game.cards))
        
        # #mahtab
        # i=0
        # while i < 5:
        #     random_card = Game.cards[randint(0,len(Game.cards))]
        #     mahtab.player_hand.append(random_card)
        #     Game.cards.remove(random_card)
        #     i+=1
        # print(mahtab.player_hand)
        # print(len(Game.cards))
    
    def level_2(self):
        #تعیین حکم
        pass
    
    def level_3(self):
        #پخش بقیه کارت ها. به هر نفر 8 تا
        pass
    
    def level_4(self):
        #شروع راند 1
        pass
    
    
    
    
    
    
    
            
obj1=Game()

obj1.level_0()
print(obj1.hakem)
obj1.level_1()