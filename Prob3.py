########################################
# Name: Noah Klarreich
# Collaborators:
# Estimate time spent (hrs): 30 mins
########################################

from pgl import GWindow, GRect, GLabel, GLine
import random

GW_WIDTH = 500                      # Width of window
GW_HEIGHT = 500                     # Height of window
SQUARE_SIZE = 50                    # Width and height of square
SCORE_DX = 10                      # Distance from left of window to origin
SCORE_DY = 10                     # Distance up from bottom of window to baseline
SCORE_FONT = "bold 40pt 'serif'"    # Font for score
x = GW_WIDTH/2-SQUARE_SIZE/2
y = GW_HEIGHT/2-SQUARE_SIZE/2
c = 0
def clicky_box():
   
    gw = GWindow(GW_WIDTH, GW_HEIGHT)

    gw.s = GRect(x, y, SQUARE_SIZE, SQUARE_SIZE)
    gw.s.set_color('Red')
    gw.s.set_filled('True')
    gw.add(gw.s)
    gw.l = GLabel('0', SCORE_DX, GW_HEIGHT-SCORE_DY)
    gw.l.set_color('Black')
    gw.add(gw.l)


    # Defining the callback function, which you won't need until Part C
    def on_mouse_down(event):
        global x, y, c
        if event.get_x()-x>= 0 and event.get_x()-x-SQUARE_SIZE<=0:
            if event.get_y()-y>= 0 and event.get_y()-y-SQUARE_SIZE<=0:
                x = random.randint(0, GW_WIDTH-SQUARE_SIZE)
                y = random.randint(0, GW_HEIGHT-SQUARE_SIZE)
                gw.s.set_location(x, y)
                c += 1
                gw.l.set_label(str(c))
                return
        c = 0
        gw.l.set_label(str(c))
    
                
    gw.add_event_listener("click", on_mouse_down)

if __name__ == '__main__':
    clicky_box()
