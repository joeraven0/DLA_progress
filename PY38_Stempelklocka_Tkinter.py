from tkinter import *
from datetime import datetime
from tkinter import scrolledtext

window = Tk()


window.title("Stämpelklocka")
def instempel():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    msgSaveString = "IN: " + current_time
    msgString = "Instämpel: " + current_time + '\n' + "Hehehe\n\n"
    #msgScroll.delete(1.0,END)
    msgScroll.insert(INSERT,msgString)
    msgScroll.yview(END)

def utstempel():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    msgScroll.configure(text="Utstämpel: " + current_time)
    
#Elements
titlelbl = Label(window, text="STÄMPLA", font=("Arial Bold", 50))

titlelbl.grid(column=0, row=0)

msgScroll = scrolledtext.ScrolledText(window,width=30,height=10)

msgScroll.grid(column=0, row=1)

btnin = Button(window, text="IN", command=instempel,font=("Arial Bold",20))

btnin.grid(column=0, row=2)

btnut = Button(window, text="UT", command=utstempel, font=("Arial Bold",20))

btnut.grid(column=1, row=2)

txt = Entry(window,width=20)
txt.grid(column=0, row=3)

#STYLING
#window.geometry('350x200')

window.mainloop()




