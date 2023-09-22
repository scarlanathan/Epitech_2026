import matplotlib as plt
import numpy as np

def test():
    x = np.linspace(0, 20, 100)  
    plt.plot(x, np.sin(x))       
    plt.show()           

def plot1(x_min,x_max):
    x_values = np. linspace (x_min , x_max, 1000)   #1000 c le nombre de points
    plt.plot(x_values,np.cos(x_values))
    plt.show()

def plot2():
    plt.xlim = (-1,3.5)
    plt.ylim = (10,55)
    plt.grid()
    plt.plot(0, 12, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="red")
    plt.plot(1, 32, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="red")
    plt.plot(2, 42, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="red")
    plt.plot(3, 52, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="red")
    plt.show()

def plot3(l=[(2,3),(4,6),(6,9)]):
    plt.grid()
    for i in l:
        plt.plot(i[0], i[1], marker="o", markersize=5, markeredgecolor="red", markerfacecolor="red")
    plt.show()

def f(x):
    return x

def plot4(fonct , a , b):
    plt.grid()
    x = np.linspace(a,b,1000)   #np.sin a la place de math.sin
    plt.plot(x, fonct(x))
    plt.show()

# plot4 ( np.sin , 0, 50)
# plot4 (f, -100, 200)
# plot4 ( lambda x: x**2 , -10, 10)
# plot4 ( lambda x: 1/x, -100, 100)

# Tkinter task 1 
# TEST labelframe
# from tkinter import *

# root = Tk()

# lframe = LabelFrame(root, text="Ceci est un LabelFrame")
# lframe.pack(fill="both", expand="yes")
 
# btn = Button(lframe, text ="Cliquez ici!")
# btn.pack()
 
# root.mainloop()

# TEST Frame
# from tkinter import *

# root = Tk()
# frame = Frame(root)
# frame.pack()

# bottomframe = Frame(root)
# bottomframe.pack( side = BOTTOM )

# redbutton = Button(frame, text="Red", fg="red")
# redbutton.pack( side = LEFT)

# greenbutton = Button(frame, text="Brown", fg="brown")
# greenbutton.pack( side = LEFT )

# bluebutton = Button(frame, text="Blue", fg="blue")
# bluebutton.pack( side = LEFT )

# blackbutton = Button(bottomframe, text="Black", fg="black")
# blackbutton.pack( side = BOTTOM)

# root.mainloop()

# TEST grid
# from tkinter import *

# gui = Tk()

# Label(gui, text="Firstname").grid(row=0)
# Label(gui, text="Lastname").grid(row=1)

# e1 = Entry(gui)
# e2 = Entry(gui)

# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)

# gui.mainloop()

##############################################################
# from tkinter import *
# import tkinter as tk
# from PIL import Image,ImageTk

# def tki():
#     root = tk.Tk()
#     root.geometry('400x400')

#     lframe = tk.LabelFrame(root, text="Ceci est un LabelFrame",width = 200, height = 200, padx =10,pady = 10)
#     lframe.pack(fill="both", side="left",padx = 10, pady = 10)

#     frame = tk.Frame(root,width=200,height = 200, bd =3, bg = "white")
#     frame.pack(fill="both", side="right",expand = True, padx = 10, pady = 10)

#     input = tk.Entry(lframe)
#     Label(lframe, text="Input field").pack()
#     input.pack(fill = "x", side="top", padx = 4, pady = 4)
    
#     def p():
#         a = input.get()
#         a = a.upper()
#         print(a)
#         input.delete(0,END)

#     btn = tk.Button(lframe, text ="Cliquez ici!", height = 3 , command = p)
#     btn.pack()

    
#     canva = tk.Canvas(frame,width=200,height=200)
#     canva.pack(fill = "both",expand = True)
#     root.update()

#     photo = ImageTk.PhotoImage(Image.open("image.jpg"))
#     canva.create_image(0,0,anchor = "nw", image = photo)
#     b = canva
#     def change_size(a):
#         b = a
#         w,h = get_size(b)
#         if (w > 1 and h > 1):
#             print(w,h)
#             new_img = ImageTk.PhotoImage(Image.open("image.jpg").resize((w,h)))
#             b.create_image(0,0,image = new_img, anchor = "nw")
#         root.after(100,change_size)
    
#     def get_size(a):
#         return a.winfo_width(),a.winfo_height()
    
#     change_size(b)

#     root.mainloop()

# Probleme avec le resize voir huo.py

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.master.title("Lines")
        self.pack(fill=BOTH, expand=1)

        self.canvas = Canvas(self)
        self.a = self.canvas.create_line(200, 150, 200, 300, fill= "dark green")
        self.b = self.canvas.create_line(200, 300, 150, 350, fill="violet")
        self.c = self.canvas.create_line(200, 300, 250, 350, fill="orange")
        self.d = self.canvas.create_line(200, 170, 150, 220, fill="red")
        self.canvas.create_line(200, 170, 250, 220, fill ="blue")
        self.canvas.create_oval(180, 110, 220, 150, fill = "green")
        self.canvas.create_text(90,90,anchor = W, font="Purisa", text = "Hello World")
        self.movement()
        self.canvas.pack(fill= BOTH, expand=1)

    def movement(self):
        self.canvas.coords(self.b,200,300,250,340)
        self.canvas.coords(self.c,200,300,150,355)
        self.after(300, lambda : self.reini())
    
    def reini(self):
        self.canvas.coords(self.b,200,300,150,350)
        self.canvas.coords(self.c,200,300,250,325)
        self.after(300, lambda : self.movement())



root = tk.Tk()
ex = Example()
root.geometry('400x400')






