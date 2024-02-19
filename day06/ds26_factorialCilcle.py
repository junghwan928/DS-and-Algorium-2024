## file: ds26_factorialCircle.py
## desc: 프랙탈 원그리기

from tkinter import *
import random

def drawCircle(x,y,r):
    # global count
    # count += 1
    # canvas.create_oval(x-r, y-r, x+r, y+r, outline=random.choice(colors))
    # canvas.create_text(x, y-r, text=str(count), font=('Gulim',30))
    canvas.create_oval(x-r, y-r, x+r, y+r, width=2, outline=random.choice(colors))
    
    if r >= 5:
        drawCircle(x-r//2, y, r//2)
        drawCircle(x+r//2, y, r//2)
# 전역변수
# count = 0
radius = 400
wSize = 1000
colors = ['red', 'green', 'blue', 'black', 'orange', 'indigo', 'violet', 'crimson', 'gray']

# main code
window = Tk()
window.title('프랙탈 원그리기')
# canvas = Canvas(window, height=1000, width=1000, bg='white')

# drawCircle(wSize//2, wSize//2, radius)
# canvas.pack()

# cx = 1000/2
# cy = 1000/2
# r = 400


# # cx-r, cy-r(좌측상단) / cx+r, cy+r(우측하단)
# canvas.create_oval(cx-r, cy-r, cx+r, cy+r, width=2, outline='red')


# window.mainloop()
canvas = Canvas(window, height=wSize, width=wSize, bg='white')

drawCircle(wSize//2, wSize//2, radius)

canvas.pack() 
window.mainloop()