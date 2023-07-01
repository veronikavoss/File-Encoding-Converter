from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMenuBar, QMenu, QWidget, QVBoxLayout, QTableView, QPushButton)
from PySide6.QtGui import QAction

class FileEncodingConverter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.set_ui()
        self.set_menu()
        self.set_list_ui()
    
    def set_ui(self):
        self.setWindowTitle("File Encoding Converter")
        self.setFixedSize(640,480)
    
    def set_menu(self):
        # menubar
        menubar = QMenuBar(self)
        self.setMenuBar(menubar)
        
        # menu
        file_menu = QMenu('&File')
        help_menu = QMenu('&Help')
        
        menubar.addMenu(file_menu)
        menubar.addMenu(help_menu)
        
        # action
        open_file_action = QAction('&Open File', file_menu)
        open_folder_action = QAction('&Open Folder', file_menu)
        exit_action = QAction('&Exit', file_menu)
        
        file_menu.addActions([
            open_file_action,
            open_folder_action,
            file_menu.addSeparator(),
            exit_action])
        
        # signal
        exit_action.triggered.connect(lambda:print("Exit"))
    
    def set_list_ui(self):
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)
        
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)
        
        tableview = QTableView()
        button = QPushButton('Open Folder')
        main_layout.addWidget(tableview)
        main_layout.addWidget(button)

if __name__ == "__main__":
    app = QApplication([])
    window = FileEncodingConverter()
    window.show()
    app.exec()