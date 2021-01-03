from tkinter import *
import random


window = Tk()
window.config(width=1000, height=800, padx=20, pady=20, bg='green4')
window.title("E.N®        BlackJack ")
concave = Canvas(width=800, height=500)
concave.config(bg='green')
concave.grid(row=0, column=0, columnspan=3)
dealer_score, player_score = 0, 0
styles = ('Ariel', 12, 'italic', 'bold')
dealer_text, player_text = '', ''
dealer_cards, player_cards = [], []
counter2, counter = 2, 0
All_cards = []
places, flipped = 360, []
t_x, t_y = 325, 335
b_x, b_y = 410, 470
dt_x, dt_y = 325, 35
db_x, db_y = 415, 165
player_Bottom = None
dlr_Bottom = None
numbers1_suit = ''
game_over = False
signals = ''


club = PhotoImage(file='mycards/club.png')
spare = PhotoImage(file='mycards/spare.png')
spare.zoom(20, 30)
heart = PhotoImage(file='mycards/heart.png')
heart.zoom(20, 30)
diamond = PhotoImage(file='mycards/diamond.png')
diamond.zoom(20, 30)
backblue = PhotoImage(file='mycards/back_blue.png')
backblue.zoom(20, 30)
backred = PhotoImage(file='mycards/back_red.png')
backred.zoom(20, 30)

slat1 = concave.create_image(300, 100, image='')
slat2 = concave.create_image(335, 100, image='')
slat3 = concave.create_image(370, 100, image='')
slat4 = concave.create_image(405, 100, image='')
slat5 = concave.create_image(440, 100, image='')
slat6 = concave.create_image(475, 100, image='')
slat7 = concave.create_image(510, 100, image='')
slat8 = concave.create_image(545, 100, image='')

slats1 = concave.create_image(300, 400, image='')
slats2 = concave.create_image(335, 400, image='')
slats3 = concave.create_image(370, 400, image='')
slats4 = concave.create_image(405, 400, image='')
slats5 = concave.create_image(440, 400, image='')
slats6 = concave.create_image(475, 400, image='')
slats7 = concave.create_image(510, 400, image='')
slats8 = concave.create_image(545, 400, image='')

concave.create_text(130, 100, text="Dealer Score:", font=('Ariel', 14, 'bold'))
dealer_display = concave.create_text(130, 135, text="0", font=('Ariel', 16, 'bold'))
concave.create_text(130, 400, text="Player Score:", font=('Ariel', 14, 'bold'))
player_display = concave.create_text(130, 435, text="0", font=('Ariel', 16, 'bold'))

winner_display1 = concave.create_text(310, 255, text="", font=('Ariel', 14, 'bold'))
winner_display2 = concave.create_text(580, 255, text="", font=('Ariel', 16, 'bold'))


dealerTop = concave.create_text(255, 35, text="", font=('Ariel', 18, 'bold'))
dealerBottom = concave.create_text(340, 165, text="", font=('Ariel', 18, 'bold'))
playerTop = concave.create_text(255, 335, text="", font=('Ariel', 18, 'bold'))
playerBottom = concave.create_text(340, 470, text="", font=('Ariel', 18, 'bold'))
dealerTop2 = concave.create_text(290, 35, text="", font=('Ariel', 18, 'bold'))
dealerBottom2 = concave.create_text(380, 165, text="", font=('Ariel', 18, 'bold'))
playerTop2 = concave.create_text(290, 335, text="", font=('Ariel', 18, 'bold'))
playerBottom2 = concave.create_text(380, 470, text="", font=('Ariel', 18, 'bold'))


dealer_home = [slat1, slat2, slat3, slat4, slat5, slat6, slat7, slat8]
player_home = [slats1, slats2, slats3, slats4, slats5, slats6, slats7, slats8]
slats = [300, 330, 360, 390, 420, 450, 480]
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1]
suits = {'heart': [heart, backred], 'spare': [spare, backblue], 'club': [club, backblue], 'diamond': [diamond, backred]}


def go_back():
    global signals
    concave.config(bg='green4')
    signals = ''


def show_signal(winner):
    if winner == 'w':
        concave.config(bg='#cdb30c')
    elif winner == 'l':
        concave.config(bg='red')
    window.after(1000, go_back)


def winner_check(playerScore, dealerScore):
    global signals
    if dealerScore == 21:
        signals = 'l'
        return 'LOSE !, Opponent has BlackJack !'
    elif playerScore == 21:
        signals = 'w'
        return 'You WIN !!,  With BlackJack !'
    elif playerScore > 21:
        signals = 'l'
        return 'Lose !, You went Over !'
    elif dealerScore > 21:
        signals = 'w'
        return 'You WIN !, Opponent went Over !'

    else:
        return ''


def calc_scores(card):
    if sum(card) == 21 and len(card) == 2:
        return 21
    if 11 in card and sum(card) > 21:
        card.remove(11)
        card.append(1)
    return sum(card)


def create_card():
    for item in cards:
        for card in suits:
            All_cards.append((item, card))   # creating the 52 playing cards


create_card()


def start_game():

    global counter, dealer_score, player_score
    global dealer_text, player_text, flipped
    global dealer_cards, player_cards, numbers1_suit
    global game_over
    dealer_cards = []
    player_cards = []
    counter = 0
    numbers1_suit = ''
    if not game_over:
        random.shuffle(All_cards)
        dealer_first = random.choices(All_cards, k=2)
        numbers1 = dealer_first[0][0]
        numbers1_suit = dealer_first[0][1]
        numbers1_back = suits[numbers1_suit][1]
        numbers2 = dealer_first[1][0]
        numbers2_suit = dealer_first[1][1]

        if numbers1 == 1:
            dealer_text = '1'
            dealer_cards.append(11)
            flipped.append("1")
        if numbers1 == 13:
            dealer_text = 'K'
            dealer_cards.append(10)
            flipped.append('K')
        elif numbers1 == 12:
            dealer_text = 'Q'
            dealer_cards.append(10)
            flipped.append('Q')
        elif numbers1 == 11:
            dealer_text = 'J'
            dealer_cards.append(10)
            flipped.append('J')
        elif numbers1 < 11 and numbers1 != 1:
            dealer_text = str(numbers1)
            dealer_cards.append(numbers1)
            flipped.append(str(numbers1))

        concave.itemconfig(slat1, image=numbers1_back)
        flipped.append(numbers1_suit)

        dealer_text = ''
    #    . . . . . . . . . . . . .. . . . . . . . . . . . . . . .  dealer num 2

        if numbers2 == 1:
            dealer_text = '1'
            dealer_cards.append(11)
        if numbers2 == 13:
            dealer_text = 'K'
            dealer_cards.append(10)
        elif numbers2 == 12:
            dealer_text = 'Q'
            dealer_cards.append(10)
        elif numbers2 == 11:
            dealer_text = 'J'
            dealer_cards.append(10)
        elif numbers2 < 11 and numbers2 != 1:
            dealer_text = str(numbers2)
            dealer_cards.append(numbers2)

        concave.itemconfig(dealerBottom, text=' ')
        concave.itemconfig(slat2, image=suits[numbers2_suit][0])
        concave.itemconfig(dealerTop2, text=dealer_text)
        concave.itemconfig(dealerBottom2, text=dealer_text)
        dealer_text = ''

        # player  . . . . . . . . . . . . . . . . . . . . . . . . .

        player_first = random.choices(All_cards, k=2)
        player_num1 = player_first[0][0]
        numbersp1_suit = player_first[0][1]
        player_num2 = player_first[1][0]
        numbersp2_suit = player_first[1][1]

        if player_num1 == 1:
            player_text = '1'
            player_cards.append(11)
        if player_num1 == 13:
            player_text = 'K'
            player_cards.append(10)
        elif player_num1 == 12:
            player_text = 'Q'
            player_cards.append(10)
        elif player_num1 == 11:
            player_text = 'J'
            player_cards.append(10)
        elif player_num1 < 11 and player_num1 != 1:
            player_text = str(player_num1)
            player_cards.append(player_num1)

        concave.itemconfig(slats1, image=suits[numbersp1_suit][0])
        concave.itemconfig(playerTop, text=player_text)
        concave.itemconfig(playerBottom, text=player_text)
        player_text = ''
        counter += 1

        concave.itemconfig(playerBottom, text=' ')
        concave.itemconfig(slats2, image=suits[numbersp2_suit][0])

        if player_num2 == 1:
            player_text = '1'
            player_cards.append(11)
        if player_num2 == 13:
            player_text = 'K'
            player_cards.append(10)
        elif player_num2 == 12:
            player_text = 'Q'
            player_cards.append(10)
        elif player_num2 == 11:
            player_text = 'J'
            player_cards.append(10)
        elif player_num2 < 11 and player_num2 != 1:
            player_text = str(player_num2)
            player_cards.append(player_num2)

        concave.itemconfig(playerTop2, text=player_text)
        concave.itemconfig(playerBottom2, text=player_text)
        player_text = ''
        counter += 1

        dealer_score = calc_scores(dealer_cards)            # calc dealer score
        player_score = calc_scores(player_cards)                # calculate the score

        num = 10 if numbers2 > 10 else numbers2   # display the first number of the dealer
        num = 11 if numbers2 == 1 else num
        concave.itemconfig(dealer_display, text=str(num))
        concave.itemconfig(player_display, text=str(player_score))

        winnerCheck = winner_check(player_score, dealer_score)
        if winnerCheck != '':
            end_of_game(winnerCheck)

        # All_cards.remove(dealer_first[1])
        # All_cards.remove(dealer_first[0])
        # All_cards.remove(player_first[1])
        # All_cards.remove(player_first[0])


def next_one():

    random.shuffle(All_cards)
    global places, counter, player_score
    global player_text, player_Bottom, player_cards
    global t_x, t_y, b_x, b_y, counter2, game_over
    player_text = ''

    if not game_over:
        concave.itemconfig(player_Bottom, text=' ')
        player_Top = concave.create_text(t_x, t_y, text="", font=('Ariel', 18, 'bold'))
        player_Bottom = concave.create_text(b_x, b_y, text="", font=('Ariel', 18, 'bold'))

        player_next = random.choice(All_cards)
        player_num = player_next[0]
        player_suits = player_next[1]

        if player_num == 1:
            player_text = '1'
            player_cards.append(11)
        if player_num == 13:
            player_text = 'K'
            player_cards.append(10)
        elif player_num == 12:
            player_text = 'Q'
            player_cards.append(10)
        elif player_num == 11:
            player_text = 'J'
            player_cards.append(10)
        elif player_num < 11 and player_num != 1:
            player_text = str(player_num)
            player_cards.append(player_num)

        player_score = calc_scores(player_cards)  # calculate the score

        concave.itemconfig(playerBottom2, text=' ')
        concave.itemconfig(player_home[counter], image=suits[player_suits][0])
        concave.itemconfig(player_Top, text=player_text)
        concave.itemconfig(player_Bottom, text=player_text)
        concave.itemconfig(player_display, text=str(player_score))
        counter += 1
        t_x += 35
        b_x += 35
        player_text = ''

        winnerCheck = winner_check(player_score, dealer_score)
        if winnerCheck != '':
            end_of_game(winnerCheck)


def dealer_turn():
    global places, dealer_score
    global dealer_text, dlr_Bottom
    global dt_x, dt_y, db_x, db_y, game_over
    global flipped, counter2, numbers1_suit
    suit = flipped[1]
    winnerCheck = None
    if not game_over:
        concave.itemconfig(slat1, image=suits[numbers1_suit][0])
        concave.itemconfig(dealerTop, text=str(flipped[0]))

        while dealer_score < 17 and dealer_score != 0:              # dealer  end of game
            random.shuffle(All_cards)
            concave.itemconfig(dealerBottom2, text='')

            dealer_text = ''
            concave.itemconfig(dlr_Bottom, text=' ')

            dlr_Top = concave.create_text(dt_x, dt_y, text="", font=('Ariel', 18, 'bold'))
            dlr_Bottom = concave.create_text(db_x, db_y, text="", font=('Ariel', 18, 'bold'))

            dealer_text = random.choice(All_cards)
            numbersD = int(dealer_text[0])
            numbersD_suit = dealer_text[1]

            if numbersD == 1:
                dealer_text = '1'
                dealer_cards.append(11)
            if numbersD == 13:
                dealer_text = 'K'
                dealer_cards.append(10)
            elif numbersD == 12:
                dealer_text = 'Q'
                dealer_cards.append(10)
            elif numbersD == 11:
                dealer_text = 'J'
                dealer_cards.append(10)
            elif numbersD < 11 and numbersD != 1:
                dealer_text = str(numbersD)
                dealer_cards.append(numbersD)

            dealer_score = calc_scores(dealer_cards)  # calc dealer score

            # concave.itemconfig(playerBottom2, text=' ')
            concave.itemconfig(dealer_home[counter2], image=suits[numbersD_suit][0])
            concave.itemconfig(dlr_Top, text=dealer_text)
            concave.itemconfig(dlr_Bottom, text=dealer_text)
            concave.itemconfig(dealer_display, text=str(dealer_score))
            counter2 += 1
            dt_x += 35
            db_x += 32
            player_text = ''

            winnerCheck = winner_check(player_score, dealer_score)
            if winnerCheck != '':
                end_of_game(winnerCheck)
        else:
            end_of_game(winnerCheck)


def end_of_game(msg):
    global signals
    global player_score, dealer_score, flipped, game_over
    suit = flipped[1]
    concave.itemconfig(slat1, image=suits[numbers1_suit][0])
    concave.itemconfig(dealerTop, text=str(flipped[0]))
    display2 = ''
    if player_score < 21 and dealer_score < 21:
        if player_score == dealer_score:
            display2 = '     DRAW !  ,  Same score !'
        elif player_score > dealer_score:
            signals = 'w'
            display2 = 'You Win !!,  Your score is higher !'
        elif dealer_score > player_score:
            signals = 'l'
            display2 = 'You lose !!,  Your score is lower !'
    else:
        display2 = msg
    show_signal(signals)
    concave.itemconfig(dealer_display, text=str(dealer_score))
    concave.itemconfig(winner_display1, text="Game Over !")
    concave.itemconfig(winner_display2, text=display2)
    game_over = True


change1 = Button(text="    start   ", font=styles, bg='#98acf8', bd=5, relief="ridge", command=start_game)
change1.grid(row=2, column=0)
change2 = Button(text="    Hit    ", font=styles, bg='#98acf8', bd=5, relief="ridge", command=next_one)
change2.grid(row=2, column=1)
change3 = Button(text="    Stand   ", font=styles, bg='#98acf8', bd=5, relief="ridge", command=dealer_turn)
change3.grid(row=2, column=2)


window.mainloop()


