from tkinter import * 
root=Tk()
root.geometry('1920x1280')
root.resizable(width=False,height=False)
#root.iconbitmap('165-1656212_download-png-ico-icns-icon.ico')

def click():
    print('Sveiciens!')

btn=Button(root,
           text='ANTARA',
           command=click,
           font='Arial 20',
           bg='blue',
           activebackground='red',
           )
img=PhotoImage(file='Untitled.png')
l_logo=Label(root,image=img)
l_logo.place(x=150,y=360)
btn.pack()




root.mainloop()
