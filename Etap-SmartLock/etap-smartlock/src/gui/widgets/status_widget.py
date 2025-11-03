from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

class StatusWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        self.status_label = QLabel('Durum: Aktif')
        layout.addWidget(self.status_label)
        self.setLayout(layout)

    def update_status(self, is_locked):
        self.status_label.setText(f'Durum: {"Kilitli" if is_locked else "Açık"}')
