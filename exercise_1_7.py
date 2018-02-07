#Now make a square rotate continuously, one full revolution (360 degrees) per second
import sys
from psychopy import visual, core, event

original_increment = increment = 6 # 360 degrees / 60 Hz screen refresh rate
 
win = visual.Window([400,400],color="black", units='pix') 
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100]) 
while True:
    square.draw()
    win.flip()
    square.ori += increment
    if event.getKeys(['q']):
        break

