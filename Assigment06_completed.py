# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added code to complete assignment 5
# SOrellana,05/15/2022,Modified code to complete assignment 6
# SOrellana, 05/23/2022, Added function doc strings
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoFile.txt"  # The name of the data file
objFile = None  # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strTask = ""  # Captures the user task data
strPriority = ""  # Captures the user priority data
strStatus = ""  # Captures the status of a processing function


# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            task, priority = line.split(",")
            row = {"Task": task.strip(), "Priority": priority.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows, 'Success'

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """ Adds data to the list

        :param task: (string) with new task:
        :param priority: (string) with new priority:
        :param list_of_rows: (list) of dictionary rows:
        :return: (list) of dictionary rows
        """
        row = {"Task": task.title(), "Priority": priority.title()}
        list_of_rows.append(row)
        return list_of_rows, 'New task is added!'

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        """ Removes data from the list

        :param task: (string) with a task:
        :param list_of_rows: (list) of dictionary rows:
        :return: (list) of dictionary rows
        """
        if any(task.lower() in row["Task"].lower() for row in list_of_rows):
            print("The task has been removed!")
        else:
            print("Task was not found")
        for row in list_of_rows:
            if row["Task"].lower() == task.lower():
                list_of_rows.remove(row)
        return list_of_rows, 'Success'

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Saves data into a file

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) of dictionary rows:
        :return: (list) of dictionary rows
        """
        file = open(file_name, "w")
        for line in list_of_rows:
            file.write(str(line["Task"]) + ',' + str(line["Priority"]) + "\n")
        file.close()
        return list_of_rows, 'Data was saved to the file!'


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("\n******* The current Tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        """ Gets new task and priority

        :return: (string) with a task
        :return: (string) with a priority
        """
        task = input('Enter a new task: ')
        priority = input('Enter a priority: ')
        return task, priority

    @staticmethod
    def input_task_to_remove():
        """ Gets a task to remove

        :return: (string) with a task
        """
        task = input('Enter a task to remove: ')
        return task


# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
try:
    Processor.read_data_from_file(strFileName, lstTable)  # read file data
except:
    print('No file is found. New file will be created.')

# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show current data
    IO.print_current_Tasks_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Task
        strTask, strPriority = IO.input_new_task_and_priority()
        lstTable, strStatus = Processor.add_data_to_list(strTask, strPriority, lstTable)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '2':  # Remove an existing Task
        strRemove = IO.input_task_to_remove()
        strChoice = IO.input_yes_no_choice("Proceed to remove " + strRemove.title() + " task from the list (y/n)?: ")
        if strChoice.lower() == "y":
            lstTable, strStatus = Processor.remove_data_from_list(strRemove, lstTable)
            IO.input_press_to_continue()   # status is displayed in the function above
        else:
            IO.input_press_to_continue(strRemove.title() + " remained on the list.")
        continue  # to show the menu

    elif strChoice == '3':  # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            lstTable, strStatus = Processor.write_data_to_file(strFileName, lstTable)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            try:
                lstTable, strStatus = Processor.read_data_from_file(strFileName, lstTable)
                IO.input_press_to_continue(strStatus)
            except:
                print("No file was found. Please save the data first.")
        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue  # to show the menu

    elif strChoice == '5':  # Exit Program
        print("Goodbye!")
        break  # and Exit
    else:
        print('Please only choose 1 - 5!')
