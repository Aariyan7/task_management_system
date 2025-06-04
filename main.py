from DATABASE.db import DataBase
from USER.user import User
from TASK.task import Task

exit = False

db = DataBase()
db.connect()

user = User(db=db)

while not exit:
   print("OPTIONS: ") 
   print("1. Login")
   print("2. Sign Up")
   print("3. Exit")

   option = int(input("Enter any option from above: "))
   
   # Login Option
   if option == 1:
      user_name = input("Enter your user name: ")
      user_password = input("Enter your password: ")

      user.login(user_name=user_name, user_password=user_password)
      
      # Task Options
      if user.is_logedin:
        task_exit = False
        
        while not task_exit:
            
            print("Task Options: ")
            print("1. Add a task")
            print("2. View Task")
            print("3. Update task")
            print("4. Exit")

            # Initiazlize the Task Class
            task = Task(db=db, user_id=user.user_id)
            
            # Get the task option
            task_option = int(input("Enter any option from above: "))
            add_task_exit = False
            
            # Add task Option
            if task_option == 1:

                while not add_task_exit:
                    
                    task_name = input("Enter the task name: ")
                    task_description = input("Enter the task description: ")
                    
                    task.add_task(task_name=task_name, task_description=task_description)

                    want_to_exit = input("Do you want to add another task(yes, no): ")

                    if want_to_exit == "yes":
                        continue
                    else:
                        add_task_exit = True

            # View Task Option
            elif task_option == 2:
                task.view_tasks()
            
            # Update Option
            elif task_option == 3:
                task_title = input("Enter the Task Title of an existing Task: ")
                task.update_task(task_title = task_title)
            
            # Exit option
            elif task_option == 4:
                task_exit = True

            else:
                print("Enter a valid option from above")
      
   # Sign Up Option
   elif option == 2:
        user_name = input("Enter your User User Name: ")
        user_password = input("Enter your password: ")

        user.signup(user_name=user_name, user_password=user_password)

   # Exit Option  
   elif option == 3:
        exit = True  
        db.close()

        
            





