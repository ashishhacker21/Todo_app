tasks = []
def total_tasks():
    a = int(input("enter how many tasks you add --> "))
    for i in range(1, a + 1):
        add = input(f"add task {i} ->")
        tasks.append(add)

    print('_'* len(tasks)*10)
    print(f"today tasks :\n{tasks}")
    print('_' * len(tasks) * 10)

total_tasks()
print('*'*23)
while True:
    print('''1 add task
2 update task
3 delete task
4 view tasks
5 exit/save''')
    print('*'*23)
    action = input("which action you perform : ")
    match action:
        case "1":
            new_task = input("enter your new task --> ")
            if new_task not in tasks:
               tasks.append(new_task)
               print("Task added successfully".center(40,'-'))
            else:
                print("task is already exist".center(40,'-'))

        case "2":
            update = input("which task you update : ")
            if update in tasks:
                updated_task = input(f"enter which task you add place of the  {update} --> ")
                idx = tasks.index(update)
                tasks[idx] = updated_task
                print("Task updated successfully".center(40,'-'))
            else:
                print('task was not exist'.center(40,'-'))

        case "3":
            delete_task = input("enter which task you delete : ")
            if delete_task in tasks:
                idx_d = tasks.index(delete_task)
                tasks.pop(idx_d)
                if delete_task not in tasks:
                    print("delete successfully".center(40,'-'))
                else:
                    print("error! occurred".center(40,'~'))
            else:
                print("Task was not exist".center(40,'-'))

        case "4":
            print("<< view your tasks  >> ")
            print(tasks)
        case "5":
            fn = input("enter file name ")
            with open(f'{fn}.txt', 'w') as file:
                for index in enumerate(tasks, start=1):
                  file.write(f"{index}\n")
                print("tasks saved successfully".center(50,'-'))
            break










