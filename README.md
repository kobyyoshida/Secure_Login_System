# Secure_Login_System
Created by Koby Yoshida
Created with Python, Tkinter and SQLite3


Application Description:
Login system through Tkinter GUI and SQLite database. The application ensures a secure login system by converting user input to MD5 hashes. All values stored in the SQLite3 database are also stored as MD5 hashes. These hashes are compared and if matched, allow a successful login. By comparing hashes instead of plain ASCII text, even if there was a breach to the database, it would be very difficult to crack the hashes.


HOW THE APPLICATION WORKS

First, the application looks for a database in the local directory called login.sqlite. If there is no such database, a new one will be created along with the appropriate table and columns.

Then, the user has the option to enter a username/password to authenticate, or create a new username password combination.


How the login authentication works:
- If the user enters credentials, all hashed usernames are pulled out of the database to be iterated and compared to the hashed user input.
- If there is no match, "Incorrect credentials".
- If there is a match, the Primary Key of the user (userID) is used to get the value of the password stored in the same tuple. This hashed value is compared with the hashed user input for password.
- If the passwords do not match, "Incorrect credentials".
- If the passwords match, "LOGIN SUCCESSFUL".


How creating a new user works:
- User is prompted to enter text for a new username and password.
- The values are converted to MD5 hashes and stored into the database.


How the system handles duplicates:
- When the user-inputted username matches with multiple username hashes stored in the database, all userIDs are pulled to be iterated and compared when checking the password hashes. Then, if one matches, "LOGIN SUCCESSFUL"

*IF THERE IS A COMBINATION WITH THE SAME USERNAME AND PASSWORD*

The application will only print "LOGIN SUCCESSFUL"
