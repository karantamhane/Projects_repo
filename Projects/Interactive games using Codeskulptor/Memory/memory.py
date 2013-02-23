#http://www.codeskulptor.org/#user5-yrjrAhtYt9Iu39t.py

# implementation of card game - Memory

import simplegui
import random

lst = []
exposed = []
first = None
second = None
state = 0
turns = 0

# helper function to initialize globals
def init():
    global lst, exposed, first, second, state, turns
    state, turns = 0, 0
    first = None
    second = None
    lst = [i//2 for i in range(16)]
    random.shuffle(lst)
    exposed = [False for i in range(16)]
    l.set_text('Moves = 0')
     
# define event handlers
def mouseclick(pos):
    global state, first, second, turns
    card_num = pos[0]//50
    print card_num + 1
    if exposed[card_num] == False:
        if state == 0:
            exposed[card_num] = True
            first = card_num
            state = 1
        elif state == 1:
            turns += 1
            exposed[card_num] = True
            second = card_num                
            state = 2
        else:
            if lst[first] == lst[second]:
                exposed[card_num] = True
                first = card_num
                second = None
                state = 1
            else:
                exposed[first] = False
                exposed[second] = False
                exposed[card_num] = True
                first = card_num
                state = 1
    l.set_text('Moves = '+str(turns))    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global lst, exposed
    pos = [0, 0]
    num_pos = [10, 75]
    for i in range(16):
        if exposed[i] == False:
            canvas.draw_polygon([pos, [pos[0] + 50, pos[1]], [pos[0] + 50, pos[1] + 100], [pos[0], pos[1] + 100]], 1, "Black")
            pos[0] += 50
            num_pos[0] += 50
        else:
            canvas.draw_polygon([(i*50, 0), ((i+1)*50, 0), ((i+1)*50, 100), (i*50, 100)], 1, "White", "Black")
            canvas.draw_text(str(lst[i]), num_pos, 48, "White")
            num_pos[0] += 50
            pos[0] += 50

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
frame.set_canvas_background("Green")
l=frame.add_label("Moves = 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()

# Always remember to review the grading rubric
