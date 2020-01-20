from tkinter import *
root = Tk()#create widget
button1 = Button(text="RED",command=lambda :root.configure(bg="red"))
button1.pack()
button2= Button(text="BLUE",command=lambda :root.configure(bg="blue"))
button2.pack()
button3=Button(text="Green",command=lambda :root.configure(bg="green"))
button3.pack()
root.mainloop()