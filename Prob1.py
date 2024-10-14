############################################################
# Name:
# Name(s) of anyone worked with:
# Est time spent (hr):
############################################################

from pgl import GWindow, GRect, GOval, GLine, GLabel

# Setting up initial window dimensions. 
# You can change these if you want. They are in number of pixels.
WIDTH = 600
HEIGHT = 600

def draw_image():
    """ Creates a window and draws a student's creation"""

    # Creating the window
    gw = GWindow(WIDTH, HEIGHT)
    
    # And now it is your turn! Add your code below! Make sure you meet all the requirements!
    r = GRect(150, 150, 200, 200)
    r.set_color('Red')
    r.set_filled(True)
    gw.add(r)
    l = GLine(100, 20, 100, 500)
    l.set_color('Grey')
    gw.add(l)
    o = GOval(300, 500)
    o.set_color('Blue')
    gw.add(o)
    gw.add(GLabel('Problem one', 300, 400))



if __name__ == '__main__':
    draw_image()
