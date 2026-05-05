# A pyside6 learning project

from PySide6.QtWidgets import QApplication, QMainWindow
from forms.mainwindow_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    app.exec()
    print("Hello, PySide6!")
