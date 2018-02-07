#Make the square red instead of blue

import sys
from psychopy import visual, core, event
 
win = visual.Window([400,400],color="black", units='pix') 
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100]) 
square.draw() 
win.flip() 
core.wait(.5) 
