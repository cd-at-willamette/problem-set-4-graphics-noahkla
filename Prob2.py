########################################
# Name:
# Collaborators:
# Estimated time spent (hrs):
########################################

from pgl import GWindow, GRect

WIDTH = 800
HEIGHT = 600
BRICK_WIDTH = 40
BRICK_HEIGHT = 20
BRICKS_IN_BASE = 15

    
def draw_pyramid():
    """ 
    Draws a pyramid of bricks centered on the screen with a height of BRICKS_IN_BASE. 
    """

    gw = GWindow(WIDTH, HEIGHT)
    h = HEIGHT-100
    for i in range(BRICKS_IN_BASE):
        row(BRICKS_IN_BASE - i, h, gw)
        h -= BRICK_HEIGHT


    
def row(n, h, gw):
    length = n*BRICK_WIDTH
    s  = WIDTH/2 - length/2
    for i in range(n):
        r = GRect(s, h, BRICK_WIDTH, BRICK_HEIGHT)
        r.set_color('Black')
        gw.add(r)
        s += BRICK_WIDTH
















if __name__ == '__main__':
    draw_pyramid()
