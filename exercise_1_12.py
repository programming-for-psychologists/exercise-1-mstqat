#Show two rotating squares simultaneously, one left of center rotating 
#clockwise, the other right of center, rotating counterclockwise

import sys
from psychopy import visual, core, event
 
win = visual.Window([400,400],color="black", units='pix') 
square = visual.Rect(win,lineColor="black",fillColor="pink",size=[100,100], pos=[100, 0])
square2 = visual.Rect(win,lineColor="black",fillColor="pink",size=[100,100], pos=[-100,0])
square.draw()
square2.draw()
win.flip()


original_increment = increment = 6 
while True:
    square.draw()
    square2.draw()
    win.flip()
    square.ori -= increment
    square2.ori += increment
    if event.getKeys(['q']):
        break
    
win.close()
