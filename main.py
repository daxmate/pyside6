# A pyside6 learning project

from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First PySide6 App")
        self.setGeometry(100, 100, 800, 600)
        self.show()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    app.exec()
    print("Hello, PySide6!")
