from datetime import datetime

class Task:
	def __init__(self, description, priority="medium", start_date=None, due_date=None):
		self.description = description
		self.is_completed = False
		self.priority = priority
		self.start_date = start_date if start_date else datetime.now()
		self.due_date = due_date
	
	def mark_completed(self):
		self.is_completed = True

	def __str__(self):		
		# Truncate description if too long
		if len(self.description) > 15:
			short_desc = self.description[:14] + "."
		else:
			short_desc = self.description
		
		# Format dates for display
		start_str = self.start_date.strftime("%Y-%m-%d") if self.start_date else "None"
		due_str = self.due_date.strftime("%Y-%m-%d") if self.due_date else "None"
		
		# Fixed column widths with padding
		return f"| {short_desc:<15} | {self.priority:^8} | {start_str:^10} | {due_str:^10} | {str(self.is_completed):^8} |"

	@staticmethod
	def get_table_header():
		return f"| {'':^3} | {'Description':<15} | {'Priority':^8} | {'Start Date':^10} | {'Due Date':^10} | {'Status':^8} |"

	@staticmethod 
	def get_table_separator():
		return "|-----|-----------------|----------|------------|------------|----------|"