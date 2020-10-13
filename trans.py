from googletrans import Translator
#translator = Translator()
#rans = translator.translate("shubh ratri krutik")

#print(trans.text)

import pyttsx3 as pp

#engine  = pp.init()
#engine.say(trans.text)
#engine.runAndWait()

import tkinter as tk

root = tk.Tk()
root.geometry("400x500")
root.title("TRANSALTOR  HINDI TO ENGLISH")
root.configure(background="black")
f=("Helvetica",18,"bold")

def transl():
	global translate_ans
	translator = Translator()
	trans = translator.translate(name.get())
	translate_ans = trans.text
	print(translate_ans)
	textb.insert('end',translate_ans)

def Speak():
	engine  = pp.init()
	engine.say(translate_ans)
	engine.runAndWait()
	

def Clear():
	textb.delete("1.0","end")
	textf.delete("0","end")

	

label = tk.Label(root,text = "Enter the text",font =f,fg="white",bg="black")
label.place(x=10,y=15,width=150,height=20)

name = tk.StringVar()
textf=tk.Entry(root,textvariable =name,bg = "yellow")
textf.place(x=180,y=15,width=200,height=50)


btn=tk.Button(root,text="Translate",font=f,command= transl)
btn.place(x=20,y=100)

btn=tk.Button(root,text="Speak",font=f,command = Speak)
btn.place(x=165,y=100,width=100)

btn=tk.Button(root,text="Clear",font=f,command = Clear)
btn.place(x=275,y=100,width=100)

textb=tk.Text(root,bg= "yellow")
textb.place(x=25,y=170,width=350,height=100)

root.mainloop()
