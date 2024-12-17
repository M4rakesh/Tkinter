from tkinter import *

root=Tk()
root.title("Teksta ievadīšana")
root.geometry('1280x720')
root.resizable(width=False,height=False)

root['bg'] = 'green'

def add():
    e.insert(END,'Hello')
def dele():
    e.delete(0,END)
def get():
    label1['text']=e.get()

e=Entry(root,show='*')
e.pack()


btn1=Button(root,font='Arial 15',text='insert',command=add)
btn1.pack()

btn2=Button(root,font='Arial 15',text='delete',command=dele)
btn2.pack()

btn3=Button(root,font='Arial 15',text='get',command=get)
btn3.pack()

label1=Label(root,bg='green',fg='white')
label1.pack()
root.mainloop()