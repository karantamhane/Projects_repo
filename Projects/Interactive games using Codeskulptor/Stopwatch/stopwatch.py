#http://www.codeskulptor.org/#user4-mFFCGjglaFSkdat.py

# template for "Stopwatch: The Game"
import simplegui

# define global variables
tenths = 0
success = 0
attempt = 0
stopped = True

# define helper function format that converts integer
# counting tenths of seconds into formatted string A:BC.D

def format(t):
    m = t//600
    s = t%600
    if s == 0:
        return str(m) + ':00.0'
    else:
        if len(str(s)) == 3:
            return str(m) + ':' + str(s)[:2] + '.' + str(s)[-1]
        elif len(str(s)) == 2:
            return str(m) + ':0' + str(s)[0] + '.' + str(s)[-1]
        elif len(str(s)) == 1:
            return str(m) + ':00.' + str(s)
            
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global stopped
    if stopped:
        stopped = False
        timer.start()
    
def stop():
    global attempt
    global stopped
    global success
    if not stopped:
        stopped = True
        timer.stop()
        attempt += 1
        if tenths%10 == 0:
            success += 1
    
def reset():
    global tenths
    global attempt
    global success
    timer.stop()
    tenths = 0
    attempt = 0
    success = 0

# define event handler for timer with 0.1 sec interval
def timer():
    global tenths
    tenths += 1
    print tenths
    
#define draw handler
def draw(canvas):
    canvas.draw_text(format(tenths), (120, 180), 52, 'White')
    canvas.draw_text(str(success) + '/' + str(attempt), (20, 50), 36, 'White')
# create frame
frame = simplegui.create_frame('Stopwatch: The Game', 400, 300)

# register event handlers
timer = simplegui.create_timer(100, timer)
frame.set_draw_handler(draw)
frame.add_button('Start', start, 80)
frame.add_button('Stop', stop, 80)
frame.add_button('Reset', reset, 80)


# start timer and frame
frame.start()
#timer.start()

# remember to review the grading rubric
