from tkinter import *
from PIL import *


root=Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print(screen_height,screen_width)

ls = "#d8d9f2"
win = "#F8F8F8"

root.geometry(f"{screen_width}x{screen_height}")
root.title("GUI")
root.iconbitmap("./components/editor.ico")


#define images
upload = PhotoImage(file="./components/Upload.png")

#b1 = Button(root, image=upload)
#b1.pack()

f1 = Frame(root, bg=ls, width=350)
f1.pack(side=RIGHT, fill=Y)
f2 = Frame(root, bg=win, height=500)
f2.pack(side=TOP, fill=X)
f3 = Frame(root, bg=win, height=220)
f3.pack(side=BOTTOM, fill=X)

b1 = Button(f2, image=upload)
b1.pack()


root.mainloop()
