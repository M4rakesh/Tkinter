from tkinter import * 
from random import *

root=Tk()
root.title("Spēle")
root.geometry("600x600")
root.resizable(width=False,height=False)
#root.iconbitmap('images.ico')
root['bg']= 'orange'

def whyknb():
    knb=['Akmens','Šķēres','Papīrs']
    value=choice(knb)
    lableText.configure(text=value)


lableText=Label(root,
              text='',
              font=('Comic Sans MS ',20,'bold'),
              bg='green',
              fg='blue'
              )


lableText.place(y=200,x=200)
stone=Button(root,
             text='Akmens',
             font=('Comic Sans MS ',20,'bold'),
             fg='white',
             command=whyknb)
stone.place(x=20,y=300)
scissors=Button(root,
                text='Šķēres',
                font=('Comic Sans MS ',20,'bold'),
                fg='white',
                command=whyknb)
scissors.place(x=220,y=300)
paper=Button(root,
                text='Papīrs',
                font=('Comic Sans MS ',20,'bold'),
                fg='white',
                command=whyknb)
paper.place(x=420,y=300)
root.mainloop() 