"""
Task 1: To-do List Application
Saiket Systems - Python Development Internship
Description: A to-do list application where users can add tasks, mark them as completed and view their tasks.
"""

class Task:
    # Class to represent a single task
    def __init__(self, task_id, description):
        self.task_id = task_id
        self.description = description
        self.completed = False

    def mark_completed(self):
        # Mark the task as completed
        self.completed = True
    def mark_incomplete(self):
        # Mark the task as incomplete
        self.completed = False

    def __str__(self):
        # String Representation of the task
        status = "Completed" if self.completed else "Pending"
        return f"[{self.task_id}] {status} - {self.description}" 
    

class ToDoList:
    # Class to manage all tasks
    def __init__(self):
        self.tasks = {}
        self.task_counter = 1

    def add_task(self, description):
        # Add new tasks
        if not description.strip():
            print("Error: Task Description cannot be empty!")
            return False
        
        task = Task(self.task_counter, description)
        self.tasks[self.task_counter] = task
        print(f"Task added successfully!! (ID: {self.task_counter})")
        self.task_counter += 1
        return True

    def view_tasks(self):
        # View all tasks
        if not self.tasks:
            print("No tasks added yet! Add some tasks to get started.")
            return 
        
        print("\n" + "="*60)
        print("YOUR TO-DO LIST")
        print("="*60)
        for task_id, task in self.tasks.items():
            print(task) 
        print("="*60 + "\n")

    def mark_task_completed(self, task_id):
        # Mark a specific task as completed
        try:
            task_id = int(task_id)
            if task_id in self.tasks:
                self.tasks[task_id].mark_completed()
                print(f"Task {task_id} marked as completed.")
                return True
            
            else:
                print(f"Error: Task {task_id} not found!")
                return False
            
        except ValueError:
            print(f"Please enter a valid task ID!")
            return False
        
    def mark_task_incomplete(self, task_id):
        # Mark a specific task as incomplete
        try: 
            task_id = int(task_id)
            if task_id in self.tasks:
                self.tasks[task_id].mark_incomplete()
                print(f"Task {task_id} is marked as incomplete.")
                return True
            
            else:
                print(f"Task {task_id} not found!")
                return False
            
        except ValueError:
            print(f"Please enter a valid task ID!")
            return False
        
    def delete_task(self, task_id):
        # Delete a task
        try:
            task_id=int(task_id)
            if task_id in self.tasks:
                del self.tasks[task_id]
                print(f"Task {task_id} is completely deleted")
                return True
            
            else:
                print(f"Task {task_id} not found! ")
                return False
            
        except ValueError:
            print(f"Please enter a valid task ID!")
            return False
        
    def get_completed_tasks(self):
        # Get count of Completed tasks
        return sum(1 for task in self.tasks.values() if task.completed)
    
    def get_pending_tasks(self):
        # Get count of Pending tasks
        return sum(1 for task in self.tasks.values() if not task.completed)
    
def display_menu():
    # Displays Main Menu
    print("\n" + "="*60)
    print("TO-DO LIST APPLICATION - MAIN MENU")
    print("="*60)
    print("1. View all Tasks.")
    print("2. Add a new Task.")
    print("3. Mark task as completed.")
    print("4. Mark task as incomplete.")
    print("5. Delete a task.")
    print("6. View task statistics")
    print("7. Exit.")
    print("="*60)

def display_statistics(todo_list):
    # Display statistics about tasks
    total = len(todo_list.tasks)
    completed = todo_list.get_completed_tasks()
    pending = todo_list.get_pending_tasks()

    print("\n" + "="*60)
    print("TASK STATISTICS")
    print("="*60)
    print(f"Total Tasks: {total}")
    print(f"Completed: {completed}")
    print(f"Pending: {pending}")
    if total > 0:
        completion_rate = (completed / total) * 100
        print(f"Completion Rate: {completion_rate:.1f}%")
    print("="*60)

def main():
    # Main function to run the application
    todo_list = ToDoList()

    print("\n" + "="*60)
    print("WELCOME TO TO-DO LIST APPLICATION")
    print("Saiket Systems - Python Developement Internship")
    print("="*60)

    while True:
        display_menu()
        choice = input("Enter your choice from (1-7): ").strip()

        if choice == "1":
            todo_list.view_tasks()

        elif choice == "2":
            description = input("\nEnter task description: ").strip()
            todo_list.add_task(description)

        elif choice == "3":
            todo_list.view_tasks()
            task_id = input("\nEnter a task ID to mark as completed: ").strip()
            todo_list.mark_task_completed(task_id)

        elif choice == "4":
            todo_list.view_tasks()
            task_id = input("\nEnter a task ID to mark as incomplete: ").strip()
            todo_list.mark_task_incomplete(task_id)

        elif choice == "5":
            todo_list.view_tasks()
            task_id = input("\nEnter a task ID to delete: ").strip()
            todo_list.delete_task(task_id)

        elif choice == "6":
            display_statistics(todo_list)

        elif choice == "7":
            print("Thank for using TO-DO LIST Application!")
            break

        else:
            print("Invalid! Please enter a valid number between 1 and 7.\n")


if __name__ == "__main__":
    main()