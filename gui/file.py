from tkinter import *
from tkinter import filedialog
def saveFile():
    file=filedialog.asksaveasfile(defaultextension=".txt",
                                  filetypes=(
                                      ("text files","*.txt"),
                                      ("all files","*.*")
                                      )
                                  )
    if file is None:
        return
    filetext=str(text.get("1.0",END))
    # filetext=input("Enter some text I gusses: ")
    file.write(filetext)
    file.close()

window=Tk()

button=Button(text="Save",command=saveFile)
button.pack()
text=Text()
text.pack()
window.mainloop()