import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="todo_user",       # 👈 Your new username
    password="todo_pass",   # 👈 Your new password
    database="todo_app"     # 👈 Your database name
)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    task VARCHAR(255) NOT NULL
)
''')
conn.commit()

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

def update_tasks(index, new_task):
    try:

        todo_list[index] = new_task
        print("New task updated.")
    except IndexError:
        print("Invalid Index Number.")




add_tasks()
view_tasks()
update_tasks(0, "Updated Task")


cursor.close()
conn.close()


