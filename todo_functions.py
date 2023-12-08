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