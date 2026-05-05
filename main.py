# A pyside6 learning project

from PySide6.QtWidgets import QApplication, QMainWindow
from forms.mainwindow_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.load_stylesheet()
        self.show()
    
    def load_stylesheet(self):
        try:
            with open('styles/listwidget.qss', 'r') as f:
                stylesheet = f.read()
                self.ui.listWidget.setStyleSheet(stylesheet)
        except FileNotFoundError:
            print("Stylesheet file not found")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    app.exec()
    print("Hello, PySide6!")