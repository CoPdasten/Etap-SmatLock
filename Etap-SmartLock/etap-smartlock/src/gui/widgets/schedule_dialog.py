from PyQt5.QtWidgets import QDialog, QVBoxLayout, QTimeEdit, QComboBox, QPushButton

class ScheduleDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setWindowTitle('Ders Programı')
        
        # Gün seçimi
        self.day_combo = QComboBox()
        self.day_combo.addItems(['Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma'])
        layout.addWidget(self.day_combo)

        # Zaman seçimi
        self.start_time = QTimeEdit()
        self.end_time = QTimeEdit()
        layout.addWidget(self.start_time)
        layout.addWidget(self.end_time)

        # Kaydet butonu
        save_btn = QPushButton('Kaydet')
        save_btn.clicked.connect(self.accept)
        layout.addWidget(save_btn)
