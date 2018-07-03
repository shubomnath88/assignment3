#ques1
import tkinter as tk
r = tk.Tk()
label=tk.Label(r,text='hello world')
button=tk.Button(r,text='exit',width=30,command=r.destroy)
label.pack()
button.pack()
r.mainloop()

#ques2
import tkinter as tk
def write():
    print("wassup bro")
r = tk.Tk()
r.title('Counting Seconds')
button = tk.Button(r,text='say',width=25,command=write())
button.pack()
r.mainloop()


#ques3
from tkinter import *
root = Tk(className = "button_click_label")
root.geometry("300x300")
message = StringVar()
message.set('hi')
l1 = Label(root, text="hi")
def press():
    l1.config(text="hello")
b1 = Button(root, text = "clickhere", command = press)
b1.pack()
b = Button(root,text='exit',command=root.destroy)
b.pack()
l1.pack()
root.mainloop()


#ques4
from tkinter import *
master = Tk()
master.geometry('200x200')
master.title('Input Test')
def UserName():
    usrE1 = usrE.get()
    usrN2 = usrN.get()
    InputExcept = usrE1 + " " + usrN2
    print(InputExcept)
usrE = Entry(master, relief=SUNKEN)
usrE.pack()
usrN = Entry(master, relief=SUNKEN)
usrN.pack()
Btn1 = Button(text="Input", command=UserName)
Btn1.pack()
master.mainloop()