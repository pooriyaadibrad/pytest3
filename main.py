from tkinter import *
import messagebox


win=Tk()

win.geometry("%dx%d+%d+%d"%(500,500,400,200))

win.resizable(False,False)
win.iconbitmap("icon/mainicon.ico")

win.configure(bg="#1D5D9B",)

#def
def sum(e):
    a1=int(txt1.get())
    a2=int(txt2.get())
    messagebox.showinfo("sum",str(a1%a2))
#txt
txt1=Entry(win,width=20)
txt1.configure(bg="red",font="20 ")

txt1.place(x=200,y=170)

txt2=Entry(win,width=20)
txt2.configure(bg="red",font="20 ")

txt2.place(x=200,y=200)
#lbl
lbl1=Label(win,text="user",bg="green",fg="#F4D160",font="20")



lbl1.place(x=100,y=170)
lbl2=Label(win,text="password",bg="green",fg="#F4D160",font="20")



lbl2.place(x=100,y=200)


#btn
btn1=Button(win,text="login")

btn1.configure(bg="#F11A7B",fg="white",width=10,height=1,font="10",)
btn1.bind("<Button-1>",sum)
btn1.place(x=200,y=250)
btn2=Button(win,text="sum")

btn2.configure(bg="#F11A7B",fg="white",width=10,height=1,font="10",)
btn2.bind("<Button-1>",sum)
btn2.place(x=200,y=350)

btn2=Button(win,text="multi")

btn2.configure(bg="#F11A7B",fg="white",width=10,height=1,font="10",)

btn2.place(x=350,y=350)
win.mainloop()