from PyQt5.QtWidgets import QMainWindow, QTabWidget, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from .widgets.schedule_widget import ScheduleWidget

class MainWindow(QMainWindow):
    def __init__(self, lock_controller, schedule_manager):
        super().__init__()
        self.lock_controller = lock_controller
        self.schedule_manager = schedule_manager
        
        self.setWindowTitle("ETAP SmartLock")
        self.setMinimumSize(800, 600)
        self.setWindowIcon(QIcon('/usr/lib/etap-smartlock/assets/logo.svg'))
        
        # Tab widget oluştur
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        
        # Sekmeleri ekle
        self.schedule_widget = ScheduleWidget(schedule_manager)
        self.tabs.addTab(self.schedule_widget, "Ders Programı")
        
        self.init_ui()
        self.load_stylesheet()
        
    def init_ui(self):
        self.setWindowTitle('Etap Smart Lock')
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        status_label = QLabel('Durum:', self)
        layout.addWidget(status_label)

        lock_btn = QPushButton('Kilitle', self)
        lock_btn.clicked.connect(self.lock_controller.lock_screen)
        layout.addWidget(lock_btn)

        unlock_btn = QPushButton('Kilidi Aç', self)
        unlock_btn.clicked.connect(self.lock_controller.unlock_screen)
        layout.addWidget(unlock_btn)

        schedule_btn = QPushButton('Program Ayarla', self)
        schedule_btn.clicked.connect(self.show_schedule_dialog)
        layout.addWidget(schedule_btn)

        # Menü ve araç çubuklarını ekle
        self.create_menus()
        self.create_toolbars()
    
    def create_menus(self):
        menubar = self.menuBar()
        
        file_menu = menubar.addMenu("Dosya")
        edit_menu = menubar.addMenu("Düzen")
        tools_menu = menubar.addMenu("Araçlar")
        help_menu = menubar.addMenu("Yardım")
    
    def create_toolbars(self):
        main_toolbar = self.addToolBar("Ana Araç Çubuğu")
    
    def show_schedule_dialog(self):
        # Program ayarlama dialogu burada implement edilecek
        pass
    
    def load_stylesheet(self):
        try:
            with open('/usr/lib/etap-smartlock/assets/style.qss', 'r') as f:
                self.setStyleSheet(f.read())
        except:
            print("Stil dosyası yüklenemedi")