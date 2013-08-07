#http://www.codeskulptor.org/#user6-OlbbTlT8IeueJ57.py

# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = True
outcome, prompt = "Welcome to Blackjack!", "Hit or Stand?"
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []

    def __str__(self):
        string = [str(card) for card in self.hand]
        return str(string)

    def add_card(self, card):
        self.hand.append(card)

    # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
    def get_value(self):
        value = 0
        for card in self.hand:
            value += VALUES[card.get_rank()]
        for card in self.hand:
            if card.get_rank() == 'A' and value + 10 <= 21:
                value += 10
        return value

    def busted(self):
        if self.get_value() > 21:
            return True
        else:
            return False
    
    def draw(self, canvas, p):
        i = 0
        #location = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(card.rank), CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        for card in self.hand:
            card.draw(canvas, [p[0] + i*(20 + CARD_SIZE[0]), p[1]])
            i += 1

# define deck class
class Deck:
    def __init__(self):
        self.deck = [Card(suit, rank) for suit in SUITS for rank in RANKS]

    # add cards back to deck and shuffle
    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop(self.deck.index(random.choice(self.deck)))
    
    def __str__(self):
        string = [str(card) for card in self.deck]
        return str(string)

player_hand = Hand()
dealer_hand = Hand()
deck = Deck()
    
#define event handlers for buttons
def deal():
    global outcome, in_play, prompt, score, player_hand, dealer_hand, deck
    prompt = 'Hit or Stand?'
    if in_play:
        outcome = 'You forfeit! New game!'
        score -= 1
    else:
        outcome = 'New hand!'
    
    player_hand = Hand()
    dealer_hand = Hand()
    deck = Deck()
    
    in_play = False
    hit()
    hit()
    
    #print outcome
    #print prompt
    
    in_play = True
    hit()
    hit()
    
    #print 'player',str(player_hand)
    #print 'dealer',str(dealer_hand)

def hit():
    global outcome, in_play, prompt, score, player_hand, dealer_hand, deck
    if in_play and not player_hand.busted():
        player_hand.add_card(deck.deal_card())
        if player_hand.busted():
            outcome = 'You went bust! You lose!'
            score -= 1
            in_play = False
            prompt = 'Deal again?'
    elif not in_play and not player_hand.busted():
        dealer_hand.add_card(deck.deal_card())
        #if dealer_hand.busted():
        #    outcome = 'Dealer busted! You win!'
        #    score += 1
        #    prompt = 'Deal again?'
            
    # if the hand is in play, hit the player
   
    # if busted, assign an message to outcome, update in_play and score
       
def stand():
    global outcome, in_play, prompt, score, player_hand, dealer_hand, deck
    if in_play:
        in_play = False
        while dealer_hand.get_value() < 17:
            hit()
        if dealer_hand.busted():
            outcome = 'Dealer busted! You win!'
            score += 1
        elif dealer_hand.get_value() >= player_hand.get_value():
            outcome = 'Dealer wins!'
            score -= 1
        else:
            outcome = 'You win!'
            score += 1
        prompt = 'Deal again?'
            
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score
    
hit()
hit()
in_play = False
hit()
hit()
in_play = True

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    player_hand.draw(canvas, [100, 370])
    dealer_hand.draw(canvas, [100, 220])
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, (100 + CARD_BACK_CENTER[0], 220 + CARD_BACK_CENTER[1]), CARD_BACK_SIZE)
    canvas.draw_text('Dealer', [50, 190], 26, "White")
    canvas.draw_text('Player', [50, 520], 26, "White")
    canvas.draw_text(outcome, [200, 190], 26, "Black")
    canvas.draw_text(prompt, [200, 520], 26, "Black")
    canvas.draw_text('Blackjack', [130, 110], 40, "Black")
    canvas.draw_text("Score: "+str(score), [430, 110], 26, "Black")


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# deal an initial hand

# get things rolling
frame.start()


# remember to review the gradic rubric
