def display_menu():
    print("\nMenu:")
    print("1.Add Tasks")
    print("2.View Tasks")
    print("3.Mark as Done")
    print("4.Exit")
def add_task(tasks):
    task = input("Enter task description:")
    tasks.append(task)
    print("Task addded successfully!")
def view_tasks(tasks):
    if not tasks:
        print("No tasks to view.")
        return
    print("\nTasks:")
    for i,task in enumerate(tasks,start=1):
        print(f"{i}.{task}")
def mark_task_done(tasks):
    if not tasks:
        print("No tasks to mark as done.")
        return
    view_tasks(tasks)
    index = int(input("Enter task index to mark as done:"))-1
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        print(f"Task '{removed_task}' marked as done and removed.")
    else:
        print("Invalid task index.")
def save_tasks(tasks):
    with opean("tasks.txt","W") as f:
        for task  in tasks:
            f.write(task + '\n')
def load_tasks():
    try:
        with open("tasks.txt","r") as f:
            return
        f.read().splitlines()
    except FileNotFoundError:
                return[]
def main():
    tasks=load_tasks()
    while True:
        display_menu()
        choice = input("Enter your choice:")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            save_tasks(tasks)
            break
        else:
            print("Invalid choice.please select a valid option.")
if __name__ == "__main__":
    main()
