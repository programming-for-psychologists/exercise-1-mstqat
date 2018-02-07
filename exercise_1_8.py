#Make a rotating square stop rotating when you press the 's' key

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
    if event.getKeys(['q']): 
        break
