#ques1
from tkinter import *
root = Tk()
Label(root,text='Output is').pack()
scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill='y')
mylist=Listbox(root,yscrollcommand=scrollbar.set)
d = {"one": 1, "two": 2, "three": 3}
for key in d:
    mylist.insert(END, '{}: {}'.format(key, d[key]))
mylist.pack(side=LEFT,fill=BOTH)
scrollbar.config(command=mylist.yview)
root.mainloop()

#ques2
import tkinter as tk
data = {"Field 1": 1,
        "Field 2": 2,
        "Field 3": 3,
        "Field 4": 4,}
class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.variables ={}
        for label in sorted(data.keys()):
            self.variables[label] = tk.IntVar()
            cb = tk.Checkbutton(self, text=label,
                                onvalue=data[label], offvalue=0,
                                variable=self.variables[label])
            cb.pack(side="top", fill="x")


        button = tk.Button(self, text="Submit", command=self.OnSubmit)
        button.pack()

    def OnSubmit(self):
        for field in sorted(data.keys()):
            print ("Value for %s: %s" % (field, self.variables[field].get()))

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()