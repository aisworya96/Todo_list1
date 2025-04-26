

todo_list = []

def add_tasks():
    tasks = input("Enter your task: ")
    todo_list.append(tasks)
    print("Task added")


def view_tasks():
    if not todo_list:
        print("No Tasks Found.")
        return
    i = 1
    for task in todo_list:
        print(str(i) + "." + task )
        i = i + 1
add_tasks()
view_tasks()



