import sys
from psychopy import visual, core
 
win = visual.Window([400,400],color="black", units='pix') 
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100]) 
square.draw() 
win.flip() 
core.wait(1) 
square.fillColor="blue"
square.draw()
win.flip()
core.wait(1)
