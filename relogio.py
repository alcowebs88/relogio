from tkinter import *
from datetime import datetime
import time


app = Tk()
app.title('relogio')
app.geometry('200x100')
app.resizable(False,False)
app.configure(bg='black')

def tempos():
	tempo = datetime.now()
	t = tempo.strftime('%H:%M:%S')
	relogio.after(200,tempos)
	relogio.config(text=t)



relogio = Label(app,font='Arial 40',width=200,bg='black',fg='white')
relogio.pack(side=LEFT)
	

tempos()

app.mainloop()