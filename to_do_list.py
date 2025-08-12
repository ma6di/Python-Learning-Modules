from task import Task
from datetime import datetime

tasks = []

def show_menu():
	print("--- To-Do List Menu ---", "1. Add task", "2. List tasks", 
	"3. Mark task as done", "4. Remove task" , "5. Exit", sep = "\n", end= "\n")

def print_selected_choice(choice):
	if choice == 1:
		print("you selected \"1. Add task\" from the menu")
		add_task()
	elif choice == 2:
		print("you selected \"2. List tasks\" from the menu")
		print_task_list(tasks)
	elif choice == 3:
		print("you selected \"3. Mark task\" as done from the menu")
	elif choice == 4:
		print("you selected \"4. Remove task\" from the menu")
	elif choice == 5:
		print("Good Bye")

def is_valid_date(date_string):
    """Check if date string is in valid YYYY-MM-DD format."""
    try:
        # Try to parse the date string
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def add_task():
	# Get valid description (keep asking until not empty)
	while True:
		description = input("Enter the task description: \n")
		if description.strip():  # If not empty
			break  # Exit the description loop
		print("Task description can't be empty! Please try again.")
		
	# Get valid priority (keep asking until valid or empty for default)
	valid_priorities = ['low', 'medium', 'high']
	while True:
		priority = input("Enter the task priority (low, medium, high) or press Enter for default: \n")
		priority = priority.strip().lower()
		
		if not priority:  # Empty = use default
			priority = "medium"
			break
		elif priority in valid_priorities:  # Valid priority
			break
		else:  # Invalid priority
			print(f"Invalid priority! Please enter one of: {', '.join(valid_priorities)} or press Enter for default.")
		
	while True:
		start_date =  input("Enter start date (YYYY-MM-DD) or press Enter for Today: \n")
		if not start_date:
			start_date = datetime.now()
			break
		elif is_valid_date(start_date):
			start_date = datetime.strptime(start_date, "%Y-%m-%d") 
			break
		else:
			print("Invalid date format! Please enter date as YYYY-MM-DD or press Enter for Today.")

	while True:
		due_date = input("Enter due date (Year-Month-Day) or press Enter for None: \n")
		if not due_date:
			due_date = None
			break
		elif is_valid_date(due_date):
			due_date = datetime.strptime(due_date, "%Y-%m-%d")  # Convert to datetime object
			break
		else:
			print("Invalid due date format! Please enter date as YYYY-MM-DD or press Enter for None.")

	my_task = Task(description, priority, start_date, due_date)
	tasks.append(my_task)
	print(f"Task '{description}' added!")

def print_task_list(tasks):
	if not tasks:
		print("No tasks found!")
		return
	
	print(f"You have {len(tasks)} tasks in the list:")
	print()
	
	# Use the static methods to create a nice table
	print(Task.get_table_header())      # Print header
	print(Task.get_table_separator())   # Print separator line
	
	# Print each task with a number
	for i, task in enumerate(tasks, 1):
		print(f"|{i:^4} {task}")        # Add task number + task info
	
	print(Task.get_table_separator())   # Print bottom separator


def get_valid_menu_choice():
    """Get a valid menu choice from user."""
    while True:
        choice_input = input("Enter a number: ")
        try:
            choice = int(choice_input)
            if 1 <= choice <= 5:  # Additional validation
                return choice
            else:
                print("Please enter a number between 1-5.")
        except ValueError:
            print("Invalid input! Please enter a number between 1-5.")

def main():
    """Main function to run the to-do list application."""
    print("Welcome to your To-Do List!")
    while True:
        show_menu()
        choice = get_valid_menu_choice()  # This always returns a valid int
        
        print_selected_choice(choice)
        if choice == 5:
            break

if __name__ == "__main__":
    main()