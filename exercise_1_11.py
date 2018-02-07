# Display a blue square and increase its width (making it a rectangle) by 10% 
# whenever the user presses the left-arrow key. Decrease the width by 10 
# %when the user presses the right-arrow key
import sys
from psychopy import visual, core, event
 
win = visual.Window([400,400],color="black", units='pix') 
square = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100]) 
while True:
    square.draw()
    win.flip()
    if (event.getKeys(['left'])):
        square.size = [square.size[0] * 1.1, square.size[1] * 1.1]
    elif (event.getKeys(['right'])):
        square.size = [square.size[0] * .9, square.size[1] * .9]
  