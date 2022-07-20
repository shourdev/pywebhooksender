from tkinter import *
import socket
import requests


def SendMsg():
   

# Make the variables

 webhookURL = Url.get()
 
# Build the structure  of  the message 
 data = {
      'username': Name.get(),
     'embeds':[{
         'title': Title.get(),
         'description': Description.get(),
     }]
  }
# Send it 
 result = requests.post(webhookURL, json = data)

 try:
     result.raise_for_status()
 except:
    pass
# Making the window
Window = Tk()
# Config of window
Window.title("WebHook Sender")
Window.resizable(False,False)
Window.iconbitmap("appicon.ico")
Window.geometry("300x140")
# Ui Elements
Url = Entry()
UrlText = Label(text="Webhook Url")
Name =  Entry()
NameText = Label(text="Name")
Send = Button(text="Send",command=SendMsg)
Title = Entry()
TitleText = Label(text="Title")
Description = Entry()
DescriptionText = Label(text="Description")

# Position
# Url
Url.grid(row=0,column=1)
UrlText.grid(row=0,column=0)
# Name
Name.grid(row=1,column=1)
NameText.grid(row=1,column=0)
# Title
Title.grid(row=2,column=1)
TitleText.grid(row=2,column=0)
# Description
Description.grid(row=3,column=1)
DescriptionText.grid(row=3,column=0)
# Send
Send.grid(row=4,column=4)
# Display the window
Window.mainloop()