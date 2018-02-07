#Make a square stop rotating when you press 's' and then start rotating again when you press 'r'

import sys
from psychopy import visual, core, event

original_increment = increment = 6 
 
win = visual.Window([400,400],color="black", units='pix') 
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100]) 
while True:
    square.draw()
    win.flip()
    square.ori += increment
    if event.getKeys(['s']):
        increment = 0
    elif event.getKeys(['r']):
        increment = original_increment
    if event.getKeys(['q']):
        break
