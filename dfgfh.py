from tkinter import *
import time
from pygame import mixer
import datetime



root=Tk()
"""Define the count down function"""
def click(event):
    global t
    text=event.widget.cget('text')

    if text=="Start":
        try:

            for i in range (int(t.get()),-2,-1):


                if i==-1:

                    t.set("Times Up... \U0001F923")
                    e.update()
                    time.sleep(2)
                    t.set("")
                    break

                time.sleep(1)
                t.set(f"{i} Sec..")
                e.update()
        except Exception as f:
                 t.set(f)



    elif text=="C":
        t.set("")
        pass
    else:
         k=t.set(t.get()+str(text))
         e.update()
         with open("history.txt","a") as g:
             g.write(f"\nAt time {time.asctime(time.localtime(time.time()))}\nAlarm for {t.get()}seconds ")


"""define privious fn"""
def privious():
    j=Toplevel(root)

    with open("history.txt","r") as o:
        Label(j,text=str(o.read()),font="arial 20 bold",bg="red").pack()



t=StringVar()


root.geometry("300x500")
root.maxsize(300,500)
root.title("Stop Watch")
root.configure(background="pink")

"""menu part"""
mainmenu=Menu(root,)
m1=Menu(mainmenu,tearoff=0)
m1.add_command(label="See Previous set time",command=privious)
m1.add_command(label="exit",command=exit,activebackground="black")

mainmenu.add_cascade(label="Options",menu=m1)
mainmenu.add_cascade(label="Exit",command=quit)
root.configure(menu=mainmenu)




"""entry"""

e=Entry(root,textvariable=t,font="comiSansms 30 bold",bd=2,fg="#2F4F4F",state=DISABLED)
e.pack(side=TOP,fill=X,pady=2)

"""frame works"""
f1=Frame(root,bg="pink")
f1.pack(pady=10)
f2=Frame(root,bg="pink")
f2.pack(pady=10)
f3=Frame(root,bg="pink")
f3.pack(pady=10)
f4=Frame(root,bg="pink")
f4.pack(pady=10)

"""button"""

for i in range(1,10,1):
    if i<4:
        b=Button(f1,text=i,width=7,height=5,font="lucida 10 bold",bg="#F0FFF0")
        b.pack(side=LEFT,padx=10,pady=3)
        b.bind("<Button-1>",click)
    elif i<7:
        b=Button(f2,text=i,width=7,height=5,font="lucida 10 bold",bg="#FFF5EE")
        b.pack(side=LEFT,padx=10,pady=3)
        b.bind("<Button-1>", click)
    elif i<10:
        b=Button(f3,text=i,width=7,height=5,font="lucida 10 bold",bg="#FFF0F5")
        b.pack(side=LEFT,padx=10,pady=3)
        b.bind("<Button-1>", click)

b=Button(f4,text="C",width=7,height=5,font="lucida 10 bold",bg="red")
b.pack(side=LEFT, padx=10, pady=3)
b.bind("<Button-1>",click)

b=Button(f4,text="0",width=7,height=5,font="lucida 10 bold")
b.pack(side=LEFT, padx=10, pady=3)
b.bind("<Button-1>",click)

b=Button(f4,text="Start",width=7,height=5,font="lucida 10 bold",bg="green")
b.pack(side=LEFT, padx=10, pady=3)
b.bind("<Button-1>",click)


root.mainloop()