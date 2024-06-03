from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMenuBar, QMenu, QWidget, QVBoxLayout, QHBoxLayout, QTableView, QPushButton,
    QLabel, QLineEdit, QFileDialog)
from PySide6.QtCore import Qt
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
        self.action = Actions(self)
        
        self.open_file_action = QAction('&Open File', file_menu)
        open_folder_action = QAction('&Open Folder', file_menu)
        self.exit_action = QAction('&Exit', file_menu)
        
        self.about_action = QAction('&About', help_menu)
        
        file_menu.addActions([
            self.open_file_action,
            open_folder_action,
            file_menu.addSeparator(),
            self.exit_action])
        help_menu.addAction(self.about_action)
    
    def set_list_ui(self):
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)
        
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)
        
        tableview = QTableView()
        # tableview.setFixedHeight(150)
        tableview.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        
        button_layout = QHBoxLayout()
        
        select_all_button = QPushButton('Select All')
        deselect_button = QPushButton('Deselect')
        delete_button = QPushButton('Delete')
        add_button = QPushButton('Add')
        
        button_layout.addWidget(select_all_button)
        button_layout.addWidget(deselect_button)
        button_layout.addWidget(delete_button)
        button_layout.addWidget(add_button)
        
        open_vertical_layout = QVBoxLayout()
        open_file_layout = QHBoxLayout()
        open_folder_layout = QHBoxLayout()
        open_vertical_layout.addLayout(open_file_layout)
        open_vertical_layout.addLayout(open_folder_layout)
        
        open_file_label = QLabel('Open File : ')
        open_file_label.setFixedWidth(80)
        open_file_lineedit = QLineEdit()
        open_file_button = QPushButton('Open File')
        open_file_button.setFixedWidth(100)
        open_folder_label = QLabel('Open Folder : ')
        open_folder_label.setFixedWidth(80)
        open_folder_lineedit = QLineEdit()
        open_folder_button = QPushButton('Open Folder')
        open_folder_button.setFixedWidth(100)
        
        open_file_layout.addWidget(open_file_label)
        open_file_layout.addWidget(open_file_lineedit)
        open_file_layout.addWidget(open_file_button)
        open_folder_layout.addWidget(open_folder_label)
        open_folder_layout.addWidget(open_folder_lineedit)
        open_folder_layout.addWidget(open_folder_button)
        # button_layout.addWidget()
        
        main_layout.addWidget(tableview)
        main_layout.addLayout(button_layout)
        main_layout.addLayout(open_vertical_layout)
        main_layout.addStretch(1)
        
        # signal
        self.open_file_action.triggered.connect(lambda:self.action.open_file(open_file_lineedit))
        self.exit_action.triggered.connect(self.close)
        
        self.about_action.triggered.connect(lambda:self.action.help())
        

class Actions:
    def __init__(self,parent):
        self.parent = parent
    
    def open_file(self,lineedit):
        print('open file')
        file_path, _ = QFileDialog.getOpenFileName(self.parent, "Open File", "", "All Files (*);;Text Files (*.txt)")
        
        if file_path:
            print(f"Selected file: {file_path}")
            lineedit.setText(file_path)
        else:
            print("No file selected.")
    
    def open_folder(self):
        pass
    
    def help(self):
        print('help')

if __name__ == "__main__":
    app = QApplication([])
    window = FileEncodingConverter()
    window.show()
    app.exec()