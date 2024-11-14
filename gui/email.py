from tkinter import *
import smtplib

sender="abate@gmail.com"
reciever="dilbo@gmail.com"
password="password123"
subject="Python email test"
body="I wrote an email to dilbo"

message=f"""From: Mr.{sender}
To:Mr.{reciever}
Subject: {subject}\n
{body}


"""

server=smtplib.SMTP("smtp.gmail.com",587)# smtplib-=simple mail transfer protocol libirary
server.starttls#starttls=start transport layer security

server.login(sender,password)
print("Loged in...")

server.sendmail(sender,reciever,message)
window=Tk()
window.mainloop()