import json
import os

tasks = []

def load_tasks():
    global tasks
    if os.path.exists("todolist.json"):
        with open("todolist.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            tasks = [tuple(item) if len(item) == 3 else (item[0], item[1], False) for item in data]

def save_tasks():
    with open("todolist.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)

load_tasks()

def todo_list():
    global tasks

    while True:
        print("\n1. Add task\n2. Remove task\n3. List tasks\n4. Complete task\n5. Exit")
        choice = input("Choose an option (1/2/3/4/5): ")

        if choice == "1":
            new_task = input("Enter task: ")
            date = input("Enter date (YYYY-MM-DD): ")
            tasks.append((new_task, date, False))
            save_tasks()
            print("Task added.")

        elif choice == "2":
            task_to_remove = input("Enter task to remove: ")
            found = False
            for item in tasks:
                if item[0] == task_to_remove:
                    tasks.remove(item)
                    found = True
                    save_tasks()
                    print("Task removed.")
                    break
            if not found:
                print("Task not found in the list.")

        elif choice == "3":
            print("\nTask List:")
            if not tasks:
                print("The list is empty.")
            else:
                for i, item in enumerate(tasks, start=1):
                    status = "✓" if item[2] else "x"
                    print(f"{i}. {item[0]} ({item[1]}) [{status}]")

        elif choice == "4":
            completed_task = input("Enter completed task: ")
            for i in range(len(tasks)):
                if tasks[i][0] == completed_task:
                    tasks[i] = (tasks[i][0], tasks[i][1], True)
                    save_tasks()
                    print("Task marked as completed.")
                    break
            else:
                print("Task not found in the list.")

        elif choice == "5":
            print("Exit...")
            break

        else:
            print("Invalid choice, please try again.")

todo_list()
#change