from task import Task
from datetime import datetime, timedelta
import json

tasks = []
TASKS_FILE = "tasks.json"

def show_menu():
	print("--- To-Do List Menu ---", "1. Add task", "2. List tasks", 
	"3. Mark task as done", "4. Remove task" , "5. Exit", sep = "\n", end= "\n")

def mark_task_as_done(task_number):
	for i in tasks:
		if i == task_number:
			tasks[i].mark_completed()

def print_selected_choice(choice):
	"""Handle user's menu choice with escape options for all."""
		
	if choice == 1:
		print("Adding new task...")
		handle_add_task()
		
	elif choice == 2:
		print("Displaying all tasks...")
		print_task_list(tasks)
		
	elif choice == 3:
		print("Mark task as completed...")
		handle_mark_task_done()
		
	elif choice == 4:
		print("Remove task...")
		handle_remove_task()
		
	elif choice == 5:
		print("Good Bye!")

def handle_mark_task_done():
	"""Handle marking a task as completed with escape options."""
	if not tasks:
		print("No tasks to mark as done!")
		return
		
	try:
		print_task_list(tasks)
		
		while True:
			user_input = input("Enter task number to mark as done: ").strip()
			
			# Check for escape commands first (before trying to convert to int)
			if user_input.lower() in ['b', 'back', 'cancel']:
				print("Returning to main menu...\n")
				return
			
			try:
				task_num = int(user_input)
				if 1 <= task_num <= len(tasks):
					tasks[task_num - 1].mark_completed()
					print(f"Task {task_num} marked as completed!")
					save_tasks()  # Save after marking complete
					return  # Exit after successful completion
				else:
					print(f"Please enter a number between 1 and {len(tasks)}")
			except ValueError:
				print("Please enter a valid number")
				
	except KeyboardInterrupt:
		print("\nOperation cancelled. Returning to main menu...")

def handle_add_task():
	"""Handle adding a new task with escape options."""
	try:		
		# Get description with escape option
		while True:
			description = input("Enter task description: ").strip()
			if description.lower() in ['b', 'back', 'cancel']:
				print("Task creation cancelled.")
				return
			if description:
				break
			print("Description cannot be empty!")
		
		# Get priority with escape option
		valid_priorities = ['low', 'medium', 'high']
		while True:
			priority = input("Enter priority (low/medium/high): ").strip().lower()
			if priority in ['b', 'cancel', 'back']:
				print("Task creation cancelled.")
				return
			if not priority:
				priority = "medium"
				break
			if priority in valid_priorities:
				break
			print(f"Invalid priority! Please enter: {', '.join(valid_priorities)}")
		
		# Get start date with escape option
		while True:
			start_input = input("Enter start date (YYYY-MM-DD) or press Enter for today: ").strip()
			if start_input.lower() in ['b', 'cancel', 'back']:
				print("Task creation cancelled.")
				return
			if not start_input:
				start_date = datetime.now()
				break
			if is_valid_date(start_input):
				start_date = datetime.strptime(start_input, "%Y-%m-%d")
				break
			print("Invalid date format! Use YYYY-MM-DD")
		
		# Get due date with escape option
		while True:
			due_input = input("Enter due date (YYYY-MM-DD), days from start, or Enter for none: ").strip()
			if due_input.lower() in ['b','cancel', 'back']:
				print("Task creation cancelled.")
				return
			if not due_input:
				due_date = None
				break
			if is_valid_date(due_input):
				due_date = datetime.strptime(due_input, "%Y-%m-%d")
				break
			if due_input.isdecimal():
				days = int(due_input)
				if 1 <= days <= 365:
					due_date = start_date + timedelta(days=days)
					break
				print("Please enter 1-365 days")
			else:
				print("Invalid input! Use date format, number of days'")
		
		# Create and add the task
		my_task = Task(description, priority, start_date, due_date)
		tasks.append(my_task)
		print(f"Task '{description}' added successfully!")
		save_tasks()  # Save after adding task
		
	except KeyboardInterrupt:
		print("\nTask creation cancelled. Returning to main menu...\n")

def handle_remove_task():
	"""Handle removing a task with escape options."""
	if not tasks:
		print("No tasks to remove!")
		return
		
	try:
		print_task_list(tasks)
		
		while True:
			user_input = input("Enter task number to remove: ").strip()
			
			# Check for escape commands
			if user_input.lower() in ['b', 'back', 'cancel']:
				print("Returning to main menu...")
				return
			
			try:
				task_num = int(user_input)
				if 1 <= task_num <= len(tasks):
					removed_task = tasks.pop(task_num - 1)  # Remove and get the task
					print(f"Task '{removed_task.description}' removed successfully!")
					save_tasks()  # Save after removing task
					return
				else:
					print(f"Please enter a number between 1 and {len(tasks)}")
			except ValueError:
				print("Please enter a valid number!")
				
	except KeyboardInterrupt:
		print("\nOperation cancelled. Returning to main menu...\m")

def is_valid_date(date_string):
	"""Check if date string is in valid YYYY-MM-DD format."""
	try:
		# Try to parse the date string
		datetime.strptime(date_string, "%Y-%m-%d")
		return True
	except ValueError:
		return False

# def add_task():
# 	# Get valid description (keep asking until not empty)
# 	while True:
# 		description = input("Enter the task description: \n")
# 		if description.strip():  # If not empty
# 			break  # Exit the description loop
# 		print("Task description can't be empty! Please try again.")
		
# 	# Get valid priority (keep asking until valid or empty for default)
# 	valid_priorities = ['low', 'medium', 'high']
# 	while True:
# 		priority = input("Enter the task priority (low, medium, high) or press Enter for default: \n")
# 		priority = priority.strip().lower()
		
# 		if not priority:  # Empty = use default
# 			priority = "medium"
# 			break
# 		elif priority in valid_priorities:  # Valid priority
# 			break
# 		else:  # Invalid priority
# 			print(f"Invalid priority! Please enter one of: {', '.join(valid_priorities)} or press Enter for default.")
		
# 	while True:
# 		start_date =  input("Enter start date (YYYY-MM-DD) or press Enter for Today: \n")
# 		if not start_date:
# 			start_date = datetime.now()
# 			break
# 		elif is_valid_date(start_date):
# 			start_date = datetime.strptime(start_date, "%Y-%m-%d") 
# 			break
# 		else:
# 			print("Invalid date format! Please enter date as YYYY-MM-DD or press Enter for Today.")

# 	while True:
# 		due_date = input("Enter due date (YYYY-MM-DD), enter a number of days to complete the task, or press Enter for None: \n")
# 		if not due_date:
# 			due_date = None
# 			break
# 		elif is_valid_date(due_date):
# 			due_date = datetime.strptime(due_date, "%Y-%m-%d")  # Convert to datetime object
# 			break
# 		elif due_date.isdecimal():
# 			days_to_add = int(due_date)
# 			if 1 <= days_to_add <= 365:  # Reasonable range
# 				due_date = start_date + timedelta(days=days_to_add)
# 				break
# 			else:
# 				print("Please enter a number between 1-365 days.")
# 		else:
# 			print("Invalid due date format! Please enter date as YYYY-MM-DD or press Enter for None.")

# 	my_task = Task(description, priority, start_date, due_date)
# 	tasks.append(my_task)
# 	print(f"Task '{description}' added!")

def print_task_list(tasks):
	if not tasks:
		print("No tasks found!")
		return
	
	print(f"You have {len(tasks)} tasks in the list:")
	print()
	
	# Use the static methods to create a nice table
	print(Task.get_table_header())	  # Print header
	print(Task.get_table_separator())   # Print separator line
	
	# Print each task with a number
	for i, task in enumerate(tasks, 1):
		print(f"|{i:^4} {task}")		# Add task number + task info
	
	print(Task.get_table_separator(), "\n")   # Print bottom separator


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

def task_to_dict(task):
	"""Convert a Task object to a dictionary for JSON serialization."""
	return {
		"description": task.description,
		"priority": task.priority,
		"start_date": task.start_date.strftime("%Y-%m-%d %H:%M:%S"),
		"due_date": task.due_date.strftime("%Y-%m-%d %H:%M:%S") if task.due_date else None,
		"completed": task.is_completed
	}

def dict_to_task(task_dict):
	"""Convert a dictionary back to a Task object."""
	start_date = datetime.strptime(task_dict["start_date"], "%Y-%m-%d %H:%M:%S")
	due_date = datetime.strptime(task_dict["due_date"], "%Y-%m-%d %H:%M:%S") if task_dict["due_date"] else None
		
	task = Task(
		task_dict["description"],
		task_dict["priority"],
		start_date,
		due_date
	)
	task.is_completed = task_dict["completed"]
	return task

def load_tasks():
	"""Load tasks from JSON file."""
	global tasks
	try:
		with open(TASKS_FILE, 'r') as f:
			tasks_data = json.load(f)
		
		# Convert dictionaries back to Task objects
		tasks = [dict_to_task(task_dict) for task_dict in tasks_data]
		
		print(f"Loaded {len(tasks)} tasks from {TASKS_FILE}")
	except FileNotFoundError:
		print(f"No saved tasks found. Starting with empty list.")
		tasks = []
	except Exception as e:
		print(f"Error loading tasks: {e}")
		tasks = []

def save_tasks():
	"""Save all tasks to JSON file."""
	try:
		# Convert all tasks to dictionaries
		tasks_data = [task_to_dict(task) for task in tasks]
		
		# Write to JSON file
		with open(TASKS_FILE, 'w') as f:
			json.dump(tasks_data, f, indent=2)
		
		print(f"Tasks saved to {TASKS_FILE}")
	except Exception as e:
		print(f"Error saving tasks: {e}")

def main():
	"""Main function to run the to-do list application."""
	print("\n** Welcome to your To-Do List! **")
	print("** Press Ctrl+C or type 'b'/'back'/'cancel' at any prompt to abort **\n")
	while True:
		try:
			load_tasks()
			show_menu()
			choice = get_valid_menu_choice()  # This always returns a valid int
			
			print_selected_choice(choice)
			if choice == 5:
				save_tasks()
				break
		except KeyboardInterrupt:
			save_tasks()
			break

if __name__ == "__main__":
    main()