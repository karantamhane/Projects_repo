#http://www.codeskulptor.org/#user4-qkjh50WrwV5FW8j.py

# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
ball_pos = [WIDTH/2, HEIGHT/2]
right = True


# helper function that spawns a ball, returns a position vector and a velocity vector
# if right is True, spawn to the right, else spawn to the left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    if right:
        ball_vel = [random.randrange(120, 240)/60, -random.randrange(60, 180)/60]
    else:
        ball_vel = [-random.randrange(120, 240)/60, -random.randrange(60, 180)/60]   
    return ball_pos, ball_vel
    pass

# define event handlers
def init():
#    timer.stop()
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    global right
    score1, score2 = 0, 0
    paddle1_pos = [HALF_PAD_WIDTH, HEIGHT/2]
    paddle2_pos = [WIDTH-HALF_PAD_WIDTH, HEIGHT/2]
    paddle1_vel = [0, 0]
    paddle2_vel = [0, 0]
    ball_pos, ball_vel = ball_init(right)
    right = not right
#    timer.start()
    pass

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, counter
 
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos[1] - HALF_PAD_HEIGHT < 0:
        paddle1_pos[1] = HALF_PAD_HEIGHT
        paddle1_vel[1] = 0
    if paddle1_pos[1] + HALF_PAD_HEIGHT > HEIGHT:
        paddle1_pos[1] = HEIGHT - HALF_PAD_HEIGHT
        paddle1_vel[1] = 0
    paddle1_pos[1] += paddle1_vel[1]

    if paddle2_pos[1] - HALF_PAD_HEIGHT < 0:
        paddle2_pos[1] = HALF_PAD_HEIGHT
        paddle2_vel[1] = 0
    if paddle2_pos[1] + HALF_PAD_HEIGHT > HEIGHT:
        paddle2_pos[1] = HEIGHT - HALF_PAD_HEIGHT
        paddle2_vel[1] = 0
    paddle2_pos[1] += paddle2_vel[1]
    
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    c.draw_polygon([(paddle1_pos[0]-HALF_PAD_WIDTH, paddle1_pos[1]-HALF_PAD_HEIGHT), (paddle1_pos[0]+HALF_PAD_WIDTH, paddle1_pos[1]-HALF_PAD_HEIGHT), (paddle1_pos[0]+HALF_PAD_WIDTH, paddle1_pos[1]+HALF_PAD_HEIGHT), (paddle1_pos[0]-HALF_PAD_WIDTH, paddle1_pos[1]+HALF_PAD_HEIGHT)], 1, 'White', 'White')
    c.draw_polygon([(paddle2_pos[0]-HALF_PAD_WIDTH, paddle2_pos[1]-HALF_PAD_HEIGHT), (paddle2_pos[0]+HALF_PAD_WIDTH, paddle2_pos[1]-HALF_PAD_HEIGHT), (paddle2_pos[0]+HALF_PAD_WIDTH, paddle2_pos[1]+HALF_PAD_HEIGHT), (paddle2_pos[0]-HALF_PAD_WIDTH, paddle2_pos[1]+HALF_PAD_HEIGHT)], 1, 'White', 'White')
   
    # update ball
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] + BALL_RADIUS >= HEIGHT:
        ball_vel[1] = -ball_vel[1]
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    if ball_pos[0] - BALL_RADIUS <= PAD_WIDTH:
        if ball_pos[1] >= paddle1_pos[1] - HALF_PAD_HEIGHT and ball_pos[1] <= paddle1_pos[1] + HALF_PAD_HEIGHT:
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] *= 1.1
            ball_vel[1] *= 1.1
        else:
            score2 += 1
            ball_init(True)
    
    if ball_pos[0] + BALL_RADIUS >= WIDTH - PAD_WIDTH:
        if ball_pos[1] >= paddle2_pos[1] - HALF_PAD_HEIGHT and ball_pos[1] <= paddle2_pos[1] + HALF_PAD_HEIGHT:
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] *= 1.1
            ball_vel[1] *= 1.1
        else:
            score1 += 1
            ball_init(False)
    
    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 1, 'White', 'White')
    c.draw_text(str(score1),(140, 80), 32, 'White')
    c.draw_text(str(score2),(440, 80), 32, 'White')
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel[1] -= 3
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel[1] += 3
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel[1] -= 3
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel[1] += 3
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w'] and paddle1_vel[1] < 0:
        paddle1_vel[1] += 3
    if key == simplegui.KEY_MAP['s'] and paddle1_vel[1] > 0:
        paddle1_vel[1] -= 3
    if key == simplegui.KEY_MAP['up'] and paddle2_vel[1] < 0:
        paddle2_vel[1] += 3
    if key == simplegui.KEY_MAP['down'] and paddle2_vel[1] > 0:
        paddle2_vel[1] -= 3

#def time_speed():
#    if ball_vel[0] > 0:
#        ball_vel[0] += 1.1
#    if ball_vel[1] > 0:
#        ball_vel[1] += 1.1
#    if ball_vel[0] < 0:
#        ball_vel[0] -= 0.1
#    if ball_vel[1] < 0:
#       ball_vel[1] -= 0.1

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", init, 100)
#timer = simplegui.create_timer(2000, time_speed)


# start frame
init()
frame.start()

