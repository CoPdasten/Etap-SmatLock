from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PyQt5.QtCore import pyqtSignal

class LockControls(QWidget):
    lockRequested = pyqtSignal()
    unlockRequested = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout()
        
        self.lock_btn = QPushButton('Kilitle')
        self.unlock_btn = QPushButton('Kilidi Aç')
        
        layout.addWidget(self.lock_btn)
        layout.addWidget(self.unlock_btn)
        self.setLayout(layout)

        self.lock_btn.clicked.connect(self.lockRequested.emit)
        self.unlock_btn.clicked.connect(self.unlockRequested.emit)
