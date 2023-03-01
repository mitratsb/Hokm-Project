#mitratsb
from random import choice,randint

x={"♥":[2,3,4,5,6,7,8,9,10,11,12,13,14],
           "♠":[2,3,4,5,6,7,8,9,10,11,12,13,14],
           "♦":[2,3,4,5,6,7,8,9,10,11,12,13,14],
           "♣":[2,3,4,5,6,7,8,9,10,11,12,13,14]}
all_cards = []
for key,value in x.items():
    for v in value:
        all_cards.append([key,v])

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
    
    def __init__(self, name, is_me, is_hakem, wins):
        self.name=name
        self.is_me=is_me
        self.is_hakem=is_hakem
        self.wins=wins
        self.hand=[]
    
    def __repr__(self):
        return self.name

me = Player("Mitra",True,False,0)
npc1 = Player("Mahtab",False,False,0)
npc2 = Player("Farhad",False,False,0)
npc3 = Player("Hamed",False,False,0)
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
        print('-------Hakem-------')
        Game.sample_db = Card.db.copy()
        i=0
        while True:
            if i==4:
                i=0
            random_card = choice(Game.sample_db)
            Game.sample_db.remove(random_card)
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
        print(f'\n--------------------------------------- hand {Game.hand} -----------------------------------------')
        print(f'Hakem : {Game.Hakem}')
        
        print(f"\n---Primary Card Distribution---")
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
            # if len(player.hand)==5 and player.is_me: #انتهای کد از کامنت در بیاد
            #     print(f'Your hand : {player.hand}')
                
            if len(player.hand)==5: #not seen
                player.hand.sort(key=func)
                print(f'{player} : {player.hand}')
                
            if len(Game.sample_db)==32 :
                break
        
        
    @classmethod
    def level_2(cls):
        #تعیین حکم
        print(f"\n-------Hokm-------")
        print(f'Hakem hand : {Game.Hakem.hand}') #not seen
        if Game.Hakem.is_me:
            Game.Hokm = input("Please pick a suit as Hokm. (♥️/♠️/♦️/♣️) : ")
            suits_list= ['♥','♦','♣','♠']
            if Game.Hokm not in suits_list:
                raise Exception("Your input must be a suit shape -> (♥️/♠️/♦️/♣️)")
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
        print(f"\n---Full Card Distribution---")
        i=players_list.index(Game.Hakem)
        while True :
            if i==4:
                i=0
            player=players_list[i]
            random_card= Game.sample_db[randint(0,len(Game.sample_db)-1)]
            player.hand.append(random_card)
            Game.sample_db.remove(random_card)
            i+=1
            # if len(player.hand)==13 and player.is_me: #انتهای کد از کامنت در بیاد
            #     player.hand.sort(key=func)
            #     print(f'Your hand : {player.hand}')
                
            if len(player.hand)==13: #not seen
                player.hand.sort(key=func)
                print(f'{player} : {player.hand}')
                
            if len(Game.sample_db)==0 :
                break
        
    
    @classmethod
    def level_4(cls):
        #هفت راند از 1 بازی
        round=1
        ground_winner = Game.Hakem
        gone_cards=[]
        while True: 
            print(f"\n------------------- hand {Game.hand} ----- Round {round} ----- Hokm : {Game.Hokm} -------------------")
            #players moves orders - (round1 starting from Hakem, next rounds starting from ground_winner) 
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
            print(f'Order of play is : {players_order}\n')
            print(f'{players_order[0]} : {players_order[0].hand} \n{players_order[1]} : {players_order[1].hand} \n{players_order[2]} : {players_order[2].hand} \n{players_order[3]} : {players_order[3].hand}\n')
            print(f'Your hand: {me.hand}\n')
            ground=[]
            
            
            
            
            #play card1 by player1 (Hakem)
            current_player = players_order[0]
            if current_player.is_me :
                Game.active_suit , value = input(f"{me} : ").split()
                card1 = [Game.active_suit,int(value)]
                #روش دوم این است که با انتخاب شماره ی کارت ورودی بدهیم
                # card_index = int(input(f"Please input a card index.(1-{len(current_player.hand)}) \n{current_player.hand} : "))
                # card1 = current_player.hand[card_index - 1]
                # Game.active_suit = card1[0]
                if card1 in me.hand:
                    me.hand.remove(card1)
                elif card1 in Card.db:
                    raise Exception("You don't have this card.")
                else:
                    raise Exception("Your input is not a correct card format.")
                
            else:
                Aces= [card for card in current_player.hand if card[1]==14 and card[0]!=Game.Hokm ]
                if len(Aces)!=0:
                    card1= Aces[0]
                else:
                    card1 = current_player.hand[randint(0,len(current_player.hand)-1)]
                    
                current_player.hand.remove(card1)
                Game.active_suit = card1[0]
                print(current_player , ":" , *card1)
                
            card_p1=Card(card1[0],card1[1])
            ground.append(card1)
            gone_cards.append(card1)
            
                
                
            #play card2 by player2
            current_player = players_order[1]
            c_actives= [card for card in current_player.hand if card[0]==Game.active_suit]
            c_actives_v= [card[1] for card in c_actives]
            c_hokms= [card for card in current_player.hand if card[0]==Game.Hokm]
            c_hokms_v= [card[1] for card in c_hokms]
            c_rads= [card for card in current_player.hand if card[0]!=Game.active_suit and card[0]!=Game.Hokm]
            c_rads_v= [card[1] for card in c_rads]
            
            if current_player.is_me :
                suit , value = input(f"{me} : ").split()
                card2 = [suit,int(value)]
                #اگر خال اکتیو داری و کارت دیگه ای آوردی
                if len(c_actives)!=0 and (card2 in me.hand) and (card2 not in c_actives):
                    raise Exception('Your card must be an active suit')
                else:
                    if card2 in me.hand:
                        me.hand.remove(card2)
                    elif card2 in Card.db:
                        raise Exception("You don't have this card.")
                    else:
                        raise Exception("Your input is not a correct card format.")
                
            else:
                #خال اکتیو بالاتر بیار
                if len(c_actives)!=0:
                    max_card= [card for card in c_actives if card[1]==max(c_actives_v)][0]
                    min_card= [card for card in c_actives if card[1]==min(c_actives_v)][0]
                    if max_card[1] > card1[1]:
                        card2= max_card
                    else:
                        card2= min_card
            
                else:
                    #خال اکتیو نداری. با کمترین حکم ببر
                    if len(c_hokms)!=0:
                        min_card= [card for card in c_hokms if card[1]==min(c_hokms_v)][0]
                        card2= min_card
                    else:
                        #حکم نداری. با مقدار کم رد کن
                        min_card= [card for card in c_rads if card[1]==min(c_rads_v)][0]
                        card2= min_card
                
                current_player.hand.remove(card2)
                print(current_player , ":" , *card2)
            card_p2=Card(card2[0],card2[1])
            ground.append(card2)
            gone_cards.append(card2)
            
            
            #play card3 by player3
            current_player = players_order[2]
            c_actives= [card for card in current_player.hand if card[0]==Game.active_suit]
            c_actives_v= [card[1] for card in c_actives]
            c_hokms= [card for card in current_player.hand if card[0]==Game.Hokm]
            c_hokms_v= [card[1] for card in c_hokms]
            c_rads= [card for card in current_player.hand if card[0]!=Game.active_suit and card[0]!=Game.Hokm]
            c_rads_v= [card[1] for card in c_rads]
            
            if current_player.is_me :
                suit , value = input(f"{me} : ").split()
                card3 = [suit,int(value)]
                #اگر خال اکتیو داری و کارت دیگه ای آوردی
                if len(c_actives)!=0 and (card3 in me.hand) and (card3 not in c_actives):
                    raise Exception('Your card must be an active suit')
                else:
                    if card3 in me.hand:
                        me.hand.remove(card3)
                    elif card3 in Card.db:
                        raise Exception("You don't have this card.")
                    else:
                        raise Exception("Your input is not a correct card format.")
                    
            else:
                if card_p1 > card_p2 and card1[1]==14:
                    #یک حالت خاص
                    #یارت تک مجاز آورده. پایین ترین خال مجازت رو بیار
                    if len(c_actives)!=0:
                        min_card=[card for card in c_actives if card[1]==min(c_actives_v)][0]
                        card3= min_card
                    else:
                        #خال مجاز نداری. یه کارت پایین رد کن
                        min_card=[card for card in c_rads if card[1]==min(c_rads_v)][0]
                        card3= min_card
                else:
                    #بالاترین خال مجازت رو بیار
                    if len(c_actives)!=0:
                        max_card= [card for card in c_actives if card[1]==max(c_actives_v)][0]
                        min_card= [card for card in c_actives if card[1]==min(c_actives_v)][0]
                        if max_card[1] > card1[1] and max_card[1] > card2[1]:
                            #خال مجاز بالاتر از بازیکن اول و دوم داری. بیارش
                            card3= max_card
                        else:
                            #پایین ترین خال مجاز رو بیار
                            card3= min_card
                        
                    else:
                        #خال مجاز نداری
                        if card2[0]==Game.Hokm :
                            #بازیکن دوم با حکم بریده. حکم بالاتر از اون بیار
                            c_hokms_higher=[card for card in c_hokms if card[1]>card2[1]]
                            c_hokms_higher_v=[card[1] for card in c_hokms_higher]
                            if len(c_hokms_higher)!=0:
                                #حکم بالاتر از بازیکن دوم داریم. کمترینش رو میاریم
                                min_card=[card for card in c_hokms_higher if card[1]==min(c_hokms_higher_v)][0]
                                card3= min_card
                            else:
                                #حکم پایین تر داری و نمیخواد. پایین رد کن
                                if len(c_rads)!=0:
                                    min_card= [card for card in c_rads if card[1]==min(c_rads_v)][0]
                                    card3= min_card
                                else:
                                    #فقط حکم پایین تر داری. کمترینش رو بیار
                                    min_card= [card for card in c_hokms if card[1]==min(c_hokms_v)][0]
                                    card3= min_card
                        else:
                            #با کمترین حکم ببر
                            if len(c_hokms)!=0:
                                min_card= [card for card in c_hokms if card[1]==min(c_hokms_v)][0]
                                card3= min_card
                            else:
                                #حکم نداری. با مقدار کم رد کن
                                min_card=[card for card in c_rads if card[1]==min(c_rads_v)][0]
                                card3= min_card
                            
                current_player.hand.remove(card3)
                print(current_player , ":" , *card3)
            card_p3=Card(card3[0],card3[1])
            ground.append(card3)
            gone_cards.append(card3)
            

            #play card4 by player4
            current_player = players_order[3]
            c_actives= [card for card in current_player.hand if card[0]==Game.active_suit]
            c_actives_v= [card[1] for card in c_actives]
            c_hokms= [card for card in current_player.hand if card[0]==Game.Hokm]
            c_hokms_v= [card[1] for card in c_hokms]
            c_rads= [card for card in current_player.hand if card[0]!=Game.active_suit and card[0]!=Game.Hokm]
            c_rads_v= [card[1] for card in c_rads]
            
            if current_player.is_me :
                suit , value = input(f"{me} : ").split()
                card4 = [suit,int(value)]
                #اگر خال اکتیو داری و کارت دیگه ای آوردی
                if len(c_actives)!=0 and (card4 in me.hand) and (card4 not in c_actives):
                    raise Exception('Your card must be an active suit')
                else:
                    if card4 in me.hand:
                        me.hand.remove(card4)
                    elif card4 in Card.db:
                        raise Exception("You don't have this card.")
                    else:
                        raise Exception("Your input is not a correct card format.")
            
            else:
                if card_p2 > card_p1 and card_p2 > card_p3:
                    #یارت کارتش بالاست. خال اکتیو پایین بیار
                    if len(c_actives)!=0:
                        min_card=[card for card in c_actives if card[1]==min(c_actives_v)][0]
                        card4= min_card
                    else:
                        #خال اکتیو نداری. پایین رد کن
                        if len(c_rads)!=0:
                            min_card=[card for card in c_rads if card[1]==min(c_rads_v)][0]
                            card4= min_card
                        else:
                            #فقط حکم داری. پایین بنداز
                            min_card= [card for card in c_hokms if card[1]==min(c_hokms_v)][0]
                            card4= min_card
                    
                else:
                    #یارت کارتش بالا نیست. تو باید کارت بالای بازیکن برنده حریف بیاری
                    if card_p3 > card_p1:
                        #کارت بالای بازیکن سوم بیار
                        if card3[0]==Game.active_suit:
                            c_actives_higher=[card for card in c_actives if card[1]>card3[1]]
                            c_actives_higher_v=[card[1] for card in c_actives_higher]
                            if len(c_actives_higher)!=0:
                                #خال مجاز بالاتر داری. کمترین بنداز
                                min_card= [card for card in c_actives_higher if card[1]==min(c_actives_higher_v)][0]
                                card4= min_card
                            else:
                                #خال مجاز پایین و کمترین بنداز
                                if len(c_actives)!=0:
                                    min_card= [card for card in c_actives if card[1]==min(c_actives_v)][0]
                                    card4= min_card
                                else:
                                    #خال مجاز نداری. پایین رد کن
                                    if len(c_rads)!=0:
                                        min_card=[card for card in c_rads if card[1]==min(c_rads_v)][0]
                                        card4= min_card
                                    else:
                                        #فقط حکم داری. پایین بنداز
                                        min_card= [card for card in c_hokms if card[1]==min(c_hokms_v)][0]
                                        card4= min_card
                        
                        elif card3[0]==Game.Hokm:   
                            if len(c_actives)!=0:
                                min_card= [card for card in c_actives if card[1]==min(c_actives_v)][0]
                                card4= min_card   
                            else:
                                c_hokms_higher=[card for card in c_hokms if card[1]>card3[1]]
                                c_hokms_higher_v=[card[1] for card in c_hokms_higher]
                                if len(c_hokms_higher)!=0:
                                    #حکم بالاتر از بازیکن سوم داریم. کمترینش رو میاریم
                                    min_card=[card for card in c_hokms_higher if card[1]==min(c_hokms_higher_v)][0]
                                    card4= min_card
                                else:
                                    #حکم پایین تر داری و نمیخواد. پایین رد کن
                                    if len(c_rads)!=0:
                                        min_card= [card for card in c_rads if card[1]==min(c_rads_v)][0]
                                        card4= min_card
                                    else:
                                        #فقط حکم پایین تر داری. کمترینش رو بیار
                                        min_card= [card for card in c_hokms if card[1]==min(c_hokms_v)][0]
                                        card4= min_card
                        
                    elif card_p1 > card_p3:
                        #کارت بالای بازیکن اول بیار
                        #خال مجاز بالاتر بیار
                        c_actives_higher=[card for card in c_actives if card[1]>card1[1]]
                        c_actives_higher_v=[card[1] for card in c_actives_higher]
                        if len(c_actives_higher)!=0:
                            #خال مجاز بالاتر داری. کمترین بنداز
                            min_card= [card for card in c_actives_higher if card[1]==min(c_actives_higher_v)][0]
                            card4= min_card
                        else:
                            #خال مجاز پایین و کمترین بنداز
                            if len(c_actives)!=0:
                                min_card= [card for card in c_actives if card[1]==min(c_actives_v)][0]
                                card4= min_card
                            else:
                                #خال مجاز نداری. با حکم پایین ببر
                                if len(c_hokms)!=0:
                                    min_card= [card for card in c_hokms if card[1]==min(c_hokms_v)][0]
                                    card4= min_card
                                else:
                                    #حکم نداری. با مقدار کم رد کن
                                    min_card=[card for card in c_rads if card[1]==min(c_rads_v)][0]
                                    card4= min_card
                     
                current_player.hand.remove(card4)
                print(current_player , ":" , *card4)
            card_p4=Card(card4[0],card4[1])
            ground.append(card4)
            gone_cards.append(card4)
            
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
            print(f'Our team score : {Player.our_team_score} \nOpp team score : {Player.opp_team_score}\n')
            
            
            #امتیاز یک دست
            if Player.our_team_score == 7:
                Player.our_team_handwins += 1
                print(f'Our team hand wins : {Player.our_team_handwins}')
                print(f'Opp team hand wins : {Player.opp_team_handwins}\n')
                
                #امتیاز کل بازی
                if Player.our_team_handwins == 3:
                    Game.winner= (f'Our Team -> {me} & {npc2}')
                    print("--------♥️♠️♦️♣️-------End of Game-------♥️♠️♦️♣️-------")
                    print(f'The Game Winner : {Game.winner}\nGreat job {me}!\nThanks for playing this game.\nhope to see you again:)')
                    break
                elif Player.opp_team_handwins == 3:
                    Game.winner= (f'Opponent Team -> {npc1} & {npc3}')
                    print("--------♥️♠️♦️♣️-------End of Game-------♥️♠️♦️♣️-------")
                    print(f'The Game Winner : {Game.winner}\n')
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
                Player.opp_team_handwins += 1
                print(f'Our team hand wins : {Player.our_team_handwins}')
                print(f'Opp team hand wins : {Player.opp_team_handwins}\n')
                
                #امتیاز کل بازی
                if Player.our_team_handwins == 3:
                    Game.winner= (f'Our Team -> {me} & {npc2}')
                    print("--------♥️♠️♦️♣️-------End of Game-------♥️♠️♦️♣️-------")
                    print(f'The Game Winner : {Game.winner}\nGreat job {me}!\nThanks for playing this game.\nhope to see you again:)')
                    break
                elif Player.opp_team_handwins == 3:
                    Game.winner= (f'Opponent Team -> {npc1} & {npc3}')
                    print("--------♥️♠️♦️♣️-------End of Game-------♥️♠️♦️♣️-------")
                    print(f'The Game Winner : {Game.winner}\n')
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
                

print('Welcome to Hokm game. (designed by mitratsb)')
print('Pay attention please, in orther to input a card in any level, you must type a suit shape and value with space.')
# my_name= input('Please Enter your name : ')
# print("Let's start!")

Game.level_0()
Game.level_1()
Game.level_2()
Game.level_3()
Game.level_4()
