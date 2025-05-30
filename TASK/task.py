from DATABASE.db import DataBase
from mysql.connector import Error
from USER.user import User

class Task:
    def __init__(self, db, user_id):
        self.db = db
        self.connection = db.connection
        self.cursor = db.cursor
        self.user_id = user_id
        
    # Add a task
    def add_task(self, task_name:str, task_description:str, status = None):
        try:
            if self.connection.is_connected():

                if status == None:
                    task_insert_query = """INSERT INTO task(user_id, task_name, task_description) VALUES(%s, %s, %s)"""
                    self.cursor.execute(task_insert_query, (self.user_id, task_name, task_description))
                    self.connection.commit()
                    print("Task Added sucessfully")

                else:
                    task_insert_query = """INSERT INTO TASK VALUES(%s, %s, %s, %s)"""
                    self.cursor.execute(task_insert_query, (self.user_id, task_name, task_description, status))
                    self.connection.commit()
                    print("Task Added sucessfully")

            else:
                print("Data Base has been disconnected while adding a task")
        
        except Error as e:
                print("Something wrong while adding a task", e)
    
    # View users tasks
    def view_tasks(self):
        try:
            if self.connection.is_connected():
                view_tasks_query = """SELECT task_name, task_description, status FROM task WHERE user_id = %s"""

                self.cursor.execute(view_tasks_query, (self.user_id,))
                tasks = self.cursor.fetchall()

                if tasks is None:
                     print("No Tasks")
                else:
                    # Print the  tasks
                    task_num = 1
                    for task in tasks:
                        print(f"Task {task_num}:")
                        print(f"    Task name: {task[0]} \n    Task_description: {task[1]} \n    Task Status: {task[2]}")
                        task_num += 1
            
            else:
                print("Data Base has been disconnected while viewing tasks")
            
        except Error as e:
            print("Something went worng while viewing the tasks",e)






                