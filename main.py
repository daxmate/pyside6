# A pyside6 learning project

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile, QTextStream, QIODevice
from forms.mainwindow_ui import Ui_MainWindow
import resources_rc


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.load_stylesheet()
        self.show()
    
    def load_stylesheet(self):
        file = QFile(":/styles/listwidget.qss")
        if file.open(QIODevice.ReadOnly | QIODevice.Text):
            stream = QTextStream(file)
            stylesheet = stream.readAll()
            self.ui.listWidget.setStyleSheet(stylesheet)
            file.close()
        else:
            print("Stylesheet resource not found")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    app.exec()
    print("Hello, PySide6!")