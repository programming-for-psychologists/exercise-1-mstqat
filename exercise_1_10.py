#Display a blue square and increase its width (making it a rectangle) by 10 
#pixels whenever the user presses the left-arrow key. Decrease the width by 10 
#pixels when the user presses the right-arrow key

import sys
from psychopy import visual, core, event
 
win = visual.Window([400,400],color="black", units='pix') 
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100]) 
while True:
    square.draw()
    win.flip()
    if (event.getKeys(['left'])):
        square.size = [square.size[0] + 10, square.size[1] + 10]
    elif (event.getKeys(['right'])):
        square.size = [square.size[0] - 10, square.size[1] - 10]
  