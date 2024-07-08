def task():
    tasks = []
    print("---------------WELCOME TO TASK MANAGER APP--------------------")
    total_tasks = int(input("Enter the number of tasks you want to add: "))
    for i in range(1,total_tasks+1):
        task_name = input(f"Enter task {i}: ")
        tasks.append(task_name)
    print(f"Today tasks are\n {tasks}")

    while True:
        try:
            operation = int(input("Press 1 to add\nPress 2 to remove\nPress 3 to update\nPress 4 to view\nPress 5 to Exit\n"))
            if operation == 1:
                add = input("Enter the task you want to add: ")
                tasks.append(add)
                print(f"Task {add} has been successfully added")
                print(f"Now total tasks are {tasks}")

            elif operation == 2:
                remove = input("Enter task you want to remove: ")
                if remove in tasks:
                    ind = tasks.index(remove)
                    del tasks[ind]
                    print(f"Now total tasks are {tasks}")
                else:
                    print(f"Task {remove} not found")

            elif operation == 3:
                update_val = input("Enter the task you want to update: ")
                if update_val in tasks:
                    up = input("Enter new task: ")
                    ind = tasks.index(update_val)
                    tasks[ind] = up

                    print(f"Total tasks are {tasks}")
                else:
                    print("Tasks not found")

            elif operation == 4:
                print(f"Total tasks are {tasks}")

            elif operation == 5:
                print("Closing...............")
                break

            else:
                print("Please enter correct value from 1 to 5")

        except ValueError:
            print("Invalid Please Enter a no between 1 to 5")

task()
