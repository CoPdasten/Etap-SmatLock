import os
import subprocess
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

class LockController:
    def __init__(self):
        self.locked = False
        self.lock_screen_widget = None
    
    def lock_screen(self):
        try:
            subprocess.run(['xdg-screensaver', 'lock'])
            if not self.locked:
                self.lock_screen_widget = LockScreenWidget()
                self.lock_screen_widget.showFullScreen()
                self.locked = True
                return True
        except Exception as e:
            print(f"Kilit hatası: {e}")
            return False

    def unlock_screen(self):
        try:
            subprocess.run(['xdg-screensaver', 'reset'])
            if self.locked and self.lock_screen_widget:
                self.lock_screen_widget.close()
                self.lock_screen_widget = None
                self.locked = False
                return True
        except Exception as e:
            print(f"Kilit açma hatası: {e}")
            return False

    def get_status(self):
        return self.locked

class LockScreenWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Ekran Kilitli"))
        self.setLayout(layout)