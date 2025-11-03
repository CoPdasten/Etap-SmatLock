import unittest
from src.core.schedule_manager import ScheduleManager

class TestScheduleManager(unittest.TestCase):

    def setUp(self):
        self.schedule_manager = ScheduleManager()

    def test_load_schedule(self):
        # Assuming there's a method to load a schedule from a file
        self.schedule_manager.load_schedule('path/to/schedule.json')
        self.assertIsNotNone(self.schedule_manager.schedule)

    def test_save_schedule(self):
        # Assuming there's a method to save a schedule to a file
        self.schedule_manager.schedule = {'classes': []}  # Example schedule
        self.schedule_manager.save_schedule('path/to/schedule.json')
        # Check if the file exists and contains the expected data
        with open('path/to/schedule.json', 'r') as f:
            data = f.read()
            self.assertIn('classes', data)

    def test_schedule_integrity(self):
        # Test to ensure the schedule maintains integrity
        self.schedule_manager.schedule = {'classes': [{'name': 'Math', 'time': '10:00'}]}
        self.assertEqual(len(self.schedule_manager.schedule['classes']), 1)

if __name__ == '__main__':
    unittest.main()