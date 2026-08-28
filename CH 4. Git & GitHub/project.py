print("-----TASK MANAGER-----")


task = []

while True:
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Done")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task_name = input("Enter task name: ")
        task.append({"name": task_name, "done": False})
        print(f"Task '{task_name}' added.\n")
        

    elif choice == '2':
        if not task:
            print("No tasks available.\n")
        else:
            for index, t in enumerate(task):
                status = "Done" if t["done"] else "Not Done"
                print(f"{index + 1}. {t['name']} - {status}\n")

    elif choice == '3':
        if not task:
            print("No tasks available to mark as done.\n")
        else:
            for index, t in enumerate(task):
                status = "Done" if t["done"] else "Not Done"
                print(f"{index + 1}. {t['name']} - {status}\n")
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(task):
                task[task_index]["done"] = True
                print(f"Task '{task[task_index]['name']}' marked as done.\n")
            else:
                print("Invalid task number.\n")

    elif choice == '4':
        print("Exiting Task Manager. Goodbye!\n")
        break

    else:
        print("Invalid choice. Please try again.\n")