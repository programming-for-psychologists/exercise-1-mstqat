#Show the following sequence: blue, red, blue, red, blue, red (with each square appearing for 1 s with a 50 ms blank screen in the middle).
import sys
from psychopy import visual, core, event
 
win = visual.Window([400,400],color="black", units='pix')
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100]) 
win.flip() 
for cur_color in ['blue','red']*3:
    square.setFillColor(cur_color)
    square.draw()
    win.flip()
    core.wait(1)
    win.flip()
    core.wait(.05)
