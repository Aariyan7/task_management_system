from DATABASE.db import DataBase
from mysql.connector import Error

class User:
    def __init__(self, db):
        self.db = db
        self.connection = db.connection
        self.cursor = db.cursor
        self.is_logedin = False
        self.user_id = None

    # Sign Up Method
    def signup(self, user_name:str, user_password:str):
        try:
            if self.connection.is_connected():

                self.cursor.execute("INSERT INTO user(user_name, user_password) VALUES(%s, %s)", (user_name, user_password))
                self.connection.commit()
                print("User Added sucessfully")

            else:

                print("Data Base has been disconnected for some reason")
        
        except Error as e:

            print("Something went wrong while signing up try again", e)
    

    # Login Method
    def login(self, user_name:str, user_password:str):

        try:
            if self.connection.is_connected():

                self.cursor.execute("SELECT user_id, user_name, user_password FROM user WHERE user_name = %s AND user_password = %s", (user_name, user_password))
                row = self.cursor.fetchone()

                if row is not None:
                    login_userid = row[0]
                    login_username = row[1]
                    login_userpassword = row[2]

                    if user_name == login_username and user_password == login_userpassword:
                        print("Logged in sucessfully")
                        self.is_logedin = True
                        self.user_id = login_userid

                    else:
                        print("User name or Password is wrong")

                else:
                     print("User does not exists")

                
            else:
                print("Data Base has been disconnected for some reason")

        except Error as e:
            print("Something went wrong while logging in try again", e)
    
