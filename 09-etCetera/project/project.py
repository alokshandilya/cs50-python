import json
from tabulate import tabulate


def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    task_name = input("Enter the task: ")
    tasks.append({"task": task_name, "completed": False})
    save_tasks(tasks)
    print("Task added successfully!")


def mark_task_completed(tasks):
    task_index = int(input("Enter the task index to mark as completed (1-based): ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed!")
    else:
        print("Invalid task index. Please enter a valid index.")


def display_tasks(tasks):
    headers = ["S.No.", "Task", "Completed"]
    table = tabulate(
        [
            [i + 1, task["task"], "✅" if task["completed"] else "❌"]
            for i, task in enumerate(tasks)
        ],
        headers,
        tablefmt="grid",
    )
    print(table)


def main():
    tasks = load_tasks()
    while True:
        print("\nTasker Application")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Display Tasks")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            mark_task_completed(tasks)
        elif choice == "3":
            display_tasks(tasks)
        elif choice == "4":
            print("Exiting Tasker Application. Have a great day!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
