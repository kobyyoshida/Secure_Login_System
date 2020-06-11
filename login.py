from tkinter import *
import hashlib
import sqlite3

conn = sqlite3.connect('login.sqlite')
c = conn.cursor()

#Create the table if it doesnt already exist
t = 'CREATE TABLE IF NOT EXISTS LoginCredentials (username VARCHAR (32), password VARCHAR (32), userID INTEGER PRIMARY KEY AUTOINCREMENT)'
c.execute(t)
conn.commit()

#Function for hiding something from the screen
def forget(widget):
    widget.place_forget()

#When the add new user button is clicked
def addNewUserPage():
    #New frame
    newUserFrame = Frame(root)
    newUserFrame.place(relwidth=.9,relheight=.9,relx=.05,rely=.03)

    #Text fields and labels
    usernameLabel = Label(newUserFrame, text="Create username:")
    usernameEntry = Entry(newUserFrame, width=30)
    usernameLabel.place(relx=.25, rely=.3)
    usernameEntry.place(relx=.37, rely=.3)

    passwordLabel = Label(newUserFrame, text="Create password:")
    passwordEntry = Entry(newUserFrame, show="*", width=30)
    passwordLabel.place(relx=.25, rely=.35)
    passwordEntry.place(relx=.37, rely=.35)

    #Buttons
    enter = Button(text="Enter", fg="green", command=lambda: insertToDB(usernameEntry.get(), passwordEntry.get()))
    enter.place(relx=.45, rely=.4)

    back = Button(newUserFrame,text="Back",command=lambda: forget(newUserFrame))
    back.place(relx=.3,rely=.4)

#Inserting hashed strings to database
def insertToDB(username, password):
    #Convert user input to md5 hash
    hashedUsername = hashlib.md5(username.encode('UTF-8')).hexdigest()
    hashedPassword = hashlib.md5(password.encode('UTF-8')).hexdigest()

    #Insert hashes into database
    c.execute("INSERT INTO LoginCredentials(username,password) VALUES (?,?)",(hashedUsername,hashedPassword))
    conn.commit()

    print("User Created")

#When the enter button is clicked to try to log in
def authenticate(username,password):

    matchedUsername = False
    matchedPassword = False

    #Convert the user input to hashes
    hashedUsername = hashlib.md5(username.encode('UTF-8')).hexdigest()
    hashedPassword = hashlib.md5(password.encode('UTF-8')).hexdigest()

    #Select all usernames to compare user input to
    c.execute("SELECT username FROM LoginCredentials")
    query = c.fetchall()

    length = len(query)

    #Iterate through all values in DB
    for i in range(length):
        dbUsername = query[i][0]

        #Compare hash to db value
        if dbUsername == hashedUsername:
            matchedUsername = True
            print("Successful Username")

    #Select all passwords to compare user input to
    c.execute("SELECT password FROM LoginCredentials")
    query = c.fetchall()

    #Iterate through all values in DB
    for i in range (length):
        dbPassword = query[i][0]

        #Compare hash to db value
        if dbPassword == hashedPassword:
            matchedPassword = True
            print("Successful Password")

    if matchedUsername == True and matchedPassword == True:
        print("LOGIN SUCCESSFUL")

    else:
        print("LOGIN UNSUCCESSFUL")


#Main function
root = Tk()
root.geometry("1000x1000")

title = Label(text="Login Screen")
title.place(relx=.4,rely=.15)

#Text fields and labels
usernameLabel = Label(root, text="Username:")
usernameEntry = Entry(root, width=30)
usernameLabel.place(relx=.25, rely=.3)
usernameEntry.place(relx=.37, rely=.3)

passwordLabel = Label(root, text="Password:")
passwordEntry = Entry(root, width=30,show="*")
passwordLabel.place(relx=.25, rely=.35)
passwordEntry.place(relx=.37, rely=.35)

#Buttons
enter = Button(text="Enter",fg="green",command=lambda: authenticate(usernameEntry.get(),passwordEntry.get()))
enter.place(relx=.45,rely=.4)

newUserButton = Button(text="Create New Account", command=addNewUserPage)
newUserButton.place(relx=.6,rely=.4)

root.mainloop()