"""
DecodeLabs Industrial Training Kit
Python Programming - Project 1: The To-Do List

Goal: Build a program where users can add tasks to a list and view them.
Key Skill: Lists (append & print loops)
"""


def show_menu():
    """Display the main menu options."""
    print("\n===== TO-DO LIST =====")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Exit")
    print("=======================")


def add_task(my_tasks):
    """Add a new task to the list."""
    task = input("Enter the task you want to add: ").strip()
    if task:
        my_tasks.append(task)
        print(f'✅ Task added: "{task}"')
    else:
        print("⚠️  Task cannot be empty. Please try again.")


def view_tasks(my_tasks):
    """Display all tasks currently stored in the list."""
    if not my_tasks:
        print("📭 Your to-do list is empty. Add a task first!")
        return

    print("\n--- Your Tasks ---")
    # enumerate() gives us both the index (ID) and the value (task) at once
    for index, task in enumerate(my_tasks, start=1):
        print(f"{index}. {task}")
    print("------------------")


def main():
    # This is our "storage" -- an empty list that lives in memory (RAM)
    # while the program runs. It's the foundation every database builds on.
    my_tasks = []

    while True:
        show_menu()
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            add_task(my_tasks)
        elif choice == "2":
            view_tasks(my_tasks)
        elif choice == "3":
            print("👋 Goodbye! Your tasks lived only in memory this session.")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
