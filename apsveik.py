from tkinter import *
from random import  *
from PIL import ImageTk,Image
root=Tk()
root.title("Apsvczms")
root.geometry('1280x720')
root.resizable(width=False,height=False)
bg_smurf=ImageTk.PhotoImage(Image.open('tuda.jpeg'))
bg=Label(image=bg_smurf)
bg.pack()
root['bg'] = '#cdf7ef'

def add():
    e.insert(END,'')
def dele():
    e.delete(0,END)
def get():
    label1['text']=e.get()

def change_color():
    colors=['red','green','blue','yellow','purple','orange']
    root.config(background=choice(colors))
def novelejums():
    novel=['Lai Jaunais gads mums piedod vecos grēkus,\nUn jauniem grēkiem dod mums atkal spēkus!',
           'Lai Jaunā gadā Jūsu mājās ne tikai baltas maizes,\nbet arī baltu domu daudz!',
           'Tik mirdzošs un balts kā Jaungada sniegs,\nLai sirdī Jums mājo dzīvesprieks!',
           'Gads nākošais par bijušo lai skaistāks,\nLai dzīves dārzā vairāk ziedu zied!',
           'Lai Jaunais gads,\nkā teiksmu avots,Ir neizsmeļams,\nveselīgs un tīrs!']
    value=choice(novel)
    lableText.configure(text=value)
e=Entry(root,show='*')
e.pack()
lableText=Label(root,
              text='',
              font=('Comic Sans MS ',20,'bold'),
              #bg='',
              fg='black'
              )
lableText.place(x=360,y=600)

btn1=Button(root,font='Arial 15',text='Vārds',command=get,border=True,borderwidth=3,width=15,height=3)
btn1.pack()
btn1.place(x=50,y=75)

btn2=Button(root,font='Arial 15',text='Krāsa',command=change_color,width=15,height=3,border=True,borderwidth=3)
btn2.pack()
btn2.place(x=50,y=225)
btn3=Button(root,font='Arial 15',text='Novēlējums',command=novelejums,width=15,height=3,border=True,borderwidth=3)
btn3.pack()
btn3.place(x=50,y=375)

label1=Label(root,fg='black',font=('Arial 20 bold'))
label1.pack()

root.mainloop()