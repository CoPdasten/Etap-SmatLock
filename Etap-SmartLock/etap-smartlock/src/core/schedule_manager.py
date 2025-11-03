from datetime import datetime
from models.lock_status import LockStatus
from utils.config import load_config, save_config

class ScheduleManager:
    def __init__(self):
        self.config = load_config()
        self.schedule = self.config.get('schedule', {})

    def get_current_status(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        day_of_week = now.strftime("%A")
        
        if day_of_week in self.schedule:
            for time_slot in self.schedule[day_of_week]:
                start, end = time_slot['start'], time_slot['end']
                if start <= current_time <= end:
                    return LockStatus.CLASS_TIME
        return LockStatus.BREAK_TIME

    def add_schedule(self, day, start_time, end_time):
        if day not in self.schedule:
            self.schedule[day] = []
        self.schedule[day].append({
            'start': start_time,
            'end': end_time
        })
        self.save()

    def save(self):
        self.config['schedule'] = self.schedule
        save_config(self.config)
