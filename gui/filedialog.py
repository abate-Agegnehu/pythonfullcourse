from tkinter import*
from tkinter import filedialog


def openFile():
    filepath=filedialog.askopenfilename(initialdir="/home/abate/Coding/AI/gui",
                                        title="Open file okey?",
                                        filetypes=(("text files","*.txt"),
                                                  ( "all files","*.*"),
                                                  ("python","*.py"),
                                                  ("Html","*.html")
                                                    )
                                        )
    file=open(filepath,'r')
    print(file.read())

window=Tk()
button=Button(text="Open",command=openFile)
button.pack()
window.mainloop()