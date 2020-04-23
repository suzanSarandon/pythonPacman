'''
Created on Dec 3, 2017

@author: apapaioa
'''

import tkinter 
import time

top = tkinter.Tk() 
top.title('DrawingPanel')

C = tkinter.Canvas(top, bg="yellow", height=300, width=500)
C.pack() 

for i in range(30):
    # clear any previous image
    C.create_polygon(0,0,500,0,500,300,0,300, fill="yellow")
    
    if i%2 == 0:
        C.create_arc(20 * i, 50,
            20 * i + 50, 100,start=20, extent=320, fill="red")
    else: 
        C.create_oval(20 * i, 50,
            20 * i + 50, 100,fill="red")
    try:
        C.update()
        time.sleep(100 / 1000.0)
    except Exception:
        pass

top.mainloop() 
