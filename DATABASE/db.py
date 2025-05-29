import mysql.connector 
from mysql.connector import Error

class DataBase:

    def __init__(self, host = "localhost", username = "root", password = "root", database = "task_management_system"):

        # Initialize the attributes
        self.host = host
        self.username = username
        self.password = password
        self.database = database

    # Connection Method
    def connect(self):
        try:
            # Initialize the object to the database
            self.connection = mysql.connector.connect(
                host = self.host,
                username = self.username,
                password = self.password,
                database = self.database
            )

            if self.connection.is_connected():
                self.cursor = self.connection.cursor()

            
        except Error as e:
            print("Cannot connect to the Data Base",e)
    
    # Close Method
    def close(self):
        
        if self.connection.is_connected():
            self.connection.close()
            self.cursor.close()
        
            



