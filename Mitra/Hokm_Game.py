#mitratsb
from random import choice,randint
from termcolor import cprint

x={"♥":[2,3,4,5,6,7,8,9,10,11,12,13,14],
           "♠":[2,3,4,5,6,7,8,9,10,11,12,13,14],
           "♦":[2,3,4,5,6,7,8,9,10,11,12,13,14],
           "♣":[2,3,4,5,6,7,8,9,10,11,12,13,14]}
all_cards = []
for key,value in x.items():
    for v in value:
        all_cards.append([key,v])

def faced_hand(hand:list):
    list1=[]
    for card in hand:
        if card[1]==11:
            card=[card[0],"J"]
            list1.append(card)
        elif card[1]==12:
            card=[card[0],"Q"]
            list1.append(card)
        elif card[1]==13:
            card=[card[0],"K"]
            list1.append(card)
        elif card[1]==14:
            card=[card[0],"Ace"]
            list1.append(card)
        else:
            list1.append(card)
    return list1

def faced_card(card:list):
    new_card=[]
    if card[1]==11:
        new_card=[card[0],"J"]
    elif card[1]==12:
        new_card=[card[0],"Q"]
    elif card[1]==13:
        new_card=[card[0],"K"]
    elif card[1]==14:
        new_card=[card[0],"Ace"]
    else:
        new_card=card
    return new_card
    
def to_value(faced_value:str):
    new_value=0
    if faced_value=="Ace":
        new_value=14
    elif faced_value=="K":
        new_value=13
    elif faced_value=="Q":
        new_value=12
    elif faced_value=="J":
        new_value=11
    else:
        new_value=faced_value
    return int(new_value)

#مرتب سازی دست ها بر اساس خال و مقدار    
def func(x):
    return x[0],x[1]

#-----------------------------------------------------------------------------------------
class Card:
    db=all_cards
    
    def __init__(self,suit,value):
        self.suit=suit
        self.value=int(value)

    def is_higher_than(self,c2,c3,c4):
        if self > c2 and self > c3 and self > c4:
            return True
    
    def __gt__(self,other):
        if self.suit == Game.Hokm and other.suit != Game.Hokm:
            return True
        elif self.suit == Game.Hokm and other.suit == Game.Hokm:
            return True if self.value > other.value else False
        elif self.suit != Game.Hokm and other.suit == Game.Hokm:
            return False
        elif self.suit != Game.Hokm and other.suit != Game.Hokm:
            if self.suit == Game.active_suit and other.suit != Game.active_suit:
                return True
            elif  self.suit == Game.active_suit and other.suit == Game.active_suit:
                return self.value > other.value
            elif  self.suit != Game.active_suit and other.suit == Game.active_suit:
                return False
            elif  self.suit != Game.active_suit and other.suit != Game.active_suit:
                return True

#-----------------------------------------------------------------------------------------
class Player:
    #امتیاز یک زمین
    our_team_score=0
    opp_team_score=0
    
    #امتیاز یک دست
    our_team_handwins=0
    opp_team_handwins=0
    
    def __init__(self, name, is_me):
        self.name=name
        self.is_me=is_me
        self.hand=[]
    
    def __repr__(self):
        return self.name

#اسامی متغیر و رندوم
my_name= input("Hello, Enter your name please: ")

names= ["Mohammad","Sara","Delaram","Ali","Iman","Negar","Peyman","Leila","Farhad","Hamed","Shabnam","Saeed","Mahtab"]
name1, name2, name3= choice(names), choice(names), choice(names)
me = Player(my_name ,True)
npc1 = Player(name1 ,False)
npc2 = Player(name2 ,False)
npc3 = Player(name3 ,False)
players_list=[me , npc1 , npc2, npc3]

#-----------------------------------------------------------------------------------------
class Game:
    sample_db = None
    Hakem = None
    Hokm = None
    active_suit = None
    winner = None
    hand = 1
    
    @classmethod
    def level_0(cls):
        #تعیین حاکم
        cprint('-------Hakem-------' , "green")
        Game.sample_db = Card.db.copy()
        i=0
        while True:
            if i==4:
                i=0
            random_card = choice(Game.sample_db)
            Game.sample_db.remove(random_card)
            if random_card[1]==14:
                player = players_list[i]
                Game.Hakem = player
                break
            else:
                i+=1                 
               
        cprint(f'Hakem : {player}' , attrs=["bold"])
        
        
    @classmethod        
    def level_1(cls):
        #پخش کارت. به هر نفر 5 تا
        cprint(f'\n--------------------------------------- Hand {Game.hand} -----------------------------------------' , "light_magenta")
        if Game.hand != 1:
            cprint(f'Hakem : {Game.Hakem}' , attrs=["bold"])
        
        cprint(f"\n---Primary Card Distribution---" , "green")
        i=players_list.index(Game.Hakem)
        Game.sample_db = Card.db.copy()
        while True :
            if i==4:
                i=0
            player=players_list[i]
            random_card= Game.sample_db[randint(0,len(Game.sample_db)-1)]
            player.hand.append(random_card)
            Game.sample_db.remove(random_card)
            i+=1
            if len(player.hand)==5 and player.is_me: 
                player.hand.sort(key=func)
                print("Your hand:", *faced_hand(player.hand))
                
            # if len(player.hand)==5 and player==Game.Hakem: #not seen
            #     player.hand.sort(key=func)
            #     print(player , ":" ,*faced_hand(player.hand))
                
            if len(Game.sample_db)==32 :
                break
        
    @classmethod
    def level_2(cls):
        #تعیین حکم
        cprint(f"\n-------Hokm-------" , "green")
        # print(f'Hakem hand : {Game.Hakem.hand}') #not seen
        suits_list= ['♥','♦','♣','♠']
        if Game.Hakem.is_me:
            while True:
                Game.Hokm = input("Please pick a suit as Hokm. (♥️/♠️/♦️/♣️) : ")
                if Game.Hokm not in suits_list:
                    cprint(f"Your input must be a suit shape -> (♥️/♠️/♦️/♣️). input again.\n", "light_yellow")
                else:
                    break
        else:
            Hakem_values=[]
            for card in Game.Hakem.hand:
                Hakem_values.append(card[1])
            max_value=max(Hakem_values)
            
            #اگر دوتا کارت ماکسیموم داشتیم اون خالی که کارت های بیشتری داره حکم باشه
            #اگر تعدادشون هم یکی بود اون خالی که مجموعا کارت های بزرگتری داره حکم باشه
            if Hakem_values.count(max_value)==2:
                temp1=[card for card in Game.Hakem.hand if card[1]==max_value]
                suits1=[card for card in Game.Hakem.hand if card[0]==temp1[0][0]]
                suits2=[card for card in Game.Hakem.hand if card[0]==temp1[1][0]]
                suits1_values=[card[1] for card in Game.Hakem.hand if card[0]==temp1[0][0]]
                suits2_values=[card[1] for card in Game.Hakem.hand if card[0]==temp1[1][0]]
                suits1_sum_values=sum(suits1_values)
                suits2_sum_values=sum(suits2_values)
                if len(suits1) == len(suits2):
                    if suits1_sum_values >= suits2_sum_values:
                        Game.Hokm= temp1[0][0]
                    else:
                        Game.Hokm= temp1[1][0]
                elif len(suits1) < len(suits2):
                    Game.Hokm= temp1[1][0]
                else:
                    Game.Hokm= temp1[0][0]    
            else:
                for card in Game.Hakem.hand:
                    if card[1]==max_value:
                        Game.Hokm= card[0] 
        print(f'Hokm : {Game.Hokm}')
    
    @classmethod
    def level_3(cls):
        #پخش بقیه کارت ها. به هر نفر 8 تا
        # cprint(f"\n---Full Card Distribution---" , "green")
        i=players_list.index(Game.Hakem)
        while True :
            if i==4:
                i=0
            player=players_list[i]
            random_card= Game.sample_db[randint(0,len(Game.sample_db)-1)]
            player.hand.append(random_card)
            Game.sample_db.remove(random_card)
            i+=1    
            if len(Game.sample_db)==0 :
                break
        
    @classmethod
    def level_4(cls):
        #هفت راند از 1 بازی
        round=1
        ground_winner = Game.Hakem
        gone_cards=[]
        while True: 
            cprint(f"\n------------------- Hand {Game.hand} ----- Round {round} ----- Hokm : {Game.Hokm} -------------------" , "cyan")
            #players moves orders - (round1 starting from Hakem, next rounds starting from ground_winner) 
            if round==1:
                #بازی باید از حاکم شروع شود
                i=players_list.index(Game.Hakem)
            else:
                #بازی باید از برنده ی راند قبلی شروع شود
                i=players_list.index(ground_winner)
            if i==0:
                players_order = players_list.copy()
            else:
                players_list_sample = players_list.copy()
                players_order=[]
                while True:
                    if i<len(players_list_sample):
                        player=players_list_sample.pop(i)
                        players_order.append(player)
                    elif len(players_list_sample)!=0:
                        player=players_list_sample.pop(0)
                        players_order.append(player)
                    else:
                        break
                
                players_list_sample= players_list.copy()    
            print("Order of play is :", players_order[0],"->",players_order[1],"->",players_order[2],"->",players_order[3],f'\n')   
            # players_order[0].hand.sort(key=func)
            # players_order[1].hand.sort(key=func)
            # players_order[2].hand.sort(key=func)
            # players_order[3].hand.sort(key=func)
            # print(players_order[0], *faced_hand(players_order[0].hand))
            # print(players_order[1], *faced_hand(players_order[1].hand))
            # print(players_order[2], *faced_hand(players_order[2].hand))
            # print(players_order[3], *faced_hand(players_order[3].hand), f'\n')
            me.hand.sort(key=func)
            print("Your hand:", *faced_hand(me.hand), f"\n")
            
            ground=[]
            card_objects=[]
            player_number=1
            
            while player_number <= 4:
                current_player = players_order[player_number-1]
                
                c_actives= [c for c in current_player.hand if c[0]==Game.active_suit]
                c_actives_v= [c[1] for c in c_actives]
                if len(c_actives)!=0:
                    max_active_card= [c for c in c_actives if c[1]==max(c_actives_v)][0]
                    min_active_card= [c for c in c_actives if c[1]==min(c_actives_v)][0]
                c_hokms= [c for c in current_player.hand if c[0]==Game.Hokm]
                c_hokms_v= [c[1] for c in c_hokms]
                if len(c_hokms)!=0:
                    min_hokm_card= [c for c in c_hokms if c[1]==min(c_hokms_v)][0]
                c_rads= [c for c in current_player.hand if c[0]!=Game.active_suit and c[0]!=Game.Hokm]
                c_rads_v= [c[1] for c in c_rads]
                if len(c_rads)!=0:
                    min_rad_card=[c for c in c_rads if c[1]==min(c_rads_v)][0]
                
                if current_player.is_me :
                    while True:
                        suit , faced_value = input(f"{me} : ").split()
                        value= to_value(faced_value)
                        card = [suit, value]
                        if player_number==1:
                            Game.active_suit = suit
                        #اگر خال اکتیو داری و کارت دیگه ای آوردی برای کارت های نفر غیر اول
                        if len(c_actives)!=0 and (card in me.hand) and (card not in c_actives) and player_number != 1:
                            cprint('Your card must be an active suit. input again.' , "light_yellow")
                        elif card in me.hand:
                            me.hand.remove(card)
                            break
                        elif card in Card.db:
                            cprint("You don't have this card. input again.", "light_yellow")
                        else:
                            cprint("Your input is not a correct card format. input again.", "light_yellow")
                    
                else:
                    if player_number==1:
                        Aces= [c for c in current_player.hand if c[1]==14 and c[0]!=Game.Hokm ]
                        if len(Aces)!=0:
                            card= Aces[0]
                        else:
                            card = current_player.hand[randint(0,len(current_player.hand)-1)]
                        Game.active_suit = card[0]
                    
                    if player_number==2:
                        #خال اکتیو بالاتر بیار
                        if len(c_actives)!=0:
                            if max_active_card[1] > ground[0][1]:
                                card= max_active_card
                            else:
                                card= min_active_card
                        else:
                            #خال اکتیو نداری. با کمترین حکم ببر
                            if len(c_hokms)!=0:
                                card= min_hokm_card
                            else:
                                #حکم نداری. با مقدار کم رد کن
                                card= min_rad_card
                    
                    if player_number==3:
                        def smart(partner_card , my_hand , gone_cards):
                            suit=partner_card[0]
                            value=partner_card[1]
                            if value==14 :
                                return True
                            elif value==13 and ([suit,14] in my_hand or gone_cards):
                                return True
                            elif value==12 and (([suit,13]and[suit,14]) in my_hand or gone_cards) or ([suit,13] in my_hand and [suit,14] in gone_cards) or ([suit,14] in my_hand and [suit,13] in gone_cards):
                                return True
                        
                        #دو حالت خاص
                        #یارت تک مجاز آورده. پایین ترین خال مجازت رو بیار
                        #یارت شاه اورده و تک اون خال دست توعه یا بازی شده. پایین ترین خال مجازت رو بیار
                        
                        if card_p1 > card_p2 and smart(ground[0] , current_player.hand, gone_cards):
                            if len(c_actives)!=0:
                                card= min_active_card
                            else:
                                #خال مجاز نداری. یه کارت پایین رد کن
                                if len(c_rads)!=0:
                                    card= min_rad_card
                                else:
                                    #فقط حکم داری. پایین بنداز
                                    card= min_hokm_card
                            
                        else:
                            #بالاترین خال مجازت رو بیار
                            if len(c_actives)!=0:
                                if max_active_card[1] > ground[0][1] and max_active_card[1] > ground[1][1]:
                                    #خال مجاز بالاتر از بازیکن اول و دوم داری. بیارش
                                    card= max_active_card
                                else:
                                    #پایین ترین خال مجاز رو بیار
                                    card= min_active_card
                            else:
                                #خال مجاز نداری
                                if ground[1][0]==Game.Hokm :
                                    #بازیکن دوم با حکم بریده. حکم بالاتر از اون بیار
                                    c_hokms_higher=[c for c in c_hokms if c[1]>ground[1][1]]
                                    c_hokms_higher_v=[c[1] for c in c_hokms_higher]
                                    if len(c_hokms_higher)!=0:
                                        #حکم بالاتر از بازیکن دوم داریم. کمترینش رو میاریم
                                        min_card=[c for c in c_hokms_higher if c[1]==min(c_hokms_higher_v)][0]
                                        card= min_card
                                    else:
                                        #حکم پایین تر داری و نمیخواد. پایین رد کن
                                        if len(c_rads)!=0:
                                            card= min_rad_card
                                        else:
                                            #فقط حکم پایین تر داری. کمترینش رو بیار
                                            card= min_hokm_card
                                else:
                                    #با کمترین حکم ببر
                                    if len(c_hokms)!=0:
                                        card= min_hokm_card
                                    else:
                                        #حکم نداری. با مقدار کم رد کن
                                        card= min_rad_card
                    
                    if player_number==4:
                        if card_p2 > card_p1 and card_p3:
                            #یارت کارتش بالاست. خال اکتیو پایین بیار
                            if len(c_actives)!=0:
                                card= min_active_card
                            else:
                                #خال اکتیو نداری. پایین رد کن
                                if len(c_rads)!=0:
                                    card= min_rad_card
                                else:
                                    #فقط حکم داری. پایین بنداز
                                    card= min_hokm_card
                        
                        else:
                            #یارت کارتش بالا نیست. تو باید کارت بالای بازیکن برنده حریف بیاری
                            if card_p3 > card_p1:
                                #کارت بالای بازیکن سوم بیار
                                if ground[2][0]==Game.active_suit:
                                    c_actives_higher=[c for c in c_actives if c[1]>ground[2][1]]
                                    c_actives_higher_v=[c[1] for c in c_actives_higher]
                                    if len(c_actives_higher)!=0:
                                        #خال مجاز بالاتر داری. کمترین بنداز
                                        min_card= [c for c in c_actives_higher if c[1]==min(c_actives_higher_v)][0]
                                        card= min_card
                                    else:
                                        #خال مجاز پایین و کمترین بنداز
                                        if len(c_actives)!=0:
                                            card= min_active_card
                                        else:
                                            #خال مجاز نداری. پایین رد کن
                                            if len(c_rads)!=0:
                                                card= min_rad_card
                                            else:
                                                #فقط حکم داری. پایین بنداز
                                                card= min_hokm_card
                                
                                elif ground[2][0]==Game.Hokm:   
                                    if len(c_actives)!=0:
                                        card= min_active_card   
                                    else:
                                        c_hokms_higher=[c for c in c_hokms if card[1]>ground[2][1]]
                                        c_hokms_higher_v=[c[1] for c in c_hokms_higher]
                                        if len(c_hokms_higher)!=0:
                                            #حکم بالاتر از بازیکن سوم داریم. کمترینش رو میاریم
                                            min_card=[c for c in c_hokms_higher if c[1]==min(c_hokms_higher_v)][0]
                                            card= min_card
                                        else:
                                            #حکم پایین تر داری و نمیخواد. پایین رد کن
                                            if len(c_rads)!=0:
                                                card= min_rad_card
                                            else:
                                                #فقط حکم پایین تر داری. کمترینش رو بیار
                                                card= min_hokm_card
                                
                            elif card_p1 > card_p3:
                                #کارت بالای بازیکن اول بیار
                                #خال مجاز بالاتر بیار
                                c_actives_higher=[c for c in c_actives if c[1]>ground[0][1]]
                                c_actives_higher_v=[c[1] for c in c_actives_higher]
                                if len(c_actives_higher)!=0:
                                    #خال مجاز بالاتر داری. کمترین بنداز
                                    min_card= [c for c in c_actives_higher if c[1]==min(c_actives_higher_v)][0]
                                    card= min_card
                                else:
                                    #خال مجاز پایین و کمترین بنداز
                                    if len(c_actives)!=0:
                                        card= min_active_card
                                    else:
                                        #خال مجاز نداری. با حکم پایین ببر
                                        if len(c_hokms)!=0:
                                            card= min_hokm_card
                                        else:
                                            #حکم نداری. با مقدار کم رد کن
                                            card= min_rad_card
                            
                    current_player.hand.remove(card)
                    print(current_player , ":" , *faced_card(card))
                
                ground.append(card)
                gone_cards.append(card)
                card_p=Card(card[0],card[1])
                card_objects.append(card_p)
                
                if len(card_objects)==2:
                    card_p1=card_objects[0]
                    card_p2=card_objects[1]
                elif len(card_objects)==3:
                    card_p3=card_objects[2]
                elif len(card_objects)==4:
                    card_p4=card_objects[3]
                    
                player_number += 1
                #پایان زمین
            
            print(f"\n------ Result ------")
        
            #امتیاز گیری آخر زمین
            if card_p1.is_higher_than(card_p2 , card_p3 , card_p4):
                ground_winner=players_order[0]
            elif card_p2.is_higher_than(card_p1 , card_p3 , card_p4):
                ground_winner=players_order[1]
            elif card_p3.is_higher_than(card_p1 , card_p2 , card_p4):
                ground_winner=players_order[2]
            elif card_p4.is_higher_than(card_p1 , card_p2 , card_p3):
                ground_winner=players_order[3]
            print(f'The ground winner is : {ground_winner}')
            #پایان این راند
            round += 1
            
            if ground_winner.is_me or ground_winner==npc2 :
                #امتیاز زمین برای تیم ما
                Player.our_team_score += 1
            else:
                #امتیاز زمین برای تیم حریف
                Player.opp_team_score += 1
            print(f'Our team score : {Player.our_team_score} \nOpp team score : {Player.opp_team_score}')
            
            
            #امتیاز یک دست
            if Player.our_team_score == 7:
                if Player.opp_team_score == 0 and (me==Game.Hakem or npc2==Game.Hakem):
                    #تیم مقابل کت شده
                    Player.our_team_handwins += 3
                elif Player.opp_team_score == 0:
                    #تیم مقابل حاکم کت شده
                    Player.our_team_handwins += 2
                else:
                    #کت نشده و حالت عادیه
                    Player.our_team_handwins += 1
    
                cprint(f'\nOur team hand wins : {Player.our_team_handwins}' , attrs=["bold"])
                cprint(f'Opp team hand wins : {Player.opp_team_handwins}' , attrs=["bold"])
                
                #امتیاز کل بازی
                if Player.our_team_handwins >= 7:
                    Game.winner= (f'Our Team -> {me} & {npc2}')
                    cprint(f"\n--------♥️♠️♦️♣️-------End of Game-------♥️♠️♦️♣️-------" , "light_red")
                    cprint(f'The Game Winner : {Game.winner}' , "light_green" , attrs=["bold"] )
                    cprint(f'\nGreat job {me}!\nThanks for playing this game.\nhope to see you again:)\n')
                    break
                elif Player.opp_team_handwins >= 7:
                    Game.winner= (f'Opponent Team -> {npc1} & {npc3}')
                    cprint(f"\n--------♥️♠️♦️♣️-------End of Game-------♥️♠️♦️♣️-------" , "light_red")
                    cprint(f'The Game Winner : {Game.winner}\n' , "light_green" , attrs=["bold"])
                    break
                
                Player.our_team_score , Player.opp_team_score = 0, 0
                #دست ها رو خالی کن
                for p in players_order:
                    p.hand.clear()
                    
                #لیست کارت های بازی شده رو هم خالی کن
                gone_cards.clear()

                if Game.Hakem==npc1:
                    Game.Hakem= npc2
                elif Game.Hakem==npc3:
                    Game.Hakem= me
                
                Game.hand += 1 
                round=1   
                Game.level_1() #پخش 5 کارت شروع از حاکم
                Game.level_2() #تعیین حکم
                Game.level_3() #پخش کل کارت ها
                
                
            elif Player.opp_team_score == 7:
                if Player.our_team_score == 0 and (npc1==Game.Hakem or npc3==Game.Hakem):
                    #تیم مقابل کت شده
                    Player.opp_team_handwins += 3
                elif Player.our_team_score == 0:
                    #تیم مقابل حاکم کت شده
                    Player.opp_team_handwins += 2
                else:
                    #کت نشده و حالت عادیه
                    Player.opp_team_handwins += 1
                    
                cprint(f'\nOur team hand wins : {Player.our_team_handwins}' , attrs=["bold"])
                cprint(f'Opp team hand wins : {Player.opp_team_handwins}', attrs=["bold"])
                
                #امتیاز کل بازی
                if Player.our_team_handwins >= 7:
                    Game.winner= (f'Our Team -> {me} & {npc2}')
                    cprint(f"\n--------♥️♠️♦️♣️-------End of Game-------♥️♠️♦️♣️-------" , "light_red")
                    cprint(f'The Game Winner : {Game.winner}' , "light_green" , attrs=["bold"] )
                    cprint(f'\nGreat job {me}!\nThanks for playing this game.\nhope to see you again:)\n')
                    break
                elif Player.opp_team_handwins >= 7:
                    Game.winner= (f'Opponent Team -> {npc1} & {npc3}')
                    cprint(f"\n--------♥️♠️♦️♣️-------End of Game-------♥️♠️♦️♣️-------" , "light_red")
                    cprint(f'The Game Winner : {Game.winner}\n' , "light_green")
                    break
                
                Player.our_team_score , Player.opp_team_score = 0, 0
                for p in players_order:
                    p.hand.clear()
                    
                gone_cards.clear()
                
                if Game.Hakem==me:
                    Game.Hakem= npc1
                elif Game.Hakem==npc2:
                    Game.Hakem= npc3
                
                Game.hand += 1
                round=1    
                Game.level_1() #پخش 5 کارت شروع از حاکم
                Game.level_2() #تعیین حکم
                Game.level_3() #پخش کل کارت ها
                
cprint(f'\n"Good day {my_name}. Welcome to Hokm Game." (Designed by mitratsb)' , "light_cyan" , attrs=["bold"])
print('Pay attention please, in order to input a card in any level, you must type a suit shape and value with space.')
print(f'Keyboard suit shapes -> (♥ : ctrl+3) (♦ : ctrl+4) (♣ : ctrl+5) (♠ : ctrl+6)\n')

Game.level_0()
Game.level_1()
Game.level_2()
Game.level_3()
Game.level_4()

#این فایل اصلی برنامه است
#در این فایل فقط دست خود بازی کننده دیده میشود
#هفت زمین برای گرفتن یک دست و هفت دست برای برد بازی لازم است طبق استاندارد بازی
#نام بازیکنان در هر اجرا متفاوت است و رندوم یارگیری میشود
