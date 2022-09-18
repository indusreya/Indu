# import modules
from tkinter import *
import winapps
 
# function to attach output
def app():
 
    for item in winapps.search_installed(e.get()):
        name.set(item.name)
        version.set(item.version)
        Install_date.set(item.install_date)
        publisher.set(item.publisher)
        uninstall_string.set(item.uninstall_string)
 
 
# object of tkinter
# and background set for gray
master = Tk()
master.configure(bg='light gray')
 
# Variable Classes in tkinter
name = StringVar()
version = StringVar()
Install_date = StringVar()
publisher = StringVar()
uninstall_string = StringVar()
 
 
# Creating label for each information
# name using widget Label
Label(master, text="Enter App name : ",
      bg="light gray").grid(row=0, sticky=W)
Label(master, text="Name : ",
      bg="light gray").grid(row=2, sticky=W)
Label(master, text="Version :",
      bg="light gray").grid(row=3, sticky=W)
Label(master, text="Install date :",
      bg="light gray").grid(row=4, sticky=W)
Label(master, text="publisher :",
      bg="light gray").grid(row=5, sticky=W)
Label(master, text="Uninstall string :",
      bg="light gray").grid(row=6, sticky=W)
 
 
# Creating label for class variable
# name using widget Entry
Label(master, text="", textvariable=name,
      bg="light gray").grid(row=2, column=1, sticky=W)
Label(master, text="", textvariable=version,
      bg="light gray").grid(row=3, column=1, sticky=W)
Label(master, text="", textvariable=Install_date,
      bg="light gray").grid(row=4, column=1, sticky=W)
Label(master, text="", textvariable=publisher,
      bg="light gray").grid(row=5, column=1, sticky=W)
Label(master, text="", textvariable=uninstall_string,
      bg="light gray").grid(row=6, column=1, sticky=W)
 
 
e = Entry(master, width=30)
e.grid(row=0, column=1)
 
# creating a button using the widget
b = Button(master, text="Show", command=app, bg="Blue")
b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5,)
 
mainloop()
