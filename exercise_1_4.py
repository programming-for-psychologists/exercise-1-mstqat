#Make the square appear for 1.5 secs, then show a blank screen for 1 sec, 
#then flash the square 3 times for 30 ms each.

import sys
from psychopy import visual, core, event
 
win = visual.Window([400,400],color="black", units='pix') 
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100]) 
square.draw() 
win.flip() 
core.wait(1.5)  
win.flip()
core.wait(1)
for i in range(3):
    square.draw()
    win.flip()
    core.wait(.03)
    win.flip()
    core.wait(.5)