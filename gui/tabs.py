from tkinter import *
from tkinter import ttk

window=Tk()
notebook=ttk.Notebook(window)#this widget that manage a collection of windows and display

tab_1=Frame(notebook)# new fram for tab 1
tab_2=Frame(notebook)# new fram for tab 2

notebook.add(tab_1,text="Tab 1")
notebook.add(tab_2,text="Tab 2")
notebook.pack(expand=True,fill="both")#expand= expand to fill any space otherwise used
                                      #fill=fill space on x axis and y axis
# Button(tab_1,text="click me tab1").pack()
# Button(tab_2,text="click me tab2" ).pack()

Label(tab_1,text="Hello, this is tab1",width=50,height=25).pack()
Label(tab_2,text="Goodby, this is tab2",width=50,height=25).pack()


window.mainloop()   