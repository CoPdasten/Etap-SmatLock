from enum import Enum
import os
import json

class LockStatus(Enum):
    CLASS_TIME = "class_time"
    BREAK_TIME = "break_time"

class AppConfig:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.default_config = {
            "lock_on_startup": True
        }
        self.config = self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                return json.load(f)
        return self.default_config.copy()
    
    def save_config(self):
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f)