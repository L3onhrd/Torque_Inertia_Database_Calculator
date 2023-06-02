# if it's saying that the port is in use, url is in use
# kill if port in use, type in terminal/command prompt
# kill -9 $(lsof -t -i:"5000")    and then hit enter
# try again python 

#Create a database
import sqlite3
from tkinter import Variable


#Create the table or connect to it, 7 columns
connection = sqlite3.connect("MEMBERSHIP.db")
cursor = connection.cursor()

#Create a d
command1 = """ CREATE TABLE IF NOT EXISTS Users(User_ID INTEGER PRIMARY KEY, 
               Name TEXT, Username TEXT, Password TEXT,
               DOB DATE)
           """
cursor.execute(command1)

connection.close()

# Check if flask is working
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/registration", methods=["POST", "GET"])
def registration():

    if request.method == "POST": 
    # Accept the values from registration.html web page
        NAME = request.form["NAMEINPUT"]
        USERNAME = request.form["USERNAMEINPUT"]
        PASSWORD = request.form["PASSWORDINPUT"]
        DOB = request.form["DOBINPUT"]

        #connect to db and insert data into the table
        connection = sqlite3.connect("MEMBERSHIP.db")
        cursor = connection.cursor()

        cursor.execute("INSERT INTO Users VALUES (NULL,?, ?, ?, ?)",(NAME, USERNAME, PASSWORD, DOB))
        connection.commit()
        connection.close()
        
        return render_template("login.html")
    
    return render_template("registration.html")

@app.route("/registrationG", methods=["POST", "GET"])
def registrationG():

    if request.method == "POST": 
    # Accept the values from registration.html web page
        NAME = request.form["NAMEINPUT"]
        USERNAME = request.form["USERNAMEINPUT"]
        PASSWORD = request.form["PASSWORDINPUT"]
        DOB = request.form["DOBINPUT"]

        #connect to db and insert data into the table
        connection = sqlite3.connect("MEMBERSHIP.db")
        cursor = connection.cursor()

        cursor.execute("INSERT INTO Users VALUES (NULL,?, ?, ?, ?)",(NAME, USERNAME, PASSWORD, DOB))
        connection.commit()
        connection.close()
        
        return render_template("login.html")
    
    return render_template("registrationG.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        #accept these from login page
        USERNAME = request.form["USERNAMEINPUT"]
        PASSWORD = request.form["PASSWORDINPUT"]

        #connect to db and insert data into the table
        connection = sqlite3.connect("MEMBERSHIP.db")
        cursor = connection.cursor()

        # To extract data from db, use query SELECT
        cursor.execute("SELECT Username, Password, Name, DOB FROM Users WHERE Username like ?", (USERNAME,))
        result = cursor.fetchall()

        USERNAMES = result[0][0]
        Name = result[0][2]
        DOB = result[0][3]

        
        # result[0][0] is the username from db
        # result[0][1] is the password from db
        
        if result[0][0] == USERNAME and result[0][1]==PASSWORD:  # if username is equal to extracted from page
            return render_template("homepage.html", name=Name, username=USERNAMES, dob=DOB)
        else:
            return render_template("login.html")
            
        connection.commit()
        connection.close()
        
    return render_template("login.html")

@app.route("/loginG", methods=["POST", "GET"])
def loginG():
    if request.method == "POST":
        #accept these from login page
        USERNAME = request.form["USERNAMEINPUT"]
        PASSWORD = request.form["PASSWORDINPUT"]

        #connect to db and insert data into the table
        connection = sqlite3.connect("MEMBERSHIP.db")
        cursor = connection.cursor()

        # To extract data from db, use query SELECT
        cursor.execute("SELECT Username, Password, Name, DOB FROM Users WHERE Username like ?", (USERNAME,))
        result = cursor.fetchall()

        USERNAMES = result[0][0]
        Name = result[0][2]
        DOB = result[0][3]

        
        # result[0][0] is the username from db
        # result[0][1] is the password from db
        
        if result[0][0] == USERNAME and result[0][1]==PASSWORD:  # if username is equal to extracted from page
            return render_template("homepage.html", name=Name, username=USERNAMES, dob=DOB)
        else:
            return render_template("login.html")
            
        connection.commit()
        connection.close()
        
    return render_template("loginG.html")


@app.route("/homepage", methods=["POST", "GET"])
def homepage(name, username, dob):
    if request.method=="GET":
        return render_template("homepage.html", name=Name, username=USERNAMES, dob=DOB)

if __name__ =="__main__":
    app.run(debug=True) # use debug=True to read the error

