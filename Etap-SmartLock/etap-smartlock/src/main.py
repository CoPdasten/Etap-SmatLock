# src/main.py

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer
from gui.main_window import MainWindow
from core.lock_controller import LockController
from core.schedule_manager import ScheduleManager
from utils.config import AppConfig
from models.lock_status import LockStatus

class SmartLockApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.config = AppConfig()
        self.lock_controller = LockController()
        self.schedule_manager = ScheduleManager()
        
        self.main_window = MainWindow(
            lock_controller=self.lock_controller,
            schedule_manager=self.schedule_manager
        )
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.check_schedule)
        self.timer.start(30000)  # 30 saniyede bir kontrol

    def check_schedule(self):
        current_status = self.schedule_manager.get_current_status()
        if current_status == LockStatus.BREAK_TIME:
            self.lock_controller.lock_screen()
        elif current_status == LockStatus.CLASS_TIME:
            self.lock_controller.unlock_screen()

    def run(self):
        self.main_window.show()
        return self.app.exec_()

def main():
    # Sistem yolu için gerekli dizinleri ekle
    base_path = "/usr/lib/python3/dist-packages/etap-smartlock"
    if base_path not in sys.path:
        sys.path.append(base_path)
    
    app = SmartLockApp()
    sys.exit(app.run())

if __name__ == "__main__":
    main()