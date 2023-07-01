from PySide6.QtWidgets import QApplication, QMainWindow

class FileEncodingConverter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Encoding Converter")

if __name__ == "__main__":
    app = QApplication([])
    window = FileEncodingConverter()
    window.show()
    app.exec()