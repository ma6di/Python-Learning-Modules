from task import Task
from datetime import datetime, timedelta
import json
import readline

# Color constants for terminal output
class Colors:
    RED = '\033[91m'        # Error messages, exit
    GREEN = '\033[92m'      # Success messages
    ORANGE = '\033[93m'     # Cancel/warning messages
    BLUE = '\033[94m'       # Info messages
    PURPLE = '\033[95m'     # Headers
    CYAN = '\033[96m'       # Highlights
    WHITE = '\033[97m'      # Normal text
    RESET = '\033[0m'       # Reset to default color

tasks = []
TASKS_FILE = "tasks.json"

def show_menu():
	print("\n--- To-Do List Menu ---", "1. Add task", "2. List tasks", 
	"3. Mark task as done", "4. Edit task", "5. Remove task" , "6. Exit", sep = "\n", end= "\n")

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
		print("Edit task...")
		handle_edit_task()
		
	elif choice == 5:
		print("Remove task...")
		handle_remove_task()

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
				print(f"{Colors.ORANGE}Returning to main menu...{Colors.RESET}\n")
				return
			
			try:
				task_num = int(user_input)
				if 1 <= task_num <= len(tasks):
					tasks[task_num - 1].mark_completed()
					print(f"{Colors.GREEN}Task {task_num} marked as completed!{Colors.RESET}")
					save_tasks()  # Save after marking complete
					return  # Exit after successful completion
				else:
					print(f"{Colors.RED}Please enter a number between 1 and {len(tasks)}{Colors.RESET}")
			except ValueError:
				print(f"{Colors.RED}Please enter a valid number{Colors.RESET}")
				
	except KeyboardInterrupt:
		print(f"\n{Colors.ORANGE}Operation cancelled. Returning to main menu...{Colors.RESET}")

def handle_add_task():
	"""Handle adding a new task with escape options."""
	try:		
		# Get description with escape option
		while True:
			description = input("Enter task description: ").strip()
			if description.lower() in ['b', 'back', 'cancel']:
				print(f"{Colors.ORANGE}Task creation cancelled.{Colors.RESET}")
				return
			if description:
				add_to_history(description)  # Only add the actual description
				break
			print(f"{Colors.RED}Description cannot be empty!{Colors.RESET}")
		
		# Get priority with escape option
		valid_priorities = ['low', 'medium', 'high']
		while True:
			priority = input("Enter priority (low/medium/high): ").strip().lower()
			if priority in ['b', 'cancel', 'back']:
				print(f"{Colors.ORANGE}Task creation cancelled.{Colors.RESET}")
				return
			if not priority:
				priority = "medium"
				break
			if priority in valid_priorities:
				add_to_history(priority)  # Only add the actual priority
				break
			print(f"{Colors.RED}Invalid priority! Please enter: {', '.join(valid_priorities)}{Colors.RESET}")
		
		# Get start date with escape option
		while True:
			start_input = input("Enter start date (YYYY-MM-DD) or press Enter for today: ").strip()
			if start_input.lower() in ['b', 'cancel', 'back']:
				print(f"{Colors.ORANGE}Task creation cancelled.{Colors.RESET}")
				return
			if not start_input:
				start_date = datetime.now()
				break
			if is_valid_date(start_input):
				start_date = datetime.strptime(start_input, "%Y-%m-%d")
				add_to_history(start_input)  # Only add the actual date
				break
			print(f"{Colors.RED}Invalid date format! Use YYYY-MM-DD{Colors.RESET}")
		
		# Get due date with escape option
		while True:
			due_input = input("Enter due date (YYYY-MM-DD), days from start, or Enter for none: ").strip()
			if due_input.lower() in ['b','cancel', 'back']:
				print(f"{Colors.ORANGE}Task creation cancelled.{Colors.RESET}")
				return
			if not due_input:
				due_date = None
				break
			if is_valid_date(due_input):
				due_date = datetime.strptime(due_input, "%Y-%m-%d")
				add_to_history(due_input)  # Only add the actual date
				break
			if due_input.isdecimal():
				days = int(due_input)
				if 1 <= days <= 365:
					due_date = start_date + timedelta(days=days)
					add_to_history(due_input)  # Only add the number of days
					break
				print(f"{Colors.RED}Please enter 1-365 days{Colors.RESET}")
			else:
				print(f"{Colors.RED}Invalid input! Use date format, number of days{Colors.RESET}")
		
		# Create and add the task
		my_task = Task(description, priority, start_date, due_date)
		tasks.append(my_task)
		print(f"{Colors.GREEN}Task '{description}' added successfully!{Colors.RESET}")
		save_tasks()  # Save after adding task
		
	except KeyboardInterrupt:
		print(f"\n{Colors.ORANGE}Task creation cancelled. Returning to main menu...{Colors.RESET}\n")

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
				print(f"{Colors.ORANGE}Returning to main menu...{Colors.RESET}")
				return
			
			try:
				task_num = int(user_input)
				if 1 <= task_num <= len(tasks):
					removed_task = tasks.pop(task_num - 1)  # Remove and get the task
					print(f"{Colors.GREEN}Task '{removed_task.description}' removed successfully!{Colors.RESET}")
					save_tasks()  # Save after removing task
					return
				else:
					print(f"{Colors.RED}Please enter a number between 1 and {len(tasks)}{Colors.RESET}")
			except ValueError:
				print(f"{Colors.RED}Please enter a valid number!{Colors.RESET}")
				
	except KeyboardInterrupt:
		print(f"\n{Colors.ORANGE}Operation cancelled. Returning to main menu...{Colors.RESET}")

def handle_edit_task():
	"""Handle editing an existing task with escape options."""
	if not tasks:
		print("No tasks to edit!")
		return
		
	try:
		print_task_list(tasks)
		
		# Select task to edit
		while True:
			user_input = input("Enter task number to edit: ").strip()
			
			# Check for escape commands
			if user_input.lower() in ['b', 'back', 'cancel']:
				print(f"{Colors.ORANGE}Returning to main menu...{Colors.RESET}")
				return
			
			try:
				task_num = int(user_input)
				if 1 <= task_num <= len(tasks):
					task_to_edit = tasks[task_num - 1]
					break
				else:
					print(f"{Colors.RED}Please enter a number between 1 and {len(tasks)}{Colors.RESET}")
			except ValueError:
				print(f"{Colors.RED}Please enter a valid number!{Colors.RESET}")
		
		print(f"\n{Colors.CYAN}Editing task: {task_to_edit.description}{Colors.RESET}")
		print(f"{Colors.BLUE}Current details:{Colors.RESET}")
		print(f"  Description: {task_to_edit.description}")
		print(f"  Priority: {task_to_edit.priority}")
		print(f"  Start date: {task_to_edit.start_date.strftime('%Y-%m-%d')}")
		print(f"  Due date: {task_to_edit.due_date.strftime('%Y-%m-%d') if task_to_edit.due_date else 'None'}")
		print(f"  Status: {'Done' if task_to_edit.is_completed else 'Pending'}")
		
		# Edit description
		while True:
			new_description = input(f"\nNew description (current: {task_to_edit.description}) or Enter to keep: ").strip()
			if new_description.lower() in ['b', 'back', 'cancel']:
				print(f"{Colors.ORANGE}Edit cancelled.{Colors.RESET}")
				return
			if new_description:
				task_to_edit.description = new_description
				add_to_history(new_description)
				break
			else:
				break  # Keep current description
		
		# Edit priority
		valid_priorities = ['low', 'medium', 'high']
		while True:
			new_priority = input(f"New priority (current: {task_to_edit.priority}) or Enter to keep: ").strip().lower()
			if new_priority in ['b', 'cancel', 'back']:
				print(f"{Colors.ORANGE}Edit cancelled.{Colors.RESET}")
				return
			if not new_priority:
				break  # Keep current priority
			if new_priority in valid_priorities:
				task_to_edit.priority = new_priority
				add_to_history(new_priority)
				break
			print(f"{Colors.RED}Invalid priority! Please enter: {', '.join(valid_priorities)}{Colors.RESET}")
		
		# Edit start date
		while True:
			current_start = task_to_edit.start_date.strftime('%Y-%m-%d')
			new_start = input(f"New start date (current: {current_start}) or Enter to keep: ").strip()
			if new_start.lower() in ['b', 'cancel', 'back']:
				print(f"{Colors.ORANGE}Edit cancelled.{Colors.RESET}")
				return
			if not new_start:
				break  # Keep current start date
			if is_valid_date(new_start):
				task_to_edit.start_date = datetime.strptime(new_start, "%Y-%m-%d")
				add_to_history(new_start)
				break
			print(f"{Colors.RED}Invalid date format! Use YYYY-MM-DD{Colors.RESET}")
		
		# Edit due date
		while True:
			current_due = task_to_edit.due_date.strftime('%Y-%m-%d') if task_to_edit.due_date else 'None'
			new_due = input(f"New due date (current: {current_due}) or Enter to keep: ").strip()
			if new_due.lower() in ['b','cancel', 'back']:
				print(f"{Colors.ORANGE}Edit cancelled.{Colors.RESET}")
				return
			if not new_due:
				break  # Keep current due date
			if new_due.lower() in ['none', 'remove', 'delete']:
				task_to_edit.due_date = None
				break
			if is_valid_date(new_due):
				task_to_edit.due_date = datetime.strptime(new_due, "%Y-%m-%d")
				add_to_history(new_due)
				break
			if new_due.isdecimal():
				days = int(new_due)
				if 1 <= days <= 365:
					task_to_edit.due_date = task_to_edit.start_date + timedelta(days=days)
					add_to_history(new_due)
					break
				print(f"{Colors.RED}Please enter 1-365 days{Colors.RESET}")
			else:
				print(f"{Colors.RED}Invalid input! Use date format, number of days, or 'none' to remove{Colors.RESET}")
		
		print(f"{Colors.GREEN}Task updated successfully!{Colors.RESET}")
		save_tasks()  # Save changes
		load_tasks()
		# Show updated task list to see the changes immediately
		print(f"\n{Colors.CYAN}Updated task list:{Colors.RESET}")
		print_task_list(tasks)
		
	except KeyboardInterrupt:
		print(f"\n{Colors.ORANGE}Operation cancelled. Returning to main menu...{Colors.RESET}")

def is_valid_date(date_string):
	"""Check if date string is in valid YYYY-MM-DD format."""
	try:
		# Try to parse the date string
		datetime.strptime(date_string, "%Y-%m-%d")
		return True
	except ValueError:
		return False

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
		choice_input = input("\nEnter Menu Number: ")
		try:
			choice = int(choice_input)
			if 1 <= choice <= 6:  # Additional validation
				return choice
			else:
				print(f"{Colors.RED}Please enter a number between 1-6.{Colors.RESET}")
		except ValueError:
			print(f"{Colors.RED}Invalid input! Please enter a number between 1-6.{Colors.RESET}")

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
		
		print(f"{Colors.GREEN}Loaded {len(tasks)} tasks from {TASKS_FILE}{Colors.RESET}")
	except FileNotFoundError:
		print(f"{Colors.BLUE}No saved tasks found. Starting with empty list.{Colors.RESET}")
		tasks = []
	except Exception as e:
		print(f"{Colors.RED}Error loading tasks: {e}{Colors.RESET}")
		tasks = []

def save_tasks():
	"""Save all tasks to JSON file."""
	try:
		# Convert all tasks to dictionaries
		tasks_data = [task_to_dict(task) for task in tasks]
		
		# Write to JSON file
		with open(TASKS_FILE, 'w') as f:
			json.dump(tasks_data, f, indent=2)
		
		print(f"{Colors.GREEN}Tasks saved to {TASKS_FILE}{Colors.RESET}")
	except Exception as e:
		print(f"{Colors.RED}Error saving tasks: {e}{Colors.RESET}")

def setup_readline():
	"""Setup readline for in-memory command history only."""
	try:
		# Set maximum history entries (in memory only)
		readline.set_history_length(50)
		
		# Enable tab completion (optional)
		readline.parse_and_bind("tab: complete")
		
		# Clear any existing history to start fresh
		readline.clear_history()
		
	except Exception as e:
		print(f"Note: Could not setup command history: {e}")

def add_to_history(command):
	"""Add a command to readline history (memory only)."""
	try:
		# Add command to readline history
		readline.add_history(command)
	except Exception:
		pass  # Ignore errors

def main():
	"""Main function to run the to-do list application."""
	# Setup readline for in-memory command history
	setup_readline()
	
	print(f"\n{Colors.PURPLE}** Welcome to your To-Do List! **{Colors.RESET}")
	print(f"{Colors.BLUE}** Press Ctrl+C or type 'b'/'back'/'cancel' at any prompt to abort **{Colors.RESET}")
	print(f"{Colors.BLUE}** Use ↑/↓ arrow keys to navigate command history **{Colors.RESET}\n")
	
	load_tasks()
	while True:
		try:
			show_menu()
			choice = get_valid_menu_choice()  # This always returns a valid int
			
			print_selected_choice(choice)
			if choice == 6:
				save_tasks()
				print(f"{Colors.RED}History cleared. Goodbye!{Colors.RESET}")
				break
		except KeyboardInterrupt:
			save_tasks()
			print(f"\n{Colors.RED}History cleared. Goodbye!{Colors.RESET}")
			break

if __name__ == "__main__":
    main()