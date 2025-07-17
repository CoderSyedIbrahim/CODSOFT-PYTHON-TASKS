# To-Do List App (Console Version)

todo_list = []

def show_menu():
    print("\n========= TO-DO LIST MENU =========")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")
    print("===================================")

def view_tasks():
    if not todo_list:
        print("\n📭 No tasks added yet.")
    else:
        print("\n📋 Your Tasks:")
        for idx, task in enumerate(todo_list, 1):
            print(f"{idx}. {task}")

def add_task():
    task = input("✍️ Enter a new task: ").strip()
    if task:
        todo_list.append(task)
        print("✅ Task added successfully!")
    else:
        print("⚠️ Task cannot be empty.")

def remove_task():
    view_tasks()
    if not todo_list:
        return
    try:
        task_num = int(input("🗑️ Enter the task number to remove: "))
        if 1 <= task_num <= len(todo_list):
            removed = todo_list.pop(task_num - 1)
            print(f"✅ Removed task: {removed}")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

# Main Program Loop
while True:
    show_menu()
    choice = input("👉 Choose an option (1-4): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("👋 Exiting To-Do List App. Goodbye!")
        break
    else:
        print("⚠️ Invalid choice. Please select from 1 to 4.")
