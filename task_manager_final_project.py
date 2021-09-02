"""
this program is a task manager: user can login, change login details, add tasks, read tasks, edit tasks, admin can register new users, generate reports and view statistics
-this program uses functions for each action
-this program reads, writes and uses data from txt files
"""
#import datetime to determine overdue tasks
from datetime import datetime

#define functions

def return_to_menu():
    choice = input("Return to main menu? y/n")

    #return boolean value based on user's choice
    if choice == 'n':
        return False
    elif choice == 'y':
        return True
    
def login():
    #open user login details file
    with open('user.txt', 'r+') as login_file:

        #set login status to false
        login = False

        #while loop while user enters login details
        while login == False:
            username = input("Please enter your username: ")
            password = input("Please enter your password: ")

            #concatenate username and password to be used in later conditon
            username_password = (f"{username}, {password}")

            #for loop to read the login details on file
            for line in login_file:

                #strip newline characters
                line = line.strip()

                #condition to secure username and password pair for valid login
                if username_password in line:
                    login = True

            #conditional statement to display error message
            if login == False:
                print("Your details are invalid, try again!")

            #set cursor to beginning of file
            login_file.seek(0)
            
    return username
    
def menu(user):
    #display menu and save selection to variable
    print("")

    if username == "admin":

        selection = input("""Please select one of the following options: \n
    r - register user \n
    a - add task \n
    va - view all tasks \n
    vm - view my tasks \n
    gr - generate reports \n
    st - display statistics\n
    e - exit \n""")
            
    else:
        print("")
        selection = input("""Please select one of the following options: \n
    r - register user \n
    a - add task \n
    va - view all tasks \n
    vm - view my tasks \n
    e - exit \n""")

    #return selection variable to main program
    return selection

def reg_user(user):
    
    #conditonal statement to ensure only 'admin' can register new users
    if username == "admin":
        
        #prompt user for new username
        new_username = input("Enter new username: ")

        #empty varibale to store file data
        file_data = ""
        
        #open file to read existing usernames
        with open('user.txt') as login_file:

            #read file and store in variable
            file_data = login_file.read()
            #check that the username doesn't already exist in the file, continuing until a new name is entered(stored passwords are also unavailable as usernames)
            while new_username in file_data:
                #prompt user for new username
                new_username = input("Enter new username: ")

        #prompt user for new password
        new_password = input("Enter new password: ")

        #confirm new password
        confirm_password = input("Enter the password again, to confirm: ")

        #while loop to confirm password
        while new_password != confirm_password:
            new_password = input("Enter new password: ")
            confirm_password = input("Enter the password again, to confirm: ")

        #open user file to append new user details to file
        with open('user.txt', 'a') as login_file:

            #write new user details on new line
            login_file.write("\n")
            login_file.write(f"{new_username}, {new_password}")

            #set cursor to beginning of file
            login_file.seek(0)

    elif username != "admin":
        print("You are not authorised to register a new user!")

def add_task():
    #prompt for task details
    task_username = input("Who does the task belong to(username)?: ")
    task_title = input("What is the title of the task?:")
    task_description = input("Describe the task: ")
    today = input("Enter today's date (day month year): ")
    task_due = input("When is this task due? (day month year) ")
    status = "No\n"

    #append new details to a file
    #[user, task, description, date added, date due, complete]
    with open('tasks.txt', 'a') as task_file:

        #write new details to file
        task_file.write(f"{task_username}, {task_title}, {task_description}, {today}, {task_due}, {status}")
    
def view_all():
    #open file in read mode
    with open('tasks.txt', 'r') as task_file:

        #read each line and split the details into seperate items
        for line in task_file:

            #save each item to variable
            task_username, task_title, task_description, date_assigned, task_due, status = line.split(", ")

            #print each task group details
            print(f"""
Username:          {task_username}
Task Title:        {task_title}
Task Description:  {task_description}
Date Assigned:     {date_assigned}
Task Due Date:     {task_due}
Task Completed:    {status}
""")      

def view_mine(user):

    #empty list for all the tasks
    tasks_list = []
    #create task number variable:
    task_num = 0
    
    #open file in read mode
    with open('tasks.txt', 'r') as task_file:

        #read each line and split the details into separate items
        for line in task_file:

            #save details to list to access later in edit stage
            tasks_list.append(line)

            #increase task_number
            task_num += 1

            #save each item to variable
            task_username, task_title, task_description, date_assigned, task_due, status = line.split(", ")

            #conditional statement to only display current user tasks and to perform subsequent functions
            if username == task_username:
                
                #print each task group details
                print(f"""
Task Number:       {task_num}
Username:          {task_username}
Task Title:        {task_title}
Task Description:  {task_description}
Date Assigned:     {date_assigned}
Task Due Date:     {task_due}
Task Completed:    {status}
""")

        #allow user to select specific task
        user_num = int(input("Select the number of the task you would like to mark or edit\n"
                             "or type -1, for main menu:\n"))
        
        #conditional statement to return to main menu(-1), mark or edit the task
        if user_num == -1:
            
            #set display menu to True, which will run the display menu again
            display_menu = True
                        
        #else, in accordance with the task number, edit: 
        else:
            
            #assign task to edit, to the index where the task is stored in the list [-1 because index starts at 0]
            task = tasks_list[user_num -1]

            #allow user to edit task, by accessing the task at its index and splitting the item into its parts
            task_username, task_title, task_description, date_assigned, task_due, status = task.split(", ")

            #condition that task can only be edited if it hasn't been completed
            if status == "No\n":
                
                #prompt user to edit
                mark_or_edit = input("Would you like to mark the task as complete or would you like to edit the task?\n"
                                     "(mark/edit):")

                #conditional statement to mark or edit
                if mark_or_edit == "mark":
                    #change status to yes
                    status = "Yes\n"
                    
                elif mark_or_edit == "edit":
                    #prompt user to change username or due date
                    name_or_due = input("Would you like to change the username or the due date?\n"
                                        "(name/due):")

                    #conditional to change username or due date
                    if name_or_due == "name":
                        task_username = input("Please enter the new username:")
                        
                    elif name_or_due == "due":
                        task_due = input("Please enter new due date (day month year):")
                    

                #save edited details to task variable
                task = (f"{task_username}, {task_title}, {task_description}, {date_assigned}, {task_due}, {status}")
                #return updated task to task_list
                tasks_list[user_num -1] = task

                #display successful message
                print("\nYour task has been successfuly updated :)")

            #if task has already been completed, it can't be dited
            else:
                print("\nThis task can't be edited because it's been completed!")
                
        #WRITE COMPLETE LIST TO FILE
        #open file in write mode
        with open('tasks.txt', 'w') as task_file:

            #join list of tasks to one string
            updated_tasks = "".join(tasks_list)

            #write to file
            task_file.write(updated_tasks)
                                                      
def stats():
    #run report generator function to create files with report dat
    generate_reports()

    #display userfriendly info
    print("")
    print("TASK STATISTICS:\n")
    #open task_report file to read
    with open('task_overview.txt', 'r') as task_report_f:
        #read each line and split data
        for line in task_report_f:
            line.split()

            #display line
            print(line)

    #display userfriendly info
    print("")
    print("USER STATISTICS:\n")
    #open user_Report file to read
    with open('user_overview.txt', 'r') as user_report_f:
        #read each line and split data
        for line in user_report_f:
            line.split()

            #display line
            print(line)
        

def generate_reports():
    #this function generates two txt files task_overview and user_overview, with statistical data from user and tasks files
    #open/create task_overview file to write statisitical data to
    with open('task_overview.txt', 'w') as task_report_f:

        #open user file to count the number of tasks
        with open('tasks.txt', 'r') as task_f:
            #set counters to 0
            num_tasks = 0
            completed_tasks = 0
            uncompleted_tasks = 0
            overdue_tasks = 0
            
            #read each line, increasing the counters
            for line in task_f:
                num_tasks += 1

                #split data of each task
                task_username, task_title, task_description, date_assigned, task_due, status = line.split(", ")

                if status == "Yes\n":
                    completed_tasks += 1
                elif status == "No\n":
                    uncompleted_tasks += 1

                    #convert due date to datetime object, to compare to current date
                    due_date = datetime.strptime(task_due, '%d %b %Y')
                    #if due_date is smaller than current date, it's overdue
                    if due_date < datetime.now():
                        overdue_tasks +=1

        percentage_incomplete = round((uncompleted_tasks/num_tasks) * 100, 2)
        percentage_overdue = round((overdue_tasks/num_tasks) * 100, 2)
                
        #write the data to task_report_f
        task_report_data = (
            f"Number of tasks: {num_tasks}\n"
            f"Completed tasks: {completed_tasks}\n"
            f"Uncompleted tasks: {uncompleted_tasks}\n"
            f"Overdue tasks: {overdue_tasks}\n"
            f"Percentage of incomplete tasks: {percentage_incomplete}%\n"
            f"Percentage of overdue tasks: {percentage_overdue}%"
            )
        #write report data to file
        task_report_f.write(task_report_data)

    #open/create user_overview file to write statistical data to        
    with open('user_overview.txt', 'w') as user_report_f:

        #open user file to count users
        with open('user.txt', 'r') as user_f:
            #set number of users to 0
            num_users = 0
            
            #read each line, increasing the counter
            for line in user_f:
                num_users += 1

       
        #empty dictionary
        user_data_dict = {}
        #open task file to collect data
        with open('tasks.txt', 'r') as task_f:
            
            #read each line, increasing the counter and spliting the data
            for line in task_f:

                #split data of each task
                task_username, task_title, task_description, date_assigned, task_due, status = line.split(", ")

                #check if username is in dictionary, else add username as a nested dictionary
                if task_username in user_data_dict:
                    #dd 1 to count another user task
                    user_data_dict[task_username]["User tasks"] += 1
                else:
                    #create nested dictionary[each dictionary is the user's name][key's are the things to count]:values are counts
                    user_data_dict[task_username] = {}
                    #set value to 1 
                    user_data_dict[task_username]["User tasks"] = 1

                #count status of tasks and add to nested dictionary
                if status == "Yes\n":
                    if "Completed tasks" in user_data_dict[task_username]:
                        #add counting value to nested dictionary
                        user_data_dict[task_username]["Completed tasks"] += 1
                    else:
                        #or add key and value to nested dictionary
                        user_data_dict[task_username]["Completed tasks"] = 1
                        
                elif status == "No\n":
                    if "Uncompleted tasks" in user_data_dict[task_username]:
                        #add counting value to nested dictionary
                        user_data_dict[task_username]["Uncompleted tasks"] += 1
                    else:
                        #or add key and value to nested dictionary
                        user_data_dict[task_username]["Uncompleted tasks"] = 1
                    

                #convert due date to datetime object, to compare to current date
                due_date = datetime.strptime(task_due, '%d %b %Y')
                #if due_date is smaller than current date, it's overdue
                if status == "No\n" and due_date < datetime.now():
                    #add to counter, 
                    if "Overdue" in user_data_dict[task_username]:
                        #add counting value to nested dictionary
                        user_data_dict[task_username]["Overdue"] += 1
                    else:
                        #or add key and value to nested dictionary
                        user_data_dict[task_username]["Overdue"] = 1

        #store num_users and num_tasks in list
        user_report_data = [f"Total number of users: {num_users}"]
        user_report_data.append(f"Total number of tasks: {num_tasks}")
        
        #loop each nested (user) dict in dict to access data for each user
        for key in user_data_dict.keys():
            #the key of each nested dictionary is the name of the user
            user = key
            #add user name to list
            user_report_data.append(f"USERNAME: {user}")
            #loop nested dictionaries to get each value associated with specific user, using get(key) to avoid key errors returns None if no key
            for value in user_data_dict[user].values():
                user_tasks = user_data_dict.get(user, {}).get('User tasks')
                completed_tasks = user_data_dict.get(user, {}).get('Completed tasks')
                uncompleted_tasks = user_data_dict.get(user, {}).get('Uncompleted tasks')
                overdue = user_data_dict.get(user, {}).get('Overdue')
                
            #do some calculations  and add data to user_report_data list
            user_report_data.append(f"Total tasks: {user_tasks}")

            percentage_tasks = round((user_tasks/num_tasks) * 100,2 )
            user_report_data.append(f"Percentage of total tasks belonging to {user}: {percentage_tasks}%")

            #conditional to skip these if the value = None
            if completed_tasks != None:
                percentage_completed = round((completed_tasks/user_tasks) * 100, 2)
                user_report_data.append(f"Percentage of {user}'s total tasks completed: {percentage_completed}%")
            if uncompleted_tasks != None:
                percentage_incomplete = round((uncompleted_tasks/user_tasks) * 100, 2)
                user_report_data.append(f"Percentage of {user}'s total tasks incomplete: {percentage_incomplete}%")
            if overdue != None:
                percentage_overdue = round((overdue/user_tasks) * 100,2 )
                user_report_data.append(f"Percentage of {user}'s tasks incomplete and overdue: {percentage_overdue}%")
                        
        #loop user_report_Data list to write each item to file
        for items in user_report_data:
            #write report data to file
            user_report_f.write('%s\n' % items)

    
"""main"""
#call login function and return username
username = login()

#boolean to loop menu
display_menu = True

while display_menu == True:

    #call menu function and return selection
    selection = menu(username)
    
    #in accordance with user selection, call function
    if selection == "r":
        #call function to register new user
        reg_user(username)
        #call display menu function
        display_menu = return_to_menu()
            
    elif selection == "a":
        #call add task function
        add_task()
        #call display menu function
        display_menu = return_to_menu()
        
    elif selection == "va":
        #call view_all function
        view_all()
        #call display menu function
        display_menu = return_to_menu()

    elif selection == "vm":
        #call view_mine function
        view_mine(username)
        #don't call menu function here, because it is called inside the vm function

    elif selection == "gr":
        #call generate reports function
        generate_reports()
        #call display menu function
        display_menu = return_to_menu()        

    elif selection == "st":
        #call stats function
        stats()
        #call display menu function
        display_menu = return_to_menu()

    elif selection == "e":
        #exit()
        display_menu = False


    
