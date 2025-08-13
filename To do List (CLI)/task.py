from datetime import datetime

class Task:
	def __init__(self, description, priority="medium", start_date=None, due_date=None):
		self.description = description
		self.is_completed = False
		self.priority = priority
		self.start_date = start_date if start_date else datetime.now()
		self.due_date = due_date
		self.days_left = self._calculate_days_left()
	
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
		
		# Format days left
		if self.days_left is None:
			days_str = "-"
		elif self.days_left < 0:
			days_str = f"OVERDUE"
		elif self.days_left == 0:
			days_str = "TODAY"
		else:
			days_str = f"{self.days_left}d"

		# Format completion status
		status_str = "Done" if self.is_completed else "Pending"
		
		# Fixed column widths with padding
		return f"| {short_desc:<15} | {self.priority:^8} | {start_str:^10} | {due_str:^10} | {status_str:^8} | {days_str:^10} |"

	def _calculate_days_left(self):
		"""Calculate days remaining until due date."""
		if not self.due_date or self.is_completed:
			return None  # No due date set
		
		# Calculate difference from today to due date
		today = datetime.now().date()
		due_date_only = self.due_date.date()
		
		difference = (due_date_only - today).days
		return difference

	@staticmethod
	def get_table_header():
		return f"| {'':^3} | {'Description':<15} | {'Priority':^8} | {'Start Date':^10} | {'Due Date':^10} | {'Status':^8} | {'Days left':^10} |"

	@staticmethod 
	def get_table_separator():
		return "|-----|-----------------|----------|------------|------------|----------|------------|"