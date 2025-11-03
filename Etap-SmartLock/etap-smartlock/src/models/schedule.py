class Schedule:
    def __init__(self):
        self.classes = []  # List to hold scheduled classes
        self.breaks = []   # List to hold break times

    def add_class(self, class_name, start_time, end_time):
        """Add a class to the schedule."""
        self.classes.append({
            'name': class_name,
            'start_time': start_time,
            'end_time': end_time
        })

    def add_break(self, break_name, start_time, end_time):
        """Add a break to the schedule."""
        self.breaks.append({
            'name': break_name,
            'start_time': start_time,
            'end_time': end_time
        })

    def get_schedule(self):
        """Return the full schedule including classes and breaks."""
        return {
            'classes': self.classes,
            'breaks': self.breaks
        }

    def clear_schedule(self):
        """Clear the entire schedule."""
        self.classes.clear()
        self.breaks.clear()