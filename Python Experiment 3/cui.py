tasks = []
def add_task(task):
     tasks.append(task)
     print(f"Task '{task}' added.")
     
def view_tasks():
     if tasks:
         print("\nYour tasks:")
         for idx, task in enumerate(tasks, 1):
             print(f"{idx}. {task}")
     else:
         print("\nNo tasks to show.")
def remove_task(task_number):
     if 0 < task_number <= len(tasks):
         removed_task = tasks.pop(task_number - 1)
         print(f"Task '{removed_task}' removed.")
     else:
         print("Invalid task number.")
def main():
     while True:
         print("\nOptions: ")
         print("1. Add Task")
         print("2. View Tasks")
         print("3. Remove Task")
         print("4. Exit")
         choice = input("Enter your choice: ")
         if choice == '1':
             task = input("Enter task: ")
             add_task(task)
         elif choice == '2':
             view_tasks()
         elif choice == '3':
             try:
                 task_number = int(input("Enter task number to remove: "))
                 remove_task(task_number)
             except ValueError:
                 print("Invalid input. Please enter a valid number.")
        elif choice == '4':
                 print("Exiting...")
                 break
        else:
                 print("Invalid choice. Please try again.")
    if __name__ == "__main__":
             main()
