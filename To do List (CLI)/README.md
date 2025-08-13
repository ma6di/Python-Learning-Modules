# Python To-Do CLI

A comprehensive command-line to-do list application built with Python. Manage your tasks efficiently with priorities, dates, completion tracking, and persistent storage.

## ✨ Features

### Core Functionality
- ➕ **Add Tasks**: Create tasks with custom descriptions, priorities, start dates, and due dates
- 📋 **List Tasks**: View all tasks in a beautifully formatted table with status indicators
- ✅ **Mark Complete**: Mark tasks as done with clear status display ("Done"/"Pending")
- ✏️ **Edit Tasks**: Modify existing tasks - change description, priority, dates with real-time updates
- 🗑️ **Remove Tasks**: Delete unwanted tasks from your list
- 💾 **Persistent Storage**: Automatic JSON file persistence - tasks save and load automatically

### User Experience
- 🛡️ **Input Validation**: Comprehensive validation for all user inputs
- 🚫 **Escape Options**: Cancel any operation with 'cancel', 'back', 'quit', or Ctrl+C
- 📅 **Flexible Date Input**: Enter dates directly (YYYY-MM-DD) or specify days from start date
- ⚠️ **Error Handling**: Graceful error handling with helpful messages
- 🎯 **Smart Priority**: Default to 'medium' priority or choose low/medium/high

### Task Display
- 📊 **Formatted Table**: Clean, organized table view with proper alignment
- ⏰ **Days Tracking**: Shows days remaining, "TODAY", or "OVERDUE" status
- 🏷️ **Priority Display**: Clear priority levels (low, medium, high)
- 📋 **Status Indicators**: Human-readable "Done" or "Pending" status

## 🚀 Usage

### Running the Application
```bash
python3 to_do_list.py
```

### Menu Options
1. **Add Task**: Create a new task with guided prompts
2. **List Tasks**: Display all tasks in a formatted table
3. **Mark Complete**: Mark any task as completed
4. **Edit Task**: Modify existing task details (description, priority, dates)
5. **Remove Task**: Delete a task from your list
6. **Exit**: Save and quit the application

### Example Task Creation
```
Enter task description: Complete Python project
Enter priority (low/medium/high): high
Enter start date (YYYY-MM-DD) or press Enter for today: 2025-08-13
Enter due date or days from start: 7
```

## 🏗️ Project Structure

```
python-todo-cli/
├── to_do_list.py      # Main application with menu and user interaction
├── task.py            # Task class definition with formatting methods
├── tasks.json         # Persistent storage (auto-generated)
├── .gitignore         # Git ignore file
└── README.md          # Project documentation
```

## 🧠 Learning Achievements

This project demonstrates mastery of:

### Python Fundamentals
- **Object-Oriented Programming**: Custom classes with methods and attributes
- **Error Handling**: try/except blocks, ValueError handling, KeyboardInterrupt
- **File I/O**: JSON serialization and deserialization
- **String Manipulation**: .strip(), .lower(), .isdecimal() methods
- **Date/Time Handling**: datetime module, strftime/strptime formatting

### Software Development
- **Input Validation**: Comprehensive user input validation
- **User Experience**: Escape options, clear feedback, error messages
- **Code Organization**: Modular design with separate files and functions
- **Version Control**: Git workflow with meaningful commits
- **Documentation**: Clear code comments and README

### CLI Application Design
- **Menu-driven Interface**: Clean, numbered menu system
- **Table Formatting**: Static methods for consistent table display
- **Data Persistence**: Automatic save/load functionality
- **Graceful Exit**: Proper cleanup and save on exit

## 🔧 Technical Implementation

### Key Features
- **JSON Persistence**: Converts Task objects to/from dictionaries for storage
- **Date Validation**: Robust date parsing with multiple input formats
- **Dynamic Table**: Auto-calculating days left with status indicators
- **Escape Handling**: Multiple escape options at every input prompt
- **Memory Management**: Efficient list operations for task management

### Code Highlights
- **Custom `__str__` method**: Professional table formatting
- **Static methods**: Reusable table headers and separators
- **List comprehension**: Efficient task-to-dict conversions
- **Exception handling**: Comprehensive error management
- **Global state management**: Clean task list handling

## � License

This project is open source and available under the MIT License.

---

## � Project Complete!

This Python To-Do CLI application represents a comprehensive learning journey from basic Python syntax to advanced software development concepts. All core functionality has been implemented including full CRUD operations (Create, Read, Update, Delete) with a professional command-line interface.
