from tkinter import * 
from random import *
def move_image():
    global img_x,img_y 
    img_x +=randint(-50,50)
    img_y +=randint(-50,50)
    l_logo.place(x=img_x,y=img_y)
root=Tk()
root.title("Attēla pārvietošana")
root.geometry("400x400")
count = 0
def in_count():
    global count
    count+= 1
    label.config(text=f'Klikšķi:{count}')


root.resizable(width=False,height=False)
#root.iconbitmap('images.ico')
#root['bg']= 'orange'
img_x,img_y = 50,50

img = PhotoImage(file='neo.png')
l_logo = Label(root,image=img)
l_logo.place(x=img_x,y=img_y)

label= Label(root,text=f'Klikšķi:{count}',font=('Arial',16))
label.pack(pady=20)
def change_color():
    colors=['red','green','blue','yellow','purple','orange']
    root.config(background=choice(colors))
btn=Button(root,
           text='Parvietot',
           command=move_image,
        
           font=('Arial 20')
           )


btn.pack()

root.mainloop() 