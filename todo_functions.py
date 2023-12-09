import csv


def add_todo(file_name):
    print("Add todo")
    #Ask the title of the todo
    todo_name = input("Enter a todo: ")
    # Insert that value into the file - list.csv (use WITH statment, it opens the file, appends and closes it in one go)
    with open(file_name, "a") as f:
        writer = csv.writer(f)
        writer.writerow([todo_name, "False"])
    # while inserting - Title = user entered
                    # - completed = False

def remove_todo(file_name):
    print("Remove todo")

def mark_todo(file_name):
    print("Mark todo")

def view_todo(file_name):
    print("View todo")
    with open(file_name, "r") as f: # with statement, opens file & reads and closes
        reader = csv.reader(f) #reader variable = csv file reader
        reader.__next__() #This tells the reader to go to the next line
        for row in reader: # for loop to go through rows in the reader
            if (row[1] == "True"):
                print(f"Todo {row[0]} is completed")
            else:
                print(f"Todo {row[0]} is not complete")