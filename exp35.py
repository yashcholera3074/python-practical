from tkinter import *
root=Tk()
def write_label():
    button1.destroy()
    label.config(text="Button Clicked")
label=Label(root)
label.pack()
button1 = Button(text="click me",command=write_label)
button1.pack()
root.mainloop()