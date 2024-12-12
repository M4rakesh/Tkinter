from tkinter import * 
from random import *

root=Tk()
root.title("Spēle")
root.geometry("600x600")
root.resizable(width=False,height=False)
#root.iconbitmap('images.ico')
#root['bg']= 'orange'

def change_color():
    colors=['red','green','blue','yellow','purple','orange']
    root.config(background=choice(colors))
btn=Button(root,
           text='tt',
           command=change_color,
           font=('Arial 20')
           
           )


btn.pack()

root.mainloop() 